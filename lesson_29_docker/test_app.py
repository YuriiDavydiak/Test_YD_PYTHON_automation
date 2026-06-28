import pytest
import allure
from app import create_table, insert_user, update_user, delete_user, get_user, get_all_users, get_connection


@pytest.fixture(scope="module", autouse=True)
def setup_database():
    with allure.step("Створення таблиці users в базі даних"):
        create_table()
    yield


@allure.feature("Database Connection")
class TestDatabaseConnection:

    @allure.story("Перевірка підключення до бази даних")
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
    def test_insert_user(self):
        with allure.step("Вставляємо нового користувача в базу"):
            user_id = insert_user("Test User", "test@example.com")

        with allure.step("Перевіряємо що користувач створений"):
            assert user_id is not None
            user = get_user(user_id)
            assert user[1] == "Test User"
            assert user[2] == "test@example.com"

        with allure.step("Видаляємо тестового користувача"):
            delete_user(user_id)

    @allure.story("Оновлення даних користувача")
    def test_update_user(self):
        with allure.step("Створюємо тестового користувача"):
            user_id = insert_user("Old Name", "old@example.com")

        with allure.step("Оновлюємо ім'я користувача"):
            update_user(user_id, name="New Name")
            user = get_user(user_id)
            assert user[1] == "New Name"

        with allure.step("Оновлюємо email користувача"):
            update_user(user_id, email="new@example.com")
            user = get_user(user_id)
            assert user[2] == "new@example.com"

        with allure.step("Видаляємо тестового користувача"):
            delete_user(user_id)

    @allure.story("Видалення користувача")
    def test_delete_user(self):
        with allure.step("Створюємо тестового користувача"):
            user_id = insert_user("To Delete", "delete@example.com")

        with allure.step("Видаляємо користувача"):
            delete_user(user_id)

        with allure.step("Перевіряємо що користувача більше немає"):
            user = get_user(user_id)
            assert user is None

    @allure.story("Вибірка всіх користувачів")
    def test_select_all_users(self):
        with allure.step("Створюємо двох тестових користувачів"):
            insert_user("User A", "a@example.com")
            insert_user("User B", "b@example.com")

        with allure.step("Отримуємо список всіх користувачів"):
            users = get_all_users()

        with allure.step("Перевіряємо що обидва користувачі є в списку"):
            assert len(users) >= 2
            emails = [u[2] for u in users]
            assert "a@example.com" in emails
            assert "b@example.com" in emails