import pandas as pd
import os
import numpy as np
import datetime


def getDataframe(path):
#declare the string columns
    str_columns=['Overall', 'Polarity', 'Response','Unit_Id','rub+buzz','thd']
    
##TODO:Append the rows in df
    def addRow(df,ls):
        """
        Given a dataframe and a list, append the list as a new row to the dataframe.
    
        :param df: <DataFrame> The original dataframe
        :param ls: <list> The new row to be added
        :return: <DataFrame> The dataframe with the newly appended row
        """
        numEl = len(ls)
        newRow = pd.DataFrame(np.array(ls).reshape(1,numEl), columns = list(df.columns))
        df = df.append(newRow, ignore_index=True)
    
        return df
##TODO:Clean all the data
    def df_replace(df):
#Data cleaning
        df['Overall']=df['Overall'].str.lower().str.replace('sin','').str.replace('1','').str.replace('\n','').str.replace(' ','').str.upper()
        df['Polarity']=df['Polarity'].str.lower().str.replace('polarity','').str.replace('\n','').str.replace(' ','').str.upper()
        df['Response']=df['Response'].str.lower().str.replace('response','').str.replace('\n','').str.replace(' ','').str.upper()
        df['Unit_Id']=df['Unit_Id'].str.lower().str.replace('unit n. ','').str.replace('good','').str.replace('bad','').str.replace('\n','').str.replace(' ','').str.upper()
        df['rub+buzz']=df['rub+buzz'].str.lower().str.replace('rub','').str.replace('+','').str.replace('buzz','').str.replace('rub+buzz','').str.replace('\n','').str.replace(' ','').str.upper()
        df['thd']=df['thd'].str.lower().str.replace('thd','').str.replace('\n','').str.replace(' ','').str.upper()
        df['Timestamp']=df['Timestamp'].str.lower().str.replace('am','').str.replace('pm','').str.rstrip().str.lstrip().str.replace('-','.').str.replace(':','.').str.upper()
        
##TODO:Discard non date-time formats and keep in datetime.datetime format
        for i,j in df['Timestamp'].iteritems():
            
            try:
                if len(j)==19:
                    try:
                        date=datetime.datetime.strptime(j, '%d.%m.%Y %H.%M.%S')
                        df.loc[i,'Timestamp']=date.date()
                    except ValueError:
                        date=datetime.datetime.strptime(j, '%Y.%m.%d %H.%M.%S')
                        df.loc[i,'Timestamp']=date.date()
                    
                else:
                    date=datetime.datetime.strptime(j, '%m.%d.%Y %H.%M.%S')
                    df.loc[i,'Timestamp']=date.date()
                    
                
            except ValueError:
                df=df.drop([df.index[i]])
                pass
                
        df=df.replace(to_replace=['GOOD', 'BAD'], value=[1, 0])
        numericCols=['Overall','Response', 'Polarity', 'rub+buzz', 'thd']
        df[numericCols]=df[numericCols].apply(pd.to_numeric, errors='ignore')

        return df

##TODO: Copy all the paths of text files    
    textFiles=[]
    for d in os.listdir(path):
        textFiles.append(os.path.join(path, d))
    
    
 
##Read and create df
    df=pd.DataFrame({'Overall':[],'Response':[],'Polarity':[],'rub+buzz':[],'thd':[],'Timestamp':[],'Unit_Id':[]})
    for i in range(len(textFiles)):
        G=open(textFiles[i],'r')    
        stringss=G.readlines()
        if len(stringss)==7:
            df=addRow(df,stringss)
   
        else:
            print(textFiles[i])
            continue
            
##Format the df        
    df[str_columns]=df[str_columns].astype(str)
    df=df_replace(df)

    return df
