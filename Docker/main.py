#import requests
#from bs4 import BeautifulSoup


#url = "https://www.geeksforgeeks.org/getting-started-with-python-programming/"


#response = requests.get(url)


#soup = BeautifulSoup(response.content, 'html.parser')


#headings = soup.find_all('h2')[:5]


#print("Extracted Headings from the page:")
#for i, heading in enumerate(headings, start=1):
#    print(f"{i}. {heading.text}")

from pymongo import MongoClient
url = 'mongodb://mongodb:27017/'
with MongoClient(url) as Client:
    db = Client['mydatabase']
    collection = db['mycollection']
    
    temp = {
        'name' : 'john',
        'age' : '22'
    }
    collection.insert_one(temp)
    
with MongoClient(url) as client:
    db = client['mydatabase']
    collection = db['mycollection']
    
    for doc in collection.find():
        print(doc)
        