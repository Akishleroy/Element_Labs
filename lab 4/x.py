from dataclasses import dataclass
@dataclass
class Person:
    age:int
    name:str
    surname:str

    def __str__(self):
        return f'age:{self.age},name:{self.name},surname:{self.surname}'

@dataclass
class Driver(Person):
    expirience:int

    def __str__(self):
        return super.__str__() + f'expirience:{self.expirience}'

akim=Person(age=15,name='Akish',surname="zhankebayev")
dias=Driver(age=15,name='Akish',surname="zhankebayev",expirience=4)
print(dias)