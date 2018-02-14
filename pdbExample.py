# python debug

import pdb

def doubleval(argsum, val):
    argsum = 0
    newval = argsum + val
    return newval

pdb.set_trace()  # break point

values = [1,2,3,4,5]

mysum = 0

for val in values:
    mysum = 0
    mysum = doubleval(mysum, val)

    
print(mysum)


    # c or continue to go to next step of loop
    # n - next line - keep the current context, not enetering e.g. functions that you calls
    # s - next step - with changing contecst
    # l - list show the code and your position
    # h - help
    # quit 
