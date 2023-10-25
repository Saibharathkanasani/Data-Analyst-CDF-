import pandas as pd
df = pd.read_csv('Georgia_Combined_Cleaned.csv')

# Define a function to parse the key-value pairs
def parse_details(details):
    if pd.isna(details):
        return {}
    pairs = details.split('; ')
    details_dict = {}
    for pair in pairs:
        parts = pair.split(': ')
        key = parts[0]
        value = ': '.join(parts[1:])
        details_dict[key] = value
    return details_dict

# Apply the parsing function to the 'Additional Details' column
df['Additional Details'] = df['Additional Details'].apply(parse_details)

# Expand the dictionary into separate columns
df = pd.concat([df.drop(['Additional Details'], axis=1), df['Additional Details'].apply(pd.Series)], axis=1)

# Save the modified DataFrame to a new CSV file
df.to_csv('Georgia_Combined_Cleaned_data.csv', index=False)

