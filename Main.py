import random

def update():
    for i in items:
        print(i)
        percent = risks[i]*100
        price = values[i]
        change = random.randint(-percent,percent)/1000
        new = price + price*change
        print(new)
        values[i] = new
    
    return

items = []

risksfile = open('C:/Users/Benji Graf/Desktop/Pete economy/risks.txt', 'r')
risks = {}

for line in risksfile:
    (key, val) = line.split()
    risks[str(key)] = float(val)
    items.append(key)
    
valuesfile = open('C:/Users/Benji Graf/Desktop/Pete economy/values.txt', 'r')
values = {}

for line in valuesfile:
    (key, val) = line.split()
    values[str(key)] = float(val)

print(risks)
print(values)
update()
print(values['gold'])

risksfile.close()
valuesfile.close()