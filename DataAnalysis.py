import pandas as pd

titanic = pd.read_csv("data/titanic.csv")

# Age column of all passengers
age = titanic["Age"]

# Maximum - Minimum - Average age of all passengers
mean_age = titanic["Age"].mean()
max_age = titanic["Age"].max()
min_age =  titanic["Age"].min()

# Age and gender information of all passengers
dt2 = pd.DataFrame(titanic[["Age","Sex"]])

# Information of all passengers whose age are greater than 35
above_35 =titanic[ titanic["Age"]>35 ]

# Names of passengers whose age are greater than 35
name_above_35 = titanic["Name"][titanic["Age"]>35]

# Searching for a specific name "Countess" in the dataset
specific_name = titanic[ titanic["Name"].str.contains("Countess") ]

# CREATING NEW COLUMN DERIVED FROM EXISTING COLUMN
titanic["New Column 1"] = titanic["Age"] * 10
titanic["New Column 2 "] = titanic["Age"] * titanic["Ticket Price"]

# Making all name characters lowercase - MANIPULATING TEXTUAL DATA EXAMPLE
titanic["Name"] = titanic["Name"].str.lower()
