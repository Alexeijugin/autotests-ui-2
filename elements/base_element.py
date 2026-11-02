import allure
from playwright.sync_api import Locator, Page, expect

from tools.logger import get_logger

logger = get_logger("BASE_ELEMENT")

class BaseElement:
    def __init__(self, page: Page, locator: str, name: str):
        self.page = page
        self.name = name
        self.locator = locator

    @property
    def type_of(self) -> str:  # Добавили свойство type_of
        return "base element"

    # Для динамической сборки передаем в функцию именованный аргумент.
    # Если обычная строка без плейсхолдера, то передавать в функцию соответственно ничего не надо. Ошибки не будет.
    def get_locator(self, nth: int = 0, **kwargs) -> Locator:  # объект локатор для взаимодействия с элементом
        # Получаем строку у которой заполнились плейсхолдеры. Для динамического использования!
        locator = self.locator.format(kwargs)

        step = f'Getting locator with "data-testid={locator}" at index "{nth}"'

        # Инициализируем и возвращаем объект локатора
        with allure.step(step):
            logger.info(step)
            return self.page.get_by_test_id(locator).nth(nth)

    def click(self, nth: int = 0, **kwargs):
        step = f'Clicking {self.type_of} "{self.name}"'

        with allure.step(step):
            # Тут уже в переменной locator лениво инициализируется объект Locator
            locator = self.get_locator(nth, **kwargs)

            logger.info(step)
            locator.click()

    def check_visible(self, nth: int = 0, **kwargs):  # Некая обертка которая инкапсулирует получение объекта Locator и проверку
        step = f'Checking that {self.type_of} "{self.name}"'

        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)
            expect(locator).to_be_visible()

    def check_have_text(self, text: str, nth: int = 0, **kwargs):
        step = f'Checking that {self.type_of} "{self.name}" has text "{text}"'

        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)
            expect(locator).to_have_text(text)