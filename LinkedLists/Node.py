
#This will be a base class for nodes in singly and double linked lists..

class Node():

    next = None #next node, should be Node Class
    data = None #no type


    def __init__ (self,data):
        self.data = data

    def get_data(self):
        return self.data

    def set_data(self,new_data):
        self.data = new_data
