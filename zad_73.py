num_likes = 1300
num_shares = 50


MIN_LIKES = 500
MIN_SHARES = 100

if num_likes >= MIN_LIKES and num_shares >= MIN_SHARES :
    print("GREAT! Today our prizes drop 10% !!!")
else :
    if num_likes < MIN_LIKES :
        print("We still need more likes start the promotion")
    else :
        print("We still need more shares to start the promotion")

print('-------------')

if num_likes >= MIN_LIKES and num_shares >= MIN_SHARES :
    print("GREAT! Today our prizes drop 10% !!!")
elif num_likes < MIN_LIKES :
    print("We still need more likes start the promotion")
else :
     print("We still need more shares to start the promotion")

print('-------------')
isPizzaOrdered = True
isBigDrinkOrdered = False
isWeekend = False
if (isPizzaOrdered or isBigDrinkOrdered) and not isWeekend:
    print("Burger for FREE!!!")
else :
    if isWeekend :
        print('Come back on non-Weekend day')
    else :
        print('You need to order Pizza or Big drink to have a Burger coupon')


print('-------------')
if (isPizzaOrdered or isBigDrinkOrdered) and not isWeekend:
    print("Burger for FREE!!!")
elif isWeekend :
    print('Come back on non-Weekend day')
else :
     print('You need to order Pizza or Big drink to have a Burger coupon')
