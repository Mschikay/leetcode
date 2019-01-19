# 没有run出来 见leetcode solution 用深度优先
import sys

class Solution:
    def __init__(self):
        # [['A1', 'B', 'C1', 'E1'], ['S1', 'F', 'C2', 'S2'], ['A2', 'D', 'E2', 'E3']]
        self.dict = {'A': [0, 8],
                'B': [1],
                'C': [2, 6],
                'D': [9],
                'E': [3, 10, 11],
                'F': [5],
                'S': [4, 7],}
        self.map = [[0, 8],
                        [1],
                        [2, 6],
                        [9],
                        [3, 10, 11],
                        [5],
                        [],
                        [],
                        [],
                        [],
                        [],
                        [],
                        [],
                        [],
                        [],
                        [],
                        [],
                        [],
                        [4, 7],
                        [],
                        [],
                        [],
                        [],
                        [],
                        [],
                        [],
                        ]

        self.board = [[0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, ],
                      [1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, ],
                      [0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, ],
                      [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, ],
                      [1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, ],
                      [0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, ],
                      [0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, ],
                      [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, ],
                      [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, ],
                      [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, ],
                      [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, ],
                      [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, ], ]

        self.reached = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,]
    def exist(self, word):
        ll = len(word)
        alpha = word[0]
        arralpha = self.map[ord(alpha)-65]  # use ascii to address
        if len(arralpha) == 0:
            print("False")
            return
        else:
            for la in arralpha:
                track = []
                track.append(la)
                self.reached[la] = 1
                start = la
                for i in range(1, ll):
                    beta = word[i]
                    arrbeta = self.map[ord(beta)-65]
                    # first check if there is an alphabet
                    if len(arrbeta) == 0:
                        print("False")
                        return
                    else:
                        end = -sys.maxsize
                        for lb in arrbeta:
                            # second check if it is reachable and used
                            if self.board[start][lb] == 0 or self.reached[lb] == 1:
                                pass
                            else:   #it is reachable and not used
                                self.reached[lb] = 1
                                start = lb
                                end = lb
                                break
                        if end < 0:
                            print("False")
                            return
                        else:
                            track.append(lb)
                            pass
                print(track)
                return True



if __name__ == "__main__":
    s = Solution()
    s.exist(sys.argv[1])