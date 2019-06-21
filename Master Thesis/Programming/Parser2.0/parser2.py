import pandas as pd
import xml.etree.ElementTree as ET
import os
import re
import csv

###DEFINING ROOT ELEMENT###
tree = ET.parse('C:\\Users\\Gina\\Documents\\Master Thesis\\Programming\\Parser2.0\\test roll.xml')
root = tree.getroot()

###SET COLUMNS FOR DATAFRAME###
dfcols = ['Date','Product', 'Buyer', 'Price']
div = root.findall('.//div')
body = root.findall('.//body')
count = 0

if count == 0:
    for member in root.findall('.//date'):
        date = member.get('value')
        count = count + 1
    for elem in root.findall('.//row//cell'):
        cell = elem.text
        count = count + 1
        print(cell)


###TRY TO COPY DATE AND CELL INTO DATAFRAME###
xml_data = [[date, cell[0] , cell[1], cell[2]]
            for div in root ]
df_xml = pd.DataFrame(xml_data, columns = dfcols)
#print(df_xml)
print(cell)





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
