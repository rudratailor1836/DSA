# given a string then reverse a string using a stack
import stacks

ans = str(input("Enter a Word : "))


def reverse_str(user):
    S = stacks.Stack()

    for i in user:
        S.push(i)

    result = ''    
    while(not S.isEmpty()):
        result = result + S.pop()
    
    return result

print(reverse_str(ans))





      


