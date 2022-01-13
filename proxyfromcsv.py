import requests
import random
import csv
import concurrent.futures

#opens a csv file of proxies and prints out the ones that work with the url in the extract function

proxylist = []

with open('gg.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        proxylist.append(row[0])
print(len(proxylist))
def extract(proxy):
    #this was for when we took a list into the function, without conc futures.
    #proxy = random.choice(proxylist)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0'}
    try:
        #change the url to https://httpbin.org/ip that doesnt block anything
        r = requests.get('https://api.airbnb.com/v2', headers=headers, proxies={'http' : proxy,'https': proxy}, timeout=4)
        print(proxy)
    except:
        pass
    return proxy

with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(extract, proxylist)
