'''
최솟값 알고리즘
'''

class MinAlgorithm:

    def __init__(self, ns):
        self.nums = ns
        self.minNum = 0

    def getMinNum(self):
        self.minNum = self.nums[0]

        for i in self.nums:
            if self.minNum > i:
                self.minNum = i

        return self.minNum




nums = [-2, -4, 5, 7, 10, 0, 8, 20, -11]
ma = MinAlgorithm(nums)
minNum = ma.getMinNum()
print(f'minNum : {minNum}')