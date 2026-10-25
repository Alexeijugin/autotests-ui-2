import allure
from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from elements.image import Image
from elements.text import Text


class ChartViewComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str, chart_tipe: str):
        super().__init__(page)

        self.title = Text(page, f"{identifier}-widget-title-text", 'Title')
        self.chart = Image(page, f"{identifier}-{chart_tipe}-chart", 'Chart')

    @allure.step('Check visible chart view "{title}"')
    def check_visible_students_chart(self, title: str):
        self.title.check_visible()
        self.title.check_have_text(title)

        self.chart.check_visible()


