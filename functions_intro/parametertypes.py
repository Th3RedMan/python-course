def func(p1, p2, *args, k, **kwargs):
    print("Positional-or-keyword:... {}, {}".format(p1, p2))
    print("var-positional (*args):...{}".format(args))
    print("Keyword:..................{}".format(k))
    print("Var-Keyword...............{}".format(kwargs))


func(1, 2, 3, 4, 5, 9, k=6, key1=7, key2=8)
