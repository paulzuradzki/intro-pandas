"""
load the ./data/planets.csv data set using pd.read_csv() into a dataframe named planets_df
display the first 5 records
dispay the first 10 records
display the last 5 records
print each file name in the /data directory using a os.listdir() and a for loop
bonus: display the filename and column names for each file in data/
    hint: loop through each dataframe in ./data/* directory using os.listdir
    read the dataset into a dataframe
    use df.columns
"""

data_dict = {'a': [1,2,3], 'b': [4,5,6]}
df = pd.DataFrame(data_dict)

data_lol = [[1,4], [2,5], [3,6]]
df = pd.DataFrame(data_lol, columns=['a', 'b'])

df.head()
df.head(10)
df.tail(5)

for fname in os.listdir('data'): 
    if fname.endswith('.csv'):
        print(fname)
        fpath = os.path.join('data', fname)
        x_df = pd.read_csv(fpath, nrows=5)
        print(x_df.columns.tolist(), end='\n\n')    

del x_df
del df