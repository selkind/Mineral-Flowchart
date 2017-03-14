#! python
import logging
from user_interface import UserInterface


logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


class UiOptions:

    def __init__(self, csv_sourcelist):
        self.name = ''
        self.dataSource = csv_sourcelist
        self.allAttributeSourceColumns = (1, len(self.dataSource[0]))
        self.handSampleSourceColumns = (1, 10)
        self.thinSectionSourceColumns = (7, 14)
        self.allAttributes = {}
        self.attributesForSampleType = []
        self.populate_all_attributes()

    def __str__(self):
        return self.name

    def change_hand_sample_source_columns(self, datasource_subset_start, datasource_subset_end):
        self.handSampleSourceColumns = (datasource_subset_start, datasource_subset_end)

    def change_thin_section_source_columns(self, datasource_subset_start, datasource_subset_end):
        self.thinSectionSourceColumns = (datasource_subset_start, datasource_subset_end)

    def populate_all_attributes(self):
        datasource_start = self.allAttributeSourceColumns[0]
        datasource_end = self.allAttributeSourceColumns[1]
        logging.debug(datasource_end)
        try:
            for attribute in range(datasource_start, datasource_end):
                self.allAttributes.setdefault(self.dataSource[0][attribute], [])
                for row in range(1, len(self.dataSource)):
                    separated_values = self.dataSource[row][attribute].split(',')
                    for attributeValue in separated_values:
                        if attributeValue.lower() not in self.allAttributes[self.dataSource[0][attribute]]:
                            self.allAttributes[self.dataSource[0][attribute]].append(attributeValue.lower())
                            self.allAttributes[self.dataSource[0][attribute]].sort()
        except IndexError:
            logging.critical('allAttributeSourceColumns range is invalid')

    def populate_attribute(self, source_columns):
        self.attributesForSampleType = []
        datasource_start = source_columns[0]
        data_source_end = source_columns[1]
        try:
            for attribute in range(datasource_start, data_source_end):
                self.attributesForSampleType.append(self.dataSource[0][attribute])
        except IndexError:
            logging.critical('SourceColumn range is invalid.')

    def populate_handsample_attributes(self):
        self.populate_attribute(self.handSampleSourceColumns)

    def populate_thinsection_attributes(self):
        self.populate_attribute(self.thinSectionSourceColumns)
