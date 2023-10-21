import pandas as pd
import numpy as np
from data_preprocessing import data_preprocess
from mlxtend.preprocessing import TransactionEncoder

def feature_engineering():
        data = data_preprocess()
        records = []
        for i in range(0, data.shape[0]):
                records.append([str(data.values[i,j]) for j in range(0, data.shape[1]) if data.values[i][j] is not np.nan])
        te = TransactionEncoder()
        te_data = te.fit(records).transform(records)
        df = pd.DataFrame(te_data,columns=te.columns_)
        df.to_csv("students_performance_prediction.csv",index=False)
        return data

feature_engineering()
