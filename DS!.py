import pandas as pd
import matplotlib.pyplot as plt

# Specify the path to your downloaded CSV file
population_data_path = r"D:\Project\P_Data_Extract_From_Gender_Statistics\cd3caa7e-2acc-4601-98d7-99e1d70c83ac_Series - Metadata.csv"
"D:\Project\P_Data_Extract_From_Gender_Statistics\cd3caa7e-2acc-4601-98d7-99e1d70c83ac_Data.csv"
# Read the CSV file into a DataFrame
population_data = pd.read_csv(population_data_path)

# Extract the relevant columns for the year 2022
age_population_2022 = population_data[["Series Name", "2022 [YR2022]"]]

# Drop rows with missing values
age_population_2022.dropna(inplace=True)

# Extract age from the Series Name
age_population_2022["Age"] = age_population_2022["Series Name"].apply(lambda x: int(x.split()[2]))

# Aggregate the population data for each age
age_population_2022_agg = age_population_2022.groupby("Age").sum()

# Create the bar chart
plt.figure(figsize=(12, 8))
plt.bar(age_population_2022_agg.index, age_population_2022_agg["2022 [YR2022]"], color='skyblue')
plt.xlabel('Age')
plt.ylabel('Population')
plt.title('Population Distribution by Age in 2022 (India)')
plt.xticks(range(0, 101, 5))
plt.grid(axis='y')

# Show the plot
plt.show()
