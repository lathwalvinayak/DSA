class Node:
    def __init__(self,d=None,n=None):
        self.data=d
        self.next=n

class LinkedList:
    def __init__(self):
        self.head=None

    def insert_at_beigning(self,data):
        node = Node(data,self.head)
        self.head=node

    def print(self):
        if self.head is None:
            print("LinkedList is empty")

        itr=self.head
        llstr=''

        while itr:
            llstr += str(itr.data)+'-->'
            itr=itr.next                   
        print(llstr)

    def inset_at_end(self,data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr=itr.next

        itr.next=Node(data, None)    

    def insert_values(self, data_list):
        self.head=None
        for values in data_list:
            self.inset_at_end(values)

    def get_lenght(self):
        count=0
        itr=self.head
        while itr:
            count+=1
            itr=itr.next
        return count    

    def remove_at(self,index):
        if index<0 or index>self.get_lenght():
            raise Exception("Invalid Index")

        if index==0:
            self.head=self.head.next

        count=0
        itr=self.head
        while itr:
            if count== index-1:
                itr.next=itr.next.next
                break

            itr=itr.next
            count+=1

    def insert_at(self,index,value):
        if index<0 or index>self.get_lenght():
            raise Exception("Invalid Index")
        
        if index==0:
            self.insert_at_beigning(value)
            return

        count = 0
        itr=self.head
        while itr:
            if count == index-1:
                node = Node(value,itr.next)
                itr.next = node
                break
            
            itr=itr.next
            count+=1

    def insert_after_value(self, data_after, data_to_insert):
        if data_after<-1 or data_after>self.get_lenght():
            raise Exception("Invalid Index")
        if data_after==-1:
            self.insert_at_beigning(data_to_insert)
        count=0
        itr = self.head
        while itr:
            if count==data_after:
                node=Node(data_to_insert,itr.next)
                itr.next=node
                break

            itr=itr.next
            count+=1    

    def remove_by_value(self, data):
        if self.head is None:
            raise Exception("List is Empty")
        
        if self.head.data == data:
            self.head=self.head.next
            return
        
        itr=self.head
        while itr.next:
            if itr.next.data == data:
                itr.next=itr.next.next
                break
            itr = itr.next


ll=LinkedList()

ll.insert_values([1,89,3,7,6,5])
ll.print()
ll.insert_after_value(-1,222)
ll.print()
ll.remove_by_value(222)
ll.print()