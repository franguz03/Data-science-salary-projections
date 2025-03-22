import pandas as pd
import datetime as dt

df_jobs = pd.read_csv('data/glassdoor_jobs.csv')

#salary parsing
df_jobs['hourly']= df_jobs['Salary Estimate'].apply(lambda x: 1 if 'per hour' in x.lower() else 0)
df_jobs['employer_provided']= df_jobs['Salary Estimate'].apply(lambda x: 1 if 'employer provided salary' in x.lower() else 0)

df_jobs=df_jobs[df_jobs['Salary Estimate']!= '-1']
salary=df_jobs['Salary Estimate'].apply(lambda x: x.split('(')[0])
minus_kd= salary.apply(lambda x : x.replace('K','').replace('$',''))
minus_cleaned=minus_kd.apply(lambda x: x.lower().replace('employer provided salary:','').replace(' per hour',''))
df_jobs['min_salary'] = minus_cleaned.apply(lambda x: int(x.split('-')[0].strip()))
df_jobs['max_salary'] = minus_cleaned.apply(lambda x: int(x.split('-')[1].strip()))
df_jobs['average_salary'] = (df_jobs['min_salary'] + df_jobs['max_salary']) / 2

#company name
df_jobs['company_text']=df_jobs.apply(lambda x: x['Company Name'] if x['Rating']<0 else x['Company Name'][0:-3],axis=1)

#state field
df_jobs['job_state']= df_jobs['Location'].apply(lambda x: x.split(',')[1])
df_jobs['same_state']=df_jobs.apply(lambda x: 1 if x['Location']==x['Headquarters'] else 0, axis=1)
#age company

df_jobs['company_age'] = df_jobs['Founded'].apply(lambda x: dt.datetime.now().year - x if x >0 else 0)

#job description--interesting requests
df_jobs['python_yn']=df_jobs['Job Description'].apply(lambda x:1 if 'python' in x.lower() else 0)
df_jobs['r_studio']=df_jobs['Job Description'].apply(lambda x:1 if 'r studio' in x.lower() or 'r-studio' in x.lower() else 0)
df_jobs['spark']=df_jobs['Job Description'].apply(lambda x:1 if 'spark' in x.lower() else 0)
df_jobs['aws']=df_jobs['Job Description'].apply(lambda x:1 if 'aws' in x.lower() else 0)
df_jobs['excel']=df_jobs['Job Description'].apply(lambda x:1 if 'excel' in x.lower() else 0)


df_jobs_cleaned=df_jobs.drop(['Unnamed: 0'],axis=1)
print(df_jobs_cleaned.columns)
df_jobs_cleaned.to_csv('./data/glassdoor_salary_cleaned.csv',index=False)