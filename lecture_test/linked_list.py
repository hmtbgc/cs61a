class link:
    empty = ()
    def __init__(self, first, rest=empty):
        self.first = first
        self.rest = rest

a = link(1, link(2, link(1)))
b = link(3, link(2, link(1)))
combined = link(a, link(b))


def sum(lnk):
    empty = ()
    if lnk.rest == empty:
        return lnk.first
    else:
        return lnk.first + sum(lnk.rest)

def display_link(lnk):
    def con_string(lnk):
        empty = ()
        if lnk.rest == empty:
            return str(lnk.first)
        else:
            return str(lnk.first) + con_string(lnk.rest)
    return con_string(lnk)

def map(f, lnk):
    empty = ()
    if lnk.rest == empty:
        return link(f(lnk.first))
    else:
        return link(f(lnk.first), map(f, lnk.rest))


def map_v2(f, lnk):
# mutate the linked list

#    empty = ()
#    while(lnk != empty):
#        lnk.first = f(lnk.first)
#        lnk = lnk.rest


    empty = ()
    if lnk == empty:
        return
    else:
        lnk.first = f(lnk.first)
        map_v2(f, lnk.rest)

def insert(num, lnk):
# insert num into index 1 of lin
    insert_link = link(num)
    insert_link.rest = lnk.rest
    lnk.rest = insert_link
