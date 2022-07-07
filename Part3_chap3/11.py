'''
선택정렬
    : 주어진 르스트 중에 최소값을 찾아, 그 값을 맨 앞에 위치한 값과 교체하는 방식
'''

nums = [4, 2, 5, 1, 3]
print(f'first nums : {nums}')

for i in range(len(nums) -1):   # 맨 앞의 숫자, 한번 정렬 싸이클이 끝나면 다음 인덱스로 넘어감
    minIdx = i

    for j in range(i+1, len(nums)):   # i 뒤의 인덱스 숫자들. i와 크기 비교 후, 제일 작은 값을 minIdx로 설정
        if nums[minIdx] > nums[j]:
            minIdx = j

    nums[i], nums[minIdx] = nums[minIdx], nums[i]   # i뒤의 최소값과 i의 자리를 변경
    print(f'nums : {nums}')


print(f'final nums : {nums}')