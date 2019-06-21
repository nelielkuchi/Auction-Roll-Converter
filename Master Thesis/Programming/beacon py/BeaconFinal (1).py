import os
import pandas as pd
import numpy as np
import re
import csv

def readAndWrite():
    ##Opening##
    ##Begrüßung##
    print('''Welcome to create your Beacon File. Please insert the name and the
          end of the data you want to parse (Example: .\dummydata.xlsx). This will
          take a moment.''')
    ##chose data to parse: name + '.xlsx' or '.xls'!##
    ##Angeben der Exceltabelle: Name + '.xlsx' oder '.xls'!##
    file = input()
    print('''Please wait for the next question.''')
    ##searches for infomation in database of collumns A, B, C, L + N##
    ##sucht informationen aus der Datenbank aus angegebenen Spalten##

    ##sets names and datatype for collumns##
    ##benennt Spalten um & Festlegen des Datentyps##
    dataExcel = pd.read_excel(
                    file, skiprows = 1, header = None,
                    index_col = None, usecols = "A, B:C , L:N",
                    names = ['Id' , 'Lastname' , 'Firstname' , 'viaf1' , 'viaf2' , 'viaf3'],
                    parse_dates = False, date_parser = None, na_values = None,
                    thousands = None, convert_float = True, converters = None,
                    dtype = object, true_values = None, flase_values = None,
                    engine = None, squeeze = False, delim_whitespace=True)
    df = pd.DataFrame(data = dataExcel)
    ##set collumns firstname and lastname together to fullname##
    ##Zusammenfügen der Spalten Lastname und Firstname zu Fullname##

    ##deletes old collumns of names##
    ##Löschen der alten Namensspalten##
    df['Fullname'] = df[['Lastname', 'Firstname']].apply(lambda x:
                    re.sub('/^[a-zàâçéèêëîïôûùüÿñæœ .-]*$/i', ' ', ','.join(x.map(str))) , axis=1)
    df = df[pd.notnull(df['Lastname'])]
    df = df.drop(['Lastname', 'Firstname'], axis=1)

    ##delets the NaN-Values##
    ##löschen der NaN-Values##
    df2 = pd.DataFrame.dropna(self = df, how = 'all', thresh = None,
                            subset = None, inplace = False)

    ##delets whitespace and NaN-Values in names##
    ##löschen der Leerzeichen und NaN-Values der Vornamen##

    ##saves collumns in correct order##
    ##Speichern der Spalten in richtiger Reihenfolge##
    df2 = df2.replace(r'\\n',' ', regex=True)
    df2.set_index('Id')
    df2 = df2[['Id', 'Fullname', 'viaf1', 'viaf2', 'viaf3']]

    ##runs over all lines to find NaN-Values##
    ##Durchgehen der Zeilen um NaN-Values zu filtern##

    ##sets lines together without NaN-Values##
    ##Zusammenfügen der Zeilen ohne NaN-Value##

    ##saves the txt file in correct order##
    ##abspeichern der txt in richtiger Reihenfolge##

    ##delets all questionmarks and tabs##
    ##löscht ? und leerzeichen/einrückungen am Zeilenende##
    for index, row in df2.iterrows():
        df2.dropna()
        lines = ''.join([str(row[0]), '|', str(row[1]), '|',
                        str(row[2]), '|', str(row[3]), '|', str(row[4])])
        f = open('relevant.txt', 'a', encoding = 'utf-8')
        f.write(str(lines).replace('?','').rstrip())
        f.write('\n')

    ##öffnen der txt als csv##
    ##opens relevant.txt as csv##

    ##renames the collumns and encodes it with ANSI##
    ##umbenennen der Spalten und encoding in ANSI##
    datacsv = pd.read_csv('relevant.txt', sep='|', header=None,
                            usecols=[0, 1, 2, 3, 4],
                            names=['id', 'name', 'viaf1', 'viaf2', 'viaf3'],
                            encoding='utf-8')
    df3 = pd.DataFrame(data=datacsv)

    df3 = df3.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

    ##check if ID is NaN, if True assign 0##
    ##überprüft ob ID ein NaN-Value ist und füllt dieses mit 0
    for index, row in df3.iterrows():
        if pd.isnull(df3.iloc[index, 0]) == True:
            row[0] = 0

        ##check if all viaf is null##
        ##überprüft ob alle viaf null sind##
        if ((pd.isnull(df3.iloc[index, 2])) == True and
            (pd.isnull(df3.iloc[index, 3])) == True and
            (pd.isnull(df3.iloc[index, 4])) == True):
            lines = ''.join([str(int(row[0])), '|', str(row[1]), '|'])
            f = open('daten.txt', 'a', encoding='utf-8')
            f.write(str(lines))
            f.write("\n")

        ##check if viaf1 exists##
        ##überprüft ob viaf1 vorhanden##
        if pd.notnull(df3.iloc[index, 2]) == True:
            lines = ''.join([str(int(row[0])),'|',str(row[1]),'|',str(row[2])])
            f = open('daten.txt', 'a', encoding ='utf-8')
            f.write(str(lines))
            f.write("\n")

    ##check if viaf 2 exists##
    ##überprüft ob viaf2 vorhanden##
        if pd.notnull(df3.iloc[index, 3]) == True:
            lines = ''.join([str(int(row[0])),'|',str(row[1]),'|',str(row[3])])
            f = open('daten.txt', 'a', encoding='utf-8')
            f.write(str(lines))
            f.write("\n")

    ##check if viaf3 exists##
    ##überprüft ob viaf3 vorhanden##
        if pd.notnull(df3.iloc[index, 4]) == True:
            lines = ''.join([str(int(row[0])),'|',str(row[1]),'|',str(row[4])])
            f = open('daten.txt', 'a', encoding='utf-8')
            f.write(str(lines))
            f.write("\n")


def creatHeader():
##opens new txt file to save header in it##
##öffnet neue txt Datei und speichert Header darin##
    with open('header.txt', 'a', encoding ='utf-8') as f:

##writes header which is saved as string##
##speichert angegeben Header als string Value (alles innerhalb ''' kann geändert werden)##
        f.write('''#FORMAT: BEACON
#PREFIX: http://www.stuttgart.de/hi/gnt/dsi2
#VERSION: 0.1
#TARGET: http://www.uni-stuttgart.de/hi/gnt/dsi2/index.php?table_name=dsi&function=details&where_field=id&where_value={ID}
#FEED: http://www.uni-stuttgart.de/hi/gnt/aktuell/dsi_beacon_file.txt
#LINK: http://www.w3.org/2000/01/rdf-schema#seeAlso
#CREATOR: Prof. Dr. Klaus Hentschel < klaus.hentschel@hi.uni-stuttgart.de>
#CONTACT: Section for History of Science & Technology, History Department, University of Stuttgart, Keplerstrasse 17 in D- 70174 Stuttgart K II: room 8.027 phone +49 / 711 / 685-82313 or -82312 fax +49 / 711 / 685-82767 http://www.uni-stuttgart.de/hi/gnt/hentschel/
#MESSAGE: index of scientific illustrators having been active mainly between 1450 and 1950 (English)
#DESCRIPTION: index of scientific illustrators (English)
#INSTITUTION: University of Stuttgart Database of Scientific Illustrators. 1450 - 1950
#NAME: Database of Scientific Illustrators. 1450 - 1950 (DSI)
#TIMESTAMP: 2018-03-01T00:00:00
#UPDATE: monthly
#REVISIT: 2018-04_01T00:00:00
#EXAMPLES: 8|6345
#REMARK:
''')
        f.close

def setTogether():
    ##sets header.txt and daten.txt together and saves it##
    ##speichert Header.txt und daten.txt zusammen in einer txt##
    filenames = ['header.txt' , 'daten.txt']
    with open('BeaconDatei.txt', 'w', encoding='utf-8') as outfile:
        for fname in filenames:
            with open(fname, encoding='utf8') as infile:
                outfile.write(infile.read())


readAndWrite()

print('Do you want to creat a header and set a whole Beacon File together? Type Yes or No')
answer = input()
if answer == 'Yes':
    creatHeader()
    setTogether()

if answer == 'No':
    exit()

else:
    exit()
