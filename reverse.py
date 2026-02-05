#Reverse String
w = "Parthipan name is good"
words = w.split()
print(words)
res = ""

for word in reversed(words):
    print(word)
    res += word + ""

res =res.strip()
print(res)