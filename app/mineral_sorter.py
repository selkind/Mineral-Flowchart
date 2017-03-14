#! python


import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
#logging.disable(logging.DEBUG)


class MineralSorter:
    def __init__(self):
        self.minerals_matched_to_history = []

    def match_minerals_to_history(self, history, minerals):
        self.minerals_matched_to_history = []
        for mineral in minerals:
            mineral.fitsSelectedAttributes = True
            for item in history:
                attribute = item[0]
                logging.debug('attribute ' + attribute)
                mineral_property = item[1]
                logging.debug('mineral property ' + mineral_property)
                logging.debug('allInfo ' + str(mineral.allInfo))
                separated_properties = mineral.allInfo[attribute].split(',')
                if mineral_property.lower() not in separated_properties:
                    mineral.fitsSelectedAttributes = False
                    break
            if mineral.fitsSelectedAttributes:
                self.minerals_matched_to_history.append(mineral)
