#!/usr/bin/env python

import logging
from ui_options import UiOptions
from user_interface import UserInterface
from mineral_sorter import MineralSorter
from mineral_repository import MineralRepository
from identification_history import IdentificationHistory

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.DEBUG)


main_mineral_repository = MineralRepository()
main_identification_history = IdentificationHistory()
main_user_interface = UserInterface()
main_ui_options = UiOptions(main_mineral_repository.CSVinList)
main_mineral_sorter = MineralSorter()


def start_program():
    print(main_user_interface.program_start_msg)
    get_sample_type()


def get_sample_type():
    main_identification_history.clear_history()
    sample_type = main_user_interface.prompt_for_sampletype()
    if sample_type == main_user_interface.sample_type_handsample:
        main_ui_options.populate_handsample_attributes()

    elif sample_type == main_user_interface.sample_type_thinsection:
        main_ui_options.populate_thinsection_attributes()
    else:
        main_user_interface.display_input_error_message()
        get_sample_type()

    add_an_attribute()
    get_next_action()


def get_next_action():
    next_action = main_user_interface.get_input_from_user(main_user_interface.user_options_msg,
                                                          main_user_interface.user_options)
    if next_action == main_user_interface.user_option_add_attribute:
        add_an_attribute()
    elif next_action == main_user_interface.user_option_edit_attribute:
        edit_an_attribute()
    elif next_action == main_user_interface.user_option_remove_attribute:
        remove_an_attribute()
    elif next_action == main_user_interface.user_option_display_all_chars:
        show_mineral_details()
    elif next_action == main_user_interface.user_option_identify_new_mineral:
        get_sample_type()
    elif next_action == main_user_interface.quit_option:
        main_user_interface.quit_program()
    else:
        main_user_interface.display_input_error_message()
    get_next_action()


def add_an_attribute():
    selected_attribute = main_user_interface.get_input_from_user(main_user_interface.next_attribute_msg,
                                                                 main_ui_options.attributesForSampleType)
    logging.debug(main_ui_options.allAttributes.keys())

    if main_identification_history.attribute_is_duplicate(selected_attribute):
        main_user_interface.get_different_input_from_user(add_an_attribute)
        return
    attribute_value = main_user_interface.get_input_from_user(main_user_interface.attribute_options_msg,
                                                              main_ui_options.allAttributes[selected_attribute])
    next_search_criteria = (selected_attribute, attribute_value)
    main_identification_history.log.append(next_search_criteria)
    refresh_mineral_list()


def edit_an_attribute():
    main_identification_history.create_attribute_history_log()
    selected_attribute = main_user_interface.get_input_from_user(main_user_interface.next_attribute_msg,
                                                                 main_identification_history.attribute_log)

    attribute_value = main_user_interface.get_input_from_user(main_user_interface.attribute_options_msg,
                                                              main_ui_options.allAttributes[selected_attribute])
    edited_history_item = (selected_attribute, attribute_value)
    main_identification_history.edit_item_in_history(edited_history_item)
    refresh_mineral_list()


def remove_an_attribute():
    main_identification_history.create_attribute_history_log()
    selected_attribute = main_user_interface.get_input_from_user(main_user_interface.next_attribute_msg,
                                                                 main_identification_history.attribute_log)
    main_identification_history.remove_item_from_history(selected_attribute)
    refresh_mineral_list()


def show_mineral_details():
    main_user_interface.show_matched_minerals_detail(main_mineral_sorter.minerals_matched_to_history)


def refresh_mineral_list():
    main_mineral_sorter.match_minerals_to_history(main_identification_history.log, main_mineral_repository.AllMinerals)
    main_user_interface.show_matched_minerals(main_mineral_sorter.minerals_matched_to_history)

if __name__ == '__main__':
    start_program()
