import xml.etree.ElementTree as ET


class TempConverter:
    def convert_celsius_to_fahrenheit(self, Tcelsius):
        return 9/5 * Tcelsius + 32
    

class XmlParser:
    def __init__(self, tconverter):
        self.tconverter = tconverter

    def parse(self, file):
        tree = ET.parse(file)
        root = tree.getroot()
        for child in root:
            day = child.find('day').text
            temperature_in_celsius = int(child.find(
                'temperature_in_celsius').text)
            temperature_in_fahrenheit = round(
                self.tconverter.convert_celsius_to_fahrenheit(
                temperature_in_celsius), 1)
            print(f'{day}: {temperature_in_celsius} Celsius,\
 {temperature_in_fahrenheit} Fahrenheit')


converter = TempConverter()
forecast = XmlParser(converter)
forecast.parse("forecast.xml")
