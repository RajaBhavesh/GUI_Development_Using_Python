import json

class Database:

    def add_data(self,name,email,password):

        with open('db.json','r') as f:
            database=json.load(f)        # storing whatever inside the db file to database
        if email in database:
            return 0
        else:
            database[email]=[name,password]
            with open('db.json','w') as f:
                json.dump(database,f)          #if not email in dictionary then we are adding and sending to json file
            return 1


    def search(self,email,password):
        #now we are going to search it is present in json or not so that we can perform login operation
        with open('db.json','r') as f:
            database=json.load(f)
            if email in database:      #if found email check for password
                if database[email][1]==password:
                    return 1             #if password also found then return 1
                else:
                    return 0
            else:           #else return 0
                return 0