# dependency injection


class DoughFactory:

    def get_dough(self):
        return "insecticide treated wheat dough"


class OrganicDoughFactory(DoughFactory):

    def get_dough(self):
        return "pure untreated wheat dough"


class Pizza(DoughFactory):

    def order_pizza(self, *toppings):
        print("Getting dough")
        dough = super().get_dough()
        print("Making pie with {}".format(dough))
        [print("Adding: {}".format(topping)) for topping in toppings]


class OrganicPizza(Pizza, OrganicDoughFactory):
    pass


if __name__ == "__main__":
    Pizza().order_pizza("Pepperoni", "Bell pepper")
    # help(Pizza)
    OrganicPizza().order_pizza("Sausage", "Mushroom")
    # help(OrganicPizza)
