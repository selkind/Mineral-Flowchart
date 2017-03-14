#! python

# This is a stupid class and really should just use a native python list
import logging


logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


class IdentificationHistory:
    def __init__(self):
        self.log = []
        self.attribute_log = []

    def attribute_is_duplicate(self, attribute):
        for items in self.log:
            if attribute in items:
                return True

    def create_attribute_history_log(self):
        self.attribute_log = []
        for item in self.log:
            self.attribute_log.append(item[0])

    def remove_item_from_history(self, attribute):
        for item in range(len(self.log)):
            if attribute == self.attribute_log[item]:
                del self.log[item]

    def edit_item_in_history(self, (attribute, value)):
        for item in self.log:
            if attribute in item[0]:
                self.remove_item_from_history(attribute)
        self.log.append((attribute, value))

    def clear_history(self):
        self.log = []
