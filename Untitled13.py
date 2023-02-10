#!/usr/bin/env python
# coding: utf-8

# In[19]:


from bs4 import BeautifulSoup
import requests

from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np


# In[20]:


class Web_Scraping:
    
    def Beautiful_Soup(self):
        # Fetch the webpage and store in a response.
        response = requests.get("https://etenders.gov.in/eprocure/app")
        html_data = response.text
        # Parse the page using BeautifulSoup
        data = BeautifulSoup(html_data,"html.parser")

        # create list of all columns and put extra column name link.
        column_name = []
        a = data.find_all("th")
        for i in a:
            column_name.append(i.get_text())
        column_name.append("link")

        # create list of all data and store the data in result. 
        result = []
        tbody = data.find("tbody")
        if tbody:
            a = tbody.findAll("tr")
            for i in a:
                ID = i.a["href"].split("/")[-1]
                name = i.find_all("td")[1].text
                date = i.find_all("td")[2].contents[0]
                link = i.a["href"]
                row = [ID,name,date,link]
                result.append(row)


        # Create a DataFrame
        df = pd.DataFrame(result,columns =column_name)

        # Store all data in to csv file

        df.to_csv('Taiyo_assing.csv', sep=',', index=False,header=True)
        # print the dataframe
        display(df)
        print("Web Scraping Successful!")


# In[21]:


obj = Web_Scraping()
obj.Beautiful_Soup()


# In[ ]:





# In[ ]:




