# Factory Design Pattern

# Separating both changing and unchanging features/methods
from abc import ABC, abstractmethod


class Pizza():
    def __init__(self):
        # we have only one type of pizza
        self.name = "Standard Pizza"


    def prepare(self):
        print(f"Preparing {self.name}")

    def bake(self):
        print(f"Baking for 30 mins")


class KTMVeggiePizza(Pizza):
    def __init__(self):
        self.name = "Veggie Pizza of KTM style"

class PokharaVeggiePizza(Pizza):
    def __init__(self):
        self.name = "Pokhara style pizza"

# separate changing feature i.e different pizza types
# class SimplePizzaFactory():
#      # creating object of Pizza

#     @staticmethod
#     def createPizza(type): 
#         if(type=="veggie"):
#             pizza = VeggiePizza()
#         else:
#             pizza = Pizza()

#         return pizza

class PizzaStore(ABC):

    def orderPizza(self, type) -> Pizza:

        pizza = self.createPizza(type)
        # separate unchanging feature i.e same way of baking, preparing
        pizza.prepare()
        pizza.bake()

        return pizza
    
    # this is Factory method
    @abstractmethod
    def createPizza(self, type) -> Pizza:
        pass


class KtmPizzaStore(PizzaStore):
    def createPizza(self, type) -> Pizza:
        if(type=="veggie"):
            return KTMVeggiePizza()

class PokharaPizzaStore(PizzaStore):
    def createPizza(self, type) -> Pizza:
        if(type=="veggie"):
            return PokharaVeggiePizza()


ps = KtmPizzaStore()
ps.orderPizza(type="veggie")

pss = PokharaPizzaStore()
pss.orderPizza(type="veggie")