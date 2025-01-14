
# Creating a scatter plot of 'year' vs 'total_cases' in the DataFrame 'df_dengue'.
df_dengue.plot.scatter('year','total_cases')

# Creating a scatter plot of 'weekofyear' vs 'total_cases' in the DataFrame 'df_dengue'.
df_dengue.plot.scatter('weekofyear','total_cases')

# Creating a new DataFrame named 'new' that contains only the columns 'total_cases' and 'city' from 'df_dengue'.
new = df_dengue[['total_cases','city']].copy()

# Creating histograms of the 'total_cases' column in 'new' separated by the values in the 'city' column.
new.hist(by="city")