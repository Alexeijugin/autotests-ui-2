from playwright.sync_api import Page, expect

from components.base_component import BaseComponent


class CourseMenuViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.course_menu_button = page.get_by_test_id("course-view-menu-button")
        self.course_edit_menu_item = page.get_by_test_id("course-view-edit-menu-item")
        self.course_delete_menu_item = page.get_by_test_id("course-view-delete-menu-item")


    def click_edit(self, index: int):
        self.course_menu_button.nth(index).click()

        expect(self.course_edit_menu_item.nth(index)).to_be_visible()
        self.course_edit_menu_item.nth(index).click()

    def click_delete(self, index: int):
        self.course_menu_button.nth(index).click()

        expect(self.course_delete_menu_item.nth(index)).to_be_visible()
        self.course_edit_menu_item.nth(index).click()