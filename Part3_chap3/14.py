# 최댓값(실습)
# 리스트에서 아스키코드가 가장 큰 값을 찾기

class MaxAlgorithm:
    def __init__(self, cs):
        self.chars = cs
        self.maxChar = 0

    def detMaxChar(self):
        self.maxChar = self.chars[0]

        for c in self.chars:
            if ord(c) > ord(self.maxChar):
                self.maxChar = c

        return self.maxChar


chars = ['c', 'x', 'Q', 'A', 'e', 'P', 'p']
mc = MaxAlgorithm(chars)
maxChar = mc.detMaxChar()
print(f'maxChar : {maxChar}')