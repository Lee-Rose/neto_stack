

class Stack:

    """ This class creates a stack and allows you to work with them using methods :
    isEmpty - check the stack for emptiness. The method returns True or False.
    push - adds a new item to the top of the stack. The method returns nothing.
    pop - removes the top element of the stack. The stack changes. The method returns the top element of the stack
    peek - Returns the top element of the stack, but does not remove it. The stack does not change.
    size - returns the number of elements on the stack."""


    def __init__(self):

        self.stack = []


    def isEmpty(self):

        if len(self.stack) == 0:
            return True
        else:
            return False


    def pop(self):

        try:
            removed_item = self.stack.pop()
            return removed_item
        except IndexError:
            pass


    def push(self, item):

        self.stack.append(item)


    def peek(self):

        try:
            copy_stack = self.stack.copy()
            remove_copy_stack_item = copy_stack.pop()
            return remove_copy_stack_item
        except IndexError:
            print('stack is empty')

        # or return self.stack[len(self.stack) -1]

    def size(self):

        return len(self.stack)


stack = Stack()

def check_balance(my_string):

    """ Return True if string's parentheses are balanced, False otherwise """

    opening = ('(', '[', '{')
    closing = (')', ']', '}')
    mapping = dict(zip(opening, closing))
    for char in my_string:
        if char in opening:
            stack.push(mapping[char])
        elif char in closing:
            if (not stack) or (char != stack.pop()):
                return 'no balanced'
    return 'balanced'

def main():

    print(check_balance('(((([{}]))))'))
    print(check_balance('[([])((([[[]]])))]{()}'))
    print(check_balance('{{[()]}}'))
    print(check_balance('}{}'))
    print(check_balance('{{[(])]}}'))
    print(check_balance('[[{())}]'))

if __name__ == '__main__':
    main()




