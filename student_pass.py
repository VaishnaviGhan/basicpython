sub1 = int(input("Enter marks of subject 1"))
sub2 = int(input("Enter marks of subject 2"))
sub3 = int(input("Enter marks of subject 3"))

if(sub1 < 33 or sub2 < 33 or sub3 < 33):
    print("You are fail beacause you got less than 33 in one of subject")
elif(sub1 +sub2 + sub3)/3 < 40:
    print("you are fail because yu gor less than 40%")
else:
    print("Congratulations....!......you pass")