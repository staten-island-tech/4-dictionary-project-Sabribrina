YURI = [
{
    "name": "IILWTV",
    "price": 14.50,
    "department": "Manga",
    "description": "Absolute peak transmigration yuri",
},
{
    "name": "TGSWIIWAGAA",
    "price": 20.00,
    "department": "Manga",
    "description": "W green yuriful yuri & Mitsuaya is peak",
},
{
    "name": "WATANARE",
    "price": 16.99,
    "department": "Manga",
    "description": "WE LOVE MAI ODUKAAAAAAAAAAAAA",
}
]

""" print(YURI[0]["name"], YURI[0]["price"], YURI[0]["department"], YURI[0]["description"])

print(YURI[1]["name"], YURI[1]["price"], YURI[1]["department"], YURI[1]["description"])

print(YURI[2]["name"], YURI[2]["price"], YURI[2]["department"], YURI[2]["description"]) """

for index, item in enumerate(YURI):
    print(index, ":", item["name"], item["price"], item["department"], item["description"])

cart = []
purchase = ""
while purchase != "done":
    purchase = input("which yuriful of the yuris for the most yuriful yurier would u like? (type 'done' to finish): ")
    cart.append(purchase)
if [0, 1, 2]:
    print("do you wish to continue..")
if 'done':
    print("thank you for your patronage..return for more peak...")

print(item["name"], cart,)