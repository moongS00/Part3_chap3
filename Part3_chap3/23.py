'''
재귀함수
'''
def recusion(num):
    if num > 0:
        print('*' * num)
        return recusion(num - 1)
    else:
        return 1

recusion(10)


# 팩토리얼
def factorial(n):
    if n > 0:
        return n * factorial(n-1)
    else:
        return 1

print(f'factorial(5) : {factorial(5)}')