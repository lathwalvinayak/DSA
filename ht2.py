#CHAINING
class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self,key):
        hash=0
        for char in key:
            hash+=ord(char)
        return hash % (self.MAX)
    
    def __setitem__(self,key,value):
        h = self.get_hash(key)
        found=False
        for idx,element in enumerate(self.arr[h]):
            if len(element)==2 and element[0]==key:
                self.arr[h][idx]= (key,value)
                found=True
                break
        if not found:    
            self.arr[h].append((key,value))

    def __getitem__(self,key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0]==key:
                return element[1]

    def __delitem__(self,key):
        h=self.get_hash(key)
        for index,element in enumerate(self.arr[h]):
            if element[0]== key:
                del self.arr[h][index]


t=HashTable()        
t['march 6']=120
t['march 6']=78
t['march 8']=12
t['march 9']=10
t['march 17']=150
print(t['march 17'])
print(t['march 6'])
del t['march 17']
print(t.arr)