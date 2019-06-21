import pandas as pd
import xml.etree.ElementTree as ET
import os
import re
import csv

###DEFINING ROOT ELEMENT###
tree = ET.parse('C:\\Users\\Gina\\Documents\\Master Thesis\\Programming\\Parser2.0\\AuctionRoll10.xml')
root = tree.getroot()
div = root.findall('.//div')
dfcols = ['Date','Product', 'Buyer', 'Price']
###SPATANS ANSATZ###
xml_lines = []
xml_line = []
count = 0
if count == 0:
    for member in root.findall('.//date'):
        date = member.get('value')
        xml_line.append(date)
        #print(xml_line)
        count = count + 1
        for elem in root.findall('.//row//cell'):
            cell = elem.text
            xml_line.append(cell)
            #print(xml_line)
            count = count + 1
        xml_lines.append(xml_line)
        xml_line = []


###TRY TO COPY DATE AND CELL INTO DATAFRAME###
xml_data = [xml_lines
            for div in root ]
df_xml = pd.DataFrame(xml_data, columns = dfcols)
#print(df_xml)
print(xml_lines)
