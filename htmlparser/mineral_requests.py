#! python
import requests
import bs4
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.INFO)


class MineralHTMLParser:
    def __init__(self, mineral):
        self.mineral_name = mineral
        self.TEST_FILENAME = r'C:\Users\Sam\PycharmProjects\Mineral_ID_v2.0.1\htmlparser\test_quartz.txt'
        self.URL_BASE = 'http://www.mindat.org/search.php?search='
        self.soup = self.create_search_page()

        self.MINDATA_CLASS_NAME = 'mindatarow'
        self.ATT_CLASS_NAME = 'mindatath'
        self.VALUE_CLASS_NAME = 'mindatam2'
        self.attribute_catalog = ['Tenacity', 'Diaphaneity (Transparency)', 'Colour', 'Cleavage', 'Fracture',
                                  'Hardness (Mohs)', 'Lustre', 'Streak', 'Morphology', 'Pleochroism', 'Type',
                                  'Crystal System', 'Surface Relief', 'Formula', 'Density']
        self.mineral_data = {'Name': mineral}
        self.locate_physical_properties()

    def create_search_page(self):
        print(self.URL_BASE + self.mineral_name)
        res = requests.get(self.URL_BASE + self.mineral_name)
        return bs4.BeautifulSoup(res.content, "html.parser")

    def locate_physical_properties(self):
        data_rows = self.soup.find_all('div', {'class': self.MINDATA_CLASS_NAME})
        logging.info('site headers:\n%s', data_rows)
        for row in data_rows:
            for attribute in self.attribute_catalog:
                try:
                    if attribute in row.find('div', {'class': self.ATT_CLASS_NAME}).getText():
                        string = row.find('div', {'class': self.VALUE_CLASS_NAME}).getText()
                        string = string.encode('utf-8')
                        self.mineral_data.setdefault(attribute, string)
                except AttributeError:
                    pass
        for att in self.attribute_catalog:
            if att not in self.mineral_data.keys():
                self.mineral_data.setdefault(att, 'n/a')
        self.mineral_data.setdefault('Name', self.mineral_name)

    def create_text_html(self):
        res = requests.get(self.URL_BASE + self.mineral_name)
        soup = bs4.BeautifulSoup(res.text, "html.parser")
        with open(r'C:\users\sam\pycharmprojects\mineral_id_v2.0.1\htmlparser\test_quartz.txt', 'w') as f:
            f.write(str(soup))
