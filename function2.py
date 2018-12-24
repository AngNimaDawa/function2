#function2
# mp = 1000
# def apply_discount(price, *,discount=0:)
# return price*(1-discount/100)

# def apply_vat(amount):
# 	return amount*1.13
# 	sp = apply_discount(mp,discount=20)
# 	total = apply_vat(sp)
# 	print(round(total,3))

#factorial_(recurssion)
# def fact(n):
# 	if n == 1 or n == 0:
# 		return 1
# 	else:
# 		return(n*fact(n-1))
# print(fact(5))

#partial function
# partial function allow one to derive a function with x perameters and fixed values set for the
# form functools import partial
# from functools import partial


# def multiply(x,y):
# 	return x*y
# #create a new function that multiplies by 2
# table = partial(multiply,5) #multiply(y, x 5)
# print(table(1))
# print(table(2))
# print(table(8))
# print(table(10))

# from functools import partial

# def quadratic(a,b,c,x):
# 	return (a*(x**2) + b*x + c)

# quadratic = partial(quadratic,2,3,4)
# print(quadratic(4))


