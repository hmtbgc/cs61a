def for_print(s):
    for x in s:
        print(x)

    print('\n')
    
    items = iter(s)
    try:
        while True:
            item = next(items)
            print(item)
    except StopIteration:
        pass
