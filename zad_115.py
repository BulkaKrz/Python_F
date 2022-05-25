f_smaller = 3.141592653589793
f_bigger = 3.87756392764

import math

#print(math.ceil(f_smaller))
#print(math.floor(f_smaller))
#print(math.ceil(-f_smaller))
#print(math.floor(-f_smaller))
#print(pow(2,8))
#print(math.pow(2,8))
#print(math.e)

degree = 360
rad = (degree*math.pi)/180
print(degree,"\t",rad,"\t",round(rad/math.pi,2),'* Π')
print(degree,"\t",math.radians(degree),"\t",round(math.radians(degree)/math.pi,2),'* Π - z math.radians(degree)')

degree = 45
rad = (degree*math.pi)/180
print(degree,"\t",rad,"\t",round(rad/math.pi,2),'* Π')
print(degree,"\t",math.radians(degree),"\t",round(math.radians(degree)/math.pi,2),'* Π - z math.radians(degree)')

small_pizza_r = 22
big_pizza_r = 27
family_pizza_r = 38
small_pizza_price = 11.50
big_pizza_price = 15.60
family_pizza_price = 22.00

print('small_pizza: ',round(math.pi*(small_pizza_r/100)**2,2),'m^2')
print('big_pizza: ',round(math.pi*(big_pizza_r/100)**2,2),'m^2')
print('family_pizza: ',round(math.pi*(family_pizza_r/100)**2,2),'m^2')
print()
print('small_pizza 1 m^2 cost: ',round(small_pizza_price/(math.pi*(small_pizza_r/100)**2),2),'zł za 1 m^2')
print('big_pizza 1 m^2 cost: ',round(big_pizza_price/(math.pi*(big_pizza_r/100)**2),2),'zł za 1 m^2')
print('family_pizza 1 m^2 cost: ',round(family_pizza_price/(math.pi*(family_pizza_r/100)**2),2),'zł za 1 m^2')

math_ls = dir(math)
print(math_ls)
for i in range(len(math_ls)):
    print(math_ls[i])
