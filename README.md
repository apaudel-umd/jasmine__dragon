# Jasmine Dragon
INST326 Final Project


## Files
- order_history.csv: This is a file used to generate a dataframe and acts as the history of the tea house. Used for pandas and seaborn.
- teahouse.py : This is the main file with all the classes and functions in one place. This is the file you have to run.
- testing_teahouse.ipynb: This is useless for the program, but it was the notebook we used to test code and do the presentation.
- dialogue.txt: This is used to randomly pick a prompt when user is logged in as a cashier. 

## Running the program
You can run the program with <`python`/`python3`> `teahouse.py`. 
Upon starting the program, you can choose to be a `waiter`, `cashier`, or a `customer`.
No matter who you choose, you have to first enter your name. This name will be used to generate the appropriate class.
- A waiter can take orders and check order history.
- A cashier can take payments check order history, and sort the list of customers.
- A customer can order tea, make a payment, and ask for tea recommendations.

Please enter the numbers shown to make your selection. From here on out, you can enter the numbers to make a choice, and type in the appropriate words when asked any questions. The last option will always be `exit` which you can use to close the program. 

## Output
**If you are a customer:**
- When choosing the 'Add Order' option, you will see the possible tea selections available at the teahouse: this then goes through the list of Tea attributes to allow a customer to full customize their tea order, prints to the terminal 
- When choosing the 'Make payment' option, you will see your full order set that you have paid  print to the terminal
- When you ask for a tea recommendation, you will see a random tea recommendation print to the terminal

**If you are a waiter:**
- When choosing the 'Take order' option, you will see a random customer dialogue print to the terminal. It is your job to input their name, how much money they have, and tea order into the teahouse system 

**If you are a cashier:**
- When choosing the 'Take payment', you will see that a customer wants to pay for their order and that you have handed their payment print to the console
- When choosing the 'Sort customers', you will first see the system ask yes for confirmation then print the list of customers, the amount of money they paid, their order, and if they received their order yet to the console 

**If you are either a Waiter or Cashier:**
When choosing to check data, you will see seaborn bar graphs as output in a new window. You can check graphs for:
- Tea Types
- Tea Temp
- Tea Size
- Add ins

All of the data will be output as bar graphs.



## Attribution:
**Katherine Argente:**
- Worker (including Cashier and Waiter): __init__()
- Worker: recommend_tea() (f-strings)
- Waiter: giveOrder() (set operations on sets)
- Customer: run() 

**Nikhita Tripuramallu:**
- Customer: __init__() 
- Waiter: takeOrder() (conditional expressions)
- TeaHouse: sorting_customers()(custom list sorting with a key)
- Cashier: receive_payment()

**Adhish Paudel**
- TeaHouse: __init__ (Uses Pandas to create a data frame)
- Teahouse: plot_data (Uses pandas and groupby method)
- Teahouse: plot_data (Uses seaborn to plot bar graphs, uses matplotlib to display the graph)
- Global Variables : Prices (Uses sequence unpacking)
- main() function

**Ashley Trang**
- Tea: __init__ method (optional parameters/keyword arguments)
- Tea: __str__() (magic methods other than __init__)
- Tea: updateprice()
- Tea: combine()
- Tea: updateTea()