from typing import List
import re
import collections

class Solution:

    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:

        # re.sub \W : 단어문자가 아닌 경우 공백으로 substitute
        # lower() 소문자 변환
        # 공백단위로 split

        print("Asis paragraph :", paragraph)
        print(re.sub(r'[^\w]', ' ', paragraph))
        words = [ word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned ]

        print("Tobe sub : words ", words)

        counts = collections.Counter(words)

        print(counts)
        # most_common(출력갯수)
        print(counts.most_common(1))

        # counts.most_common(1) : [('ball', 2)]
        # counts.most_common(1)[0] : ('ball', 2)
        # counts.most_common(1)[0][0] : ball
        # counts.most_common(1)[0][1] : 2

        return counts.most_common(1)[0][0]

if __name__ == "__main__":

    T = Solution()

    paragraph = "Bob hit a ball, the hit Ball flew far after it was hit"
    banned = ['hit']

    print(T.mostCommonWord(paragraph, banned))

