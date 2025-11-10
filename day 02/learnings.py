#string

#can use with single and double quote
#immutable

my_str = "Fahim"
print(my_str[3])

print(len(my_str))
print("h" in my_str)

name= "LoopNest"

print(name[1:4])


mail = "fahimalhassan4@gmail.com"
username = mail[:mail.index('@')]
print(username)

print(name[::-1]) #start end step


#modifying String

x = "Python"
print(x.lower())
print(x.upper())

y = "a bcd s e  fd sd "
print(y.strip()) #only removes spaces from front and back

z = "Zohraan Mamdani"
print(z.replace("Z","M"),z.replace("M","Z"))

m = "Hello, World"
print(m.split(","))

#string concat

p = "Hello"
q = "World!"

print(p+" "+q)

print(f"{p} {q}")