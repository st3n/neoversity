# install mongo db
> sudo apt-get install gnupg curl
> curl -fsSL https://pgp.mongodb.com/server-7.0.asc | \
   sudo gpg -o /usr/share/keyrings/mongodb-server-7.0.gpg \
   --dearmor
> echo "deb [ arch=amd64,arm64 signed-by=/usr/share/keyrings/mongodb-server-7.0.gpg ] https://repo.mongodb.org/apt/ubuntu jammy/mongodb-org/7.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-7.0.list
> sudo apt-get update
> sudo apt-get install -y mongodb-org

# run daemon
> sudo systemctl start mongod
> sudo systemctl enable mongod

# configuration file
> sudo nano /etc/mongod.conf

# run mongo client
> mongosh
> mongosh -u [username] -p [password]

# mongosh auth
> use admin
> db.auth("username", "password")

# support js
> function factorial (n) {
   if (n <= 1) return 1;
   return n * factorial(n - 1);
   }
> factorial(5);
> let current_date = new Date();
> current_date;
> factorial()

# show all databases
> show dbs

# show current db
> db

# use db
> use <db_name>
> use movies

# create collection
> db.createCollection(<collection_name>);
> db.createCollection("favorites");

# show all collections
> show collections

# drop collection
> db.<collection_name>.drop()
> db.favorites.drop()

# rename collection
> db.oldCollectionName.renameCollection(<new_name>)

# rename and move to other db
> use newDatabase
> db.createCollection("newCollectionName")
> use oldDatabase
> db.oldCollectionName.find().forEach(function(doc) {
    db.getSiblingDB("newDatabase").newCollectionName.insertOne(doc);
});

> db.favorites.find().forEach(function(doc) {
    db.getSiblingDB("movies_new").favorites_new.insertOne(doc);
});

# drop db
> db.dropDatabase()

# clone collection to other db
> db.runCommand({
     cloneCollection: "sourceDB.sourceCollection",
     from: "localhost:27017",
     query: {},
     copyIndexes: true
   });

# create document
> movie_star_wars = {"title" : "Star Wars: Episode IV – A New Hope", "director" : "George Lucas", "year" : 1977}
> db.favorites.insertOne(movie)

# many insert
> lotr_fellowship = {"title" : "The Lord of the Rings : The Fellowship of the Ring", director: "Peter Jackson", "year" : 2001} 
> pulp_fiction = {"title" : "Pulp Fiction", "director" : "Quentin Tarantino", "year" : 1994}
> db.favorites.insertMany([lotr_fellowship, pulp_fiction])

# show all documents in collection
> db.favorites.find()

# show "first" using _id(timestamp)
> db.favorites.findOne()

# find document
> db.favorites.find({_id: ObjectId("65a792603facbc7c18557fb7")})
> db.favorites.findOne({_id: ObjectId("64f77091bd83b790821322a8")})
> db.favorites.find({ director: /Peter/ }) 
> db.favorites.find({ year: { $gte: 2000 } })

# find using complex conditions
> db.favorites.find({
      $and: [
        { director: /Peter/ },
        { year: { $gte: 2000 } }
      ]
    });
> db.favorites.find({
      director: /Peter/,
      year: { $gte: 2000 }
    });
> db.favorites.find({
      $or: [
        { director: /Peter/ },
        { year: { $gte: 1990 } }
      ]
    });
> db.favorites.find({
      $and: [
        {
          $or: [
            { director: /Peter/ },
            { year: { $gte: 2000 } }
          ]
        },
        { director: { $ne: "Quentin Tarantino" } }
      ]
    });

# update document
> db.favorites.updateOne(
    { _id: ObjectId("65a792e33facbc7c18557fb8") }, 
    { $set: { title: 'The Lord of the Rings: The Fellowship of the Ring (Updated Title)' } }
);

# delete document
> db.favorites.deleteOne({ _id: ObjectId("64f774cfbd83b790821322a9") });
> db.favorites.deleteMany({ director: "Peter Jackson" });
> db.favorites.deleteMany({ year: { $lt: 2000 } });

# add new field
> db.favorites.updateMany({}, { $set: { reviews: [] } });

# connect to remote db
> mongosh mongodb://admin:secret_password@192.168.1.100:27017/mydb
> mongosh mongodb://192.168.1.100:27017/mydb

> conn = new Mongo("some-host:27017")
> db = conn.getDB("mydb")

# count documents 
> db.favorites.countDocuments()

# count collections
> db.getCollectionNames().length

# install compass
> wget https://downloads.mongodb.com/compass/mongodb-compass_1.39.3_amd64.deb
> sudo dpkg -i mongodb-compass_1.39.3_amd64.deb
> sudo apt update
> sudo apt install -f
> sudo dpkg -i mongodb-compass_1.39.3_amd64.deb
> mongodb-compass

# use schema for collection
> db.createCollection("users", {
       validator: {
          $jsonSchema: {
             bsonType: "object",
             required: ["name", "age"],
             properties: {
                name: {
                   bsonType: "string",
                   description: "must be a string and is required"
                },
                age: {
                   bsonType: "int",
                   minimum: 0,
                   description: "must be an integer >= 0 and is required"
                }
             }
          }
       }
    });

# show validation schema 
> db.getCollectionInfos({name: "users"})
> db.runCommand({
    listCollections: 1,
    filter: { name: "Genre" }
}).cursor.firstBatch[0].options.validator

> db.runCommand({
    listCollections: 1,
    filter: { name: { $in: ["Genre", "Movie", "Director"] } }
}).cursor.firstBatch.forEach(collection => {
    print(`Collection: ${collection.name}`);
    if (collection.options && collection.options.validator) {
        printjson(collection.options.validator);
    } else {
        print("No validation rules.");
    }
});

# modify schema
> db.runCommand({
   collMod: "users",
   validator: {
      $jsonSchema: {
         bsonType: "object",
         required: ["name", "age"],
         properties: {
            _id: {
               bsonType: "objectId"
            },
            name: {
               bsonType: "string",
               description: "must be a string and is required"
            },
            age: {
               bsonType: "int",
               minimum: 0,
               description: "must be an integer >= 0 and is required"
            }
         },
         additionalProperties: false
      }
   },
   validationLevel: "strict"
});

# delete field
> db.users.updateMany({}, { $unset: { is_admin: 1 } });

# aggregation
> db.favorites.aggregate([
        {
            $group: {
                _id: "$director",
                numberOfMovies: { $sum: 1 }
            }
        },
        { $sort: { numberOfMovies: -1 } }  
    ]);
> db.favorites.aggregate([
        {
            $group: {
                _id: null,
                averageYear: { $avg: "$year" }
            }
        }
    ]);
> db.favorites.aggregate([
        {
            $group: {
                _id: null,
                averageYear: { $avg: "$year" }
            }
        },
        {
            $project: {
                _id: 0,
                averageYear: { $round: ["$averageYear", 2] }
            }
        }
    ]);
> db.favorites.aggregate([
        {
            $match: { year: { $gte: 1990, $lt: 2000 } }
        },
        {
            $group: {
                _id: null,
                numberOfMovies: { $sum: 1 }
            }
        }
    ]);
> db.favorites.aggregate([
        {
            $match: { reviews: { $not: { $size: 0 } } }
        }
    ]);

# sort 
> db.favorites.find().sort({ year: 1 });
> db.favorites.find().sort({ year: -1 });
> db.favorites.find().sort({ year: 1, director: 1 });

# relations
> db.directors.insertOne({ name: "George Lucas",})
> db.favorites.updateMany(
    { director: "George Lucas" }, 
    { $set: { director: ObjectId("65a79b943facbc7c18557fba") } }
);

# "join"
> db.favorites.aggregate([
   {
      $lookup:
         {
           from: "directors",     
           localField: "director",     
           foreignField: "_id",       
           as: "directorDetails"
         }
   }
])

# m2m
> db.actors.insertMany([{
        "name": "Harrison Ford"
    },
    {
        "name": "Samuel L. Jackson"
    },
    {
        "name": "John Travolta"
    }])
> db.favorites.updateOne(
        { _id: ObjectId("65a792603facbc7c18557fb7") },
        { $set: { actors: [ObjectId("65a79c843facbc7c18557fbb")] } }
    );
> db.favorites.updateOne(
    { _id: ObjectId("64f774cfbd83b790821322aa") },
    { $set: { actors: [ObjectId("64f78fd5bd83b790821322b0"), ObjectId("64f78fd5bd83b790821322b1")] } }
 );
> db.favorites.aggregate([
        {
            $lookup: {
                from: "actors",
                localField: "actors",
                foreignField: "_id",
                as: "actorDetails"
            }
        }
    ]).pretty();
> db.favorites.aggregate([
        {
            $lookup: {
                from: "directors",
                localField: "director",
                foreignField: "_id",
                as: "directorDetails"
            }
        },
        {
            $lookup: {
                from: "actors",
                localField: "actors",
                foreignField: "_id",
                as: "actorDetails"
            }
        }
    ]);

# use foreign js scripts
> mongosh script1.js script2.js script3.js


>db.Movie.aggregate([
  {
    $lookup: {
      from: "Genre",
      localField: "genres",
      foreignField: "_id",
      as: "genre_names"
    }
  },
  {
    $lookup: {
      from: "Director",
      localField: "directors",
      foreignField: "_id",
      as: "director_names"
    }
  },
  {
    $lookup: {
      from: "Star",
      localField: "stars",
      foreignField: "_id",
      as: "star_names"
    }
  },
  {
    $project: {
      name: 1,
      year: 1,
      time: 1,
      imdb: 1,
      votes: 1,
      meta_score: 1,
      gross: 1,
      description: 1,
      certification: 1,
      "genre_names.name": 1,
      "director_names.name": 1,
      "star_names.name": 1
    }
  }
]).pretty()

# count movies by genres
> db.Movie.aggregate([
  {
    $unwind: "$genres"
  },
  {
    $lookup: {
      from: "Genre",
      localField: "genres",
      foreignField: "_id",
      as: "genre_info"
    }
  },
  {
    $unwind: "$genre_info"
  },
  {
    $group: {
      _id: "$genre_info.name",
      movie_count: { $sum: 1 }
    }
  },
  {
    $sort: {
      movie_count: -1
    }
  },
  {
    $project: {
      genre_name: "$_id",
      movie_count: 1,
      _id: 0
    }
  }
]).pretty()
