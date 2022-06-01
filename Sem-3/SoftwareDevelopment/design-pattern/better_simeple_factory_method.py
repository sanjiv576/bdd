# Factory Design Pattern

# Separating both changing and unchanging features/methods
class Pizza():
    def __init__(self):
        # we have only one type of pizza
        self.name = "Standard Pizza"


    def prepare(self):
        print(f"Preparing {self.name}")

    def bake(self):
        print(f"Baking for 30 mins")


class VeggiePizza(Pizza):
    def __init__(self):
        self.name = "Veggie Pizza"

# separate changing feature i.e different pizza types
class SimplePizzaFactory():
     # creating object of Pizza

    @staticmethod
    def createPizza(type): 
        if(type=="veggie"):
            pizza = VeggiePizza()
        else:
            pizza = Pizza()

        return pizza

class PizzaStore():

    def orderPizza(self, type) -> Pizza:

        # sf = SimplePizzaFactory()
        #this is changing feature so separating it
        pizza = SimplePizzaFactory.createPizza(type)

        # separate unchanging feature i.e same way of baking, preparing
        pizza.prepare()
        pizza.bake()

        return pizza
    


ps = PizzaStore()
ps.orderPizza(type="veggie")