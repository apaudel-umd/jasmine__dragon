# Jasmine Dragon
INST326 Final Project


## Files
- order_history.csv
- teahouse.py
- testing_teahouse.ipynb

## Running the program
You can run the program with <`python` or `python3`> `teahouse.py`. 
Upon starting the program, you can choose to be a `waiter`, `cashier`, or a `customer`.
A waiter can take/deliver orders and check order history.
A cashier can handle payments and check order history.
A customer can order tea and make payments.

## Output
When choosing to check data, you will see seaborn bar graphs as output in a new window. You can check graphs for:
- Tea Types
- Tea Temp
- Tea Size
- Add ins

All of the data will be output as bar graphs.

## Attribution:
**Katherine Argente:**
- recommend_tea() [Worker class]
- giveOrder() [Waiter class]

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