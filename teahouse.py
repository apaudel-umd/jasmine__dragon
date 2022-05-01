SIZES_PRICE = ("small", 2.50), ("medium", 4.00),("large", 5.50)

class TeaHouse:
    """A TeaHouse object which consists of customer objects, tea objects, and worker objects. (using composition)
      
    Atrributes:
        customers(list of Customer objects): the customers inside the TeaHouse
        teas(list of Tea objects): teas that are available to order
        workers(list of Worker objects): workers at the TeaHouse
    """
    def __init__(self, name):
        """Initialize a TeaHouse object.
        
        Args:
            name(string): Name of the teaHouse
        """   
        pass
    
    def add_teas(self, tea):
        """Add a new tea to the list teas available at this TeaHouse.

        Args:
            tea(Tea): new tea to add to the list of teas
            
        Returns:
            The updated list of teas.
        
        Side effects:
            Updating the teas attribute of TeaHouse.
        """
        pass
    
    def add_customers(self, customer):
        """Add a new customer to the list customers at the TeaHouse.

        Args:
            customer(Customer): new customer to add to the list of customers
            
        Returns:
            The updated list of customers.
        
        Side effects:
            Updating the customers attribute of TeaHouse.
        """
        pass
    
    def sorting_customers(self, key):
        """Sort the list of customers by the key provided.
        
        Args:
            key(string): key function used to sort the list of customers a certain way.
         
        Returns:
            The sorted list of customers.    
        """
        pass
    
    def current_customers(self):
        """Look at the customers attribute and show the names of all the customers at the TeaHouse.
        
        Returns:
            customer_names(string): f-string of all the customers at the TeaHouse.
        """
        pass
    
    def add_workers(self, worker):
        """Add a new worker to the list workerss at the TeaHouse.

        Args:
            worker(Worker): new worker to add to the list of workers
            
        Returns:
            The updated list of workers.
        
        Side effects:
            Updating the workers attribute of TeaHouse.
        """
        pass

class Customer:
    """A customer object.
    
     Attributes:
        name (string): name of customer
        money (float): how much money a customer has
        order (set of tea): order of customer
        received (set of tea): their order that the waiter will give to them after receiving their order
    """
    def __init__(name, money):
        """Initialize a customer object.
        
        Args:
            name(string): name of customer
            money (float): how much money a customer has
            order(string list): order of customer
            received (string list): their order that the waiter will give to them after receiving their order
        """
        pass
    
    def __str__(self):
        """Informal representation of a Customer object.
        
        The format of informal representation will be: 
            "Customer Name: ___" + "Money:___ + "order:___" + "received:____ " 
        
        Return:
            string of formal representation of the Customer object    
        """
        pass
    
    def __repr__(self):
        """Formal representation of a Customer object.
        
        Return:
            string of formal representation of the Customer object
        """
        
        pass
    
    def addOrder(order):
        """Add a order to a customer object if customer has enough money.
        
        Args:
            order(tea): order of customer
        """
        pass
    
    def orderReceived(received):
        """Waiter has given a customer object their order.
        
        Args: 
            received(tea): their order that the waiter will give to them after receiving their order
        """
        pass
    
    def remaining_order(self):
        """Compare the order set and received set to see how much of their order a customer still needs to receive.
        
        Return:
            Set of the tea that the customer has ordered but hasn't received yet.
        """
        pass
    
    def pay_order(worker):
        """Asks a worker for the bill and pays the amount (according to the received set).
        
        Return:
            paid(string): states if the bill has been paid or not
            
        Side effect:
            Changes the money attribute of the customer object.
        """
        pass

class Tea:
    """A Tea object.
    
     Attributes:
            type(string): The type of tea
            price(float): The prices of the tea, which is determined by the size of tea.
            temp(string): default value is "hot", Values of temp can only be: ‘hot’ or ‘cold’    
            size(string): default value is ""medium, Values can only be: small , medium, or large
    """
    def __init__(type, temp = "hot", size = "medium"):
        """Initialize a Tea object. 
        
        Args: 
            type(string): The type of tea
            temp(string): default value is "hot", Values of temp can only be: ‘hot’ or ‘cold’    
            size(string): default value is ""medium, Values can only be: small , medium, or large
            
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
            
        Side effects:
            Changes the size and price attributes of the tea object.
        """
        pass

class Worker:
    """A Worker object.(There are two types of workers: Cashiers and Waiters.)

     Attributes:
        Worker.name(string): name of the worker
    """
    def __init__(name):
        """Initialize a Worker object.
        
        Args:
            name(string): name of the worker   
        """
        pass
    def recommend_tea(teaHouse):
        """Worker will recommend a random tea available at the TeaHouse.
         
        Args:
            teaHouse(TeaHouse): the teaHouse that the worker works in.
         
        Return:
            tea_rec(string): A tea recommendation
        """
    

class Cashier(Worker):
    """A Worker object.(There are two types of workers.)

     Attributes:
        name(string): name of the worker
    """
    def __init__(name):
        """Initialize a Cashier object. Only Cashiers can received payment from a customer.
        
        Args:
            name(string): name of the worker   
        """
        Cashier.name = name
    
    def receive_payment(customer):
        """Will take payment from a customer and return the any remaining money to the customer.
        
        Args:
            customer(Customer): customer that wishes to pay their bill
        
        Return:
            has_paid(string): String stating if the bill was paid or not and if the customer has any remaining money.
        """
        pass

class Waiter(Worker):
    """A Worker object.(There are two types of workers.)

     Attributes:
        name(string): name of the worker
    """
    def __init__(name):
        """Initialize a Waiter object. Waiters can only take orders of customers.
        
        Args:
            name(string): name of the worker   
        """
        Waiter.name = name
    
    def takeOrder(order):
        """Checks if a customer has enough money for their order then takes order of a customer if possible.
        
        Args:
            order(string): order of a customer.
            
        Returns: 
            The order has been taken or state that the customer does not have 
                sufficient amount of money for their order.
        """
        pass