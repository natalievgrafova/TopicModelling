
# pip install --upgrade pip
# git clone nat's git 
# git switch Sarkis
# virtualenv venvmedia
# source venvmedia/bin/activate
# pip install pandas numpy matplotlib pymongo


import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydatabase"]