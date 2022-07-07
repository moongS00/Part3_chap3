# 이진 검색 (실습)
# 리스트를 오름차순으로 정렬한 후 7을 검색하고 인덱스 출력

nums = [4, 10, 22, 5, 0, 17, 7, 11, 9, 61, 88]
nums.sort()

searData =int(input('찾으려는 숫자 입력 : '))
searIdx = -1
staIdx = 0
endIdx = len(nums) - 1
midIdx = (staIdx + endIdx) // 2
midVal = nums[midIdx]
print(f'midIdx : {midIdx}')
print(f'midVal : {midVal}')

n = 0
while n <= len(nums):
    if searData > midVal:
        staIdx = midIdx
        midIdx = (staIdx + endIdx) // 2
        midVal = nums[midIdx]
        print(f'midIdx : {midIdx}')
        print(f'midVal : {midVal}')

    elif searData < midVal:
        endIdx = midIdx
        midIdx = (staIdx + endIdx) // 2
        midVal = nums[midIdx]
        print(f'midIdx : {midIdx}')
        print(f'midVal : {midVal}')

    else:
        searIdx = midIdx
        break

    n += 1

print(f'searIdx = {searIdx}')