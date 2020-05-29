from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.indeed.com/jobs?q=python+developer&l=').text