f = open('poem.txt')
t = f.read()
if 'twinkle' in t:
     print("twinkle is present in file")
else:
     print("twinkle is not present in file")
f.close()