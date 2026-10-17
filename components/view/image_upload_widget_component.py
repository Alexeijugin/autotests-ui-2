from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from components.view.empty_view_components import EmptyViewComponents


class ImageUploadWidgetComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str):
        super().__init__(page)
        self.preview_empty_view = EmptyViewComponents(page, identifier)

        # Картинка предпросмотра
        self.preview_image = page.get_by_test_id(f"{identifier}-image-upload-widget-preview-image")

        # Кнопка загрузки, удаления картинки предпросмотра курса и блок с информацией о загружаемой картинке
        self.image_upload_info_icon = page.get_by_test_id(f"{identifier}-image-upload-widget-info-icon")
        self.image_upload_info_title = page.get_by_test_id(
            f"{identifier}-image-upload-widget-info-title-text"
        )
        self.image_upload_info_description = page.get_by_test_id(
            f"{identifier}-image-upload-widget-info-description-text"
        )

        self.upload_button = page.get_by_test_id(
            f"{identifier}-image-upload-widget-upload-button"
        )
        self.remove_button = page.get_by_test_id(
            f"{identifier}-image-upload-widget-remove-button"
        )
        self.upload_input = page.get_by_test_id(f"{identifier}-image-upload-widget-input")

    def check_visible(self, is_image_upload: bool = False):
        expect(self.image_upload_info_icon).to_be_visible()

        expect(self.image_upload_info_title).to_be_visible()
        expect(self.image_upload_info_title).to_have_text('Tap on "Upload image" button to select file')

        expect(self.image_upload_info_description).to_be_visible()
        expect(self.image_upload_info_description).to_have_text('Recommended file size 540X300')

        expect(self.upload_input).to_be_visible()

        if is_image_upload:
            expect(self.remove_button).to_be_visible()
            expect(self.preview_image).to_be_visible()

        if not is_image_upload:
            # Если картинка не загружена, проверяем наличие компонента EmptyViewComponents
            self.preview_empty_view.check_visible_empty_view(
                title='No image selected',
                description='Preview of selected image will be displayed here'
            )

    def click_remove_image_button(self):
        self.remove_button.click()

    def upload_preview_image(self, file: str):
        self.upload_input.set_input_files(file)
