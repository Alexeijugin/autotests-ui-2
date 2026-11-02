import allure
from playwright.sync_api import expect, Locator

from elements.base_element import BaseElement
from tools.logger import get_logger

logger = get_logger("INPUT")

class Input(BaseElement):

    @property
    def type_of(self) -> str:
        return 'input'

    # для получения более сложного локатора - переопределяем метод родителя
    def get_locator(self, nth: int = 0, **kwargs) -> Locator:
        # Сначала через метод родителя находим элемент по атрибуту data-testid, затем внутри него - конкретный тег input
        return super().get_locator(nth, **kwargs).locator('input')

    # Некая обертка которая инкапсулирует получение объекта Locator и проверку
    def fill(self, value: str, nth: int = 0, **kwargs):
        step = f'Fill {self.type_of} "{self.name}" to value "{value}"'

        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)
            locator.fill(value)

    def check_have_value(self, value: str, nth: int = 0, **kwargs):
        step = f'Checking that {self.type_of} "{self.name}" has a value "{value}"'

        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)
            expect(locator).to_have_value(value)