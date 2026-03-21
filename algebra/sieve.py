#sieve
def sieve(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

    primes = [i for i in range(2, n + 1) if is_prime[i]]
    return primes, is_prime

N = 2 * 10**5 + 5
spf = list(range(N))

def sieve():
    for i in range(2, int(N**0.5) + 1):
        if spf[i] == i:  # i is prime
            for j in range(i * i, N, i):
                if spf[j] == j:
                    spf[j] = i
sieve()

def factorize(x):
    res = []
    while x > 1:
        p = spf[x]
        cnt = 0
        while x % p == 0:
            x //= p
            cnt += 1
        res.append((p, cnt))
    return res