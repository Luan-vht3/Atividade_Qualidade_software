import math
def divisores(n):
    try:
        n = int(n)
    except TypeError:
        return "Argumento inválido"
    else:
        if n<=0:
            return "O número é inteiro não positivo"
        else:
            divisors_set = {1,n}
            for i in range(2,int(math.sqrt(n))+2):
                if n%i == 0:
                    divisors_set.add(i)
                    divisors_set.add(int(n/i))
            return sorted(divisors_set)