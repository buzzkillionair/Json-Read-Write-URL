import json
from urllib.request import urlopen
#Author: Buzzkillionair
#Date Completed: September 25, 2019
#Job: Parses through the fresh onions website json and take all urls,
#then writes them to a file.

#Url where JSON is found(Changes based on where json is found)
jsonUrl ='INPUT JSON URL HERE'
#File being written to
white_lst = open('white_list.txt', 'w+')
#Reaches to retrieve json
with urlopen() as response:
    source = response.read()

#print(source)

data = json.loads(source)

#print(json.dumps, indent=2)

#parses json and writes to file.
for item in data:
    url = item['url']
    white_lst.write(url + "\n")
    print(url)

#This portion was used when you manually extracted
#the json from the fresh onions site
#
#with open('all.json', 'r') as f:
#    all_url = json.load(f)
#
#for url in all_url:
#    print(url['url'])
#    white_lst.write(url['url'] + "\n")
