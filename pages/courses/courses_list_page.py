from playwright.sync_api import Page, expect

from components.courses.course_list_toolbar_view_component import CoursesListToolbarViewComponent
from components.courses.course_view_component import CourseViewComponent
from components.view.empty_view_components import EmptyViewComponents
from components.navigation.navbar_component import NavbarComponent
from components.navigation.sidebar_component import SidebarComponent
from pages.base_page import BasePage




class CoursesListPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.sidebar = SidebarComponent(page)
        self.navbar = NavbarComponent(page)
        # Блок, который отображается, когда нет курсов
        self.empty_view = EmptyViewComponents(page, 'courses-list')
        # Карточка курса и меню курса(композиция)
        self.course_view = CourseViewComponent(page)
        # Заголовок и кнопка создания курса.
        self.toolbar_view = CoursesListToolbarViewComponent(page)

    def check_visible_empty_view(self):
        self.empty_view.check_visible_empty_view(
            title="There is no results",
            description="Results from the load test pipeline will be displayed here"
        )