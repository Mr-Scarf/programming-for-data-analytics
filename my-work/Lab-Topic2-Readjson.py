#Read JSON from internet 
#6. Copy this URL into browser and see the JSON it returns. 
#https://www.gov.uk/bank-holidays.json 
#7. Write a program to print this JSON to the console. 

# Author: David Scally
# https://www.w3schools.com/python/module_requests.asp

import requests

url = "https://www.gov.uk/bank-holidays.json"
response = requests.get(url)
data = response.json()
#print(data)

#8. Modify the program to only output the first holiday in northern ireland 

print(data['northern-ireland']['events'][0]) 
