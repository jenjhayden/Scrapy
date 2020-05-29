from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.indeed.com/jobs?q=python+developer&l=').text
soup = BeautifulSoup(source,'lmxl')

for jobs in soup.find_all(class_='result'):
    #print(jobs.precertify())

try:
    job_title = jobs.h2.text.strip()
except Exception as e:
    job_title = None
print('Job_Title:', job_title)

try:
    company = jobs.span.text.strip()
except Exception as e:
    company= None
print('Company:', company)

try:
    location = jobs.find('span', class_='location').text.strip()
except Exception as e:
    location = None
print('Location:', location)

try:
    summary = jobs.find('span', class_='summary').text.strip()
except Exception as e:
    summary = None
print('Summary:', summary)

try:
    salary = jobs.find('span',class_='no-wrap').text.strip()
except Exception as e:
    salary = None
print('salary:', salary)

print('------------------')

