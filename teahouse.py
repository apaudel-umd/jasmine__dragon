from random import choice
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

SIZE_PRICE = [2.50, 4.00, 5.50]
TEA_TYPE = ['black', 'green', 'oolong', 'jasmine', 'peach', 'taro', 'jasmine green', 'herbal']
ADD_INS = ['honey', 'sweetner', 'boba', 'milk']

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
            
        Raises:
            ValueError: The choice should be between customer and worker.
        """ 
        self.name = name
        self.customers = []
        self.teas = []
        self.workers = []
        self.order_history = pd.read_csv('order_history.csv', sep=',', encoding='utf-8')
    
    
    def add_teas(self, tea):
        """Add a new tea to the list teas available at this TeaHouse.

        Args:
            tea(Tea): new tea to add to the list of teas
            
        Returns:
            The updated list of teas.
        
        Side effects:
            Updating the teas attribute of TeaHouse.
        """
        return self.teas.append(tea)
    
    def add_customers(self, customer):
        """Add a new customer to the list customers at the TeaHouse.

        Args:
            customer(Customer): new customer to add to the list of customers
        
        Side effects:
            Updating the customers attribute of TeaHouse.
        """
        self.customers.append(customer)
        self.order_history + customer.order + customer.received
    
    def sorting_customers(self, key):
        """Sort the list of customers by the key provided.
        
        Args:
            key(string): key function used to sort the list of customers a certain way.
         
        Returns:
            The sorted list of customers.    
        """
        return sorted(self.customers, key)
    
    def current_customers(self):
        """Look at the customers attribute and show the names of all the customers at the TeaHouse.
        
        Returns:
            customer_names(string): f-string of all the customers at the TeaHouse.
        """
        
        customer_names = []
        for c in self.customers:
            customer_names.append(c.name)
        return customer_names
    
    def add_workers(self, worker):
        """Add a new worker to the list workerss at the TeaHouse.

        Args:
            worker(Worker): new worker to add to the list of workers
            
        Returns:
            The updated list of workers.
        
        Side effects:
            Updating the workers attribute of TeaHouse.
        """
        return self.workers.append(worker)
    
    def plot_data(self):
        ''' Uses pandas and seaborn to plot the data from order_history. 
        
        Args:
            column (string): the name of the column to plot
        
        Side effects:
            Plots the graph in a new window.
        
        Raises:
            ValueError: the options should be one of the 4 columns listed  
        '''
        choice = input('What data would you like to see?\n0 : Tea Type\n1 : Tea Temp\n2 : Tea Size\n3 : Add ins\n4 : Exit\n>')
        
        if choice == '0' or 'Tea Type':
            a = self.order_history.groupby(['tea_type']).size()
            sns.barplot(x=a.index, y=a.values)
            plt.show()
        elif choice == '1' or 'Tea Temp':
            b = self.order_history.groupby(['tea_temp']).size()
            sns.barplot(x=b.index, y=b.values)
            plt.show()
        elif choice == '2' or 'Tea Size':
            c = self.order_history.groupby(['tea_size']).size()
            sns.barplot(x=c.index, y=c.values)
            plt.show()
        elif choice == '3' or 'Add ins':
            d = self.order_history.groupby(['add_in']).size()
            sns.barplot(x=d.index, y=d.values)
            plt.show()
        else:
            raise ValueError('Please enter one of the listed options!')
            
class Customer:
    """A customer object.
    
     Attributes:
        name (string): name of customer
        money (float): how much money a customer has
        order (set of tea): order of customer
        received (set of tea): their order that the waiter will give to them after receiving their order
    """
    def __init__(self, name, money):
        """Initialize a customer object.
        
        Args:
            name(string): name of customer
            money (float): how much money a customer has
        """
        self.name = name
        self.money = money
        self.orders = set()
        self.received = set()
    
    def __str__(self): #add price #update docstring
        """Informal representation of a Customer object.
        
        The format of informal representation will be: 
            "Customer Name: ___" + "Money:___ + "order:___" + "received:____ " 
        
        Return:
            string of formal representation of the Customer object    
        """
        print(f'Customer Name: {self.name!r}\nMoney: {self.money!r}\nOrders:{self.orders!r}\nReceived: {self.received!r}')
    
    def __repr__(self):
        """Formal representation of a Customer object.
        
        Return:
            string of formal representation of the Customer object
        """
        print(f'Customer({self.name!r}, {self.money!r})')
        
    
    def pay_order(self, worker): #ashley
        """Asks a worker for the bill and pays the amount (according to the received set).
        
        Return:
            paid(string): states if the bill has been paid or not
            
        Side effect:
            Changes the money attribute of the customer object.
        """
        pass
    
    def run(self, teahouse):
        while True:
            print(f'''Hello, {self.name}. What would you like to do?\n
                  0 : Add Order 
                  1 : Make Payment
                  2 : Ask for tea recommendation
                  3 : Exit''')
            choice = input('> ')
            
            waiter1 = Waiter("")
            
            #if user is a customer: need to make some default worker objects    
            for w in teahouse.workers:
                if w is Waiter:
                    waiter1 = w
            if choice == '0':
                
                counter = 0
                tea_types_available = ""
                for t in TEA_TYPE:
                    tea_types_available += t 
                    counter+=1
                    if counter != len(TEA_TYPE): 
                        tea_types_available += ", "
                
                tea_type = input("For your order, what type of tea do you prefer? \nWe have: " + tea_types_available + "\n")
                
                while True:
                    tea_temp = input("Is that hot or cold? \n")
                    if (tea_temp == "hot") or (tea_temp == "cold"):
                        break
                    else:
                        print("Please provide a valid input: 'hot' or 'cold'")
                        continue
                
                while True:    
                    tea_size = input("Will that size be: small, medium, or large?\n")
                    if (tea_size == "small") or (tea_size == "medium") or (tea_size == "large"):
                        break
                    else:
                        print("Please provide a valid input: 'small', 'medium', or 'large'")
                        continue
                while True:    
                    more_add = input("Any add ins? y for yes, and n for no\n")
                    if(more_add == 'y'):
                        if more_add == "y":
                            while True:
                                tea_add_in = input("What add ins would you prefer? We have: 'honey', 'sweetner', 'boba', or 'milk'\n")
                                if (tea_add_in == "honey") or (tea_add_in == "sweetner") or (tea_add_in == "boba") or (tea_add_in == "milk"):
                                   break 
                                else:
                                    print("Please provide a valid input: 'honey', 'sweetner','boba', or 'milk'")
                                    continue                            
                            
                            break    
                    elif more_add == 'n':
                        tea_add_in = "Nothing"
                        break
                    else:
                        print("Please provide a valid input: 'y'or 'n'")
                        continue
                
                tea_order = Tea(tea_type, tea_temp, tea_size, tea_add_in)
                
                waiter1.addOrder(tea_order, self)
            elif choice == '1':
                cashier1 = Cashier("")
                
                for w in teahouse.workers:
                    if w is Cashier:
                        cashier1 = w
                        
                waiter1.giveOrder(self)        
                print(cashier1.receive_payment(self))
                
                continue        
            elif choice == '2':
                #recommendation
                worker = teahouse.workers[0]
                print(worker.recommend_tea(teahouse))
                continue
            elif choice == '3':
                print("Good bye and have a nice day~!")
                break
            else:
                print("Please provide a valid input!")
                continue

class Tea:
    """A Tea object.
    
     Attributes:
            type(string): The type of tea
            price(float): The prices of the tea, which is determined by the size of tea.
            temp(string): default value is "hot", Values of temp can only be: ‘hot’ or ‘cold’    
            size(string): default value is ""medium, Values can only be: small , medium, or large
            price(float): The price of the tea based on its size.
    """
    def __init__(self, type, temp = "hot", size = "medium", add_in = "Nothing"):
        """Initialize a Tea object. 
        
        Args: 
            type(string): The type of tea
            temp(string): default value is "hot", Values of temp can only be: ‘hot’ or ‘cold’    
            size(string): default value is ""medium, Values can only be: small , medium, or large
            add_in(string): default value is None, options are: boba, sugar, honey, and sweetner
            
        """
        a,b,c = SIZE_PRICE
        if size == "small":
            self.price = a
        elif size == "medium":
            self.price = b
        else:
            self.price = c
        self.type = type
        #type = ["Oolong", "Jasmine Green Tea", "Green Tea", "Black Tea", "Herbal Tea"]
        #for i in TEA_TYPE:
        #    if i != type:
        #        raise ValueError("We do not have that tea, please choose a different one.")
        self.temp = temp
        self.size = size 
        self.add_in = add_in
        #Add_in = ["Boba", "Sugar", "Honey", "Sweetner", "Milk"]
        #for i2 in ADD_INS:
        #    if i2 != add_in:
        #        raise ValueError("We do not have that Add_in, please choose a different one.")
        
        
    def updateTea(self, newType = "", newTemp = None, newSize = None, newAdd_in = ""):
        """Change one or many attributes of the tea object.
        
        Args:
            newType(string): new type of the tea object.
            newTemp(string): new temperature of the tea object.
            newSize(string): new size of the tea object.
            newAdd_in(string): new add_in of the tea object.
            
        Side effect:
            Changes the desired attribute(s) of the tea object.
        """
        if(newType != None):
            self.type = newType               
        elif(newTemp != None):
            self.temp = newTemp
        elif(newSize != None):   
            self.size = newSize
            #need to also update price attribute if size of tea changed
            a,b,c = SIZE_PRICE
            if newSize == "small":
                self.price = a
            elif newSize == "medium":
                self.price = b
            else:
                self.price = c
        elif(newAdd_in != None):     
            self.Add_in = newAdd_in
            
    def combine(self, combineType = "", combineAdd_in = []): #unable to combine temp and size, max combine 2
        if combineType == self.type:
            raise ValueError("You are trying to combine the same tea")
        elif combineType != None:
            return self.type + combineType
        if combineAdd_in == self.Add_in:
            return(f"Extra {self.Add_in}")
        elif combineAdd_in != None:
            return self.Add_in + combineAdd_in
    
    def updatePrice(self):
        if Tea.combine(combineType= ""):
            return self.price + 1.25
        if Tea.combine(combineAdd_in= ""):
            return self.price + .75
                    
            
    def __str__(self):
            """Informal representation of a Tea object.
            
            The format of informal representation will be: 
                "Tea Order: Type:___" + "Temperature:___ + "Size:___" + "Add_in:____" + "Price:___" 
            
            Return:
                string of informal representation of the tea object    
            """
            print(f'Tea Order: Type: {self.type!r} Temperature: {self.temp!r} Size:{self.size!r} Add_in: {self.Add_in!r} Price: {self.price!r}')
                 
class Worker:
    """A Worker object.(There are two types of workers: Cashiers and Waiters.)

     Attributes:
        Worker.name(string): name of the worker
    """
    def __init__(self, name, tea=None):
        """Initialize a Worker object.
        
        Args:
            name(string): name of the worker
            tea (Tea): Worker's favorite tea. Defaults to none.  
        """
        self.name = name
        self.tea = tea
    
    def recommend_tea(self, teaH):
        """Worker will recommend a random tea available at the TeaHouse.
         
        Args:
            teaH(TeaHouse): the teaHouse that the worker works in.
         
        Return:
            tea_rec(string): A tea recommendation
        """
        #random tea at the teaHouse
        tea_reco =   choice(teaH.teas)
        
        if tea_reco.add_in == "Nothing":
            return f"A tea I would recommend is a {tea_reco.temp} {tea_reco.type} tea."
        else:
            return f"A tea I would recommend is a {tea_reco.temp} {tea_reco.type} tea that has {tea_reco.add_in}"    
                   
class Cashier(Worker):
    """A Worker object.(There are two types of workers.)

     Attributes:
        name(string): name of the worker
    """
    def __init__(self, name):
        """Initialize a Cashier object. Only Cashiers can received payment from a customer.
        
        Args:
            name(string): name of the worker   
        """
        self.name = name
        
         
    def receive_payment(self, customer): 
        """Will take payment from a customer 
        
        Args:
            customer(Customer): customer that wishes to pay their bill
        
        Return:
            has_paid(string): String stating if the bill was paid or not and if the customer has any remaining money.
        Side effects:
            Changes the customer attribute: money.
        """
        has_paid = ""
        for i in customer.orders:
            if i == "small":
                customer.money -= SIZE_PRICE[0]
            elif i == "medium":
                customer.money -= SIZE_PRICE[1]
            elif i == "large":
                customer.money -= SIZE_PRICE[2]
        if customer.money < 0:
            has_paid = "The bill was not paid"
        elif customer.money == 0:
            has_paid = "The bill was paid. The customer has no money left"
        else:
            due_amount = 0
            for m in customer.received:
                due_amount += m.price
                
            customer.money-= due_amount    
            
            has_paid = f"The bill was paid. The customer has ${customer.money} left" 
        return has_paid
    
    def recommend_tea(self, teaHouse):
        return super().recommend_tea(teaHouse)
    
    def run(self, teahouse):
        while True:
            print(f'''Hello, {self.name}. What would you like to do?\n
                  0 : Take payment 
                  1 : Check Data
                  2 : Exit''')
            choice = input('> ')
            if choice == '0':
                pass #self.receive_payment(c1.name)
            elif choice == '1':
                teahouse.plot_data()
            elif choice == '2':
                break

class Waiter(Worker):
    """A Worker object.(There are two types of workers.)

     Attributes:
        name(string): name of the worker
    """
    def __init__(self, name):
        """Initialize a Waiter object. Waiters can only take orders of customers.
        
        Args:
            name(string): name of the worker   
        """
        self.name = name
    
    def addOrder(self, order, customer):
        """Add a order to a customer object if customer has enough money.
        
        Args:
            order(tea): order of customer
            customer (Customer): the customer with the order
        """
        if self.takeOrder(order) is True:
            customer.orders.add(order)      

    def giveOrder(self, customer):
        """ Gives the orders a customer has requested.
        Args:
            order(tea): order of customer
            customer(Customer): customer object.
            
        Side effect:
            Changes the order and received attributes of the customer object.
        
        """
        #if self.takeOrder(customer.orders) is True:
        #    customer.orders.add(order)
            
        #goes through the set of teas that the customer has ordered and 
        #gives the customer their orders(move their set of teas to the received set)
        for t in customer.orders:
            customer.received.add(t)
        
        #clear the order set after completing order
        customer.orders = customer.orders - customer.received
    
    def takeOrder(self, customer):
        """Checks if a customer has enough money for their order
        
        Args:
            customer(Customer object): Customer object
            
        Returns: 
            The order has been taken or state that the customer does not have 
            sufficient amount of money for their order.
        """
        total = 0
        for x in customer.orders:
            total = total + x.price
        return True if customer.money >= total else print("Customer does not have sufficient amount of money for their order.")
        
    def recommend_tea(self, teaHouse):
        return super().recommend_tea(teaHouse)
    
    def run(self, teahouse):
        dialogue = []
        with open("dialogue.txt", 'r',  encoding = 'utf-8') as f:
            for l in f:
                dialogue.append(str(l))
        while True:
            print(f'''Hello, {self.name}. What would you like to do?\n
                  0 : Take order 
                  1 : Check Data
                  2 : Exit''')
            choice = input('> ')
            if choice == '0':
                #guest1 = choice(random_customer_dialogue)
                #a = choice(dialogue)
                random_d = "Hi, I'm Carl and I would like a large cold black tea with boba. I have $7."
                print(random_d)
                customer_name = input("Input name of customer:\n")
                customer_money = input("Input customer money amount:\n")
                #create customer object from customer_name variable look at customer class run method for tea and follow that, slightly changing the dialogue
                c = Customer(customer_name, customer_money)
                tea_type = input("For your order, what type of tea do you prefer? \nWe have: " + "\n")  #change
                
                while True:
                    tea_temp = input("Is that hot or cold? \n") #change to statements
                    if (tea_temp == "hot") or (tea_temp == "cold"):
                        break
                    else:
                        print("Please provide a valid input: 'hot' or 'cold'")
                        continue
                
                while True:    
                    tea_size = input("Will that size be: small, medium, or large?\n")  #change
                    if (tea_size == "small") or (tea_size == "medium") or (tea_size == "large"):
                        break
                    else:
                        print("Please provide a valid input: 'small', 'medium', or 'large'")
                        continue
                while True:    
                    more_add = input("Any add ins? y for yes, and n for no\n")  #change
                    if(more_add == 'y'):
                        if more_add == "y":
                            while True:
                                tea_add_in = input("What add ins would you prefer? We have: 'honey', 'sweetner', 'boba', or 'milk'\n")  #change
                                if (tea_add_in == "honey") or (tea_add_in == "sweetner") or (tea_add_in == "boba") or (tea_add_in == "milk"):
                                   break 
                                else:
                                    print("Please provide a valid input: 'honey', 'sweetner','boba', or 'milk'")
                                    continue                            
                            
                            break    
                    elif more_add == 'n':
                        tea_add_in = "Nothing"
                        break
                    else:
                        print("Please provide a valid input: 'y'or 'n'")
                        continue
                
                tea_order = Tea(tea_type, tea_temp, tea_size, tea_add_in)
                teahouse.add_teas(tea_order)
                
                pass #self.takeOrder('Jasmine Tea')
            elif choice == '1':
                teahouse.plot_data()
            elif choice == '2':
                break


def main():
    th = TeaHouse('Jasmine Dragon')
    t1 = Tea(TEA_TYPE[0], 'hot', ADD_INS[0])
    t2 = Tea(TEA_TYPE[2], 'cold', ADD_INS[2])
    c1 = Customer('Rand', 10.25)
    w1 = Cashier('Perrin')
    w2 = Waiter('Mat')
    
    th.add_teas(t1)
    th.add_teas(t2)
    th.add_workers(w1)
    th.add_workers(w2)
    
    while True:
        state = input('Are you a waiter, cashier, or a customer?\n> ')
        if state.lower() == 'waiter':
            user = Waiter(input('Welcome back! Please enter your name:\n> '))
            user.run(th)
            break
        elif state.lower() == 'cashier':
            user = Cashier(input('Welcome back! Please enter your name:\n> '))
            user.run(th)
            break
        elif state.lower() == 'customer':
            user = Customer(input(f'Welcome to the {th.name}! Please enter your name:\n> '), 10.00)
            print(f'Hi {user.name}, you have ${user.money} to spend. Enjoy!')
            user.run(th)
            break
        else:
            print('Please pick one of the three options!')
            continue
    
    
    
if __name__ == "__main__":
    main()
