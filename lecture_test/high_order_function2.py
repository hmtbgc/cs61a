def print_sum(n):
    print(n)
    def next_sum(k):
        return print_sum(k + n)
    return next_sum
