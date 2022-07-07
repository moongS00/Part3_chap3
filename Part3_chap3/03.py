'''
이진 검색
    : 정렬되어 있는 자료구조에서 중앙값과의 크고 작음을 이용해서 데이터를 검색

데이터가 정렬되어 있어야 함!
'''

datas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(f'datas : {datas}')
print(f'datas length : {len(datas)}')

searData =int(input('찾으려는 숫자 입력 : '))
searIdx = -1
staIdx = 0
endIdx = len(datas) - 1
midIdx = (staIdx + endIdx) // 2
midVal = datas[midIdx]
print(f'midIdx : {midIdx}')
print(f'midVal : {midVal}')

n = 0
while n <= len(datas):
    if searData > midVal:
        staIdx = midIdx
        midIdx = (staIdx + endIdx) // 2
        midVal = datas[midIdx]
        print(f'midIdx : {midIdx}')
        print(f'midVal : {midVal}')

    elif searData < midVal:
        endIdx = midIdx
        midIdx = (staIdx + endIdx) // 2
        midVal = datas[midIdx]
        print(f'midIdx : {midIdx}')
        print(f'midVal : {midVal}')

    else:
        searIdx = midIdx
        break

    n += 1

print(f'searIdx = {searIdx}')
