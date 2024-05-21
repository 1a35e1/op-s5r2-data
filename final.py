import csv
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

from lib.cell import extract_criteria_data

FOLDER = 'tmp'

# remove the .tmp directory and create a new one
if os.path.exists(FOLDER):
  os.system(f'rm -rf {FOLDER}')
  
os.mkdir(FOLDER)

# Read the raw data file
data = []
with open('data/cycle-22-final-scores.csv', 'r') as file:
  reader = csv.reader(file)
  for row in reader:
    # Skip the first row
    if row[0] == 'Title':
      continue
    
    # Map the row to a dictionary based on the headers
    data.append({
      'title': row[0],
      'proposal_url': row[1],
      'mission': row[2],
      'total': row[3],
      'rubric_results': row[4],
    })

  # Convert the data to a pandas dataframe
  df = pd.DataFrame(data)

# Get all the unique missions in the file
missions = df['mission'].unique()


# Dump results of each mission to a csv file
for mission in missions:
  # convert mission to a file name, also replace / with -
  key = mission.replace('/', '-').replace(' ', '-').lower()
  
  # Filter the dataframe by mission  
  df.loc[df['mission'] == mission].to_csv(f'{FOLDER}/{key}.csv', index=False)
  
  
# Count number of rows for each mission in the df
total_rows = df['mission'].value_counts()

# => Plot, Entries by mission
plt.figure(figsize=(20, 12))

bars = plt.bar(total_rows.index, total_rows.values)
plt.xlabel('Mission', fontsize=12)
plt.ylabel('Number of submissions', fontsize=12)
plt.title('Final entries scored per Mission', fontsize=18)
plt.xticks(rotation=45, ha='right')

# Add counts on top of the bars
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.5, int(yval), ha='center', va='bottom')


plt.tight_layout()
plt.savefig('plots/final-entries-per-mission.png')

print(total_rows)


# Create an empty dataframe to store the expanded data
master_list = []

# iterate over each row in the dataframe
for index, row in df.iterrows():
  
  # Split the rubric results by the delimiter
  criteria_data = extract_criteria_data(row['rubric_results'])
  criteria_scored = len(criteria_data)
  
  # Mark the row as not scored when we have no rubric_results
  if criteria_scored == 0:    
    master_list.append({
      'proposal_url': row['proposal_url'],
      'title': row['title'],
      'total': row['total'],
      'mission': row['mission'],
      'criteria_name': 'Not Scored',
      'criteria_average': 0,
      'criteria_total': 0,
      'criteria_scored': criteria_scored
    })    
  
  # Add the criteria data to the new dataframe
  for criteria in criteria_data:  
    master_list.append({
      'proposal_url': row['proposal_url'],
      'title': row['title'],
      'total': row['total'],
      'mission': row['mission'],
      'criteria_name': criteria['name'],
      'criteria_average': criteria['average'],
      'criteria_total': criteria['total'],
      'criteria_scored': criteria_scored
    })
  


df2 = pd.DataFrame(master_list)  
# print(df2)

# save the new dataframe to a csv file
df2.to_csv('final-scores-expanded.csv', index=False)