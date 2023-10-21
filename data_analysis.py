from loading_data import loading_data

def data_analysis():
    data = loading_data()
    print (data.head())
    print (data.tail())
    print (data.describe())
    print ("Rows     : " ,data.shape[0])
    print ("Columns  : \n" ,data.shape[1])
    print ("Total no of Unique Features : \n" ,df.stack().nunique())
    return data

data_analysis()
