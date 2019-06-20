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
        ###searching through div for the "Date"-Tag and storing the value in date
        date = div.find('.//date')
        #iteration over cells in body
        for cells in body:
            ###searching through div for 'cell'-Tag and storing it in text (debugging reasons)
            text = div.findall('.//row/cell')
            ###text returns the cell structure of the Document
            ###USUALLY TAGS ARE LISTE OBJECTS IN ELEMENTTREE!
            #print(text)
            ###Taking the information of the cells to insert them into the DataFrame
            ###USing the Taglist that is returned by the findall function
            product = text[3]
            buyer = text[4]
            price = text[5]
####PARSES DATA INTO DATAFRAME####
###setting up the dataframe, inserting the values of the cells and date
        df_xml = df_xml.append(
                pd.Series([getvalueofnode(date), getvalueofnode(product),
                getvalueofnode(buyer), getvalueofnode(price)], index=dfcols),
                ignore_index=True)

####PRINTS DATAFRAME###
#printing out the dataframe

    #print(ET.tostring(div))
    #print('--------------------')
print(df_xml)

#debugging printing to see if text gives the arguments I need
print(getvalueofnode(date))
print(getvalueofnode(product))
print(getvalueofnode(buyer))
print(getvalueofnode(price))
