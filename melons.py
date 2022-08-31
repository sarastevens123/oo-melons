
from random import randint
from datetime import datetime

"""Classes for melon orders."""
class AbstractMelonOrder:
    order_type = None
    tax = 0

    def __init__(self, species, qty):
        self.species = species
        self.qty = qty
        self.shipped = False
        self.christmas_time = False


    def get_base_price(self):
        base_price = randint(5,9)
        return base_price


    def get_total(self):
        """Calculate price, including tax."""

        if self.qty > 100:
            raise TooManyMelonsError("No more than 100 melons!")

        base_price = self.get_base_price()
        
        current_time = datetime.now()
        # if current_time.weekday() in range(5)
        # if (0 <= current_time.weekday() <= 4)
           # if (8 <= current_time.hour <= 11):
        if (0 <= current_time.weekday() <= 4) and (8 <= current_time.hour <= 11):
            base_price += 4 

        if self.christmas_time:
            base_price = 1.5 * base_price
        
        #if self.species == "Christmas melon":
            # base_price = 1.5 * base_price
        
        total = ((1 + self.tax) * self.qty * base_price) 

        if self.order_type == "international" and self.qty <10:
            total += 3
        
        return total 


    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

    #Change the method time and update the docstring
    def set_christmas_time(self):
        """Sets christmas time to True if called"""

        self.christmas_time = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""
    order_type = "domestic"
    tax = 0.08


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""
    order_type = "international"
    tax = 0.17


    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""
        super().__init__(species, qty)
        self.country_code = country_code

    def get_country_code(self):
        """Return the country code."""

        return self.country_code


class GovernmentMelonOrder(AbstractMelonOrder):
    order_type = "government"
    
    def __init__(self, species, qty):
        super().__init__(species, qty)
        self.passed_inspection = False


    def mark_inspection(self, passed):
        self.passed_inspection = passed 


class TooManyMelonsError(ValueError):
    pass
    # Inherits from ValueError and returns error when melons > 100"""""

# try 
# except TooManyMelonsError
