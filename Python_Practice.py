print ("Hello World")
counties = ["Arapahoe", "Denver", "Jefferson"]
if counties[2] != 'Jefferson' :
    print(counties[2])
else :
     print(counties[0])



temp = int(input("what is the temperature outside? "))
if temp > 80 :
    print ("Turn on the AC.")
else :
    print("open the windows.")

# What is the score?
score = int(input ("What is your test score?"))
if score >= 90 :
    print("Your grade is an A")
else:
    if score >= 80 :
        print("Your grade is a B")
    else :
        if score >= 70 :
            print ("Your grade is a C")
        else :
            if score >= 60 :
                print ("Your grade is a D")
            else : 
                print ("Your grade is an F")

if "El Paso" in counties :
    print ("El Paso is in the list of counties")
else :
    print ("El Paso is not in the list of counties")

if "Arapahoe" and "El Paso" in counties :
    print ("Arapahoe and El Paso are in the list of counties")
else :
    print ("Arapahoe and El Paso are not in the list of counties")

if "Arapahoe" or "El Paso" in counties :
    print ("Arapahoe or El Paso are in the list of counties")
else :
    print ("Arapahoe or El Paso are not in the list of counties")

if "Arapahoe" in counties or "El Paso" in counties:
    print ("Arapahoe or El Paso are in the list of counties")
else:
    print("Neither Arapahoe or El Paso are int he list of counties")

x=0
while x <=5 :
    print(x)
    x = x+1


counties = ["Arapahoe", "Denver", "Jefferson"]

for county in counties :
    print(county)

for i in range(len(counties)) :
    print(counties[i])