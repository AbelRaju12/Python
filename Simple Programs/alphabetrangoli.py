def print_rangoli(n):
    import string

    alphabet_list = list(string.ascii_lowercase) #imports all aplhabets in lowercase

    rangoli = alphabet_list[:n]
    rangoli.reverse()

    ln_str = 0

    while ln_str < n:
        for i in range(1, n+1):
            pattern = ('-'.join(rangoli[0:i])).rjust(n*2-1, '-')
            print(pattern + pattern[::-1][1:])
            ln_str += 1

    for _ in range(1, n):
        pattern = ('-'.join(rangoli[:-1])).rjust(n*2-1, '-')
        print(pattern + pattern[::-1][1:])
        rangoli.pop()
n = int(input())
print_rangoli(n)
