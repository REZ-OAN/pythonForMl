"""
 written in {}
 key, value pairs
 key must be under ""
 can be nested
 can use array as value
 can use object as value
a light weight data represting method . Which helps
us to transfer data easily 
JSON converted into python dictionary to use in python
and Python dictionary converted into JSON to transfer data

"""
## python dictionary which represents some information
## about some books

books = {
    "Whispers of Eternity": {
        "name": "Whispers of Eternity",
        "author": "Isabella Bennett",
        "release_date": "2023-04-15",
        "overview": "In a world where time travel is a reality, a young historian discovers a hidden message from the future that could change the course of history."
    },
    "Crimson Skies": {
        "name": "Crimson Skies",
        "author": "Nathan Archer",
        "release_date": "2022-08-02",
        "overview": "Amidst an intergalactic war, a skilled pilot finds herself torn between loyalty to her planet and a growing love for an enemy from the stars."
    },
    "Echoes of Silence": {
        "name": "Echoes of Silence",
        "author": "Eleanor Collins",
        "release_date": "2021-11-19",
        "overview": "A reclusive artist's life takes an unexpected turn when a mysterious new neighbor moves in next door, bringing with them a haunting secret."
    },
    "The Clockwork Conspiracy": {
        "name": "The Clockwork Conspiracy",
        "author": "Samuel Holloway",
        "release_date": "2020-03-08",
        "overview": "In a steampunk-inspired world, a brilliant inventor and a cunning detective must unravel a web of clockwork-driven espionage threatening their city."
    },
    "Beneath the Amber Tree": {
        "name": "Beneath the Amber Tree",
        "author": "Grace Thompson",
        "release_date": "2019-06-25",
        "overview": "Set in a medieval fantasy realm, a young scribe's quest for an ancient manuscript leads her to a forgotten forest where magical secrets lie dormant."
    },
    "City of Glass and Shadows": {
        "name": "City of Glass and Shadows",
        "author": "Lucas Blackwood",
        "release_date": "2018-01-12",
        "overview": "A master thief and an enigmatic sorcerer are reluctantly teamed up to uncover a sinister plot that threatens to plunge their city into eternal darkness."
    },
    "Sands of Destiny": {
        "name": "Sands of Destiny",
        "author": "Amina Patel",
        "release_date": "2017-09-30",
        "overview": "In a desert realm where water is scarce and power struggles are fierce, a young warrior seeks a legendary oasis that is said to grant incredible abilities."
    },
    "The Artisan's Dilemma": {
        "name": "The Artisan's Dilemma",
        "author": "Oliver West",
        "release_date": "2016-05-14",
        "overview": "A gifted craftsman becomes entangled in a web of political intrigue and forbidden magic as he strives to perfect his greatest masterpiece yet."
    },
    "Beyond the Nebula": {
        "name": "Beyond the Nebula",
        "author": "Serena Morrison",
        "release_date": "2015-02-07",
        "overview": "In the far future, a spacefaring archaeologist stumbles upon an ancient alien artifact that holds the key to understanding the mysteries of the universe."
    },
    "The Enchanted Chronicles: Origins": {
        "name": "The Enchanted Chronicles: Origins",
        "author": "Jonathan Rivers",
        "release_date": "2014-08-20",
        "overview": "This enchanting tale delves into the origins of a magical realm, revealing the untold stories of legendary creatures and the rise of a forgotten hero."
    }
}
## importing json module
import json
booksJSON = json.dumps(books)
## it converts the dictionary into a string but in json format
print(booksJSON)
## writing to file 
with open("./pythonJSON/books.txt",'w') as file :
    file.write(booksJSON)

## reading the json 
file = open("./pythonJSON/books.txt","r")

stringBooks = file.read()
print(type(stringBooks))
jsonBooks = json.loads(stringBooks)
print(type(jsonBooks))
## checking this dictionary is working fine or not
print(jsonBooks['The Enchanted Chronicles: Origins'])

for name in jsonBooks :
    print(jsonBooks[name])