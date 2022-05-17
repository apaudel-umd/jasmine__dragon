# Jasmine Dragon
INST326 Final Project


## Files
- order_history.csv
- teahouse.py
- testing_teahouse.ipynb
- dialogue.txt

## Running the program
You can run the program with <`python` or `python3`> `teahouse.py`. 
Upon starting the program, you can choose to be a `waiter`, `cashier`, or a `customer`.
A waiter can take/deliver orders and check order history.
A cashier can handle payments and check order history.
A customer can order tea and make payments.

## Output
**If you are a customer:**
When choosing the make payment, you will see your full order set that you payed for, print to the terminal

**If you are a Waiter/Cashier:**
When choosing to check data, you will see seaborn bar graphs as output in a new window. You can check graphs for:
- Tea Types
- Tea Temp
- Tea Size
- Add ins

All of the data will be output as bar graphs.



## Attribution:
**Katherine Argente:**
- Worker(including Cashier and Waiter): __init__() method
- Worker:recommend_tea() (f-strings)
- Waiter: giveOrder() (set operations on sets)
- Customer: run() method

**Nikhita Tripuramallu:**
- Customer __init__() method
- takeOrder() [Waiter class] (conditional expressions)
- sorting_customers() [Teahouse class] (custom list sorting with a key)
- receive_payment() [Cashier class]

**Adhish Paudel**
- TeaHouse: __init__ (Uses Pandas to create a data frame)
- Teahouse: plot_data (Uses pandas and groupby method)
- Teahouse: plot_data (Uses seaborn to plot bar graphs, uses matplotlib to display the graph)
- Global Variables : Prices (Uses sequence unpacking)

**Ashley Trang**
- Tea: __init__ method (optional parameters/keyword arguments)
- Tea: magic methods __str__ (fstrings)
- Tea: updateprice()
- Tea: combine()
- Tea: updateTea()