from bs4 import BeautifulSoup
import requests
import csv
import time
import os


pages = [10, 20, 30, 40, 50]

with open('C:/Users/Jenjhayden/Desktop/scrapper_data/python_list.csv', 'a', encoding='utf-8', newline='') as f_output:
    csv_print = csv.writer(f_output)

    file_is_empty = os.stat('C:/Users/Jenjhayden/Desktop/scrapper_data/python_list.csv').st_size == 0
    if file_is_empty:
        csv_print.writerow(['Job_Title', 'Company', 'Location', 'Summary', 'Salary'])

    for page in pages:
        source = requests.get('https://www.indeed.com/jobs?q=python+developer&l={}'.format(page)).text

        soup = BeautifulSoup(source,'html5lib')

        for jobs in soup.find_all (class_='result'):

            try:
                title = jobs.h2.text.strip()
            except Exception as e:
                title = None
            print('Job Title:', title)

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
                salary = jobs.find('span', class_='no-wrap').text.strip()
            except Exception as e:
                salary = None
            print('salary:', salary)

            csv_print.writerow([title, company, location, summary, salary])
            
            print('------------------')

            time.sleep(0.5)