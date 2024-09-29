# -*- coding: utf-8 -*-
"""CDC_2024.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1J6esfvjLeLdzqPURyyHz0z6GHXxDgX6b

## Initial setup and data cleaning
"""

import pandas as pd
import matplotlib.pyplot as plt
from google.colab import drive

# Uploading the file instead of accessing from drive
# drive.mount('/content/drive')

file_path = '/content/Social_Science_Dataset_Cleaned.xlsx'#
df = pd.read_excel(file_path)
df.columns = ['Users', 'Churches','Resorts','Beaches','Parks','Theatres','Museums','Malls','Zoos','Restaurants','Pubs/Bars','Local Services','Burger/Pizza','Lodgings','Juice Bars','Art Galleries','Dance Clubs','Pools','Gyms','Bakeries','Spas','Cafes','View Points','Monuments','Gardens']

# Display the DataFrame
print(df.head())

Reviews = df

average_review = {}

num_rows = len(Reviews)
columns = Reviews.columns.tolist()
columns.pop(0)

for attraction in columns:
    average_review[attraction] = 0

for index, row in Reviews.iterrows():
    for attraction in columns:
        average_review[attraction] += row[attraction]

for attraction in columns:
    average_review[attraction] = average_review[attraction] / num_rows

print(average_review)

sorted_average_review = dict(sorted(average_review.items(), key=lambda item: item[1]))
categories = sorted_average_review.keys();

"""# Graphing the average values of each column"""

# Get the list of columns
columns_list = df.columns.tolist()

# Filter to only numeric columns for standard deviation and mean calculations
numeric_df = df.select_dtypes(include='number')

# Check if there are any numeric columns
if numeric_df.empty:
    raise ValueError("No numeric columns found in the DataFrame.")

numeric_df.columns = ['Churches','Resorts','Beaches','Parks','Theatres','Museums','Malls','Zoos','Restaurants','Pubs/Bars','Local Services','Burger/Pizza','Lodgings','Juice Bars','Art Galleries','Dance Clubs','Pools','Gyms','Bakeries','Spas','Cafes','View Points','Monuments','Gardens']

# Calculate the averages for each numeric column
averages = numeric_df.mean().sort_values(ascending=False)

# Calculate the standard deviation for each numeric column
std_deviation = numeric_df.std().reindex(averages.index)

# Convert averages to a list
averages_list = averages.tolist()

# Prepare categories for plotting
categories = averages.index.tolist()  # Use the names of the numeric columns as categories

# Modifying the size & labels of the figure before it is graphed
plt.figure(figsize=(10,5))
# Create the bar plot with error bars
plt.bar(categories, averages_list, yerr=std_deviation, capsize=5, color='skyblue', alpha=0.7)
# Add labels and title
plt.title('Average Ratings According to Attraction')
plt.xlabel('Categories')
plt.ylabel('Mean Values')

# Show the plot
plt.xticks(rotation=45)  # Rotate x-axis labels if needed
plt.tight_layout()  # Adjust layout to prevent clipping of labels
plt.show()

# prompt: plot a radar graph of the mean values of the following categories: Churches, Gardens, Local Services, Monuments, Museums, View Points. I would like for the max value of the graph to be 5 and min value to be 0

# Select the desired categories
categories = ['Churches', 'Gardens', 'Art Galleries', 'Monuments', 'Museums', 'View Points']
selected_averages = averages[categories]

# Convert to a list for plotting
values = selected_averages.tolist()

# Number of variables
N = len(categories)

# Create the angles for the radar graph
angles = [n / float(N) * 2 * np.pi for n in range(N)]
angles += angles[:1]  # Close the circle

# Initialize the spider plot
ax = plt.subplot(111, polar=True)

# Plot the data
ax.plot(angles, values + values[:1], 'o-', linewidth=2)

# Fill the area
ax.fill(angles, values + values[:1], alpha=0.25)

# Set the labels for each angle
ax.set_thetagrids(np.degrees(angles[:-1]), categories)

# Set the radial limits
ax.set_ylim(0, 5)

# Add title
plt.title("Average Ratings for Selected Sight-Seeing Attractions")

# Show the plot
plt.show()

# prompt: Now do the same thing for the columns Bakeries, Burger/Pizza, Cafes, Juice Bars, Pubs/Bars, Restaurants

import matplotlib.pyplot as plt
import numpy as np
# Select the desired categories
categories = ['Bakeries', 'Burger/Pizza', 'Cafes', 'Juice Bars', 'Pubs/Bars', 'Restaurants']
selected_averages = averages[categories]

# Convert to a list for plotting
values = selected_averages.tolist()

# Number of variables
N = len(categories)

# Create the angles for the radar graph
angles = [n / float(N) * 2 * np.pi for n in range(N)]
angles += angles[:1]  # Close the circle

# Initialize the spider plot
ax = plt.subplot(111, polar=True)

# Plot the data
ax.plot(angles, values + values[:1], 'o-', linewidth=2)

# Fill the area
ax.fill(angles, values + values[:1], alpha=0.25)

# Set the labels for each angle
ax.set_thetagrids(np.degrees(angles[:-1]), categories)

# Set the radial limits
ax.set_ylim(0, 5)

# Add title
plt.title("Average Ratings for Selected Food & Drink Attractions")

# Show the plot
plt.show()

# prompt: now do the same thing for the following columns: Beaches, Lodgings, Parks, Resorts, Spas
# Select the desired categories
categories = ['Beaches', 'Lodgings', 'Parks', 'Resorts', 'Spas', 'Local Services']
selected_averages = averages[categories]

# Convert to a list for plotting
values = selected_averages.tolist()

# Number of variables
N = len(categories)

# Create the angles for the radar graph
angles = [n / float(N) * 2 * np.pi for n in range(N)]
angles += angles[:1]  # Close the circle

# Initialize the spider plot
ax = plt.subplot(111, polar=True)

# Plot the data
ax.plot(angles, values + values[:1], 'o-', linewidth=2)

# Fill the area
ax.fill(angles, values + values[:1], alpha=0.25)

# Set the labels for each angle
ax.set_thetagrids(np.degrees(angles[:-1]), categories)

# Set the radial limits
ax.set_ylim(0, 5)

# Add title
plt.title("Average Ratings for Selected Leisure Attractions")

# Show the plot
plt.show()

# prompt: now do the same thing for the following columns Dance Clubs, Gyms, Pools, Malls, Theatres, Zoos
# Select the desired categories
categories = ['Dance Clubs', 'Gyms', 'Pools', 'Malls', 'Theatres', 'Zoos']
selected_averages = averages[categories]

# Convert to a list for plotting
values = selected_averages.tolist()

# Number of variables
N = len(categories)

# Create the angles for the radar graph
angles = [n / float(N) * 2 * np.pi for n in range(N)]
angles += angles[:1]  # Close the circle

# Initialize the spider plot
ax = plt.subplot(111, polar=True)

# Plot the data
ax.plot(angles, values + values[:1], 'o-', linewidth=2)

# Fill the area
ax.fill(angles, values + values[:1], alpha=0.25)

# Set the labels for each angle
ax.set_thetagrids(np.degrees(angles[:-1]), categories)

# Set the radial limits
ax.set_ylim(0, 5)

# Add title
plt.title("Average Ratings for Selected Entertainment Attractions")

# Show the plot
plt.show()

# Prepare categories for plotting
categories = std_deviation.index.tolist()  # Use the names of the numeric columns as categories
std_values = std_deviation.tolist()         # Convert standard deviations to a list

plt.figure(figsize=(10,5))
# Create the bar plot for standard deviations
plt.bar(categories, std_values, color='orange', alpha=0.7)

# Add labels and title
plt.title('Standard Deviations for Each Category')
plt.xlabel('Categories')
plt.ylabel('Standard Deviation')

# Show the plot
plt.xticks(rotation=45)  # Rotate x-axis labels if needed
plt.tight_layout()        # Adjust layout to prevent clipping of labels
plt.show()

"""# Grouping the Columns by Similarity
Similar groups:


1.   Sightseeing - Churches, Gardens, Museums, View Points, Art Galleries, Monuments
2.   Food - Bakeries, Burger/Pizza, Cafes, Juice Bars, Pubs/Bars, Restaurants
3.   Relaxing - Beaches, Lodgings, Parks, Resorts, Spas, Local Services
4.   Entertainment - Dance Clubs, Gyms, Pools, Malls, Theatres, Zoos


"""



sightseeing = df[['Churches', 'Gardens', 'Art Galleries', 'Monuments', 'Museums', 'View Points']]
food = df[['Bakeries', 'Burger/Pizza', 'Cafes', 'Juice Bars', 'Pubs/Bars', 'Restaurants']]
relaxing = df[['Beaches', 'Lodgings', 'Parks', 'Resorts', 'Spas', 'Local Services']]
entertainment = df[['Dance Clubs', 'Gyms', 'Pools', 'Malls', 'Theatres', 'Zoos']]
sightseeing



"""

# Grouping the Columns by Similarity
Similar groups:


1.   Sightseeing - Churches, Gardens, Monuments, Museums, View Points, Art Galleries
2.   Food - Bakeries, Burger/Pizza, Cafes, Juice Bars, Pubs/Bars, Restaurants
3.   Relaxing - Beaches, Lodgings, Parks, Resorts, Spas, Local Services
4.   Entertainment - Dance Clubs, Gyms, Pools, Malls, Theatres, Zoos


"""

import pandas as pd
import matplotlib.pyplot as plt
from google.colab import drive

# Load the Excel file
file_path = '/content/Social_Science_Dataset_Cleaned.xlsx'
df = pd.read_excel(file_path)

# Rename columns
df.columns = ['Users', 'Churches', 'Resorts', 'Beaches', 'Parks', 'Theatres',
              'Museums', 'Malls', 'Zoos', 'Restaurants', 'Pubs/Bars',
              'Local Services', 'Burger/Pizza', 'Lodgings', 'Juice Bars',
              'Art Galleries', 'Dance Clubs', 'Pools', 'Gyms', 'Bakeries',
              'Spas', 'Cafes', 'View Points', 'Monuments', 'Gardens']

# Prepare to calculate means, medians, and standard deviations
means = {}
medians = {}
std_deviation = {}

# Calculate means, medians, and standard deviations for all columns
for attraction in df.columns[1:]:  # Skip the 'Users' column
    means[attraction] = df[attraction].mean()
    medians[attraction] = df[attraction].median()
    std_deviation[attraction] = df[attraction].std()

# List of columns to repeat the process for
attractions_to_filter = [
      'Parks', 'Museums',
     'Restaurants', 'Malls'
]

# Dictionary to hold means for filtered DataFrames
filtered_means_dict = {}

# Loop through each attraction in the specified list
for attraction in attractions_to_filter:
    # Calculate the mean for the current attraction
    mean_value = means[attraction]

    # Filter the DataFrame for users who rated the current attraction >= mean
    filtered_df = df[df[attraction] >= mean_value]

    # Calculate the means for all numeric columns in the filtered DataFrame
    filtered_means = filtered_df.select_dtypes(include='number').mean()

    # Store the means in the dictionary
    filtered_means_dict[attraction] = filtered_means

# Display the filtered means for each attraction
for attraction, means in filtered_means_dict.items():
    sorted_means = means.sort_values(ascending=False)
    print(f"\nMean values for users who rated {attraction} greater than or equal to the mean:")
    print(sorted_means)

import matplotlib.pyplot as plt

# Data for the highest means
categories = ['Sightseeing', 'Food', 'Relaxing', 'Entertainment']
highest_means = [3.48, 2.81, 4.43, 4.13]  # Corresponding highest means

# Specific attractions for each category
attractions = [
    'Museums',    # Sightseeing
    'Restaurants', # Food
    'Parks',       # Relaxing
    'Theatres'     # Entertainment
]

# Create a bar chart
plt.figure(figsize=(8, 5))
bars = plt.bar(categories, highest_means, color=['skyblue', 'lightgreen', 'salmon', 'orange'], alpha=0.7)

# Add data labels on top of the bars
for i, value in enumerate(highest_means):
    plt.text(i, value + 0.05, f'{value:.2f}', ha='center', va='bottom')

# Add subtext (attractions) below each bar
for i, attraction in enumerate(attractions):
    plt.text(i, -0.15, attraction, ha='center', va='top', fontsize=10)

# Adding title and labels
plt.title('Averages for Users Who Rated Parks Above Average', size=12, weight='bold')
plt.xlabel('Categories', size=12)
plt.ylabel('Mean Values', size=12)

# Set y-axis limits to ensure the subtext is visible
plt.ylim(-0.5, 5)

# Show grid for better readability
plt.grid(axis='y')

# Show the plot
plt.tight_layout()
plt.show()

import matplotlib.pyplot as plt

# Data for the highest means
categories = ['Sightseeing', 'Food', 'Relaxing', 'Entertainment']
highest_means = [3.48, 2.81, 4.43, 4.13]  # Corresponding highest means

# Specific attractions for each category
attractions = [
    'Museums',    # Sightseeing
    'Restaurants', # Food
    'Parks',       # Relaxing
    'Theatres'     # Entertainment
]

# Create a bar chart
plt.figure(figsize=(8, 5))
bars = plt.bar(categories, highest_means, color=['skyblue', 'lightgreen', 'salmon', 'orange'], alpha=0.7)

# Add data labels on top of the bars
for i, value in enumerate(highest_means):
    plt.text(i, value + 0.05, f'{value:.2f}', ha='center', va='bottom')

# Add subtext (attractions) below each bar
for i, attraction in enumerate(attractions):
    plt.text(i, -0.15, attraction, ha='center', va='top', fontsize=10)

# Adding title and labels
plt.title('Averages for Users Who Rated Museums Above Average', size=12, weight='bold')
plt.xlabel('Categories', size=12)
plt.ylabel('Mean Values', size=12)

# Set y-axis limits to ensure the subtext is visible
plt.ylim(-0.5, 5)

# Show grid for better readability
plt.grid(axis='y')

# Show the plot
plt.tight_layout()
plt.show()

import matplotlib.pyplot as plt

# Data for the highest means
categories = ['Sightseeing', 'Food', 'Relaxing', 'Entertainment']
highest_means = [4.19, 3.40, 3.15, 3.98]  # Corresponding highest means

# Specific attractions for each category
attractions = [
    'Museums',    # Sightseeing
    'Restaurants', # Food
    'Parks',       # Relaxing
    'Malls'        # Entertainment
]

# Create a bar chart
plt.figure(figsize=(8, 5))
bars = plt.bar(categories, highest_means, color=['skyblue', 'lightgreen', 'salmon', 'orange'], alpha=0.7)

# Add data labels on top of the bars
for i, value in enumerate(highest_means):
    plt.text(i, value + 0.05, f'{value:.2f}', ha='center', va='bottom')

# Add subtext (attractions) below each bar
for i, attraction in enumerate(attractions):
    plt.text(i, -0.15, attraction, ha='center', va='top', fontsize=10)

# Adding title and labels
plt.title('Averages for Users Who Rated Restaurants Above Average', size=12, weight='bold')
plt.xlabel('Categories', size=12)
plt.ylabel('Mean Values', size=12)

# Set y-axis limits to ensure the subtext is visible
plt.ylim(-0.5, 5)

# Show grid for better readability
plt.grid(axis='y')

# Show the plot
plt.tight_layout()
plt.show()

import matplotlib.pyplot as plt

# Data for the highest means
categories = ['Sightseeing', 'Food', 'Relaxing', 'Entertainment']
highest_means = [3.43, 3.61, 2.59, 4.93]  # Corresponding highest means

# Specific attractions for each category
attractions = [
    'Museums',    # Sightseeing
    'Restaurants', # Food
    'Parks',       # Relaxing
    'Malls'        # Entertainment
]

# Create a bar chart
plt.figure(figsize=(8, 5))
bars = plt.bar(categories, highest_means, color=['skyblue', 'lightgreen', 'salmon', 'orange'], alpha=0.7)

# Add data labels on top of the bars
for i, value in enumerate(highest_means):
    plt.text(i, value + 0.05, f'{value:.2f}', ha='center', va='bottom')

# Add subtext (attractions) below each bar
for i, attraction in enumerate(attractions):
    plt.text(i, -0.15, attraction, ha='center', va='top', fontsize=10)

# Adding title and labels
plt.title('Averages for Users Who Rated Malls Above Average', size=10, weight='bold')
plt.xlabel('Categories', size=12)
plt.ylabel('Mean Values', size=12)

# Set y-axis limits to ensure the subtext is visible
plt.ylim(-0.5, 5)

# Show grid for better readability
plt.grid(axis='y')

# Show the plot
plt.tight_layout()
plt.show()

"""Tukeys tests for Sightseeing, Food, Relaxing, and Entertainment Categories"""

'''Prompt: can you perform a t-test between 6 different means at once,
Group 1: mean = 1.455674, n = 5455, standard deviation = 0.8276731757185378
Group 2: mean = 1.560475, n = 5455, standard deviation = 1.1716979106485346
Group 3: mean = 1.530818, n = 5455, standard deviation = 1.3161717158520108
Group 4: mean = 2.893809, n = 5455, standard deviation = 1.282300603264681
Group 5: mean = 1.749941, n = 5455, standard deviation = 1.5982751509792257
Group 6: mean = 2.206060, n = 5455, standard deviation = 1.7157009812296609
'''

import scipy.stats as stats
import pandas as pd
import numpy as np
from statsmodels.stats.multicomp import pairwise_tukeyhsd


#Means & Standard Deviations
mean = {}
std_deviation = {}

for attraction in df.columns[1:]:
    mean[attraction] = df[attraction].mean()
    std_deviation[attraction] = df[attraction].std()



# Sightseeing Data - Museums, Art Galleries, View Points, Monuments, Gardens, Churches
means = [mean["Museums"], mean["Art Galleries"], mean["View Points"], mean["Monuments"], mean["Gardens"], mean["Churches"]]
std_devs = [std_deviation["Museums"], std_deviation["Art Galleries"], std_deviation["View Points"], std_deviation["Monuments"], std_deviation["Gardens"], std_deviation["Churches"]]
n = [len(df)] * 6  # All groups have the same n

# Generate random data for each group based on the means and standard deviations
np.random.seed(0)
museums = np.random.normal(means[0], std_devs[0], n[0])
galleries = np.random.normal(means[1], std_devs[1], n[1])
view_points = np.random.normal(means[2], std_devs[2], n[2])
monuments = np.random.normal(means[3], std_devs[3], n[3])
gardens = np.random.normal(means[4], std_devs[4], n[4])
churches = np.random.normal(means[5], std_devs[5], n[5])

# Perform one-way ANOVA
f_statistic, p_value = stats.f_oneway(museums, galleries, view_points, monuments, gardens, churches)
f_statistic, p_value

# Perform Tukey's HSD (Honestly Significant Difference) test

# Combine all the groups into one data array
data = np.concatenate([museums, galleries, view_points, monuments, gardens, churches])
labels = np.array(["Museums"]*n[0] + ["Art Galleries"]*n[0] + ["View Points"]*n[0] +
                  ["Monuments"]*n[0] + ["Gardens"]*n[0] + ["Churches"]*n[0])

# Perform Tukey's HSD test
tukey = pairwise_tukeyhsd(endog=data, groups=labels, alpha=0.05)
print("Sightseeing attractions Tukey's tests")
print(tukey.summary())


# Food Data - Bakeries, Burger/Pizza Shops, Cafes, Juice Bars, Pubs/Bars, Restaurants
means = [mean["Bakeries"], mean["Burger/Pizza"], mean["Cafes"], mean["Juice Bars"], mean["Pubs/Bars"], mean["Restaurants"]]
std_devs = [std_deviation["Bakeries"], std_deviation["Burger/Pizza"], std_deviation["Cafes"], std_deviation["Juice Bars"], std_deviation["Pubs/Bars"], std_deviation["Restaurants"]]
n = [len(df)] * 6  # All groups have the same n

# Generate random data for each group based on the means and standard deviations
np.random.seed(0)
bakeries = np.random.normal(means[0], std_devs[0], n[0])
burger_pizza = np.random.normal(means[1], std_devs[1], n[1])
cafes = np.random.normal(means[2], std_devs[2], n[2])
juice = np.random.normal(means[3], std_devs[3], n[3])
pubs = np.random.normal(means[4], std_devs[4], n[4])
restaurants = np.random.normal(means[5], std_devs[5], n[5])

# Perform one-way ANOVA
f_statistic, p_value = stats.f_oneway(bakeries, burger_pizza, cafes, juice, pubs, restaurants)
f_statistic, p_value

# Perform Tukey's HSD (Honestly Significant Difference) test

# Combine all the groups into one data array
data = np.concatenate([bakeries, burger_pizza, cafes, juice, pubs, restaurants])
labels = np.array(["Bakeries"]*n[0] + ["Burger/Pizza"]*n[0] + ["Cafes"]*n[0] +
                  ["Juice Bars"]*n[0] + ["Pubs/Bars"]*n[0] + ["Restaurants"]*n[0])

# Perform Tukey's HSD test
tukey = pairwise_tukeyhsd(endog=data, groups=labels, alpha=0.05)
print("Food options Tukey's tests")
print(tukey.summary())


# Relaxing Data - Beaches, Lodgings, Parks, Resorts, Spas, Local Services
means = [mean["Beaches"], mean["Lodgings"], mean["Parks"], mean["Resorts"], mean["Spas"], mean["Local Services"]]
std_devs = [std_deviation["Beaches"], std_deviation["Lodgings"], std_deviation["Parks"], std_deviation["Resorts"], std_deviation["Spas"], std_deviation["Local Services"]]
n = [len(df)] * 6  # All groups have the same n

# Generate random data for each group based on the means and standard deviations
np.random.seed(0)
beaches = np.random.normal(means[0], std_devs[0], n[0])
lodgings = np.random.normal(means[1], std_devs[1], n[1])
parks = np.random.normal(means[2], std_devs[2], n[2])
resorts = np.random.normal(means[3], std_devs[3], n[3])
spas = np.random.normal(means[4], std_devs[4], n[4])
services = np.random.normal(means[5], std_devs[5], n[5])

# Perform one-way ANOVA
f_statistic, p_value = stats.f_oneway(beaches, lodgings, parks, resorts, spas, services)
f_statistic, p_value

# Perform Tukey's HSD (Honestly Significant Difference) test

# Combine all the groups into one data array
data = np.concatenate([beaches, lodgings, parks, resorts, spas, services])
labels = np.array(["Beaches"]*n[0] + ["Lodgings"]*n[0] + ["Parks"]*n[0] +
                  ["Resorts"]*n[0] + ["Spas"]*n[0] + ["Local Services"]*n[0])

# Perform Tukey's HSD test
tukey = pairwise_tukeyhsd(endog=data, groups=labels, alpha=0.05)
print("Relaxing options Tukey's tests")
print(tukey.summary())


# Entertainment Data - Dance Clubs, Gyms, Pools, Malls, Theatres, Zoos
means = [mean["Dance Clubs"], mean["Gyms"], mean["Pools"], mean["Malls"], mean["Theatres"], mean["Zoos"]]
std_devs = [std_deviation["Dance Clubs"], std_deviation["Gyms"], std_deviation["Pools"], std_deviation["Malls"], std_deviation["Theatres"], std_deviation["Zoos"]]
n = [len(df)] * 6  # All groups have the same n

# Generate random data for each group based on the means and standard deviations
np.random.seed(0)
clubs = np.random.normal(means[0], std_devs[0], n[0])
gyms = np.random.normal(means[1], std_devs[1], n[1])
pools = np.random.normal(means[2], std_devs[2], n[2])
malls = np.random.normal(means[3], std_devs[3], n[3])
theatres = np.random.normal(means[4], std_devs[4], n[4])
zoos = np.random.normal(means[5], std_devs[5], n[5])

# Perform one-way ANOVA
f_statistic, p_value = stats.f_oneway(clubs, gyms, pools, malls, theatres, zoos)
f_statistic, p_value

# Perform Tukey's HSD (Honestly Significant Difference) test

# Combine all the groups into one data array
data = np.concatenate([clubs, gyms, pools, malls, theatres, zoos])
labels = np.array(["Dance Clubs"]*n[0] + ["Gyms"]*n[0] + ["Pools"]*n[0] +
                  ["Malls"]*n[0] + ["Theatres"]*n[0] + ["Zoos"]*n[0])

# Perform Tukey's HSD test
tukey = pairwise_tukeyhsd(endog=data, groups=labels, alpha=0.05)
print("Entertainment options Tukey's tests")
print(tukey.summary())

# Sightseeing Data Plot - Museums, Art Galleries, View Points, Monuments, Gardens, Churches
plt.figure(figsize=(10,5))
# Create the bar plot with error bars
sightseeing = ["Museums", "Art Galleries", "View Points", "Gardens", "Monuments", "Churches"]
sightseeing_mean = [mean["Museums"], mean["Art Galleries"], mean["View Points"], mean["Gardens"], mean["Monuments"], mean["Churches"]]
sightseeing_std = [std_deviation["Museums"], std_deviation["Art Galleries"], std_deviation["View Points"], std_deviation["Gardens"], std_deviation["Monuments"], mean["Churches"]]
plt.bar(sightseeing, sightseeing_mean, yerr=sightseeing_std, capsize=5, color='skyblue', alpha=0.7)
# Add labels and title
plt.title('Sightseeing Attraction Rankings')
plt.xlabel('Sightseeing Attractions')
plt.ylabel('Mean Values')

# Show the plot
plt.xticks(rotation=45)  # Rotate x-axis labels if needed
plt.tight_layout()  # Adjust layout to prevent clipping of labels
plt.show()

# Food Data Plot - Bakeries, Burger/Pizza Shops, Cafes, Juice Bars, Pubs/Bars, Restaurants
plt.figure(figsize=(10,5))
# Create the bar plot with error bars
food = ["Restaurants", "Pubs/Bars", "Juice Bars", "Burger/Pizza", "Bakeries", "Cafes"]
food_mean = [mean["Restaurants"], mean["Pubs/Bars"], mean["Juice Bars"], mean["Burger/Pizza"], mean["Bakeries"], mean["Cafes"]]
food_std = [std_deviation["Restaurants"], std_deviation["Pubs/Bars"], std_deviation["Juice Bars"], std_deviation["Burger/Pizza"], std_deviation["Bakeries"], std_deviation["Cafes"]]

plt.bar(food, food_mean, yerr=food_std, capsize=5, color='skyblue', alpha=0.7)
# Add labels and title
plt.title('Food Option Rankings')
plt.xlabel('Food Options')
plt.ylabel('Mean Values')

# Show the plot
plt.xticks(rotation=45)  # Rotate x-axis labels if needed
plt.tight_layout()  # Adjust layout to prevent clipping of labels
plt.show()

# Relaxing Data Plot - Beaches, Lodgings, Parks, Resorts, Spas, Local Services
plt.figure(figsize=(10,5))
# Create the bar plot with error bars
relax = ["Parks", "Local Services", "Beaches", "Resorts", "Lodgings", "Spas"]
relax_mean = [mean["Parks"], mean["Local Services"], mean["Beaches"], mean["Resorts"], mean["Lodgings"], mean["Spas"]]
relax_std = [std_deviation["Parks"], std_deviation["Local Services"], std_deviation["Beaches"], std_deviation["Resorts"], std_deviation["Lodgings"], std_deviation["Spas"]]

plt.bar(relax, relax_mean, yerr=relax_std, capsize=5, color='skyblue', alpha=0.7)
# Add labels and title
plt.title('Relaxation Option Rankings')
plt.xlabel('Relaxation Options')
plt.ylabel('Mean Values')

# Show the plot
plt.xticks(rotation=45)  # Rotate x-axis labels if needed
plt.tight_layout()  # Adjust layout to prevent clipping of labels
plt.show()

# Entertainment Data Plot - Dance Clubs, Gyms, Pools, Malls, Theatres, Zoos
plt.figure(figsize=(10,5))
# Create the bar plot with error bars
entertainment = ["Malls", "Theatres", "Zoos", "Dance Clubs", "Pools", "Gyms"]
entertainment_mean = [mean["Malls"], mean["Theatres"], mean["Zoos"], mean["Dance Clubs"], mean["Pools"], mean["Gyms"]]
entertainment_std = [std_deviation["Malls"], std_deviation["Theatres"], std_deviation["Zoos"], std_deviation["Dance Clubs"], std_deviation["Pools"], std_deviation["Gyms"]]

plt.bar(entertainment, entertainment_mean, yerr=entertainment_std, capsize=5, color='skyblue', alpha=0.7)
# Add labels and title
plt.title('Entertainment Option Rankings')
plt.xlabel('Entertainment Options')
plt.ylabel('Mean Values')

# Show the plot
plt.xticks(rotation=45)  # Rotate x-axis labels if needed
plt.tight_layout()  # Adjust layout to prevent clipping of labels
plt.show()