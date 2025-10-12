# Write a program called assignment02-bankholdiays.py
# The program should print out the dates of the bank holidays that happen in northern Ireland.
#Last few marks (ie this is more tricky)
#Modify the program to print the bank holidays that are unique to northern Ireland (i.e. do not happen elsewhere in the UK)
#you can choose if you want to use the name or the date of the holiday to decide if it is unique.

#Author: David Scally

import requests    # lecture info https://atlantictu-my.sharepoint.com/personal/andrew_beatty_atu_ie/_layouts/15/stream.aspx?id=%2Fpersonal%2Fandrew%5Fbeatty%5Fatu%5Fie%2FDocuments%2FPFDA%20private%202025%2Fvideos%2FPFDA02%2E2%20CSV%2Emp4&ga=1&referrer=StreamWebApp%2EWeb&referrerScenario=AddressBarCopied%2Eview%2E3747d123%2D921a%2D4248%2Dbdbe%2D254ae9602aef

url = "https://www.gov.uk/bank-holidays.json"
response = requests.get(url)
data = response.json()

print(data['northern-ireland']['events']) 


