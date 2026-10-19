from playwright.sync_api import expect, Locator

from elements.base_element import BaseElement


class Input(BaseElement):
    # для получения более сложного локатора - переопределяем метод родителя
    def get_locator(self, nth: int = 0, **kwargs) -> Locator:
        # Сначала через метод родителя находим элемент по атрибуту data-testid, затем внутри него - конкретный тег input
        return super().get_locator(nth, **kwargs).locator('input')

    # Некая обертка которая инкапсулирует получение объекта Locator и проверку
    def fill(self, value: str, nth: int = 0, **kwargs):
        locator = self.get_locator(nth, **kwargs)
        locator.fill(value)

    def check_have_value(self, value: str, nth: int = 0, **kwargs):
        locator = self.get_locator(nth, **kwargs)
        expect(locator).to_have_value(value)