import pandas as pd
import xml.etree.ElementTree as ET

####DEFINE NODE####
def get_value(node):
    """return node text or None"""
    return node.text if node is not None else None
    ###Will get the value as a text in the end to insert the data into the dataframe
    ###if there is no data it returns None

###DEFINING ROOT ELEMENT###
dfcols = ['Date', 'Product', 'Buyer', 'Price'] ###nameing the columns of the dataframe (header of the table)
df_xml = pd.DataFrame(columns=dfcols) ###sets DataFrame to use the header as columns

###takes the test roll and parses it with ElementTree
###defines root as the root - Element from Test roll.xml
tree = ET.parse('C:\\Users\\Gina\\Documents\\Master Thesis\\Programming\\Parser2.0\\test roll.xml')
root = tree.getroot()

for body in root:
    ###itertion over divs in body
    for div in body:
        ###searching through div for the "Date"-Tag and storing the value in date
        ###searching for the "Cell"-Tags and storing value in cell
        date = div.find('.//date')
        cell = div.findall('.//cell')
        print(cell)
        ###takes the date and iterates over the cells
        for cell in table:
            #print(date)
            #print(cell)
            #print(get_value(date))
            #print(get_value(product))
            #print(get_value(buyer))
            #print(get_value(price))

    #for date in range(len(text)):
        #print(date)


####PARSES DATA INTO DATAFRAME####
###setting up the dataframe, inserting the values of the cells and date
            #df_xml = df_xml.append(
            #        pd.Series([get_value(date), get_value(product),
            #        get_value(buyer), get_value(price)], index=dfcols),
            #        ignore_index=True)

####PRINTS DATAFRAME###
#printing out the dataframe

    #print(ET.tostring(div))
    #print('--------------------')
        #print(df_xml)

#debugging printing to see if text gives the arguments I need
#print(getvalueofnode(date))
#print(getvalueofnode(product))
#print(getvalueofnode(buyer))
#print(getvalueofnode(price))
