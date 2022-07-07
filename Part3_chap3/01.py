'''
선형검색
    : 선형으로 나열되어있는 데이터를 순차적으로 스캔하면서 원하는 값을 찾는다
'''

datas = [3, 2, 5, 7, 1, 0, 8, 6, 4]
print(datas)

searchData = int(input('찾으려는 숫자 입력 : '))
searchResIdx = -1

n = 0
while True:
    if n == len(datas):
        searchResIdx = -1
        print('일치하는 결과가 없습니다')
        break

    elif datas[n] == searchData:
        searchResIdx = n
        break


    n += 1

print(f'searchResIdx : {searchResIdx}')

'''
보초법
    : 마지막 인덱스에 찾으려는 값을 추가해서 찾는 과정을 간략화 한다.

예) 찾는 숫자 = 9 일때
검색 성공 : 마지막 이전에 9가 검색된 경우
검색 실패 : 마지막에 9가 검색된 경우
'''

datas = [3, 2, 5, 7, 1, 0, 8, 6, 4]

searchData = int(input('찾으려는 숫자 입력 : '))
searchResIdx = -1
datas.append(searchData)


n = 0
while True:
    if datas[n] == searchData:
        if n != len(datas) - 1:
            searchResIdx = n
        break
    n += 1

print(f'searchResIdx : {searchResIdx}')
