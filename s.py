import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("student_performance.csv")

print(df.head())
print(df.info())
print(df.describe())

print(df.corr(numeric_only=True))

df['Attendance'].hist()
plt.title("Attendance Distribution")
plt.xlabel("Attendance")
plt.ylabel("Frequency")
plt.show()

plt.scatter(df['StudyHours'], df['ExamScore'])
plt.title("Study Hours vs Exam Score")
plt.xlabel("Study Hours")
plt.ylabel("Exam Score")
plt.show()

df['FinalGrade'].value_counts().plot(kind='bar')
plt.title("Final Grade Distribution")
plt.xlabel("Final Grade")
plt.ylabel("Number of Students")
plt.show()

df['StressLevel'].value_counts().plot(kind='bar')
plt.title("Stress Level Distribution")
plt.xlabel("Stress Level")
plt.ylabel("Number of Students")
plt.show()
