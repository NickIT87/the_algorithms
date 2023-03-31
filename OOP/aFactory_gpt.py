# generate abstract factory methods on python
# command+shift+i
"""
Here is a sample Python code for implementing 
Abstract Factory pattern with code GPT:
"""

from abc import ABC, abstractmethod

# Abstract classes
class AbstractFactory(ABC):
    @abstractmethod
    def create_product_a(self):
        pass
    
    @abstractmethod
    def create_product_b(self):
        pass
    

class AbstractProductA(ABC):
    @abstractmethod
    def operation_a(self):
        pass
    

class AbstractProductB(ABC):
    @abstractmethod
    def operation_b(self):
        pass
    

# Concrete classes
class ConcreteProductA1(AbstractProductA):
    def operation_a(self):
        print("Operation A from ConcreteProductA1")
        

class ConcreteProductA2(AbstractProductA):
    def operation_a(self):
        print("Operation A from ConcreteProductA2")
        

class ConcreteProductB1(AbstractProductB):
    def operation_b(self):
        print("Operation B from ConcreteProductB1")
        

class ConcreteProductB2(AbstractProductB):
    def operation_b(self):
        print("Operation B from ConcreteProductB2")
        

class ConcreteFactory1(AbstractFactory):
    def create_product_a(self):
        return ConcreteProductA1()
    
    def create_product_b(self):
        return ConcreteProductB1()
    

class ConcreteFactory2(AbstractFactory):
    def create_product_a(self):
        return ConcreteProductA2()
    
    def create_product_b(self):
        return ConcreteProductB2()
    
    
# Client code
def client(factory: AbstractFactory):
    product_a = factory.create_product_a()
    product_b = factory.create_product_b()
    
    product_a.operation_a()
    product_b.operation_b()

    
# Usage    
if __name__ == "__main__":
    client(ConcreteFactory1())
    client(ConcreteFactory2())
