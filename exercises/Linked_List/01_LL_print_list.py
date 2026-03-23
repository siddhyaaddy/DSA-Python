#in order to look all values in LL we create Print List

def print_list(self):
    temp = self.head
    while temp is not None:
        print(temp.value)
        temp = temp.next

        