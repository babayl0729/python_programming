import requests

# GET 
# useful of retrieving data. Data passed in
# query string. Should have no "side-effects".
# Can be cached. Can be bookmarked
# POST
# Useful for writing data. Data passed in 
# request body. Can have "side-effects".
# Not cached. Can't be bookmarked.

# API-application programming interface
# Allows you to get data from another 
# application without needing to understand
# how the application works. Can often send
# data back in different formats. Examples
# of companies with APIs: GitHub,Spotify,Google.

# requests Module
# Lets us make HTTP requests from our Python
# code! Installed using pip. Useful for web
# scraping/crawling,grabbing data from other
# APIs,etc.

url = "https://icanhazdadjokes.com/"
# will show html elements 
# response = requests.get(url,headers={"Accept":"text/html"})
# print(response.text)

# plain format
# response = requests.get(url,headers={"Accept":"text/plain"})
#print(response)

# in JSON format and it's better
response = requests.get(url,headers={"Accept":"application/json"})
data = response.json()
print(data["joke"])
print(f"status: {data['status']}")

# Query String-a way data to the server as
# part od a GET request.
# http://www.example.com/?key1=value1&key2=value2
url2 = "https://icanhazdadjokes.com/search"

response2 = requests.get(
    url,
    headers={"Accept":"application/json"},
    params={"term":"cat","limit":1}
)

data2 = response2.json()
print(data2["results"])