import time


def is_prime_default(n: int, table):
    ret = [n % i for i in table]
    return (
        all(ret),
        sum(ret),
    )


primes_list = []
primes_list.append(2)
start = time.perf_counter()
for j in range(3, 50000, 2):
    tmp = is_prime_default(j, primes_list)
    if tmp[0]:
        primes_list.append(j)
end = time.perf_counter()
total = end - start
print("function: {0}".format(total))


primes_list = []
primes_list.append(2)
start = time.perf_counter()
for n in range(3, 50000, 2):
    ret = [n % primes_list[j] for j in primes_list]
    tmp = (all(ret), sum([bool(i) for i in ret]))
    if tmp[0]:
        primes_list.append(j)
end = time.perf_counter()
total = end - start
print("Inline: {0}".format(total))
