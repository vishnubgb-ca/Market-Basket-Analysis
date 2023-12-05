import matplotlib.pyplot as plt
from data_preprocessing import data_preprocess
import seaborn as sns
import plotly.express as px
import squarify
import pandas as pd

def data_visualization():

    data = data_preprocess()
    value_counts = data.stack().value_counts()
    # Select the top 10 unique values and their counts
    unique_values = value_counts.index[:10]  # Get the top 10 unique values
    value_counts_top_10 = value_counts.values[:10]  # Get the counts for the top 10 unique values




    fig = px.bar(x=unique_values, y=value_counts_top_10, labels={'x': 'Products', 'y': 'Counts'},
                 title='Top 10 Products', text=value_counts_top_10)
    fig.update_layout(template='plotly_dark')
    #fig.update_layout(plot_bgcolor = "black")
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=False)
    fig.write_image(f"bar.jpg")
    # Create a bar graph
    # plt.figure(figsize=(18,16))
    # plt.bar(unique_values, value_counts_top_10)
    # plt.xlabel("Products")
    # plt.ylabel("Counts")
    # plt.title("Top 10 Products")
    # plt.xticks(rotation=90)
    # plt.show()

    top15items = pd.DataFrame(data.stack().value_counts().head(15))
    top15items = top15items.reset_index()
    top15items.columns = ["Itemname","Frequency"]
    labels = top15items["Itemname"]
    sizes = top15items["Frequency"]
    fig = px.pie(names=labels, values=sizes, title='Most frequently purchased items')
    fig.update_traces(textposition='inside', textinfo='percent+label')
    fig.update_layout(template='plotly_dark')
    fig.write_image(f"pie.jpg")
    # plt.figure(figsize=(15,13))
    # plt.pie(sizes,labels=labels)
    # plt.show()
    
    top20items = pd.DataFrame(data.stack().value_counts().head(20))
    top20items = top20items.reset_index()
    top20items.columns = ["Itemname","Frequency"]
    labels = top20items["Itemname"]
    sizes = top20items["Frequency"]
    df = pd.DataFrame({'labels': labels, 'sizes': sizes})
    
    fig = px.treemap(df, path=['labels'], values='sizes',
                     color_continuous_scale='Spectral', title='Top 20 Products')
    
    fig.update_layout(width=800, height=500)
    fig.update_layout(template='plotly_dark')
    #fig.update_layout(plot_bgcolor = "black")
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=False)
    fig.write_image(f"square.jpg")
    
    # fig = plt.figure(figsize=(16,10))
    # colors = sns.color_palette("Spectral",20)
    # squarify.plot(sizes, label=labels, color =  colors)
    # plt.title("Top 20 Products")
    # plt.show()
    
    return data

data_visualization()
