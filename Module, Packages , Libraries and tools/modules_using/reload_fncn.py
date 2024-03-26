#  The reload function reloads an imported module in Python. The only precondition is that the argument passed to it must be a module that has already been successfully imported within the program. 

import importlib
import file_changes

#reloads the sample module multiple times 
def changes():
    try:
        importlib.reload(file_changes)
        file_changes.print_changes()
    except:
        pass

for i in range(5):
    changes()
    input("Hit Enter to reload")