import  pandas as pd

def loading_data():
    data = pd.read_csv("Market_Basket_Optimisation.csv",header=None)
    return data

loading_data()
