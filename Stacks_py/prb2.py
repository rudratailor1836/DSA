# To create a text editor
# there will be 2 input
# word
# u or r -> u = undo, r = redo
import stacks

def text_editor(text, pattern):
    u = stacks.Stack()
    r = stacks.Stack()

    # push all chr of text in u stack
    for i in text:
        u.push(i)

    # looping on all item of pattern and check if it is undo or redo
    for i in pattern:
        # if u, than we need to get top item from u and store it in r
        if i == 'u':
            data = u.pop()
            r.push(data)
        # if r, than we neeed to get top item from r and store it in u
        else:
            data = r.pop()
            u.push(data)
        
    res = ''
    while (not u.isEmpty()):
        res = u.pop() + res
    
    print(res)


text_editor('Kolkata', 'uuuu')



         
    
    


    