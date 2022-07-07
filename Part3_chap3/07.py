'''
버블정렬
    : 인접한 두개의 값을 비교 해서 크기에 따라 위치를 서로 교환
'''
nums = [10, 2, 7, 21, 0]
print(f'not sorted nums : {nums}')

elngth = len(nums) - 1

for i in range(elngth):
    for j in range(elngth - i):
        if nums[j] > nums[j+1]:
            temp = nums[j]
            nums[j] = nums[j + 1]
            nums[j + 1] = temp  # nums[j], nums[j+1] = nums[j+1], nums[j] 파이썬에는 한줄로 간단히 하는 방법이 존재
        print(nums)

    print()

print(f'sorted nums : {nums}')