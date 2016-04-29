'''
Column mapping python script that translates column headers based on a saved mapping schema. 

The script also translates the Local's provided Member Types to the 7 standard values. 

Column order is flexible as long as all mapped columns are present. 


-author- Endrin Tushe
-date- 4/29/16

'''

import pandas as pd # import pandas library

# Read mapping table and original file using pandas 

ColTable = pd.read_excel('401Cols.xlsx',header=None)
MemTypes = pd.read_excel('401Mems.xlsx',header=None)

OrigFile = pd.read_excel('401File.xlsx')


  
oldCols = []
newCols = []
oldMemVal = []
newMemVal = []

fileCols = OrigFile.columns.tolist() #pulls out the original file's column headers

#function creates key value pair from two lists 

def MappingSchema(oldCols,newCols,oldMemVal,newMemVal):
    for row in ColTable[0]:
        oldCols.append(row.upper())
    for row in ColTable[1]:
        newCols.append(row)
    for row in MemTypes[0]:
        oldMemVal.append(row.upper())
    for row in MemTypes[1]:
        newMemVal.append(row)
    
MappingSchema(oldCols,newCols,oldMemVal,newMemVal)

#a dicitionary is created based on the saved mapped schema on file
columnDict = dict(zip(oldCols,newCols))
memDict = dict(zip(oldMemVal,newMemVal))


#There may be situations when the column order in the mapped schema may differ from the file that is actually uploaded. To accomodate for that, this script iterates over each of column headers in the uploaded file and compares it to the Key/Value pairs in the columnDict dicitionary.  If there is a match in the original file and mapped schema dicitionary the new standard column name is applied. 

OrigFile.rename(columns = {k: columnDict[k] for k in fileCols if k in columnDict},inplace=True)

#The script below iterates over the values in the MemberSubType column.  It appends a MemberTypeName column to the file and populates it based on the mapping schema we have on file for MemberTypes.

MemTypeList = []

for index,row in OrigFile.iterrows():
    if row['MemberSubTypeName'] in memDict:
         MemTypeList.append(memDict[row['MemberSubTypeName']])

OrigFile['MemberTypeName'] = MemTypeList

#File is saved as tab delimited and is ready to be processed by the the portal.
OrigFile.to_csv("Standard401v10.txt", sep='\t',index=False)



