import pandas as pd
# dictionary
captains = {}
captains["Enterprise"] = "Kirk"
captains["Enterprise D"] = "Picard"
captains["Deep Space Nine"] = "Sisko"
captains["Voyager"] = "Janeway"

# df = pd.DataFrame(captains, columns=['Enterprise', 'Enterprise D', C'Deep Space Nine','Voyager'])
# print(df)
cars = {'Brand': ['Honda Civic','Toyota Corolla','Ford Focus','Audi A4'],
        'Price': [22000,25000,27000,35000]
        }

df = pd.DataFrame(cars, columns= ['Brand', 'Price'])
df.to_csv("clgt.csv", index=0)

print(captains, "\n")
print(captains["Enterprise D"],"\n")
print("list of ship: ")
for ship in captains:
    print(ship + ": " + captains[ship])
#tuple

print("\n //tuple type")
(age, income) = "32,120000".split(',')
print(age)
print(income)
print(type(age))

x = (1, 2, 3)
print(len(x))

print("\n try boolean")
print((1+1)==3)
print((1+1)==2)

l = [1,2,3,4,5,6,7,8,9,10]

h = l[2:]
t = l[:8]

print(h)
print(t)
