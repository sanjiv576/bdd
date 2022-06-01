from abc import ABC, abstractmethod


class IBuilder(ABC):

    @abstractmethod
    def build_part_a(self):
        pass


    @abstractmethod
    def build_part_b(self):
        pass

    @abstractmethod
    def getProduct(self):
        pass


class Product():

    def __init__(self):
        # trying to ad sth in above abc meht
        self._parts = []


class ProductBuilder(IBuilder):

    def __init__(self):
        self.product = Product()

    
    def build_part_a(self):
        self.product._parts.append('part A')

        return self
    

    def build_part_a(self):
        self.product._parts.append('part B')
        return self

    def getProduct(self):
        return self.product


class Director():
    @staticmethod
    def construct():
         return ProductBuilder()\
            .build_part_a()\
                .build_part_b()\
                    .getProduct()


p = Director.construct()
print(p._parts)
