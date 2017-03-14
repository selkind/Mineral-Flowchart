# Creates a generic mineral class with physical properties of minerals
class Mineral:
    def __init__(self, attribute_headers, mineral_values):
        self.fitsSelectedAttributes = True
        self.name = mineral_values[0]
        self.allInfo = {}
        self.build_allinfo(attribute_headers, mineral_values)

    def __str__(self):
        return self.name

    def build_allinfo(self, attribute_headers, mineral_values):
        for column in range(len(mineral_values)):
            attribute = attribute_headers[column]
            value = mineral_values[column]
            self.allInfo.setdefault(attribute, value.lower())
