import pytest
import allure
from app import create_table, insert_user, update_user, delete_user, get_user, get_all_users, get_connection


@pytest.fixture(scope="module", autouse=True)
def setup_database():
    with allure.step("Створення таблиці users в базі даних"):
        create_table()
    yield


@allure.step("Створюємо тестового користувача: {name} / {email}")
def create_test_user(name="Test User", email="test@example.com"):
    return insert_user(name, email)


@allure.step("Видаляємо тестового користувача з id={user_id}")
def remove_test_user(user_id):
    delete_user(user_id)


@allure.feature("Database Connection")
class TestDatabaseConnection:

    @allure.story("Перевірка підключення до бази даних")
    @allure.title("Перевірка активного підключення до бази даних")
    def test_database_connection(self):
        with allure.step("Відкриваємо з'єднання з базою даних"):
            conn = get_connection()

        with allure.step("Перевіряємо що з'єднання активне"):
            assert conn is not None
            assert conn.closed == 0

        with allure.step("Закриваємо з'єднання"):
            conn.close()


@allure.feature("User CRUD Operations")
class TestUserOperations:

    @allure.story("Вставка нового користувача")
    @allure.title("Вставка нового користувача в базу даних")
    def test_insert_user(self):
        user_id = create_test_user("Test User", "test@example.com")

        with allure.step("Перевіряємо що користувач створений"):
            assert user_id is not None
            user = get_user(user_id)
            assert user[1] == "Test User"
            assert user[2] == "test@example.com"

        remove_test_user(user_id)

    @allure.story("Оновлення даних користувача")
    @allure.title("Оновлення імені та email користувача")
    def test_update_user(self):
        user_id = create_test_user("Old Name", "old@example.com")

        with allure.step("Оновлюємо ім'я користувача"):
            update_user(user_id, name="New Name")
            user = get_user(user_id)
            assert user[1] == "New Name"

        with allure.step("Оновлюємо email користувача"):
            update_user(user_id, email="new@example.com")
            user = get_user(user_id)
            assert user[2] == "new@example.com"

        remove_test_user(user_id)

    @allure.story("Видалення користувача")
    @allure.title("Видалення користувача з бази даних")
    def test_delete_user(self):
        user_id = create_test_user("To Delete", "delete@example.com")

        with allure.step("Видаляємо користувача"):
            delete_user(user_id)

        with allure.step("Перевіряємо що користувача більше немає"):
            user = get_user(user_id)
            assert user is None

    @allure.story("Вибірка всіх користувачів")
    @allure.title("Отримання списку всіх користувачів")
    def test_select_all_users(self):
        with allure.step("Створюємо двох тестових користувачів"):
            create_test_user("User A", "a@example.com")
            create_test_user("User B", "b@example.com")

        with allure.step("Отримуємо список всіх користувачів"):
            users = get_all_users()

        with allure.step("Перевіряємо що обидва користувачі є в списку"):
            assert len(users) >= 2
            emails = [u[2] for u in users]
            assert "a@example.com" in emails
            assert "b@example.com" in emails