import allure
from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from components.courses.course_menu_view_component import CourseMenuViewComponent
from elements.image import Image
from elements.text import Text


class CourseViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.menu = CourseMenuViewComponent(page)

        self.course_title = Text(page, "course-widget-title-text", "Title")
        self.course_image = Image(page, "course-preview-image", "Image")
        self.course_max_score_text = Text(page,"course-max-score-info-row-view-text", "Max score")
        self.course_min_score_text = Text(page,"course-min-score-info-row-view-text", "Min score")
        self.course_estimated_time_text = Text(
            page,"course-estimated-time-info-row-view-text", "Estimated time"
        )

    @allure.step('Check visible course view at index "{index}"')
    def check_visible(
            self,
            index: int,
            title: str,
            max_score: str,
            min_score: str,
            estimated_time: str
    ):

        self.course_image.check_visible(nth=index)


        self.course_title.check_visible(nth=index)
        self.course_title.check_have_text(text=title, nth=index)

        self.course_max_score_text.check_visible(nth=index)
        self.course_max_score_text.check_have_text(text=f'Max score: {max_score}', nth=index)

        self.course_min_score_text.check_visible(nth=index)
        self.course_min_score_text.check_have_text(f'Min score: {min_score}', nth=index)

        self.course_estimated_time_text.check_visible(nth=index)
        self.course_estimated_time_text.check_have_text(f'Estimated time: {estimated_time}', nth=index)