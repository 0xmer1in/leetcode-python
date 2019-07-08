from collections import defaultdict
# 方向数组
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


END_OF_WORD = "#"


class Solution:
    def findWords(self, board, words):
        # 参数的判断
        if not board or not board[0]: return []
        if not words: return []

        self.result = set()

        # root 和 node 共享同一个地址，即node = node.setdefault(char, defaultdict())会影响root
        # 将 words 数组里的元素按照一个个单独的字母存进root
        root = defaultdict()
        for word in words:
            node = root
            for char in word:
                node = node.setdefault(char, defaultdict())
            node[END_OF_WORD] = END_OF_WORD

        # m 是矩阵的长度，n 是矩阵的宽度
        self.m, self.n = len(board), len(board[0])
        # print(root)
        for i in range(self.m):
            for j in range(self.n):
                if board[i][j] in root:
                    self._dfs(board, i, j, "", root)

        return list(self.result)

    def _dfs(self, board, i, j, cur_word, cur_dict):
        cur_word += board[i][j]
        cur_dict = cur_dict[board[i][j]]
        print(cur_dict)

        if END_OF_WORD in cur_dict:
            self.result.add(cur_word)

        tmp, board[i][j] = board[i][j], '@'
        for k in range(4):
            x, y = i + dx[k], j + dy[k]
            if 0 <= x < self.m and 0 <= y <self.n \
                and board[x][y] != '@' and board[x][y] in cur_dict:
                self._dfs(board, x, y, cur_word, cur_dict)
        board[i][j] = tmp


test = Solution()
board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]
test.findWords(board, words)