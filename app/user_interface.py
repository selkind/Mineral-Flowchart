#!python

import logging
import time

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


class UserInterface:

    def __init__(self):
        self.quit_option = 'quit program'
        self.program_start_msg = 'Welcome to Wut R Rox!\n'
        self.sample_type_msg = 'What type of sample would you like to identify?\n'
        self.user_options_msg = '\nWhat would you like to do?\n'
        self.next_attribute_msg = 'Select an attribute\n'
        self.duplicate_attribute_msg = 'You have already selected that attribute. Please try again'
        self.attribute_options_msg = 'Select the characteristic exhibited by your sample'
        self.show_matched_minerals_msg = 'Here are the minerals that match your selected attributes'
        self.end_program_msg = 'Thank you for using Wut R Rox.\n\nHuge thanks to M. Schmidt, B. Karimi and N. Cutter'
        self.user_input_error_msg = 'Invalid selection.\n Please select one of the numbers displayed below'

        self.sample_type_handsample = 'hand sample'
        self.sample_type_thinsection = 'thin section'
        self.sample_type_options = [self.sample_type_handsample, self.sample_type_thinsection,
                                    self.quit_option]

        self.user_option_add_attribute = 'add an attribute'
        self.user_option_edit_attribute = 'edit an attribute'
        self.user_option_remove_attribute = 'remove an attribute'
        self.user_option_display_all_chars = 'display all characteristics of matched minerals'
        self.user_option_identify_new_mineral = 'start identifying a different mineral'
        self.user_options = [self.user_option_add_attribute, self.user_option_edit_attribute,
                             self.user_option_remove_attribute, self.user_option_display_all_chars,
                             self.user_option_identify_new_mineral, self.quit_option]

    def get_input_from_user(self, message, selection_options):
        while True:
            print(message)
            for option in range(len(selection_options)):
                print(str(option) + ') ' + str(selection_options[option]))
            try:
                user_selection = selection_options[input()]
            except SyntaxError:
                print(self.user_input_error_msg)
                continue
            if user_selection == self.quit_option:
                self.quit_program()
            return user_selection

    def prompt_for_sampletype(self):
        return self.get_input_from_user(self.sample_type_msg, self.sample_type_options)

    def get_different_input_from_user(self, function_to_restart):
        print(self.duplicate_attribute_msg)
        function_to_restart()

    def show_matched_minerals(self, matched_minerals):
        print(self.show_matched_minerals_msg)
        for minerals in range(0, len(matched_minerals), 3):
            print(matched_minerals[minerals].name.ljust(20)),
            try:
                print(matched_minerals[minerals + 1].name.ljust(20)),
                print(matched_minerals[minerals + 2].name)
            except IndexError:
                pass
        print

    def show_matched_minerals_detail(self, matched_minerals):
        print(self.show_matched_minerals_msg)
        for mineral in matched_minerals:
            print('\n' + mineral.name + ': ')
            for mineral_characteristic in mineral.allInfo.keys():
                print('\n' + mineral_characteristic + ':')
                values = mineral.allInfo[mineral_characteristic].split(',')
                for characteristic_value in values:
                    print('\t' + characteristic_value)

    def display_input_error_message(self):
        print(self.user_input_error_msg)

    def quit_program(self):
        print(self.end_program_msg)
        time.sleep(3)
        quit()