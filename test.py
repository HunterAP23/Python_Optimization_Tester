import time


def is_prime(n, table):
    ret = [n % table[i] for i in range(len(table))]
    return (all(ret), sum([bool(i) for i in ret]))

primes_list = []
ret.append(2)
start = time.time()
for j in range(3, my_max, 2):
    tmp = is_prime(j, tuple(primes_list))
    if tmp[0]:
        div_list.append("Primality Test for {0} took {1} divisions.\n\n".format(j, tmp[1]))
        primes_list.append(j)
end = time.time()
total = end - start
print("function: {0}".format(total))


ret = []
ret.append(2)
start = time.time()
for i in range(10000):
    for j in range(1000):
        ret = [j % table[i] for i in range(len(table))]
        ret.append(all(ret), sum([bool(i) for i in ret]))
end = time.time()
total = end - start
print("local: {0}".format(total))
