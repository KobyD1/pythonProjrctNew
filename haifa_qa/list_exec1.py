
cities = ["Tel-Aviv","New-York","St-Pitesburg"]

for city in cities:
    if (city.count("-")>0):
        print(f"{city} contains more thann single word")

    if (city.index("-")==2):
        print (f"{city} contains - at special position ")
