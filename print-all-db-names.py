import pymongo

# Verbindung zur lokalen MongoDB-Instanz herstellen
client = pymongo.MongoClient("mongodb://root:example@localhost:27017/")

# Eine Liste aller Datenbanken abrufen
database_names = client.list_database_names()

# Alle Datenbanken abfragen und ausgeben
for db_name in database_names:
    print(db_name)