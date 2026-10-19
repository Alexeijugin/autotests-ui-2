from playwright.sync_api import Page, expect

from components.courses.create_course_exercise_form_component import CreateCourseExerciseFormComponent
from components.courses.create_course_exercises_toolbar_view_component import CreateCourseExercisesToolbarViewComponent
from components.courses.create_course_form_component import CreateCourseFormComponent
from components.courses.create_course_toolbar_view_component import CreateCourseToolbarViewComponent
from components.view.empty_view_components import EmptyViewComponents
from components.view.image_upload_widget_component import ImageUploadWidgetComponent
from pages.base_page import BasePage


class CreateCoursePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        # Компонент. Блок с элементами в состоянии до загрузки картинки и после. + Методы
        self.image_upload_widget = ImageUploadWidgetComponent(page, "create-course-preview")
        # Компонент с блоком, который отображается, когда в курсе нет заданий + методы
        self.exercises_empty_view = EmptyViewComponents(page, "create-course-exercises")
        #  Компонент с блоком для заполнения формы задания + методы
        self.create_exercise_form = CreateCourseExerciseFormComponent(page)
        # Компонент. Форма создания курса
        self.create_course_form = CreateCourseFormComponent(page)
        # Компонент. Заголовок и кнопка создания курса
        self.create_course_toolbar_view = CreateCourseToolbarViewComponent(page)
        # Компонент. Кнопка и заголовок создания задания
        self.create_course_exercise_toolbar_view = CreateCourseExercisesToolbarViewComponent(page)


    def check_visible_exercises_empty_view(self):
        self.exercises_empty_view.check_visible_empty_view(
            title="There is no exercises",
            description='Click on "Create exercise" button to create new exercise'
        )





























