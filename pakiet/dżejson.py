import json

# with open('person.json') as p:
#     data = json.load(p)


# person = '{"name":"Bob","languages":["Polish","English"]}'
# dict = json.loads(person)

# print(dict)
# print(data)


slownik = {"imie": "Tomek",
           "2": 2,
           "trzeci": 3,
           "czyPali": False,
           "czyPije": None
           }
with open('slownik.json', 'w') as f:
    json.dump(slownik, f, indent=4, sort_keys=True)

# slowni_json = json.dumps(slownik)

# print(slowni_json)
