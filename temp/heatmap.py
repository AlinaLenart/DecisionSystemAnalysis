import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Wczytanie danych
path = "Students_Grading_Dataset.csv"
df = pd.read_csv(path)

numeric_df = df.select_dtypes(include=['number'])
correlation_matrix = numeric_df.corr()
plt.figure(figsize=(12, 6))
sns.heatmap(correlation_matrix, annot=True, cmap="cividis", fmt=".3f", linewidths=0.5)
plt.title("The Correlation ")
plt.show()

# df['Family_Income_Level'] = df['Family_Income_Level'].map({'High': 2, 'Medium': 1, 'Low': 0})
# df['Parent_Education_Level'] = df['Parent_Education_Level'].map({'PhD': 5, "Master's": 4, "Bachelor's": 3, 'High School': 2, 'Missing': 1})
# df['Internet_Access_at_Home'] = df['Internet_Access_at_Home'].map({'Yes': 2, 'No': 1})
# df['Extracurricular_Activities'] = df['Extracurricular_Activities'].map({'Yes': 2, 'No': 1})

# selected_columns = [
#     'Attendance (%)', 'Midterm_Score', 'Final_Score', 'Assignments_Avg', 
#     'Quizzes_Avg', 'Participation_Score', 'Projects_Score', 'Total_Score', 
#     'Study_Hours_per_Week', 'Extracurricular_Activities', 'Internet_Access_at_Home',
#     'Parent_Education_Level', 'Family_Income_Level', 'Stress_Level (1-10)', 
#     'Sleep_Hours_per_Night'
# ]

# df_selected = df[selected_columns].copy()

# corr_matrix = df_selected.corr()

# plt.figure(figsize=(12, 8))
# sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
# plt.title("Correlation Matrix Heatmap")
# plt.show()

plt.figure(figsize=(10, 6))
sns.heatmap(df.isnull(), cmap="viridis", cbar=False, yticklabels=False)
plt.title("Missing Values Heatmap")
plt.show()