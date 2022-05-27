
# a=0.7
# b=0.2
# print(a+b)
# print('%.1f'%(a+b))
# c=0.1
# d=0.2
# print(c+d)
''' from decimal import Decimal'''
# from decimal import Decimal as d
# print(d('0.1')+d('0.2')) 
# print(d('0.7')+d('0.2')) 
# from decimal import Decimal 
# print(Decimal('0.1')+Decimal('0.2')) 

'''import math'''
# a=[float(x) for x in input("enter a,b values:").split( )]
# import math
# # print(math.factorial(10))
# print(math.prod(a))

# print(dir(__builtins__))

# print(7/0)  ZeroDivisionError: division by zero

'''to identify the value of number easily we use underscore in between numbers
we dont use underscore before and after  decimal point value of the float'''

# a=2_435
# print(a,type(a)) #2435 <class 'int'>
# from this import d


# b=1.26_561
# c=12_36.3
# e=1._525
# f=14_.35
# g=_12.36
# h=12.69_
# print(b)#1.26561
# print(c)#1236.3
# print(e)#SyntaxError: invalid decimal literal   
# print(f)#SyntaxError: invalid decimal literal   
# print(g)#SyntaxError: invalid syntax
# print(h) #SyntaxError: invalid decimal literal

''' isintence is used to give value is what kind of datatype it is'''
'''sysntax:isinstance(variable,datatype)'''
# a=5.36
# print(isinstance(a,int))False
# print(isinstance(a,float))True

"""complex datatype it in the form of a+bj
a=real number,b=imaginary number"""
# a=3j
# b=2+5j
# print(a,type(a)) #3j <class 'complex'>
# print(b,type(b)) #(2+5j) <class 'complex'>






















