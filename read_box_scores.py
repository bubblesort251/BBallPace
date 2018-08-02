"""This file should be a basic web scraper"""

from bs4 import BeautifulSoup
import requests

"""Being Basic Scrape"""
source = requests.get('https://www.basketball-reference.com/leagues/NBA_2018_games-october.html').text
soup = BeautifulSoup(source, 'lxml')
schedule = soup.find('table', id='schedule')

table = schedule.find('tbody')
row = table.find('tr')

print (row)