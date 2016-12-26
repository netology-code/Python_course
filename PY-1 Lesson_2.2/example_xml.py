import xml.etree.ElementTree as ET

tree = ET.parse('GodFather.xml')

for e in tree.iter():
	print(e)