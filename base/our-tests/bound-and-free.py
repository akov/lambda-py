# var is bound and free in class

def f(x):
    class C:
        def m(self):
            return x
        a = x
    return C

inst = f(3)()
inst.a
inst.m()
