stock_price = []
with open("Book1.csv", "r") as f:
    for line in f:
        token = line.split(',')
        day  = token[0]
        price =  float(token[1])
        stock_price.append([day,price])

print(stock_price)

# for element in stock_price:
#     if element[0]=="10-Mar":
#         print(element[1])                   #O(n) complexity

# stock_prices = {}
# with open("Book1.csv", "r") as f:
#     for line in f:
#         token = line.split(',')
#         day  = token[0]
#         price =  float(token[1])
#         stock_prices[day]=price

# print(stock_prices['09-Mar'])               #O(1) complexity


# def get_hash(key):
#     h = 0
#     for char in key:
#         h+= ord(char)
#     return h % 100
# print(ord('m'))
# print(get_hash('28-Mar'))


# class HashTable:
#     def __init__(self):
#         self.MAX = 100
#         self.arr = [None for i in range(self.MAX)]

#     def get_hash(self,key):
#         h=0
#         for char in key:
#             h+=ord(char)
#         return h % (self.MAX)
    
#     def __setitem__(self,key,value):
#         h = self.get_hash(key)
#         self.arr[h]=value

#     def __getitem__(self,key):
#         h = self.get_hash(key)
#         return self.arr[h]

#     def __delitem__(self,key):
#         h=self.get_hash(key)
#         self.arr[h] = None

# t=HashTable()
# t['09-Mar']= 140
# t['20-Dec']=420
# t['16-sept']=111

# print(t['16-sept'])
# print(t.arr)
# del t['09-Mar']
# print(t.arr)