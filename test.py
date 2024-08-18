def test(*args, list_=None):
    if list_ is None:
        list_ = []
        n = 1
    for i in args:
        x = args[n]
        if i == x:
            if n < (len(args) - 1):
                n += 1
            list_.append(i)
        else:
            list_ = [0, 0, 0]
            break
    print(list_)


test(1, 1, 1, 1)
