wards = {
    "Cardiology":  ["Alice", "Bob", "Carol"],
    "Neurology":   ["Diana", "Eve"],
    "Orthopedics": ["Frank", "Grace", "Hank"],
    "Oncology":    ["Ivy", "Bob"]
}

staff = {}
for dept, docs in wards.items(): #thingys in the dictionary
    for doc in docs: #one person in doctors
        if doc not in staff: #add persons not in the dictionary
            staff[doc] = [dept] #stick them in a list
        else:
            staff[doc].append(dept) #add the departments of said persons
print(staff['Bob']) #print for Bobby

""" def receipt (orders):
    the_receipt = {}
    for sushi in orders:
        if sushi['name'] in the_receipt:
            the_receipt[sushi['name']]['quantity'] += 1
        else:
            the_receipt[sushi['name']] = {
                'price': sushi['price'],
                'quantity': 1
            }
    for sushi, value in the_receipt.items():
        price = value['price'] * value['quantity']
        print(sushi, value['quantity'], price)
        
receipt(sushi_orders) """