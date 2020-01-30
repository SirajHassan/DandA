from Node import Node #base class

class SinglyNode(Node):

    #print all links beyond the node until end.
    def print_links(self):
        if self.next != None:
            print("(" + str(self.data) + ")")
            print(" | ")
            print(" v ")

            self.next.print_links()
        else:
            print("(" + str(self.data) + ")")

    def append_to_tail(self,new_node):
        if (self.next == None):
            self.next = new_node
        else:
            temp_node = self.next

            while(temp_node.next != None):
                temp_node = temp_node.next # go down the line
            temp_node.next = new_node

    #might be more space than iteration..
    def append_to_tail_recursive(self,new_node):
        if self.next == None:
            self.next = new_node
            return
        else:
            self.next.append_to_tail_recursive(new_node)




#testing.....
# n1 = SinglyNode(2)
# n1.append_to_tail_recursive(SinglyNode(1))
# n1.append_to_tail_recursive(SinglyNode(3))
# n1.print_links()
# print(n1.get_data())
