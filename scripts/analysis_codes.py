import pandas as pd

# reading the csv file 
df = pd.read_csv("data/student_ai_usage_data.csv")

# inspect my dataset for clear understanding of how many rows and columns are in my dataset
print(df.head())
print(df.columns)
print(df.info())
print(df.describe())
print(df.shape)


# checking the missing values 
print(df.isnull().sum())

# checking the duplicate values
print(df.duplicated().sum())

# Which AI tool is most preferred and the no. of students uses this tool?
counts=df["Preferred_AI_Tool"].value_counts()
tool=counts.idxmax()
users=counts.max()
print(f'The most preferred tool is {tool} and the no of users are {users}')

