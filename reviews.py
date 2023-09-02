# Overivew
#In this exercise we will create a summary of wine reviews by country and write the data to a CSV file. This exercise is based on the 
#Kaggle Learn Pandas exercise 3.
#
#Create a Python program that reads in the data/winemag-data-130k-v2.csv.zip file. Create a summary of the data that contains 
#the name, number of reviews, and the average points for each unique country in the dataset. Write the summary data to a new 
#file in the data folder named reviews-per-country.csv.
#
#Example Output Data
#country	count	points
##US	54504	88.6
#France	22093	88.8
#Italy	19540	88.6
#Spain	6645	87.3
#Portugal	5691	88.3
#...	...	...
#Bosnia and Herzegovina	2	86.5
#Armenia	2	87.5
#Slovakia	1	87.0
#China	1	89.0
#Egypt	1	84.0
#Notes
#The csv file created by your program should be saved in the data folder.
#The csv file created by your program should be added, committed and pushed to GitHub.
#The column names should match the example above.
#The values in the points column should be rounded to 1 decimal point.


import pandas as pd

# Read in the wine reviews dataframe
reviews = pd.read_csv("data/winemag-data-130K-v2.csv.zip")

# build a new dataframe grouped by country with avg reviews per unique country, rename columns and then sort for correct output
avg_country_df = reviews.groupby("country").agg({"country": "count", "points": "mean"}).round(1)
avg_country_df_adjust = avg_country_df.rename(columns = {"country":"count"})
avg_country_df_adjust = avg_country_df_adjust.sort_values("count", ascending = False)
df = pd.DataFrame(avg_country_df_adjust)

# Write output to csv in the data folder
df.to_csv("data/reviews-per-country.csv")