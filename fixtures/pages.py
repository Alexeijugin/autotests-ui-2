import pytest
from playwright.sync_api import Page

from pages.courses_list_page import CoursesListPage
from pages.create_course_page import CreateCoursePage
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage


@pytest.fixture
def login_page(chromium_page_with_state: Page):
    return LoginPage(page=chromium_page_with_state)

@pytest.fixture
def courses_list_page(chromium_page_with_state: Page):
    return CoursesListPage(page=chromium_page_with_state)

@pytest.fixture
def create_course_page(chromium_page_with_state: Page):
    return CreateCoursePage(page=chromium_page_with_state)

@pytest.fixture
def dashboard_page(chromium_page_with_state: Page):
    return DashboardPage(page=chromium_page_with_state)

@pytest.fixture
def dashboard_page(chromium_page_with_state: Page):
    return RegistrationPage(page=chromium_page_with_state)