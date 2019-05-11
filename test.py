def foo(xyz=None, u='abc', z=123):
    if xyz is None:
        xyz = []
    xyz.append(1)
    print(xyz)
    
foo()
print(1, foo.__defaults__, id(foo))
foo()
print(2, foo.__defaults__, id(foo))
lst = [10]
foo(lst)
print(lst)
print(3, foo.__defaults__, id(foo))
foo([10,5])
print(4, foo.__defaults__, id(foo))
