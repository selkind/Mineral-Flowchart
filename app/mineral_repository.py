from mineral_class import Mineral
import os
import csv


class MineralRepository:

    def __init__(self):
        self.CSVinList = []
        self.AllMinerals = []
        self.read_data_source()
        self.populate_all_minerals()

    def read_data_source(self):
        realpath = os.path.dirname(os.path.realpath(__file__))
        filelocation = realpath + '\database.csv'
        with open(filelocation) as f:
            reader = csv.reader(f)
            for row in reader:
                self.CSVinList.append(row)

    def populate_all_minerals(self):
        attribute_headers = self.CSVinList[0]
        for row in range(1, len(self.CSVinList)):
            new_mineral = Mineral(attribute_headers, self.CSVinList[row])
            self.AllMinerals.append(new_mineral)
