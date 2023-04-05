class Person:
    def __init__(self,name,age,gender,salary):
        self.name=name
        self.age=age
        self.gender = gender
        self.salary=salary
    def __str__ (self):
       if self.gender=="kaci":
           return f"{self.age}თქვენი ასაკია{self.name}თქვენი სახელია{self.salary}არის შემოსავალი"
       elif self.gender=="qali":
           return f"{self.age}თქვენი ასაკია{self.name}თქვენი სახელია{self.salary}არის შემოსავალი"
    def tviuri(self):
        pension = self.salary/5
        income=self.salary/100
        g=pension+income
        return f"თქვენი ყოველთვიური გადასახადია{g}"
    def danazogi(self):
        wliuri_danazogi=(self.salary/100)*12
        if self.gender =="kaci":
            return f"თქვენი დაანაზოგია:{wliuri_danazogi*35}"
        elif self.gender =="qali":
            return f"თქვენი დაანაზოგია:{wliuri_danazogi*30}"
    def gapensionereba(self):
        if self.gender=="kaci":
            return f"თქვენ გაპენსიონერება იქნება{65-self.age}"
        if self.gender=="qali":
            return f"თქვენ გაპენსიონერება იქნება{60-self.age}"

person1=Person("wiwiko",50,"kaci",1000)
# print(person1)
print(person1.tviuri())
print(person1.danazogi())
print(person1.gapensionereba())

