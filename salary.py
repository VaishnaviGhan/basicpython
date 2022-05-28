class Employee:
    salary = 1000
    increament = 0.5

    @property
    def SalaryAfterIncreament(self):
        return self.salary*self.increament

    @SalaryAfterIncreament.setter
    def SalaryAfterIncreament(self,sai):
        self.increament=sai/self.salary

e = Employee()
print(e.SalaryAfterIncreament)
SalaryAfterIncreament = 2000
print(e.increament)
    
    