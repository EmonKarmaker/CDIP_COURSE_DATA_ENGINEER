import pandas as pd

# Load the CSV file into a DataFrame
file_path = 'D:/Emon Karmaker - data.csv'
df = pd.read_csv(file_path)



df['Period_Year'] = df['Period'].apply(lambda x: str(x)[:4])


group_mapping = {
    'Industry by financial variable (NZSIOC Level 1)': 'Category 1',
    'Industry by financial variable (NZSIOC Level 2)': 'Category 2'
}


df['Group_Category'] = df['Group'].map(group_mapping)


df_filtered = df[df['Data_value'] > 500]



df_filtered.loc[df_filtered['Series_reference'] == 'BDCQ.SF2QQCA', 'STATUS'] = 'A'



output_file_path = 'D:/class14824/transformed_data.csv'
df_filtered.to_csv(output_file_path, index=False)

