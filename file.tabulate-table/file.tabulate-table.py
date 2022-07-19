from tabulate import tabulate

x = 46
y = 23
body = [[x, y, x+y, x-y, x*y]]
print(tabulate(body, headers=['variabel_x', 'variabel_y', 'sum', 'minus', 'multiplication'], tablefmt='grid'))