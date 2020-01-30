from Node import Node #base class

class DoublyNode(Node):

    previous = None #linked both ways

    def print_links(self):
        if self.next != None:
            print("(" + str(self.data) + ")")
            print(" ^ ")
            print(" | ")
            print(" v ")
            self.next.print_links()
        else:
            print("(" + str(self.data) + ")")

    #Append node to end
    def append_to_tail(self,new_node):
        if (self.next == None):
            self.next = new_node
            self.next.previous = self
        else:
            temp_node = self.next

            while(temp_node.next != None):
                temp_node = temp_node.next # go down the line
            temp_node.next = new_node

    # might be more space than iteration..
    def append_to_tail_recursive(self,new_node):
        if self.next == None:
            self.next = new_node
            self.next.previous = self
            return
        else:
            self.next.append_to_tail_recursive(new_node)
