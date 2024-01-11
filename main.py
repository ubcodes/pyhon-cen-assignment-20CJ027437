import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Creating a dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emily'],
    'Age': [25, 30, 22, 35, 28],
    'Salary': [50000, 60000, 45000, 70000, 55000]
}

# Creating a DataFrame from  dictionary
df = pd.DataFrame(data)

# display the DataFrame
print("DataFrame:")
print(df)

#  bar chart using matplotlib
plt.figure(figsize=(8, 5))
plt.bar(df['Name'], df['Salary'], color='blue')
plt.title('Salary Distribution')
plt.xlabel('Name')
plt.ylabel('Salary')
plt.show()

# numpy operations on the data
average_age = np.mean(df['Age'])
max_salary = np.max(df['Salary'])

print("\nAverage Age:", average_age)
print("Maximum Salary:", max_salary)
