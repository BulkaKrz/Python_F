'''
age = 23
if age >= 18:
    print("You are adult and yuu can buy alcohol")
else :
    print("You are too young to buy alcochol")

isDrunk = False

if age >= 18 and not isDrunk:
    print("You are adult and yuu can buy alcohol")
else :
    print("Sorry we cannot sell you alcochol")

isRestrictedArea = True

if age >= 18 and not isDrunk and not isRestrictedArea:
    print("You are adult and yuu can buy alcohol")
else :
    print("Sorry we cannot sell you alcochol")


num_likes = 1300
num_shares = 55

MIN_LIKES = 500
MIN_SHARES = 100


if num_likes >= MIN_LIKES and num_shares >= MIN_SHARES :
    print("GREAT! Today our prizes drop 10% !!!")
else :
    print("We still need more likes and shares to start the promotion")
print()
print("--------------------------------------------")
print()
isPizzaOrdered = True
isBigDrinkOrdered = False
isWeekend = False
if (isPizzaOrdered or isBigDrinkOrdered) and not isWeekend:
    print("Burger for FREE!!!")
else :
    print("Come to us on week day and consider buying Pizza or BigDrink to have Burger for free")

print()
print("--------------------------------------------")
print()
diskSize = 160
diskSizeUsed = 133
fileSize = 50
if diskSize - diskSizeUsed >= fileSize :
    print('File can be downloaded')
else :
    print('There isn\'t enough free disk space to download the file. Sorry :(')
'''

age = 30
isDrunk = False
isRestrictedArea = False

if age < 18:
    print("You are too young to buy alcochol")
else :
    if isDrunk:
       print("Are you drunk? We cannot sell you alcochol")
    else:
        if isRestrictedArea :
            print("Restricted area. Alcochol is forbidden")
        else :
            print("OK, you can buy alcochol")


print('------------')
if age < 18 :
    print("You are too young to buy alcochol")
elif isDrunk :
    print("Are you drunk? We cannot sell you alcochol")
elif isRestrictedArea :
    print("Restricted area. Alcochol is forbidden")
else :
    print("OK, you can buy alcochol")



