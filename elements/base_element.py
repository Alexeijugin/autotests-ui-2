from playwright.sync_api import Locator, Page, expect


class BaseElement:
    def __init__(self, page: Page, locator: str, name: str):
        self.page = page
        self.name = name
        self.locator = locator

    # Для динамической сборки передаем в функцию именованный аргумент.
    # Если обычная строка без плейсхолдера, то передавать в функцию соответственно ничего не надо. Ошибки не будет.
    def get_locator(self, nth: int = 0, **kwargs) -> Locator:  # объект локатор для взаимодействия с элементом
        # Получаем строку у которой заполнились плейсхолдеры. Для динамического использования!
        locator = self.locator.format(kwargs)
        # Инициализируем и возвращаем объект локатора
        return self.page.get_by_test_id(locator).nth(nth)

    def click(self, nth: int = 0, **kwargs):
        # Тут уже в переменной locator лениво инициализируется объект Locator
        locator = self.get_locator(nth, **kwargs)

        locator.click()

    def check_visible(self, nth: int = 0, **kwargs):  # Некая обертка которая инкапсулирует получение объекта Locator и проверку
        locator = self.get_locator(nth, **kwargs)

        expect(locator).to_be_visible()

    def check_have_text(self, text: str, nth: int = 0, **kwargs):
        locator = self.get_locator(nth, **kwargs)

        expect(locator).to_have_text(text)