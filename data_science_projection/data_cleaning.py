import pandas as pd

df_jobs = pd.read_csv('data/glassdoor_jobs.csv')

#salary parsing


df_jobs=df_jobs[df_jobs['Salary Estimate']!= '-1']
salary=df_jobs['Salary Estimate'].apply(lambda x: x.split('(')[0])
minus_kd= salary.apply(lambda x : x.replace('K','').replace('$',''))
print(minus_kd.head())

#company name

#state field

#age company

#job description