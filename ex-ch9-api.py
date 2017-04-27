import requests, json
serialized = """{ "title" : "Data Science Book",
 "author" : "Joel Grus",
 "publicationYear" : 2014,
 "topics" : [ "data", "science", "data science"] }"""
# parse the JSON to create a Python dict
deserialized = json.loads(serialized)
if "data science" in deserialized["topics"]:
 print deserialized

endpoint = "https://api.github.com/users/joelgrus/repos"
repos = json.loads(requests.get(endpoint).text)

for rows in repos:
    data1=rows["name"]
    print (data1)