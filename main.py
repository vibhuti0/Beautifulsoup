#install all the requirements
import requests
from bs4 import BeautifulSoup
url="https://codewithharry.com"
#Step1: Get the html
r=requests.get(url)# helps in get and post request
htmlcontent=r.content #extracts the content of the website
#print(htmlcontent)

#Step2:Parse the HTML
soup=BeautifulSoup(htmlcontent,'html.parser')# after extracting data it it important to parse into a more readable format
#print(soup.prettify)
 
#Step3:HTML Tree traversal
# commonly used types of objects:
#print(type(soup))     #3.Beautiful soup
#print(type(title))     #1.Tag
#print(type(title.string)) #2.Navigable string
#4.comment
title=soup.title #get the title of HTML Page
#get the paragraphs from the page
para=soup.find_all('p')
#print(para)
#anchor=soup.find_all('a') # get the anchors of the page
#print(anchor)
print(soup.find('p'))# gives the first paragraph
#print(soup.find('p')['class']) get the class
print(soup.find('p').get_text())
print(soup.get_text())
