import xml.etree.ElementTree as ET


class XmlTreeHelper:
    def add_tags_with_text(self, parent, tags):
        elements = []
        for tag in tags:
            element = ET.SubElement(parent, tag)
            element.text = tags[tag]
            elements.append(element)
        return elements


root = ET.Element('shop')

category = ET.SubElement(root, 'category', {'name': 'Vegan Products'})
product1 = ET.SubElement(category, 'product', {'name': 'Goodmorning Sunshine'})
product2 = ET.SubElement(category, 'product', {'name': 'Spaghetti'})
product3 = ET.SubElement(category, 'product', {'name': 'Almond Milk'})

xml_tree = XmlTreeHelper()

xml_tree.add_tags_with_text(product1, {
    'type': 'cereals',
    'producer': 'Foods Limited',
    'price': '9.90',
    'currency': 'USD'
})

xml_tree.add_tags_with_text(product2, {
    'type': 'pasta',
    'producer': 'Programmers Eat Past',
    'price': '14.90',
    'currency': 'EUR',
})

xml_tree.add_tags_with_text(product3, {
    'type': 'beveages',
    'producer': 'Drinks4Coders',
    'price': '19.50',
    'currency': 'USD'
})


tree = ET.ElementTree(root)
tree.write('shop.xml', 'UTF-8', True)
