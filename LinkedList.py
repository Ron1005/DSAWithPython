#Linked List Impelementation using Python
class Node:
    """"CLass Node is used to add new Nodes to Linked List"""
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class LinkedList:
    def __init__(self):
        self.head=None

    def insert_at_begining(self,data):
        node = Node(data,self.head)
        self.head=node

    def printlist(self):
        if self.head is None:
            print("Linked List is empty")
            return
        else:
            itr = self.head
            lstr=""
            while itr:
                lstr = lstr + str(itr.data) + "-->"
                itr = itr.next
            print(lstr)

    def insert_at_end(self,data):
        itr=self.head
        while itr.next:
            itr=itr.next
        node = Node(data,None)
        itr.next=node

    def get_countoflist(self):
        count=0
        itr = self.head
        while itr:
            itr=itr.next
            count+=1
        return count

    def insert_at_index(self,data,index):
        if index==0:
            self.insert_at_begining(data)
        else:
            count=0
            itr=self.head
            while itr:
                if count==index-1:
                    node=Node(data,itr.next)
                    itr.next=node
                else:
                    itr=itr.next
                count+=1

    def remove_at_beginig(self):
        if self.head is not None:
         self.head=self.head.next

    def remove_at_end(self):
        itr=self.head
        countoflist = self.get_countoflist()
        count=1
        while itr:
            if count==(countoflist-1):
                itr.next=None
                break
            else:
                itr=itr.next
            count+=1

    def remove_at_index(self,index):
        count=0
        itr=self.head
        while itr:
            if count==index-1:
                itr.next=itr.next.next
            else:
                itr=itr.next
            count+=1

    def insert_after_value(self,data_after,data_value):
        itr = self.head
        while itr:
            if itr.data == data_after:
                node=Node(data_value,itr.next)
                itr.next=node
                break
            else:
                itr=itr.next

    def remove_by_value(self,value):
        itr = self.head
        prev=itr
        while itr:
            if itr.data == value:
                prev.next=itr.next
                break
            else:
                prev=itr
                itr=itr.next


l1=LinkedList()
l1.insert_at_begining(5)
l1.insert_at_begining(7)
l1.insert_at_end(8)
l1.insert_at_end(10)
l1.insert_at_index(6,2)
l1.insert_after_value(6,3)
l1.remove_by_value(3)
# l1.remove_at_beginig()
# l1.remove_at_end()
# l1.remove_at_index(1)
l1.printlist()
res = l1.get_countoflist()
print(res)