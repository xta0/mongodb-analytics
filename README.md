## MongoDB Atlas 

### Setup Environment

1. Setup MongoDB Atlas Cluster
    - Cluster name - mflix
    - Project name - anaylitcs
    - Admin user
2. Setup local development environment
    - install mongo shell on OSX

    ```shell
    brew install mongodb --with-openssl
    ```
    - test connection

    ```shell
    mongo "mongodb+srv://mflix-1hs5t.mongodb.net/test" --username analytics
    ```

    - setup python dev environment
3. Upload `.csv` file to cluster
    - download [movie_initial.csv](https://s3.amazonaws.com/edu-static.mongodb.com/lessons/coursera/building-an-app/getting-data-into-mongodb/movies_initial.csv) 
    - upload to the cluster using commandline 

    ```shell
    mongoimport --type csv --headerline --db mflix --collection movies_initial --host "<CLUSTER>/<SEED_LIST>" --authenticationDatabase admin --ssl --username <username> --password <password> --file movies_initial.csv
    ```

4. Setup MongoDB Compass
    - [Download here](https://www.mongodb.com/download-center?jmp=hero#compass)
    - Connect to the cluster 

5. Test connectionvia PyMongo

```python
from pymongo import MongoClient

client = MongoClient("mongodb+srv://analytics:<PASSWORD>@mflix-1hs5t.mongodb.net/test?retryWrites=true")
db = client.mflix
print(db)
```

### Aggregation Framework

The Aggregation framework is a set of analytics tools within MongoDB, that allow you to run various types of reports or analysis on documents in one or more MongoDB collections. The aggregation framework is based on the concept of a pipeline.

![Pipeline](https://image.ibb.co/m7Bes9/Screen_Shot_2018_09_10_at_4_56_27_PM.png)

The idea with an aggregation pipeline is that we take input from a MongoDB collection and pass the documents from that collection through one or more stages,each of which performs a different operation on its inputs.
