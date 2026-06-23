import os
import pytest
from dotenv import load_dotenv
from pages.login_page import LoginPage
from pages.secure_page import SecurePage

load_dotenv()

import os
import pytest
from dotenv import load_dotenv
from pages.login_page import LoginPage
from pages.secure_page import SecurePage

load_dotenv()

LOGIN_URL = os.getenv("LOGIN_URL")
USERNAME = os.getenv("LOGIN_USERNAME")
PASSWORD = os.getenv("LOGIN_PASSWORD")


@pytest.fixture
def login_page(page):
    lp = LoginPage(page)
    lp.open(LOGIN_URL)
    return lp


@pytest.fixture
def authenticated_page(page):
    lp = LoginPage(page)
    lp.open(LOGIN_URL)
    lp.login(USERNAME, PASSWORD)
    return page


@pytest.fixture
def secure_page(authenticated_page):
    return SecurePage(authenticated_page)