import sqlite3
import csv



class Upload:
    def __init__(self):
        self.dbPath = ""

    def getDbPath(self) -> str:
        return self.dbPath

    def setDbPath(self, path: str) -> bool:
        self.dbPath = path
        print("\tUpload.setDbPath is running...")
        print("\t\tdbPath --> ", self.dbPath)
        return True

    def uploadData(self, path: str) -> bool:
        try:
            print("\tUpload.uploadData is running...")
            conn = sqlite3.connect(self.dbPath)
            cursor = conn.cursor()
            
##            cursor.execute("""
##            DROP TABLE CulturalHeritageObject
##            """)
##            cursor.execute("""
##            DROP TABLE Person
##            """)
##            cursor.execute("""
##            DROP TABLE HasAuthor
##            """)

            cursor.execute("""
            CREATE TABLE IF NOT EXISTS CulturalHeritageObject (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                date TEXT NOT NULL,
                type TEXT NOT NULL
            )""")
            
            print("\t\tCulturalHeritageObject table was Created.")
            
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS Person (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            )""")

            print("\t\tPerson table was Created.")

            cursor.execute("""
            CREATE TABLE IF NOT EXISTS HasAuthor (
                cho_id INTEGER,
                person_id INTEGER,
                FOREIGN KEY (cho_id) REFERENCES CulturalHeritageObject(id),
                FOREIGN KEY (person_id) REFERENCES Person(id)
            )""")
            print("\t\tHasAuthor table was Created.")


            with open(path, "r", encoding="utf-8") as file:
                reader = csv.reader(file)
                next(reader)  # Skip header row
                for row in reader:
                    if len(row) != 4:
                        print(f"Error: CSV row does not have exactly 4 fields: {row}")
                        continue
                    cho_type, title, date, authors = row
                    cursor.execute("""
                    INSERT INTO CulturalHeritageObject (type, title, date)
                    VALUES (?, ?, ?)
                    """, (cho_type, title, date))
                    cho_id = cursor.lastrowid
                    for author in authors.split("; "):
                        cursor.execute("SELECT id FROM Person WHERE name = ? ", (author,))
                        result = cursor.fetchone()
                        if result:
                            person_id = result[0]
                        else:
                            cursor.execute("INSERT INTO Person (name) VALUES (?)", (author,))
                            person_id = cursor.lastrowid

                        cursor.execute("INSERT INTO HasAuthor (cho_id, person_id) VALUES (?, ?)", (cho_id, person_id))

            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print("Error uploading data:", e)
            return False
    print("Upload Class is imported.")


    


class Query:
    def __init__(self):
        self.dbPath = ""

    def getDbPath(self) -> str:
        return self.dbPath

    def setDbPath(self, path: str) -> bool:
        self.dbPath = path
        return True

    def getAllPeople(self) -> list:
        try:
            conn = sqlite3.connect(self.dbPath)
            cursor = conn.cursor()
            cursor.execute("SELECT name FROM Person")
            people = [Person(row[0]) for row in cursor.fetchall()]
            conn.close()
            return people
        except Exception as e:
            print("Error fetching people:", e)
            return []

    def getAllCulturalHeritageObjects(self) -> list:
        try:
            conn = sqlite3.connect(self.dbPath)
            cursor = conn.cursor()
            cursor.execute("SELECT title, date, type FROM CulturalHeritageObject")
            chos = [CulturalHeritageObject(row[0], row[1], row[2]) for row in cursor.fetchall()]
            conn.close()
            return chos
        except Exception as e:
            print("Error fetching cultural heritage objects:", e)
            return []

    def getCulturalHeritageObjectByType(self, cho_type: str) -> list:
        try:
            conn = sqlite3.connect(self.dbPath)
            cursor = conn.cursor()
            cursor.execute("SELECT title, date, type FROM CulturalHeritageObject WHERE type = ?", (cho_type,))
            chos = [CulturalHeritageObject(row[0], row[1], row[2]) for row in cursor.fetchall()]
            conn.close()
            return chos
        except Exception as e:
            print("Error fetching cultural heritage objects by type:", e)
            return []
    print("Query Class is imported.")
        
class Person:
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name
    print("Person Class is imported.")

class CulturalHeritageObject:
    def __init__(self, title: str, date: str, cho_type: str):
        self.title = title
        self.date = date
        self.type = cho_type

    def getTitle(self) -> str:
        return self.title

    def getDate(self) -> str:
        return self.date

    def getType(self) -> str:
        return self.type

    def getAuthors(self) -> list:
        try:
            conn = sqlite3.connect(Query().getDbPath())
            cursor = conn.cursor()
            cursor.execute("""
            SELECT Person.name FROM Person
            JOIN HasAuthor ON Person.id = HasAuthor.person_id
            JOIN CulturalHeritageObject ON HasAuthor.cho_id = CulturalHeritageObject.id
            WHERE CulturalHeritageObject.title = ?
            """, (self.title,))
            authors = [Person(row[0]) for row in cursor.fetchall()]
            conn.close()
            return authors
        except Exception as e:
            print("Error fetching authors:", e)
            return []
    print("CulturalHeritageObject Class is imported.")
    for _ in range(3):
        print()

