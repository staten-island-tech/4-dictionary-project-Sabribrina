YURI = [
{
    "name": "IILWTV",
    "price": 19.99,
    "department": "Manga",
    "description": "Absolute peak transmigration yuri",
},
{
    "name": "TGSWIIWAGAA",\
    "price": 20.00,
    "department": "Manga",
    "description": "W green yuriful yuri",
}
]

print(YURI[0]["name"])
print(YURI[0]["price"])
print(YURI[0]["department"])
print(YURI[0]["description"])

print(YURI[1]["name"])
print(YURI[1]["price"])
print(YURI[1]["department"])
print(YURI[1]["description"])

for index, item in enumerate(best_buy_items):
    print(index, ":", item["name"])