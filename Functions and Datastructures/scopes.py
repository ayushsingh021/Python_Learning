# LEGB --- (Built-In Scope-> Global Scope-> Enclosing Scope-> Local Scope ) Bigger set to smaller set order

# Built scopes are print , def , for...in --anywhere accesible
#global scope
my_global = 10

def fn1():
    enclosed_v = 8
    def fn2():
        local_v = 5
        print("Access to global variabel : ", my_global )
        print("Access to enclosed variable : " , enclosed_v)
    fn2()        
fn1()

print("Cant access enclosed var ", enclosed_v)