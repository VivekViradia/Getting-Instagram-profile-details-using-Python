#!/usr/bin/env python
# coding: utf-8

# # Getting Instagram profile details using Python
# 

# In[4]:


pip install requests


# In[1]:


pip install beautifulsoup4


# In[2]:


# importing libraries
from bs4 import BeautifulSoup
import requests

# instagram URL
URL = "https://www.instagram.com/{}/"

# parse function
def parse_data(s):
	
	# creating a dictionary
	data = {}
	
	# splitting the content
	# then taking the first part
	s = s.split("-")[0]
	
	# again splitting the content
	s = s.split(" ")
	
	# assigning the values
	data['Followers'] = s[0]
	data['Following'] = s[2]
	data['Posts'] = s[4]
	
	# returning the dictionary
	return data

# scrape function
def scrape_data(username):
	
	# getting the request from url
	r = requests.get(URL.format(username))
	
	# converting the text
	s = BeautifulSoup(r.text, "html.parser")
	
	# finding meta info
	meta = s.find("meta", property ="og:description")
	
	# calling parse method
	return parse_data(meta.attrs['content'])

# main function
if __name__=="__main__":
	
	# user name
	username = "vivek_0710"
	
	# calling scrape function
	data = scrape_data(username)
	
	# printing the info
	print(data)


# In[ ]:




