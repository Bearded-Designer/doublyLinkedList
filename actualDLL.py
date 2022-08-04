class node:
    # def node(self, next=None, prev=None, data=None):
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DLL:
    def __init__(self):
        self.head = None

    # adds to the front of the list
    def push(self, new_data):
        new_node = node(new_data)

        new_node.next = self.head
        new_node.prev = None

        if self.head is not None:
            self.head.prev = new_node

        self.head = new_node

    # adds to the back of the list

    def insertAfter(self, prev_node, new_data):
        """This function inserts data into the middle of the DLL."""

        if prev_node is None:
            print(f"This node does not exist")
            return

        new_node = node(new_data)

        new_node.next = prev_node.next
        prev_node.next = new_node
        new_node.prev = prev_node

        if new_node.next is not None:
            new_node.next.prev = new_node

    def append(self, new_data):
        """This function is what is used to append the DLL at the end"""

        new_node = node(new_data)
        last = self.head

        if self.head is None:
            self.head = new_node
            return
        last = self.head

        while last.next:
            last = last.next

        last.next = new_node
        new_node.prev = last

        return

    def printList(self, node):

        print("\nTraversal in forward direction")
        while node:
            print(" {}".format(node.data))
            last = node
            node = node.next

        print("\nTraversal in reverse direction")
        while last:
            print(" {}".format(last.data))
            last = last.prev
