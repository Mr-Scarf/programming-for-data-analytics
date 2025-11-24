# Write a program called assignment02-bankholdiays.py
# The program should print out the dates of the bank holidays that happen in northern Ireland.
#Last few marks (ie this is more tricky)
#Modify the program to print the bank holidays that are unique to northern Ireland (i.e. do not happen elsewhere in the UK)
#you can choose if you want to use the name or the date of the holiday to decide if it is unique.

#Author: David Scally

import pandas as pd
import requests    # lecture info https://atlantictu-my.sharepoint.com/personal/andrew_beatty_atu_ie/_layouts/15/stream.aspx?id=%2Fpersonal%2Fandrew%5Fbeatty%5Fatu%5Fie%2FDocuments%2FPFDA%20private%202025%2Fvideos%2FPFDA02%2E2%20CSV%2Emp4&ga=1&referrer=StreamWebApp%2EWeb&referrerScenario=AddressBarCopied%2Eview%2E3747d123%2D921a%2D4248%2Dbdbe%2D254ae9602aef

url = "https://www.gov.uk/bank-holidays.json"
response = requests.get(url)
data = response.json()

# i)Show bank holidays that happen in Northern Ireland 2024 - 2027
print(data['northern-ireland']['events']) 




# ii)Show bank holidays that are unique to Northern Ireland


# Convert to dataframe & get list of Northern Ireland holidays(events) vs England/Wales & Scotland
df_nort_ireland_events = pd.DataFrame(data['northern-ireland']['events'])
df_eng_wales = pd.DataFrame(data["england-and-wales"]["events"])
df_scotland = pd.DataFrame(data["scotland"]["events"])

# Merge England/Wales & Scotland holidays
df_uk_holidays = pd.concat([df_eng_wales, df_scotland])                 # Ref: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.concat.html
# Find unique Northern Ireland holidays by excluding UK holidays
unique_ni_holidays = df_nort_ireland_events[~df_nort_ireland_events['title'].isin(df_uk_holidays['title'])]        # Ref: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.isin.html + https://www.geeksforgeeks.org/python/python-pandas-dataframe-isin/
                                                                                                                    # The ~ operator is used to invert the boolean mask returned by isin() https://stackoverflow.com/questions/46054318/tilde-sign-in-pandas-dataframe

print("\nUnique Northern Ireland Bank Holidays 2024 - 2027:")
print(unique_ni_holidays)







