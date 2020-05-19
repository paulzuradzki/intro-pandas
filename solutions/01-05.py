"""
### Exercises
* load the mpg.csv data set
* create a column called 'pw_ratio' and calculate the power to 10-pound weight ratio
    * power-to-10lb-weight ratio = (horsepower / weight)*10
* sort the data set from highest to lowest power-weight ratio
* create a dataframe for each country of origin (fitler using boolean indexing)
     * use value_counts() on 'origin' field to determine the unique values
* for each origin country, determine the model with the highest power-weight ratio and ratio
   * 
   * this is a manual application of Group By
   * check your answer against the result of `mpg_df.groupby(['origin'])[['pw_ratio']].max().T`
   * or check against:
    ```python
    max_ratio_list = mpg.groupby(['origin'])[['pw_ratio']].max()['pw_ratio']
    mpg.loc[mpg['pw_ratio'].isin(max_ratio_list), ['origin', 'name', 'pw_ratio']]
    ```

"""

mpg = pd.read_csv('./data/mpg.csv')
mpg['pw_ratio'] = mpg['horsepower'] / mpg['weight']*10

mpg_sorted = mpg.sort_values(by='pw_ratio', ascending=False)
# mpg_sorted

countries = mpg['origin'].value_counts().index.tolist()
print('country list:', countries, end='\n\n')

usa = mpg[mpg['origin']=='usa']
japan = mpg[mpg['origin']=='japan']
europe = mpg[mpg['origin']=='europe']

# take first value after sorting
max_pw_usa = usa.sort_values(by='pw_ratio', ascending=False).loc[:,['origin', 'name', 'pw_ratio']].head(1)
max_pw_japan = japan.sort_values(by='pw_ratio', ascending=False).loc[:,['origin', 'name', 'pw_ratio']].head(1)
max_pw_europe = europe.sort_values(by='pw_ratio', ascending=False).loc[:,['origin', 'name', 'pw_ratio']].head(1)

for df in [max_pw_usa, max_pw_japan, max_pw_europe]:
    print(df.to_markdown(), end='\n\n')