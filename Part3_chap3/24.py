# 재귀 (실습)
# 재귀 알고리즘을 이용한 최대 공약수 계산(유클리드 호제법)

def gcd(n1, n2):
    if n1 % n2 == 0:
        return n2

    else:
        return gcd(n2, n1 % n2)


print(f'gcd(82, 32) : {gcd(82, 32)}')
print(f'gcd(96, 40) : {gcd(96, 40)}')
