N = int(input())


def star(depth, shape):
    if depth <= N:
        star(depth + 1, shape)
        # for _ in range(int(2**depth)):
        #     star(depth + 1, shape)
        if depth >= 1:
            for _ in range(2 ** int(depth)):
                print("*", end="")
            print("")
            for _ in range(2 ** int(depth) // 2):
                print("* ", end="")
        else:
            print("*")
    return print("")


star(0, "*")
