class Programmer :
    def __init__(self,Name,Lang,Salary):
        self.name = Name
        self.lang = Lang
        self.sal = Salary
        self.com = "Microsoft"
    def intro(self) :
        print(f"Hey I'm {self.name} my language is  {self.lang} and work with {self.com}")
e1 = Programmer("Parth","Python",2000000)
e1.intro()
    









