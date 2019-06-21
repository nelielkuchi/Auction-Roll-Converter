import pandas as pd
import xml.etree.ElementTree as ET
import os
import re

#First get into XML File and extract register
#root = ET.parse('C:\\Users\\Gina\\Documents\\Master Thesis\\Programming\\Parser2.0\\AuctionRoll10.xml').getroot()
#print(root)
tree = ET.parse('C:\\Users\\Gina\\Documents\\Master Thesis\\Programming\\Parser2.0\\AuctionRoll10.xml')
root = tree.getroot()

#body = root.findall('.//body')
#r_names = []
#for child in body:
#     for subchild in child.find('.//date', './/row//cell'):
#          r_names.append(subchild.text)



path = 'C:\\Users\\Gina\\Documents\\Master Thesis\\Programming\\Parser2.0\\AuctionRoll10.xml'
dfcols = ['Date', 'Number & Product', 'Buyer', 'Price']
table = root.findall('.//table//row')
cell = root.findall('.//cell')

for elem in root.findall('.//date'):
    date = elem.get('value')
    #print(date)

for elem in root.findall('.//row'):
    for subelem in elem:
        cell = subelem.text
        #print(cell)

xml_data = [['hi', 'hi', 'hi', 'hi']
for i in cell]
df_xml = pd.DataFrame(xml_data, columns = dfcols)

print(df_xml)



#body = root.findall('.//body')
#div = root.findall('.body//div')
#date = root.findall('.//head//date')
#table = root.findall('.//table//row')
#row1 = root.findall('.//row')
#cell = root.findall('.//cell')
#print(date)
#print(div, date, table, row1, cell)
#xml_data = [[date.get('value'), row1, cell, cell]
#            for div in cell]
#df_xml = pd.DataFrame(xml_data, columns = dfcols)

#print(df_xml)

#dfcols = ['Date', 'Number & Product', 'Buyer', 'Price']
#df_xml = pd.DataFrame(columns = dfcols)
#root = ET.parse(path)
#div = root.findall('.//div')
#for div in div:
#    Date = div.find('date')
#    Number = div.find('row//cell') #>>LIKE JUPYTER NOTEBOOK
#    Buyer = div.find('row//cell//cell')
#    Price = div.find('row//cell//cell//cell')
#print(Date, Number, Buyer, Price)
#df_xml = df_xml.append(pd.Series([Date, Number, Buyer, Price], index=dfcols), ignore_index = True)



#print(len(tree.getroot()[0]))
#print(len(tree.getroot()))
#print(root)
#tag = root.tag
#print(tag)
#attribute = root.attrib
#print(attribute)

#for child in root:
#    print (body.tag)
#for child in root:
#    print(child.tag, child.attrib)

#print([elem.tag for elem in root.iter()]) ALL ELEMENTS IN xml

#for name in root.iter('name'):
#    print(name.attrib)

#for date in root.iter('date'):
#    print(date.tag,date.attrib)

###extracts date value from ALL date tags###
#for date in root.iter('date'):
#    date = date.get('value')
#    print(date)

#print(ET.tostring(root, encoding='utf-8'))

#for date in root.findall('./body/div/head/date')

#child = root[0]
#print(child.tag)
#grandchild = root[0][1]
#print(grandchild.tag)

#for child in root:
#    print(child.tag)
