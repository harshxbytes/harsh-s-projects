# class Cooker:
#     def __init__(self,color):
#         self.color = color

#     def __str__(self):
#         return self.color
    
# my_cookie = Cooker('green')
# print(my_cookie)

#dictonary 
# dic1 = {
#     "valuet" : 11
#        }
# print(dic1)

#LinkedList
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
class LinkedList:
    def __init__(self,value):
        my_node = Node(value)
        self.head = my_node
        self.tail = my_node
        self.length = 1



my_linked_list = LinkedList(4)

print('Head:', my_linked_list.head.value)
print('Tail:', my_linked_list.tail.value)
print('Length:', my_linked_list.length)