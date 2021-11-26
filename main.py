# My DataSet: https://data.wprdc.org/dataset/pbp-fire-arm-seizures/resource/e967381d-d7e9-48e3-a2a2-39262f7fa5c4?view_id=4c4fa4d5-71cd-4aa7-92e8-18206b9140a0
# The dataset I chosen discusses the number of firearms siezed by the Pittsburgh Police on a monthly basis. This can vary from individuals who were suspected of criminal offense to firearms that were left unattended in public. I chose this dataset because I believe it can help determine how  safe a neighborhood is because of how dangerous firearms are. According to Amnesty.Org, m ore than 500 people die every day from gun violence, and 44% of all homicides globally involve gun violence. We can use the numbers to determine which neighborhood is the safest in Pittsburgh by checking which have the least number of firearms siezed as it can help show which neigborhoods own more firearms than others.
# I plan to abstract the code in order to see the siezed firearms rate rates per neighborhood. This will allow to determine which neighborhoods are safer or more dangerous based on the number of siezed firearms. I will also use the data to make a bar graph showing the number 
# importing csv module

import pandas as pd
  
# csv file name
filename = "dataset.csv"
df = pd.read_csv(filename)
# print(df)

# List of unique neighborhoods
print(df['neighborhood'].unique().tolist())
print("========")

# I have to ways to do this: both approaches are outlined
# APPROACH ONE
# Group addresses into neighborhoods
# neighborhood_total_df = df.groupby(['neighborhood'])["total_count"].sum()
# print(neighborhood_total_df)
# print()
# print("SORTED")
# sorted_neighborhood_total_df = neighborhood_total_df.sort_values(ascending=False)
# print(sorted_neighborhood_total_df)
# df.loc[df['column_name'] == 3]

# APPROACH TWO
# Group addresses into neighborhoods
neighborhood_total_df = df.groupby(['neighborhood']).sum()
print("Total Number of Neighborhoods: ", len(neighborhood_total_df))
# Sort neighborhood by total firearms seized
sorted_neighborhood_total_df = neighborhood_total_df.sort_values(by=['total_count'], ascending=False)
print(sorted_neighborhood_total_df)

# Safest neighborhoods
safest_df = sorted_neighborhood_total_df.loc[sorted_neighborhood_total_df['total_count'] == 3]
print("Number of safest neighborhoods: ", len(safest_df))
print("\n", safest_df)

#Results:
# Homewood South: 298
#South Side Flats: 172
# Homewood North: 138
 
#Based on the monthly firearms siezed in each neighborhood, there is a four way tie with the lowest number:Swisshelm Park,Olive Borough,Regent Square,Summit Hill and Oakwood. Homewood South has the most firearms siezed. However, my data might be misleading as it does not take into account the population of each neighborhood, or 