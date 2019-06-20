import pandas as pd
import xml.etree.ElementTree as ET

####DEFINE NODE####
def getvalueofnode(node):
    """return node text or None"""
    return node.text if node is not None else None

###DEFINING ROOT ELEMENT###
tree = ET.parse('C:\\Users\\Gina\\Documents\\Master Thesis\\Programming\\Parser2.0\\test roll.xml')
dfcols = ['Date', 'Product', 'Buyer', 'Price']
df_xml = pd.DataFrame(columns=dfcols)

####GET DATA####
for node in tree.getroot():
    date = node.find('.//date')
    product = node.find('.//row//cell')
    buyer = node.find('.//row//cell//cell')
    price = node.find('.//row//cell//cell//cell')

####PARSES DATA INTO DATAFRAME####
    df_xml = df_xml.append(
            pd.Series([getvalueofnode(date), getvalueofnode(product),
            getvalueofnode(buyer), getvalueofnode(price)], index=dfcols),
            ignore_index=True)

####PRINTS DATAFRAME###
    print(df_xml)

#print(date)
#print(product)
#print(buyer)
#print(price)
