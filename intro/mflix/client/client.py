from pymongo import MongoClient
import pprint 

client = MongoClient("mongodb+srv://analytics:analytics-password@mflix-1hs5t.mongodb.net/test?retryWrites=true")

### query
pipeline = [
    {
        #identifier begins with $
        '$group':{
            #取每一条记录的language值
            '_id':{'language':'$language'},
            'count':{'$sum':1}
        }
    }
]

pprint.pprint(list(client.mflix.movies_initial.aggregate(pipeline)))

