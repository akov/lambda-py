def f(x):
    class c:
        nonlocal x
        x += 1
        def get(self):
            return x
    return c()

c = f(0)
___assertEqual(c.get(), 1)
print('x' in c.__class__.__dict__)
print(dict.__dict__)
