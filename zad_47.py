name='Krzysztof'
age=17
dayslnYear=365
message = '{0:s} is {1:d} years old so its about {2:d} days old'
print(message.format(name,age,age*dayslnYear))

message_1 = "%s is %d years old so its about %d days old"

print(message_1 % (name,age,age*dayslnYear))

#Wyznacz wynik dzielenia całkowitego i resztę z dzielenia 1234567890 przez 12345:

#Dzielenie /; dzielenie bez reszty //; reszta z dzielenia %
print(1234567890//12345)
print('1234567890 divided by 12345 is',1234567890//12345, 'and the rest is',1234567890%12345)

