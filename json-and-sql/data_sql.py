import pandas as pd
from sqlalchemy import create_engine

# Database connection details
username = "root"
password = ""
host = "localhost"
database = "world"

# Create SQLalchemy engine
engine = create_engine(f"mysql+pymysql://{username}:{password}@{host}/{database}")

#Fetch the data using pandas.
df= pd.read_sql_query("SELECT * FROM city", engine)

country_df = df= pd.read_sql_query("SELECT * FROM country WHERE Continent LIKE 'Asia'", engine)

# Print the data frame
print(df)
print(country_df)