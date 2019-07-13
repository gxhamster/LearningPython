import math
# sqrt(9) = sqrt(3 * 3)

prime_nums = [2, 3, 5, 7, 11, 13, 17] # So on

def simplify(num):
    for i in range(2, num):
        div, mod = divmod(num, i)
        if mod == 0:
            sq1, sq2 = simplify(div)
            return (i * sq1, sq2)
        if div == 0:
            break
    return (1, num)

print(simplify(75))
print(simplify(50))

