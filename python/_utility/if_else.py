'''
None, 0, False in `if` conditions evaluate to `don't execute IF_BLOCK`
'''
if None:
    print("NONE")
else:
    print("NOT NONE")

if 0:
    print("ZERO")
else:
    print("NON ZERO")

if False:
    print("false")
else:
    print("true")