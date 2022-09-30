import math
def divisores(n):
    try:
        divisors_set = {1,n}
        for i in range(2,int(math.sqrt(n))+2):
            if n%i == 0:
                divisors_set.add(i)
                divisors_set.add(int(n/i))
        return sorted(divisors_set)
    except TypeError:
        return "Argumento inválido"