'''n = 6
for i in range(6):
  print("@" * (i+1))


  # fpr space star
n = 6
for i in range(6):
    print(" "* (n-i-1),end=" ")
    print("@"* (2*i+1),end=" ")
    print(" "*(n-i-1))'''

 n = 3
    for i in range(3):
        print("*"*(n-i))
        print("*"*(i+1)+" "*(i+1)+"*"*(i+1))
        print("*"*(n-i))