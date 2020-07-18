import time


def is_prime_default(n:int, table):
    ret = [n % table[i] for i in range(len(table))]
    return (all(ret), sum([bool(i) for i in ret]))

primes_list = []
primes_list.append(2)
start = time.time()
for j in range(3, 50000, 2):
    tmp = is_prime_default(j, primes_list)
    if tmp[0]:
        primes_list.append(j)
end = time.time()
total = end - start
print("function: {0}".format(total))


primes_list = []
primes_list.append(2)
start = time.time()
for n in range(3, 50000, 2):
    ret = [n % primes_list[j] for j in range(len(primes_list))]
    tmp = (all(ret), sum([bool(i) for i in ret]))
    if tmp[0]:
        primes_list.append(j)
end = time.time()
total = end - start
print("local: {0}".format(total))
