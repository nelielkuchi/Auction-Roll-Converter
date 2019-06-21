import pandas as pd
import xml.etree.ElementTree as ET

####DEFINE NODE####
def getvalueofnode(node):
    """return node text or None"""
    return node.text if node is not None else None
    ###Will get the value as a text in the end to insert the data into the dataframe
    ###if there is no data it returns None

###DEFINING ROOT ELEMENT###
dfcols = ['Date', 'Product', 'Buyer', 'Price'] ###nameing the columns of the dataframe (header of the table)
df_xml = pd.DataFrame(columns=dfcols) ###sets DataFrame to use the header as columns

###takes the test roll and parses it with ElementTree
tree = ET.parse('C:\\Users\\Gina\\Documents\\Master Thesis\\Programming\\Parser2.0\\test roll.xml')
###defines root as the root - Element from Test roll.xml
root = tree.getroot()

####GET DATA####
###iteration over body in root
for body in root:
    ###itertion over divs in body
    for div in body:
        date = div.find('.//date')
        rows = div.findall('.//row')
        for row in rows:
            cells = row.findall('.//cell')
            getvalueofnode(date)
            #print(cells)
            product = getvalueofnode(cells[0])
            buyer = getvalueofnode(cells[1])
            price = getvalueofnode(cells[-1])
            print(getvalueofnode(date))
            print(product)
            print(buyer)
            print(price)
