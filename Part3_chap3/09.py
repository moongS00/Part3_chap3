'''
삽입정렬
    : 정렬되어 있는 자료 배열과 비교해서 정렬 위치를 찾는다
'''

nums = [5, 10, 2, 1, 0]
print(f'정렬 전 : {nums}')
'''
endIdx = 0
curIdx = 0

for i in range(len(nums) - 2):
    endIdx = i + 1
    curIdx = endIdx + 1

    if endIdx == 1:
        if nums[i] > nums[i+1]:
            nums[i], nums[i+1] = nums[i+1], nums[i]

    if nums[endIdx] > nums[curIdx]:
        nums[0] = nums[curIdx]

    endIdx += 1
    curIdx += 1

print(f'정렬 후 : {nums}')
'''
# 선생님 풀이 (오름차순) (내림차순인 경우, while문에서 첫번째 부등호 방향 반대로 하기)

for i1 in range(1, len(nums)):
    i2 = i1 - 1  # 기준점 이전 숫자들과 비교
    cNum = nums[i1]   # 기준점

    while (nums[i2] > cNum) and (i2 >= 0):    # 기준점 이전 숫자가 더 큰 경우 & 인덱스 범위 내
        nums[i2+1] = nums[i2]   # 자리 교환 반복문
        i2 -= 1   # 기준점 이전 숫자들과 비교. But, 인덱스가 0보다 작으면 오류.

    nums[i2+1] = cNum   # 자리 교환 끝

    print(f'nums : {nums}')

