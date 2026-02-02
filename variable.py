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
p = e.capitalize()
print(p)
print(p.casefold())

#file handle
f = open('demotext.txt')
print(f.read())

#use with Keyowords
with open('demotext.txt') as f:
 print(f.read())

 #
 with open('demotext.txt') as f:
    print(f.read(10))

#use append using 
text = 'Now add to New Words'
with open('demotext.txt', 'r') as f:
    checked = f.read()
if text not in checked :
    with open('demotext.txt', 'a') as f:
        f.write(text+'\n')
with open('demotext.txt') as f:
    print(f.read())