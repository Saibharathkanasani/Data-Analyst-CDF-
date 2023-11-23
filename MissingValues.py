import pandas as pd
# Specify the data types for problematic columns
#dtype_options = {'column7': str, 'column9': str, 'column26': str, 'column35': str, 'column36': str,
#                 'column37': str, 'column38': str, 'column39': str, 'column40': str, 'column48': str,
#                 'column49': str, 'column50': str, 'column51': str}

df=pd.read_csv('Combineddata.csv', low_memory=False)


#Define the paraphase to fill the blank value to None
df.replace('', None, inplace=True)

# If you want to replace NaN values as well, you can use the following line:
fill_value="None"
df.fillna(value=fill_value, inplace=True)


#Save the modified csv file to new csv file 
df.to_csv('CleanedCombineddata1.csv',index=False)