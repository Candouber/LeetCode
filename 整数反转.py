def reverse(x: int) :
        if x > 0:
            x = str(x)[::-1]
            x = int(x.lstrip('0'))
        if x == 0:
            return 0
        if x < 0:
            x = str(x)[:0:-1]
            x = x.lstrip('0')
            x = -int(x)
        if x in range(-2 ** 31, 2 ** 31 - 1):
            return x
        else:
            return 0