import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

prakashdata = pd.read_csv("E:/Prakash/youtube/apple_products.csv")
# print(prakashdata.head())

# print(prakashdata.describe())
# print(prakashdata.isnull().sum())

highest_rated=prakashdata.sort_values(by=["Star Rating"],ascending=False)
highest_rated=highest_rated.head(10)
# print(highest_rated['Product Name'])
# iphone=highest_rated['Product Name'].value_counts()
# label=iphone.index
# counts=highest_rated["Number Of Ratings"]
# figure=px.bar(highest_rated, x=label, y=counts, title="Number Of ratings of highest rated Iphone")
# figure.show()

figure=px.scatter(data_frame=prakashdata, x="Number Of Ratings", y="Sale Price", size="Discount Percentage", trendline="ols",
                  title="Relationship between sale price and number of ratings of iphones")
           
figure.show()

