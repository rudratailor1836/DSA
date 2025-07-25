# balancing the brackets by checking that it is mathematically correct or not
import stacks
exp = '[{(a + b) + (b + c))}]'

def balance_brackets(eqation):
    B = stacks.Stack()
    for i in eqation:
       if i == '[' or i == '':
           pass
        
