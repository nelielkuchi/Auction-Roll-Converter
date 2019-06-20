import pandas as pd
import xml.etree.ElementTree as ET
import ctypes as ct

####DEFINE NODE####
def getvalueofnode(node):
    return node.text if node is not None else None

###DEFINING ROOT ELEMENT###
dfcols = ['Date', 'Product', 'Buyer', 'Price']
df_xml = pd.DataFrame(columns=dfcols)
tree = ET.parse("C:\\Users\\Gina\\Documents\\Master Thesis\\Programming\\Parser2.0\\test roll.xml")
root = tree.getroot()

for body in root:
    for div in body:
        date = div.find('.//date')
        product = div.find('.//row//cell')
        buyer = div.find('.//row//cell//cell')
        price = div.find('.//row//cell//cell//cell')

        df_xml = df_xml.append(
            pd.Series([getvalueofnode(date), getvalueofnode(product),
            getvalueofnode(buyer), getvalueofnode(price)], index=dfcols),
            ignore_index=True)
    print("----------")

print(df_xml)
