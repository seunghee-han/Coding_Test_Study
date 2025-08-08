class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# 한 곳에서만 자료를 넣고 뺄 수 있다
# LIFO -> last in first out 가장 마지막에 넣은게 제일 빨리 나옴


class Stack:
    def __init__(self):
        self.head = None

    def push(self, value):
        new_head=Node(value)
        new_head.next= self.head
        self.head = new_head
        return

    # pop 기능 구현
    def pop(self):
        delete_head = self.head
        self.head = self.head.next
        return delete_head

    def peek(self):
        return self.head.data

    # isEmpty 기능 구현
    def is_empty(self):
        return self.head is None


stack = Stack()
stack.push(4)
# print(stack.head.data)

stack.push(3)
print(stack.head.data)
print(stack.peek())
