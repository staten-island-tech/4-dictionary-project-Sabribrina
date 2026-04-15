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

cart = [] #list for items being purchased
total = 0 #for add all prices of items together
purchasing = int(input("which yuriful of the yuris for the most yuriful yurier would u like?")) #ask user for which item they want
cart.append(YURI[purchasing]) #add the WHOLE thing to cart
print(cart) #prints items in cart
total += YURI[purchasing]['price'] #separate part to calc total of things

while True:
    checkout = input("do you wanna continue to get more yuriful of the yuris??? heuehrui") #ask if user wants to buy more
    if checkout == "yes": #when receiving a confirmation for more...
        purchasing = int(input("which other yuriful of the yuris for the most yuriful yurier would u like?")) #ask again
        cart.append(YURI[purchasing]) #add the WHOLE thing to cart
        print(cart) #prints items in cart
        total += YURI[purchasing]['price'] #separate part to calc total of things
    elif checkout == "no": #when NOT wanting more
        break #ends while loop
    else:
        print("say yes/no") #response to checkout input question

for item in cart:
    print(f"{(item['name'])}, ${float(item['price'])}") #f strings to print ONLY the items name and price from cart
print(f"Total: ${total}") #prints total amount of money needed to purchase items