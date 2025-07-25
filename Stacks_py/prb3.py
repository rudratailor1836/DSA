# celebrity problem : input will have nxn matrix
# [0,0,1,1]
# [0,0,1,1]
# [1,0,0,1]
# [0,0,0,0]
# in return we will get single value which is in between o to n-1 or n
# what is celebrity
#  the person which dont know any other but every other knows that person
import stacks

S = [
    [0,0,0,0] ,
    [1,0,1,1],
    [1,0,0,1],
    [1,0,1,0]
]

def find_celeb(L):
    S = stacks.Stack()

    
    for i in range(len(L)) :
        S.push(i)
          
    
    while S.size() >= 2:
        i = S.pop()
        j = S.pop()

        if L[i][j] == 0:
            # j knows i
            # j is not a celeb
            S.push(i)
        else:
            # i knows j
            # i is not a celeb
            S.push(j)
    
    celeb = S.pop()

    for i in range(len(L)):
        if i != celeb:
            if L[i][celeb] == 0 or L[celeb][i] == 1:
                return ('No one is Celeb')
        
    return (f'the celebrity is {celeb}')



print(find_celeb(S))