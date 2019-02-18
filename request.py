import csv
import urllib.request
import requests
from bs4 import BeautifulSoup
import re

def retrieve_last_seen_date(file_name):
	f_read = open(file_name, 'r')
	last_seen_date = int(f_read.read().strip())
	f_read.close()
	return last_seen_date

def store_last_seen_date(last_seen_date, file_name):
	f_write = open(file_name, 'w')
	f_write.write(str(last_seen_date))
	f_write.close()

def download_csv(url, newfilename):
	CSV_URL = url
	urllib.request.urlretrieve(CSV_URL, newfilename + '.csv')

def find_latest():
	url = 'http://www.football-data.co.uk/englandm.php'
	response = requests.get(url)
	soup = BeautifulSoup(response.content, 'lxml')
	match = soup.i.text
	match = match.split()[-1]
	match = re.sub('/', '', match)
	last_seen_date = match
	if match != currentdate:
		download_csv('http://www.football-data.co.uk/mmz4281/1819/E0.csv', 'E0')
		store_last_seen_date(match, file_name)

file_name = 'lastseendate.txt'
currentdate = (retrieve_last_seen_date(file_name))
find_latest()