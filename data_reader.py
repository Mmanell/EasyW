import sqlite3
import pandas as pd

# Connect to your SQLite database
conn = sqlite3.connect('sensor_data.db')
cursor = conn.cursor()

# Read all data from the table
cursor.execute('SELECT * FROM sensor_data')
rows = cursor.fetchall()

# Get column names (optional but good)
column_names = [description[0] for description in cursor.description]

# Convert to pandas DataFrame
df = pd.DataFrame(rows, columns=column_names)

# Save the DataFrame to CSV
df.to_csv('sensor_data.csv', index=False)

# Close the connection
conn.close()

print("Data successfully saved to sensor_data.csv!")

