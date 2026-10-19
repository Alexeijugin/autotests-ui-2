from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from elements.button import Button


class CourseMenuViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.course_menu_button = Button(page,"course-view-menu-button", "Menu")
        self.course_edit_menu_item = Button(page,"course-view-edit-menu-item", "Edit")
        self.course_delete_menu_item = Button(page,"course-view-delete-menu-item", "Delete")


    def click_edit(self, index: int):
        self.course_menu_button.click(nth=index)

        self.course_edit_menu_item.check_visible(nth=index)
        self.course_edit_menu_item.click(nth=index)

    def click_delete(self, index: int):
        self.course_menu_button.click(nth=index)

        self.course_delete_menu_item.check_visible(nth=index)
        self.course_edit_menu_item.click(nth=index)