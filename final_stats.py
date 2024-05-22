import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# read csv into pandas dataframe
df = pd.read_csv('final-scores-expanded.csv')

# # => Average Total Scores per Mission
# avg_scores_per_mission = df.groupby('mission')['total'].mean().sort_values()
# plt.figure(figsize=(20, 12))
# avg_scores_per_mission.plot(kind='barh', color='lightgreen')
# plt.xlabel('Average Total Score')
# plt.ylabel('Mission')
# plt.title('Average Total Scores per Mission')
# plt.grid(True)
# plt.savefig('plots/final_average_total_scores_per_mission.png')

# # Distribution, Criteria Scores per Mission
# plt.figure(figsize=(20, 12))
# df.boxplot(column='criteria_average', by='criteria_name', grid=True, vert=False)
# plt.xlabel('Criteria Average Score')
# plt.ylabel('Criteria Name')
# plt.title('Distribution of Criteria Average Scores')
# plt.suptitle('')
# plt.savefig('plots/final_distribution_criteria_average_scores.png')

# # Top proposals by total score
# top_proposals = df.groupby('title')['total'].mean().sort_values(ascending=False).head(10)
# plt.figure(figsize=(20, 12))
# top_proposals.plot(kind='barh', color='orange')
# plt.xlabel('Average Total Score')
# plt.ylabel('Proposal Title')
# plt.title('Top 10 Proposals by Average Total Score')
# plt.grid(True)
# plt.savefig('plots/final_top_10_proposals_by_total_score.png')




# # => Identify Top Scoring Criteria
# average_criteria_scores = df.groupby('criteria_name')['criteria_average'].mean().sort_values(ascending=False)

# # Plot the average scores for each criteria
# plt.figure(figsize=(20, 12))
# average_criteria_scores.plot(kind='bar', color='skyblue')
# plt.xlabel('Criteria Name')
# plt.ylabel('Average Score')
# plt.title('Average Scores for Each Criteria')
# plt.xticks(rotation=90)
# plt.grid(True)
# plt.tight_layout()
# plt.savefig('plots/final_average_scores_for_each_criteria.png')


# => Heatmap of Criteria Scores for Builder Category Missions
# Filter the data to include only rows where the mission contains "Builder"
builder_data = df[df['mission'].str.contains("Builder", case=False, na=False)]
builder_heatmap_data = builder_data.pivot_table(index='title', columns='criteria_name', values='criteria_average', aggfunc='mean')
# Plot heatmap without annotations due to a potential issue with the size of the annotations
plt.figure(figsize=(16, 14))
sns.heatmap(builder_heatmap_data, cmap='viridis')
plt.title('Heatmap of Criteria Scores for Builder Category Missions')
plt.tight_layout()
plt.savefig('plots/final_builder_mission_heatmap.png')


# Create heatmap for all missions
# get unique missions in df
missions = df['mission'].unique()

# iterate over each mission
for mission in missions:
  slug = mission.replace('/', '-').replace(' ', '-').lower()
  mission_data = df[df['mission'].str.contains(mission, case=False, na=False)]
  heatmap_data = mission_data.pivot_table(index='title', columns='criteria_name', values='criteria_average', aggfunc='mean')
  
  # Plot heatmap
  plt.figure(figsize=(16, 14))
  sns.heatmap(heatmap_data, annot=True, cmap='viridis')
  plt.title('Heatmap of Criteria Scores by Proposals')
  plt.savefig(f'plots/final_heatmap_scores_by_{slug}.png')


