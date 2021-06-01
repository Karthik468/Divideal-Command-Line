# Divideal-Command-Line
Split the expenses among group of people .This is command line Project in python

App to split your expenses and simplify them to their minimum number of transactions possible.

CLI python app takes the user input and calculates the total debts each person in the group have. At the end we run Ford-fulkerson or a simple greedy approach to reduce the no. of transactions to their minimum.

Input for CLI:

<EXPENSE/SHOW> (payer) (Payee Amount) (No.of users) (Type of split) (Users involved) <Amounts/Values>

Example:
        EXPENSE u1 2000 4 u3 u4 u6 u2 PERCENT 23 27 35 15

We can make 5 different kinds of splits

1.EQUAL
2.EXACT
3.SHARES
4.PERCENT
5.ADJUST
You can access the same app from our flask app at [divideal](https://divideal.pythonanywhere.com/)
