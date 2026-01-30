a = 5
b = 4
c = 'Python is'
d = 'awesome'
e = 'fantastic'
print(a) #5
print(a+b) #9
print(c+d) #Python is awesome
print(c,e) #Python is fantastic
#print(b+e) #error
f,g,h = 5,7,9
print(f,g,h) #5 7 9
print(g) #7

def myfunc():
    d = "looks-good"
    print(d)
myfunc()
print(d)

def myfunc1():
    global e
    e = "smart"
    print(d)
    print(e)
myfunc1()
print(e)