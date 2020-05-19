"""
Exercises
---------
load the flights.csv data set into a dataframe
identify the total number of passengers for the year 1960
hint: boolean index for year condition, use .loc to get passenger column, then .sum()
identify the average/mean monthly number of passengers for the year 1955
"""

flights = pd.read_csv('./data/flights.csv')

x_sum = flights.loc[flights['year']==1960, 'passengers'].sum()
x_mean = flights.loc[flights['year']==1955, 'passengers'].mean()

print(f'1960 passenger sum: {x_sum}')
print(f'1955 passenger mean: {x_mean}')