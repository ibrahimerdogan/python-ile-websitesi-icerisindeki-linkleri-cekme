import urllib
import re
import requests
import mysql.connector
import os
import argparse
from bs4 import BeautifulSoup
from array import *

parser = argparse.ArgumentParser()
parser.add_argument("--url", help="URL Adresi Yaziniz (http://example.com)")
args = parser.parse_args()
url = args.url
#url    = raw_input("Taranacak bir websitesi giriniz : ")
r  = requests.get(url)
data = r.text
soup = BeautifulSoup(data)

for link in soup.find_all('a'):
    con=mysql.connector.connect(user="root", passwd="root", database="root")
    print(link.get('href'))+"\n"
    cur = con.cursor()
    sql_insert=('INSERT INTO site (site,linkler) values ("%s","%s")' % (url,link.get('href')))
    cur.execute(sql_insert)
    con.commit()
    con.close()
