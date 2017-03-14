#!/usr/bin/env python

import logging
from ui_options import UiOptions
from user_interface import UserInterface
from mineral_sorter import MineralSorter
from mineral_repository import MineralRepository
from identification_history import IdentificationHistory

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.DEBUG)


mineral_repo = MineralRepository()
history = IdentificationHistory()
UI = UserInterface()
options = UiOptions(mineral_repo.CSVinList)
sorter = MineralSorter()


def start_program():
    UI.print_start_msg()
    get_sample_type()

    while True:
        get_next_action()


def get_sample_type():
    history.clear_history()
    sample_type = UI.get_sampletype()
    if sample_type == UI.sample_type_handsample:
        options.populate_handsample_attributes()

    elif sample_type == UI.sample_type_thinsection:
        options.populate_thinsection_attributes()
    else:
        UI.display_input_error_message()
        get_sample_type()

    add_attribute()
    get_next_action()


def get_next_action():
    selection = UI.get_input(UI.options_msg,
                             UI.options)

    action = {UI.option_add_attribute: add_attribute,
              UI.option_edit_attribute: edit_attribute,
              UI.option_remove_attribute: remove_attribute,
              UI.option_display_all_chars: show_mineral_details,
              UI.option_identify_new_mineral: get_sample_type,
              UI.quit_option: UI.quit_program}\
              .get(selection, UI.display_input_error_message)

    action()


def add_attribute():
    selected_attribute = UI.get_input(UI.next_attribute_msg,
                                      options.attributesForSampleType)
    logging.debug(options.allAttributes.keys())

    if history.attribute_is_duplicate(selected_attribute):
        UI.get_different_input(add_attribute)
        return
    attribute_value = UI.get_input(UI.attribute_options_msg,
                                   options.allAttributes[selected_attribute])
    next_search_criteria = (selected_attribute, attribute_value)
    history.log.append(next_search_criteria)
    refresh_mineral_list()


def edit_attribute():
    history.create_attribute_history_log()
    selected_attribute = UI.get_input(UI.next_attribute_msg,
                                      history.attribute_log)

    attribute_value = UI.get_input(UI.attribute_options_msg,
                                   options.allAttributes[selected_attribute])
    edited_history_item = (selected_attribute, attribute_value)
    history.edit_item_in_history(edited_history_item)
    refresh_mineral_list()


def remove_attribute():
    history.create_attribute_history_log()
    selected_attribute = UI.get_input(UI.next_attribute_msg,
                                      history.attribute_log)
    history.remove_item_from_history(selected_attribute)
    refresh_mineral_list()


def show_mineral_details():
    UI.show_matched_minerals_detail(sorter.minerals_matched_to_history)


def refresh_mineral_list():
    sorter.match_minerals_to_history(history.log, mineral_repo.AllMinerals)
    UI.show_matched_minerals(sorter.minerals_matched_to_history)

if __name__ == '__main__':
    start_program()
