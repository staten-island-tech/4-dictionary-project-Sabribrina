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

""" for index, item in enumerate(YURI):
    print(index, ":", item["name"], item["price"], item["department"], item["description"])

cart = []
prices = []
purchase = ""
money = ""
while purchase != "done":
    purchase = input("which yuriful of the yuris for the most yuriful yurier would u like? (type 'done' to finish): ")
    cart.append(purchase)
    money = float(input("GIMME THE COST OF IT BOY (type '0' to finish): "))
    prices.append(money)
if 'done':
    input("do you wish to continue..?")
elif 'yes':
    input("thank you for your patronage..return for more peak!!")
elif 'no':
    purchase = input("which yuriful of the yuris for the most yuriful yurier would u like? (type 'done' to finish): ")
    cart.append(purchase)
    money = float(input("GIMME THE COST OF IT BOY"))
    prices.append(money)
print(cart, prices)
total = sum(prices)

print(cart, total) """

for index, item in enumerate(YURI):
    print(index, ":", item["name"], item["price"], item["department"], item["description"])

cart = []
purchase = ""
while purchase != "done":
    purchase = input("which yuriful of the yuris for the most yuriful yurier would u like? (type 'done' to finish): ")
    cart.append(
    print(cart)
if 'done':
    input("do you wish to continue..?")
elif 'yes':
    input("thank you for your patronage..return for more peak!!")
elif 'no':
    purchase = input("which yuriful of the yuris for the most yuriful yurier would u like? (type 'done' to finish): ")
    cart.append(
    print(cart)

print(cart)