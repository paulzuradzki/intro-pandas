"""
### Exercises
* load the diamonds.csv data set
* identify the distribution for the 'cut' variable with counts by value
* identify the percentage distribution
* add the `dropna=False` argument to make sure there are no null values
"""

diamonds = pd.read_csv('./data/diamonds.csv')

vc1 = diamonds['cut'].value_counts()
vc2 = diamonds['cut'].value_counts(normalize=True)
vc3 = diamonds['cut'].value_counts(normalize=True, dropna=False)

print(vc1, end='\n\n')
print(vc2, end='\n\n')
print(vc3)