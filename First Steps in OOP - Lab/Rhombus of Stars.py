def rhombus_of_stars(n):
    for i in range(1, n + 1):
        spaces = n - i
        stars = i
        print(' ' * spaces + '* ' * stars)

    for i in range(n - 1, 0, -1):
        spaces = n - i
        stars = i
        print(' ' * spaces + '* ' * stars)


size = int(input())
rhombus_of_stars(size)
