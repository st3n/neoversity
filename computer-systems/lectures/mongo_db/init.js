db = db.getSiblingDB('movie_db');
db.createCollection('initCollection');
db.initCollection.insert({ initialized: true });
