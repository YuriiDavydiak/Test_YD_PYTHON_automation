import os
import pytest
from dotenv import load_dotenv
from pages.login_page import LoginPage
from pages.secure_page import SecurePage

load_dotenv()

BASE_URL = os.getenv("LOGIN_URL", "https://the-internet.herokuapp.com").replace("/login", "")
USERNAME = os.getenv("LOGIN_USERNAME")
PASSWORD = os.getenv("LOGIN_PASSWORD")


def _open_login_page(page):
    lp = LoginPage(page)
    lp.open(BASE_URL)
    return lp


@pytest.fixture
def login_page(page):
    return _open_login_page(page)


@pytest.fixture
def authenticated_page(login_page):
    login_page.login(USERNAME, PASSWORD)
    return login_page.page


@pytest.fixture
def secure_page(authenticated_page):
    return SecurePage(authenticated_page)
