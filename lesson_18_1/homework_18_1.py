import requests

BASE_URL = "https://images-api.nasa.gov"


def search_images(query, media_type="image", page_size=20):
    search_url = f"{BASE_URL}/search"
    params = {
        "q": query,
        "media_type": media_type,
        "page_size": page_size
    }
    response = requests.get(search_url, params=params)
    response.raise_for_status()
    return response.json()


def get_nasa_ids(search_data):
    items = search_data.get("collection", {}).get("items", [])
    print(f"Знайдено елементів: {len(items)}")
    nasa_ids = []
    for item in items:
        data = item.get("data", [])
        if data:
            nasa_id = data[0].get("nasa_id")
            if nasa_id:
                nasa_ids.append(nasa_id)
    print(f"Зібрано nasa_id: {len(nasa_ids)}")
    return nasa_ids


def get_asset_urls(nasa_id):
    asset_url = f"{BASE_URL}/asset/{nasa_id}"
    response = requests.get(asset_url)
    response.raise_for_status()
    return response.json()


def find_jpg_url(asset_data):
    items = asset_data.get("collection", {}).get("items", [])
    for item in items:
        href = item.get("href", "")
        if href.lower().endswith(".jpg"):
            return href
    return None


def download_image(url, filename):
    response = requests.get(url)
    response.raise_for_status()
    with open(filename, "wb") as f:
        f.write(response.content)
    print(f"Збережено: {filename}")


def save_mars_photos(nasa_ids, count=2):
    saved = 0
    for nasa_id in nasa_ids:
        if saved >= count:
            break
        print(f"Отримуємо assets для nasa_id: {nasa_id}")
        try:
            asset_data = get_asset_urls(nasa_id)
            jpg_url = find_jpg_url(asset_data)
            if jpg_url:
                filename = f"mars_photo{saved + 1}.jpg"
                print(f"Скачуємо: {jpg_url}")
                download_image(jpg_url, filename)
                saved += 1
            else:
                print(f"JPG не знайдено для {nasa_id}, пропускаємо")
        except requests.HTTPError as e:
            print(f"Помилка для {nasa_id}: {e}, пропускаємо")
    print(f"\nЗбережено {saved} фото.")


if __name__ == "__main__":
    print("Шукаємо зображення Curiosity rover Mars...")
    search_data = search_images("Curiosity rover Mars")
    nasa_ids = get_nasa_ids(search_data)
    save_mars_photos(nasa_ids)