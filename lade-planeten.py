import pymongo

# Verbindung zur lokalen MongoDB-Instanz herstellen
client = pymongo.MongoClient("mongodb://root:example@localhost:27017/")

# Wähle die Datenbank und die Kollektion aus
db = client['Sonnensystem']
collection = db['Planeten']

# Erstelle die Abfrage
query = {"Umlaufzeit_in_Tagen": {"$lt": 400}}

# Führe die Abfrage aus und gib das Ergebnis aus
result = collection.find(query)

for planet in result:
    print(planet['Name'] + ": " + str(planet['Umlaufzeit_in_Tagen']))
