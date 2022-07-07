# 최솟값(실습)
# 리스트에서 아스키코드가 가장 작은 값을 찾기

class MinAlgorithm:
    def __init__(self, cs):
        self.chars = cs
        self.minNum = 0

    def detMinChar(self):
        self.minNum = self.chars[0]

        for c in self.chars:
            if ord(c) < ord(self.minNum):
                self.minNum = c

        return self.minNum


chars = ['c', 'x', 'Q', 'A', 'e', 'P', 'p']
mc = MinAlgorithm(chars)
minChar = mc.detMinChar()
print(f'minChar : {minChar}')
