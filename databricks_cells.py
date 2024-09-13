# Install necessary packages
%pip install 'typing-extensions>=4.3.0'
%pip install snowflake-connector-python

# Import libraries and connect to Snowflake
import snowflake.connector
import pandas as pd

conn = snowflake.connector.connect(
    user='x',
    password='x',
    account='x'
)

query = "SELECT * FROM STUDENTPERFORMANCE.PUBLIC.STUDENTPERFORMANCEFACTORS"
df = pd.read_sql(query, conn)

# Perform data processing and feature engineering
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

df['TOTAL_STUDY_TIME'] = df['HOURS_STUDIED'] + df['TUTORING_SESSIONS']

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
df[['HOURS_STUDIED', 'ATTENDANCE', 'SLEEP_HOURS', 'PREVIOUS_SCORES', 'TUTORING_SESSIONS', 'PHYSICAL_ACTIVITY', 'TOTAL_STUDY_TIME']] = scaler.fit_transform(df[['HOURS_STUDIED', 'ATTENDANCE', 'SLEEP_HOURS', 'PREVIOUS_SCORES', 'TUTORING_SESSIONS', 'PHYSICAL_ACTIVITY', 'TOTAL_STUDY_TIME']])

df['EXTRACURRICULAR_ACTIVITIES'] = df['EXTRACURRICULAR_ACTIVITIES'].astype(int)
df['INTERNET_ACCESS'] = df['INTERNET_ACCESS'].astype(int)
df['LEARNING_DISABILITIES'] = df['LEARNING_DISABILITIES'].astype(int)

categorical_columns = ['PARENTAL_INVOLVEMENT', 'ACCESS_TO_RESOURCES', 'MOTIVATION_LEVEL', 'FAMILY_INCOME', 'TEACHER_QUALITY', 'SCHOOL_TYPE', 'PEER_INFLUENCE', 'PARENTAL_EDUCATION_LEVEL', 'DISTANCE_FROM_HOME', 'GENDER']

for column in categorical_columns:
    if column in df.columns:
        df[column + '_ENCODED'] = df[column].astype('category').cat.codes

df = df.drop(categorical_columns, axis=1, errors='ignore')

df = df.drop(columns=['Total_Study_Time'], errors='ignore')

X = df.drop('EXAM_SCORE', axis=1)
y = df['EXAM_SCORE']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}')

results = pd.DataFrame({
    'Actual': y_test,
    'Predicted': y_pred
})
print(results.head(10))
