import pytest
from tipalti.dev_dogs.utils.dogs_names import dogsNames
from tipalti.dev_dogs.utils.globals import EXP_MENU_ITEMS, CONTACT_NAME, CONTACT_EMAIL, MESSAGE_PREFIX


class TestDevDogs():
    @pytest.mark.flaky(reruns=1)
    def test_items_names(self, setup_dev_dogs):
        page, welcome_page, dog_page = setup_dev_dogs
        welcome_page.click_on_menu_button()
        welcome_page.get_and_assert_menu_items(EXP_MENU_ITEMS)

    @pytest.mark.flaky(reruns=1)
    def test_filling_content_kika(self, setup_dev_dogs):
        page, welcome_page, dog_page = setup_dev_dogs
        welcome_page.click_on_item_and_verify(dogsNames.Kika.value)
        dog_page.fill_contant_details(CONTACT_NAME, CONTACT_EMAIL)
        dog_page.fill_message(MESSAGE_PREFIX, dogsNames.Kika.value)
        dog_page.click_on_send()

    def test_filling_content_lychee(self, setup_dev_dogs):
        page, welcome_page, dog_page = setup_dev_dogs
        welcome_page.click_on_item_and_verify(dogsNames.Lychee.value)
        dog_page.fill_contant_details(CONTACT_NAME, CONTACT_EMAIL)
        dog_page.fill_message(MESSAGE_PREFIX, dogsNames.Lychee.value)
        dog_page.click_on_send()

    def test_filling_content_kimba(self, setup_dev_dogs):
        page, welcome_page, dog_page = setup_dev_dogs
        welcome_page.click_on_item_and_verify(dogsNames.Kimba.value)
        dog_page.fill_contant_details(CONTACT_NAME, CONTACT_EMAIL)
        dog_page.fill_message(MESSAGE_PREFIX, dogsNames.Kimba.value)
        dog_page.click_on_send()
