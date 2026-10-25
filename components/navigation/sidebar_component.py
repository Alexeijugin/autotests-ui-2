import re

import allure
from playwright.sync_api import Page

from components.base_component import BaseComponent
from components.navigation.sidebar_list_item_compnent import SidebarListItemComponent


class SidebarComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.logout_item_list = SidebarListItemComponent(page, 'logout')
        self.courses_item_list = SidebarListItemComponent(page, 'courses')
        self.dashboard_item_list = SidebarListItemComponent(page, 'dashboard')

    @allure.step("Check visible sidebar")
    def check_visible(self):
        self.logout_item_list.check_visible('Logout')
        self.courses_item_list.check_visible('Courses')
        self.dashboard_item_list.check_visible('Dashboard')

    @allure.step("Click logout on sidebar")
    def click_logout(self):
        self.logout_item_list.navigate(re.compile(r'.*/#/auth/login'))

    @allure.step("Click courses on sidebar")
    def click_courses(self):
        self.courses_item_list.navigate(re.compile(r'.*/#/auth/courses'))

    @allure.step("Click dashboard on sidebar")
    def click_dashboard(self):
        self.dashboard_item_list.navigate(re.compile(r'.*/#/auth/dashboard'))