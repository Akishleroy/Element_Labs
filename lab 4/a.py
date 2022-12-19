from dataclasses import dataclass

@dataclass
class Person:
    age:int
    fullName:str

    def __str__(self):
        return f'\n age:{self.age},\n fullName:{self.fullName}'

@dataclass
class Driver(Person):
    expirience:int

    def __str__(self):
        return Person.__str__(self) + f' \n expirience:{self.expirience}'


@dataclass
class Engine:
    power:int
    company:str

    def __str__(self):
        return f'\n power:{self.power},\n company:{self.company}'

@dataclass
class Car:
    marka:str
    car_class:str
    driver: Driver
    engine: Engine

    def start(self):
        print('Поехали')

    def stop(self):
        print('Останавливаемся')

    def turnRight(self):
        print('Поворот направо')

    def turnLeft(self):
        print('Поворот налево')   

    def __str__(self) -> str:
        return f'\n mark:{self.marka},\n car_class:{self.car_class}'+Engine.__str__(self.engine)+Driver.__str__(self.driver)

@dataclass
class Lorry(Car):
    carrying:int
    
    def __str__(self) -> str:
        return super.__str__(self) + f'\n carrying:{self.carrying}'


@dataclass
class SportCar(Car):
    speed:int
    
    def __str__(self) -> str:
        return super.__str__(self) + f'\n speed:{self.speed}'

