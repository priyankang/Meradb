import json
import os
import random

# fileName = "hello.db"
# Default argument dena ek acchi coding practice hai.
# Isse agar user koi argument nahi bhi de, toh bhi code sahi chalega
def load(fileName='hello.db'):
    # meradb.MeraDB("table.db").load_file()
    
    meraDB = MeraDB(fileName)
    meraDB.load_file()
    return meraDB

class MeraDB():
    
    fileName = ""
    jObject = {}

    def __init__(self, fileName):
      
        self.fileName = fileName

    def load_file(self):
   
        print ("Loading Database from ", self.fileName, " !")
        if os.path.exists(self.fileName):
            file = open(self.fileName,'r')
        else:
            file = open(self.fileName,'w')
        data = file.read()
        if data == "":
            self.dump()   
        else:
            self.jObject = json.loads(data)
        print "DB loaded successfully!"
        return self.jObject

    def dump(self):
    
        print "Dumping database to ", self.fileName, " !"
        
        # open(self.fileName, 'w').write(json.dumps(self.jObject))
        # ```
        # You can also write the above line as:
        file_handler = open(self.fileName, 'w')
        json_dump = json.dumps(self.jObject)
        file_handler.write(json_dump)
        file_handler.close()
        # ```

        print "DB dumped successfully!"
        return "OK" 
    def set(self,key,value):
        self.jObject[key]=value
        print(value)
        return True
    def get(self,key):
        print (self.jObject[key])
        return True
    def get(self,key):
        try:
            print(self.jObject[key])
            return True
        except:
            print("There is no key" + key)
            return False
    def get_all(self):
        key_list = []
        for i in self.jObject: 
            key_list.append(i)
        print (key_list)    
        return key_list
    def rem(self,key):
        try:
            del self.jObject[key]
            return True
        except:
            print("There is no key"+ key)
            return False
    def exists(self,key):
        if key in self.jObject:
            print True
            return True
        else:
            print False
            return False
    def total_key(self,key):
        print len(self.jObject)
        return True
    def del_db(self,key):
        print(self.jObject.clear())
        return True
    def random_insert(self,key):
        new_list =[]
        for i in self.jObject:
            new_list.append[key,Value]
            



    