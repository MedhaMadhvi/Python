# Write a Python program to create a class named Stack with methods for pushing and popping elements from the stack. Also, implement an iterator for the Stack class that returns the elements in LIFO (last in first out) order.
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def __iter__(self):
        # The __iter__ method returns an iterator for the stack
        self.index = len(self.items) - 1
        return self

    def __next__(self):
        if self.index >= 0:
            item = self.items[self.index]
            self.index -= 1
            return item
        else:
            raise StopIteration
stack = Stack()
num_elements = int(input("Enter the number of elements to push onto the stack: "))

for i in range(num_elements):
    element = input(f"Enter element {i + 1}: ")
    stack.push(element)

print("Popping elements from the stack in LIFO order:")
for item in stack:
    print(item)
