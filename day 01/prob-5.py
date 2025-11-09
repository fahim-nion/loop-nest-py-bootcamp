'''
Practice Problem - 5: 
Type conversion: convert string to int, float to int and complex to string. 

'''

data_1 = "10"
print(type(data_1))
data_1_conv = int(data_1)
print(type(data_1_conv))

data_2 = 12.24
print(type(data_2))
data_2_conv = int(data_2)
print(type(data_2_conv))

data_3 = 96j
print(type(data_3))
data_3_conv = str(data_3)
print(type(data_3_conv))

'''Output:
<class 'str'>
<class 'int'>
<class 'float'>
<class 'int'>
<class 'complex'>
<class 'str'>
'''