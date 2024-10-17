class Node:
    def __init__(self,data,next):
        self.data=data
        self.next=next

class LinkedList:
    def __init__(self):
        self.head=None

    def insertAtBegin(self,data):
        node=Node(data,self.head)
        if self.head==None:
            self.head=node
        else:
            node.next=self.head
            self.head=node
        return 
    
    def insertAtEnd(self,data):
        node=Node(data,self.head)
        if self.head==None:
            self.head=node
        else:
            ptr=self.head
            while(ptr.next!=None):
                ptr=ptr.next
            ptr.next=Node(data,None)    
        return
    
    def insert_values(self,l):
        for i in l:
            self.insertAtEnd(i)
        return 
    
    def getLength(self):
        itr=self.head;c=1
        while(itr):
            itr=itr.next
            c+=1
        return c


    def remove(self,index):
        if index<0 or index>self.getLength():
            print("invalid")
        elif index==0:
            self.head=self.head.next
        elif index==self.getLength():
            ptr=self.head;c=0
            while(ptr):
                if c==self.getLength()-2:
                    ptr.next=None
                c+=1
                ptr=ptr.next
        else:
            ptr=self.head;count=0
            while(ptr):
                if count==index-1:
                    ptr.next=ptr.next.next
                ptr=ptr.next
                count+=1
        return
    
    def insertAtIndex(self,index,val):
        if index==0:
            self.insertAtBegin(val)
        elif index==self.getLength()-1:
            self.insertAtEnd(val)
        else:
            ptr=self.head;c=0
            while(ptr):
                if c==index-1:
                    ptr.next=Node(val,ptr.next.next)
                    break
                ptr=ptr.next
                c+=1
        return 
    
    def insert_after_value(self,data_after,data_to_insert):
        ptr=self.head
        while(ptr):
            if ptr.data==data_after:
                ptr.next=Node(data_to_insert,ptr.next)
                break
            ptr=ptr.next
        return 
    
    def remove_by_value(self,data):
        ptr=self.head
        while(ptr):
            if ptr.next.data==data:
                ptr.next=ptr.next.next
                break
            ptr=ptr.next
        return      
    
    def print(self):
        if self.head==None:
            print("the linkedlist is empty")
        else:
            ptr=self.head;llstr=""
            while(ptr):
                llstr+=str(ptr.data)+"-->"
                ptr=ptr.next
            llstr+="NULL"
            print(llstr)
                
ll=LinkedList()
ll.insertAtBegin(9)
ll.insertAtBegin(10)
ll.insertAtBegin(11)
ll.insertAtEnd(33)
ll.insertAtEnd(50)
ll.insert_values([2,3,4,5,6])
ll.print()
ll.insertAtIndex(1,100)
ll.print()
ll.insertAtIndex(3,1000)
ll.print()
ll.remove(0)
ll.print()
ll.insert_after_value(9,1000000000)
ll.print()
ll.remove_by_value(5)
ll.print()
