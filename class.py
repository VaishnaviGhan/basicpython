class Programmer:
    company = "Microsoft"
    def __init__(self,name,sallary):
        self.name=name
        self.salary=salary 
       
    def getInfo(self):
        print( f"name is:{self.name} and salary is:{self.salary}")

        Shlok = Programmer("Shlok","50")
        Vaishu = Programmer("Vaishu","40")
        Shlok.getInfo()
        Vaishu.getInfo()
