import requests
from urllib.parse import quote

BASE_URL = "http://127.0.0.1:8080"
IMAGE_PATH = "mars_photo1.jpg"


def upload_image(image_path):
    url = f"{BASE_URL}/upload"
    with open(image_path, "rb") as img:
        files = {"image": img}
        response = requests.post(url, files=files)
    response.raise_for_status()
    data = response.json()
    print(f"Завантажено. Відповідь: {data}")
    return data["image_url"]


def get_image_url(filename):
    encoded = quote(filename)
    url = f"{BASE_URL}/image/{encoded}"
    headers = {"Content-Type": "text"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    data = response.json()
    print(f"Отримано URL: {data}")
    return data["image_url"]


def get_image_file(filename, save_as="downloaded.jpg"):
    encoded = quote(filename)
    url = f"{BASE_URL}/image/{encoded}"
    headers = {"Content-Type": "image"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    with open(save_as, "wb") as f:
        f.write(response.content)
    print(f"Зображення збережено як: {save_as}")


def delete_image(filename):
    encoded = quote(filename)
    url = f"{BASE_URL}/delete/{encoded}"
    response = requests.delete(url)
    response.raise_for_status()
    data = response.json()
    print(f"Видалено. Відповідь: {data}")


if __name__ == "__main__":
    # 1. Завантажуємо зображення
    image_url = upload_image(IMAGE_PATH)

    # 2. Витягуємо ім'я файлу з URL
    filename = image_url.split("/uploads/")[-1]

    # 3. Отримуємо URL зображення через GET (Content-Type: text)
    get_image_url(filename)

    # 4. Отримуємо саме зображення через GET (Content-Type: image)
    get_image_file(filename, save_as="downloaded.jpg")

    # 5. Видаляємо зображення
    delete_image(filename)