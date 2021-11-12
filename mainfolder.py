import pymongo as pym
from pymongo import MongoClient
from pymongo import collection
import pandas as pd

cluster = MongoClient("mongodb+srv://admindaddy:ormAXKQVdsfLZ10q@cluster0.3wbpf.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
def databaseAccess():
    db = cluster["myFirstDatabase"]
    print("Db connection in process")
    collection = db["notes"]
    # x = collection.find({"id":"6174be71c3d47b41011de7c3"})
    # print(x)
    # post = {"temperature": 22.6,"accelerometer": "123,12312,1323", "pressure_sensor":"1231"}

    # collection.insert_one(post) #this is to find stuff
    # for x in range(1,10):
    #     collection.delete_one( { "accelerometer" : "12312" } );
    #     print(x)

    # result = collection.find({"temperature":22.6}) #This is called querying
    print("halo")
    print(collection)
    comments = pd.DataFrame(collection.find({}, {'_id': 0}))
    print("comments")

    print(comments)
    comments[['x','y','z']] = comments["accelerometer"].str.split(",",expand=True)
    return comments
# print(comments.head()) #i am now able to dataframe the object.

### Here it is time to create something that should be able to create another subsystem of sorts.\



# for a cursor object we can iterate thru the entire data base. 
# how to convert this to a dataframe?
databaseAccess().head()