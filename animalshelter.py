#Example Python Code to Insert a Document
from pymongo import MongoClient
from bson.objectid import ObjectId
import json

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self,username,password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections. 
        self.client = MongoClient('mongodb://%s:%s@localhost:54550'%(username,password))
        self.database = self.client['AAC']

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            self.database.animals.insert_one(data)  # data should be dictionary 
            print("++++++++++++++++++ animal created successfully+++++++++++++++")           
        else:
            raise Exception("Nothing to save, because data parameter is empty")
            
# THIS IS A READ METHOD
    def read(self, data):
        if data is not None:
            data = self.database.animals.find_one(data,{"_id":False}) # data should be dictionary   
            return data
        else:
            raise Exception("nothing to read, hint is empty")

# this method will recieve a dictonary, find all items that match the dictonary 
#values and delete them 
    def delete(self, _data):
        if _data is not None:
            data = self.read(_data) # check if animal exists
            if data is None:
                print("Animal not found")
                return
            #if found delete the animal or animals 
            self.database.animals.delete_many(_data) #data should be dictionary 
            data = self.read(_data) #confirm of animal was deleted 
            return data
        else: 
            raise Exception("nothing to read, hint is empty")

     # this method update using the id of the collection, one can alos update using any key 
     def update(self, _keys,_data):
        if _data is not None and _keys is not None: 
            self.database.animals.update_many(_keys,{'$set':_data}) #_keys will check for the doc to update 
            data = self.read(_data)
            return data 
        else: 
            raise Exception("please enter both key and data to modify the collection")

