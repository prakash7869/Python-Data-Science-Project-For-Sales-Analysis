import pandas as pd                 #These lines import necessary libraries for data manipulation and visualization in Python. pandas is used for data manipulation, 
                                    #numpy for numerical operations, and plotly for creating interactive plots and graphs.
import numpy as np
import plotly.express as px
import plotly.graph_objects as go



prakashdata = pd.read_csv("E:/Prakash/youtube/apple_products.csv")  #This line reads a CSV file named "apple_products.csv" located at the specified file path and stores its contents in a pandas DataFrame named prakashdata. 
# print(prakashdata.head())                                         #This assumes that the CSV file contains data related to Apple products.

# print(prakashdata.describe())
# print(prakashdata.isnull().sum())

highest_rated=prakashdata.sort_values(by=["Star Rating"],ascending=False) #This line sorts the prakashdata DataFrame in descending order based on the "Star Rating" column. It is arranging the data in such a way that the products with the highest star ratings will be at the top.
highest_rated=highest_rated.head(10)              #This line selects the top 10 rows from the highest_rated DataFrame. It means you are interested in the top 10 highest-rated Apple products.
# print(highest_rated['Product Name'])


# iphone=highest_rated['Product Name'].value_counts()
# label=iphone.index
# counts=highest_rated["Number Of Ratings"]
# figure=px.bar(highest_rated, x=label, y=counts, title="Number Of ratings of highest rated Iphone")
# figure.show()

figure=px.scatter(data_frame=prakashdata, x="Number Of Ratings", y="Sale Price", size="Discount Percentage", trendline="ols", #This line creates a scatter plot using Plotly Express (px.scatter). It uses data from the prakashdata DataFrame and sets the "Number Of Ratings" column as the x-axis, "Sale Price" as the y-axis, and "Discount Percentage" as the size of the markers. It also adds a trendline to the plot using ordinary least squares (OLS) regression, and sets a title for the plot.
                  title="Relationship between sale price and number of ratings of iphones")
           
figure.show() #Finally, this line displays the created scatter plot with the specified attributes using Plotly's interactive plotting capabilities. It opens a new window or renders the plot in your development environment, depending on where you are running the code.

