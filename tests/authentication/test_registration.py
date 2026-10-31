import allure
import pytest
from allure_commons.types import Severity

from config import settings
from pages.dashboard.dashboard_page import DashboardPage
from pages.authentication.registration_page import RegistrationPage
from tools.epics import AllureEpic
from tools.features import AllureFeature
from tools.routes import AppRoute
from tools.stories import AllureStory
from tools.tags import AllureTag


@pytest.mark.regression
@pytest.mark.registration
@allure.tag(AllureTag.REGISTRATION, AllureTag.REGRESSION)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.AUTHENTICATION)
@allure.story(AllureStory.REGISTRATION)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.AUTHENTICATION)
@allure.sub_suite(AllureStory.REGISTRATION)
class TestRegistration:
    @allure.title("User registration with correct email, username and password")
    @allure.severity(Severity.CRITICAL)
    @pytest.mark.xdist_group(name="authorization-group")
    def test_successful_registration(self, dashboard_page: DashboardPage, registration_page: RegistrationPage):  # Теперь используем фикстуру
        registration_page.visit(AppRoute.REGISTRATION)

        registration_page.registration_from.fill(
            email=settings.test_user.email,
            username=settings.test_user.username,
            password=settings.test_user.password
        )

        registration_page.click_registration_button()

        dashboard_page.dashboard_toolbar_view.check_visible()