'''
최댓값 알고리즘
    : 자료구조에서 가장 큰 값을 찾기
'''

class MaxAlgorithm:

    def __init__(self, ns):
        self.nums = ns
        self.maxNum = 0

    def getMaxNum(self):
        self.maxNum = self.nums[0]

        for i in self.nums:
            if self.maxNum < i:
                self.maxNum = i

        return self.maxNum




nums = [-2, -4, 5, 7, 10, 0, 8, 20, -11]
ma = MaxAlgorithm(nums)
maxNum = ma.getMaxNum()
print(f'maxNum : {maxNum}')