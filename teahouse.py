class TeaHouse:
    """A TeaHouse object which consists of customer objects, tea objects, and worker objects. (using composition)
      
    """
    
    pass

class Customer:
    """A customer object.
    
     Attributes:
        Customer.name (string): name of customer
        Customer.order (string list): order of customer
        Customer.received (string list): their order that the waiter will give to them after receiving their order
    """
    def __init__(name, order, received):
        """Initialize a customer object.
        
        Args:
            name(string): name of customer
            order(string list): order of customer
            received (string list): their order that the waiter will give to them after receiving their order
        """
        pass
    
    def addOrder(order):
        """Add a order to a customer object.
        
        Args:
            order(string list): order of customer
        """
        pass
    
    def orderReceived(received):
        """Waiter has given a customer object their order.
        
        Args: 
            received(string list): their order that the waiter will give to them after receiving their order
        """
        pass

class Tea:
    """A Tea object.
    
     Attributes:
        Tea.temp(string): Only ‘hot’ or ‘cold’    
        Tea.type(string): The type of tea
        Tea.size(string): small , medium, or large
        Tea.price(float): The prices of the tea
    """
    def __init__(temp, type, size, price):
        """Initialize a Tea object.
        
        Args:
            temp(string): Only ‘hot’ or ‘cold’    
            type(string): The type of tea
            size(string): small , medium, or large
            price(float): The prices of the tea
        """
        pass
    
    def changeTemp(self, newTemp):
        """Change the temperature attribute of the tea object.
        
        Args:
            newTemp(string): new temperature of the tea object.
            
        Return:
            Current tea object.
        """
        pass
    
    def changeSize(self, newSize):
        """Change the size attribute of the tea object.
        
        Args:
            newSize(string): new temperature of the tea object.
            
        Return:
            Current tea object.
        """
        pass

class Worker:
    """A Worker object.(There are two types of workers.)

     Attributes:
        Worker.name(string): name of the worker
    """
    def __init__(name):
        """Initialize a Worker object.
        
        Args:
            name(string): name of the worker   
        """
        pass
    

class Cashier(Worker):
    """A Worker object.(There are two types of workers.)

     Attributes:
        Cashier.cash(list of floats): the amounts of money the customer pays for the bill
    """
    def __init__(name, cash):
        """Initialize a Cashier object.
        
        Args:
            name(string): name of the worker   
            Cashier.cash(list of floats): the amounts of money the customer pays for the bill
        """
        pass

class Waiter(Worker):
    """A Worker object.(There are two types of workers.)

     Attributes:
        Worker.change(list of floats): the remaining money, the worker gives back to the customer
    """
    def __init__(name, change):
        """Initialize a Waiter object.
        
        Args:
            name(string): name of the worker   
            change(list of floats): the remaining money, the worker gives back to the customer
        """
        pass
    
    def takeOrder(order):
        """Takes order of a customer.
        
        Args:
        
            order:
        """
        pass