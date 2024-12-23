# Data Science: project

The goal of the project is to develop a software that enables one to process data stored in CSV format and to upload them into an relational databases to query it according to predefined operations. 

## Data

Exemplar data for testing the project have been made available. In particular:

* for creating the relational database, there is two one, [a CSV file](meta.csv), containing metadata about cultural heritage objects. Please note that multiple authors of the same object will be contained in just one string and split by `; `.


## Workflow

![Workflow of the project](img/workflow.png)


## UML of data model classes

![Data model classes](datamodel-uml.png)

All the methods of each class must return the appropriate value that have been specified in the object of that class when it has been created. It is up to the implementer to decide how to enable someone to add this information to the object of each class, e.g. by defining a specific constructor. While one can add additional methods to each class if needed, it is crucial that the *get* methods introduced in the UML diagram are all defined.

## UML of additional classes

![Additional classes](classes-uml.png)

All the attributes methods of each class are defined as follows. All the constructors of each of the class introduced in the UML diagram do not take in input any parameter. While one can add additional methods to each class if needed, it is crucial that all the methods introduced in the UML diagram are defined.


### Class `Upload`

#### Attributes
`dbPath`: the variable containing the path of the database, initially set as an empty string, that will be updated with the method `setDbPath`.

#### Methods
`getDbPath`: it returns the path of the database.

`setDbPath`: it enables to set a new path for the database to handle.

`uploadData`: it takes in input the path of the CSV file containing metadata and uploads them in the database.


### Class `Query`

#### Attributes
`dbPath`: the variable containing the path of the database, initially set as an empty string, that will be updated with the method `setDbPath`.

#### Methods
`getDbPath`: it returns the path of the database.

`setDbPath`: it enables to set a new path for the database to handle.

`getAllPeople`: it returns a list of objects having class `Person` containing all the people included in the database accessible.

`getAllCulturalHeritageObjects`: it returns a list of objects having class `CulturalHeritageObject` containing all the cultural heritage objects included in the database.

`getCulturalHeritageObjectByType`: it returns a list of objects having class `CulturalHeritageObject` containing all the cultural heritage objects having the type specified as input.



## Uses of the classes

```
# Supposing that all the classes developed for the project
# are contained in the file 'impl.py', then:

# 1) Importing all the classes for creating the relational database
from impl import Upload

# 3) Importing the class for querying the database
from impl import Query

# Once all the classes are imported, first create the relational
# database using the related source data
rel_path = "relational.db"
ul = Upload()
ul.setDbPath(rel_path)
ul.uploadData("meta.csv")

# In the next passage, create the query object for the
# database, using the related class
qy = Query()
qy.setDbPath(rel_path)

# Finally, you run the methods querying the database
result_q1 = qy.getAllPeople()
result_q2 = qy.getCulturalHeritageObjectByType("Nautical chart")
# etc...
```