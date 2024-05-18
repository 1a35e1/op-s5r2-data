import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# read csv into pandas dataframe
df = pd.read_csv('expanded-data.csv')

# Mission DF
mission_df = df[df['mission'] == 'Builder Grants 2']
mission_df['criteria'] = mission_df['criteria_name'].apply(lambda x: x.split(' - ')[0])

# Assign a random 6 character hash to each project for consistent comparison
mission_df['project'] = mission_df['title'].apply(lambda x: x.split(' ')[0])


# Create a sorted order of projects for consistent comparison across facets
project_order = mission_df['project'].unique()


# Create a FacetGrid with improved readability and sorting
g = sns.FacetGrid(mission_df, col='criteria', col_wrap=4, height=5, aspect=1.5)
g.map(sns.barplot, 'project', 'criteria_total', order=project_order, palette='viridis', ci=None)

# Set titles and labels
g.set_titles("{col_name}")
g.set_axis_labels("Project", "Total Score")
for ax in g.axes.flatten():
    ax.tick_params(labelbottom=True)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=90)

# Adjust the layout
g.fig.subplots_adjust(top=0.9)
g.fig.suptitle('Individual Criteria Scores Across Projects in "Builder Grants 2" Mission', fontsize=16)

plt.show()


# # Filter data for the specific mission
# # Correct the mission name and filter the data
# mission_df = df[df['mission'] == 'Builder Grants 2']

# # Extract criteria name and project name for better readability
# mission_df['criteria'] = mission_df['criteria_name'].apply(lambda x: x.split(' - ')[0])
# mission_df['project'] = mission_df['title']

# # Box Plot: Distribution of Scores for Each Criteria
# plt.figure(figsize=(14, 8))
# sns.boxplot(x='criteria', y='criteria_total', data=mission_df)
# plt.title('Box Plot of Criteria Total Scores in "Builder Grants 2" Mission')
# plt.xlabel('Criteria')
# plt.ylabel('Total Score')
# plt.xticks(rotation=90)
# plt.show()


# # Facet Grid: Individual Criteria Scores Across Projects
# g = sns.FacetGrid(mission_df, col='criteria', col_wrap=4, height=4)
# g.map(sns.barplot, 'project', 'criteria_total', order=mission_df['project'].unique())
# g.set_titles("{col_name}")
# g.set_xticklabels(rotation=90)
# g.fig.suptitle('Individual Criteria Scores Across Projects in "Builder Grants 2" Mission', y=1.02)
# plt.show()

# # Heatmap of Criteria Scores
# heatmap_data = mission_df.pivot_table(index='project', columns='criteria', values='criteria_total')
# plt.figure(figsize=(14, 10))
# sns.heatmap(heatmap_data, annot=True, cmap='viridis')
# plt.title('Heatmap of Criteria Total Scores by Project in "Builder Grants 2" Mission')
# plt.xlabel('Criteria')
# plt.ylabel('Project')
# plt.xticks(rotation=90)
# plt.show()

# # Scatter Plot: Criteria vs. Scores
# plt.figure(figsize=(14, 8))
# sns.scatterplot(x='criteria', y='criteria_total', data=mission_df, hue='project', s=100)
# plt.title('Scatter Plot of Criteria vs. Scores in "Builder Grants 2" Mission')
# plt.xlabel('Criteria')
# plt.ylabel('Total Score')
# plt.xticks(rotation=90)
# plt.show()
