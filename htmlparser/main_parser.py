from htmlparser.mineral_requests import MineralHTMLParser
import csv


master_atts = ['Name', 'Tenacity', 'Diaphaneity (Transparency)', 'Colour', 'Cleavage', 'Fracture',
                                  'Hardness (Mohs)', 'Lustre', 'Streak', 'Morphology', 'Pleochroism', 'Type',
                                  'Crystal System', 'Surface Relief', 'Formula', 'Density']

with open('C:\users\sam\pycharmprojects\mineral_id_v2.0.1\htmlparser\mineral_names.txt', 'r') as names:
    nameslist = names.read().split('\n')

with open('C:\users\sam\desktop\min_test.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=master_atts, delimiter=',', lineterminator='\n')
    writer.writeheader()
    for i in range(len(nameslist)):
        new_min = MineralHTMLParser(nameslist[i])
        writer.writerow(new_min.mineral_data)
