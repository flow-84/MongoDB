import pymongo

# Verbindung zur MongoDB-Instanz herstellen
client = pymongo.MongoClient("mongodb://root:example@localhost:27017/")

# Datenbank "Music" auswählen
db = client['Music']

# Kollektion "Interpret" erstellen und Daten einfügen
interpret = db['Interpret']
if interpret.count_documents({}) == 0:
    interpret_data = [
        {
            'name': 'Ton Steine Scherben',
            'genre': 'Rock',
            'origin': 'Berlin'
        },
        {
            'name': 'The Beatles',
            'genre': 'Rock',
            'origin': 'Liverpool'
        }
    ]
    interpret.insert_many(interpret_data)

# Kollektion "Musikstück" erstellen und Daten einfügen
musikstueck = db['Musikstück']
if musikstueck.count_documents({}) == 0:
    interpret_data = list(interpret.find())
    musikstuecke_data = [
        {
            'title': 'Keine Macht für Niemand',
            'year': '1972',
            'album': 'Keine Macht für Niemand',
            'interpret': interpret_data[0]['_id']
        },
        {
            'title': 'Der Traum ist aus',
            'year': '1972',
            'album': 'Keine Macht für Niemand',
            'interpret': interpret_data[0]['_id']
        },
        {
            'title': 'Macht kaputt, was euch kaputt',
            'year': '1971',
            'album': 'Warum geht es mir so dreckig?',
            'interpret': interpret_data[0]['_id']
        },
        {
            'title': 'Rauch-Haus-Song',
            'year': '1972',
            'album': 'Keine Macht für Niemand',
            'interpret': interpret_data[0]['_id']
        },
        {
            'title': 'Wir müssen hier raus',
            'year': '1976',
            'album': 'IV',
            'interpret': interpret_data[0]['_id']
        },
        {
            'title': 'Let It Be',
            'year': '1970',
            'album': 'Let It Be',
            'interpret': interpret_data[1]['_id']
        },
        {
            'title': 'Hey Jude',
            'year': '1968',
            'album': 'The Beatles Again',
            'interpret': interpret_data[1]['_id']
        },
        {
            'title': 'Yesterday',
            'year': '1965',
            'album': 'Help!',
            'interpret': interpret_data[1]['_id']
        }
    ]
    musikstueck.insert_many(musikstuecke_data)

# Verknüpfung der Kollektionen
if 'interpret' not in musikstueck.index_information():
    musikstueck.create_index([('interpret', 1)])

print('Daten erfolgreich in MongoDB eingefügt.')
