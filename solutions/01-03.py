"""
Exercises
---------
load the mpg.csv data set
return a dataframe of the model name sorted in order of descending weight
return a dataframe sorted by origin and model name (name) in ascending order for both

"""

mpg = pd.read_csv('./data/mpg.csv')

mpg_sorted1 = mpg.sort_values(by='weight', ascending=False)
mpg_sorted2 = mpg.sort_values(by=['origin', 'name'], ascending=[True, True])

mpg_sorted1.head(10)
# mpg_sorted2.head(10)