class Tree:
    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = branches

    def is_leaf(self):
        return not self.branches

t = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
t2 = Tree(3, [Tree(1, [Tree(0), Tree(1)]),
              Tree(2, [Tree(1), Tree(1,
                                     [Tree(0), Tree(1)])])])


def display_tree(t):
    if t.is_leaf():
        return [t.label]
    else:
        ans = [t.label]
        for b in t.branches:
            ans += [display_tree(b)]
        return ans

def map_v3(f, t):
    t.label = f(t.label)
    for b in t.branches:
        map_v3(f, b)

def prune(t, x):
# remove each branch with label equal to x
