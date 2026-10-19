from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from elements.icon import Icon
from elements.text import Text


class EmptyViewComponents(BaseComponent):
    def __init__(self, page: Page, identifier: str):
        super().__init__(page)

        self.empty_view_icon = Icon(page, f"{identifier}-empty-view-icon", "Icon")
        self.empty_view_title = Text(page, f"{identifier}-empty-view-title-text", "Title")
        self.empty_view_description = Text(page,f"{identifier}-empty-view-description-text", "Description")

    def check_visible_empty_view(self, title: str, description: str):
        self.empty_view_icon.check_visible()

        self.empty_view_title.check_visible()
        self.empty_view_title.check_have_text(title)

        self.empty_view_description.check_visible()
        self.empty_view_description.check_have_text(description)
