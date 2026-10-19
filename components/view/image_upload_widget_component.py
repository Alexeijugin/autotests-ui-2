from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from components.view.empty_view_components import EmptyViewComponents
from elements.button import Button
from elements.file_input import FileInput
from elements.icon import Icon
from elements.image import Image
from elements.input import Input
from elements.text import Text


class ImageUploadWidgetComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str):
        super().__init__(page)
        self.preview_empty_view = EmptyViewComponents(page, identifier)

        # Картинка предпросмотра
        self.preview_image = Image(page, f"{identifier}-image-upload-widget-preview-image", "Preview")

        # Кнопка загрузки, удаления картинки предпросмотра курса и блок с информацией о загружаемой картинке
        self.image_upload_info_icon = Icon(
            page, f"{identifier}-image-upload-widget-info-icon", "Image upload info"
        )
        self.image_upload_info_title = Text(
            page, f"{identifier}-image-upload-widget-info-title-text", "Image upload info title"
        )
        self.image_upload_info_description = Text(
            page, f"{identifier}-image-upload-widget-info-description-text", "Image upload info description"
        )

        self.upload_button = Button(
            page,f"{identifier}-image-upload-widget-upload-button", "Upload image"
        )
        self.remove_button = Button(
            page, f"{identifier}-image-upload-widget-remove-button", "Remove image"
        )
        self.upload_input = FileInput(page,f"{identifier}-image-upload-widget-input", "Upload")

    def check_visible(self, is_image_upload: bool = False):
        self.image_upload_info_icon.check_visible()

        self.image_upload_info_title.check_visible()
        self.image_upload_info_title.check_have_text('Tap on "Upload image" button to select file')


        self.image_upload_info_description.check_visible()
        self.image_upload_info_description.check_have_text('Recommended file size 540X300')

        self.upload_input.check_visible()

        if is_image_upload:
            self.remove_button.check_visible()
            self.preview_image.check_visible()

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
