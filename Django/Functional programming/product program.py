from functools import reduce
products=[
    {"item_name":"boost","mrp":290,"stock":50},
    {"item_name":"complan","mrp":240,"stock":10},
    {"item_name":"bournvita","mrp":320,"stock":20},
    {"item_name":"horlicks","mrp":280,"stock":13},
    {"item_name":"nutricharge","mrp":275,"stock":0},
]

# highest cost

prices=list(map(lambda product:product["mrp"],products ))
high_cost=reduce(lambda price1,price2:price1 if price1>price2 else price2,prices)
print(high_cost)