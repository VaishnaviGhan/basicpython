letter = ''' Dear , <|NAME|>,
you are selected!

Date: <|DATE|>'''
name = input ("Enter your name :\n")
Date = input ("Enter Date :\n")
letter = letter.replace("<|NAME|>",name)
letter = letter.replace("<|DATE|>",Date)
print(letter)