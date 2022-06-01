# Simple factory Design Pattern

# Problems of Simple Factory design pattern: it has both changing and unchanging features/methods
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




class PizzaStore():

    def orderPizza(self, type):

         # creating object of Pizza

        if(type=="veggie"):
            pizza = VeggiePizza()
        else:
            pizza = Pizza()

       
        
        pizza.prepare()
        pizza.bake()

        return pizza
    


ps = PizzaStore()
ps.orderPizza("veggie")