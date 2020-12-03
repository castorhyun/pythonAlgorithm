
from typing import List

class Solution:

    def reorderLogfile(self, logs: List[str]) -> List[str]:

        letters, digits = [], []

        for log in logs:
            # 1번 index 값이 숫자이면
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)

        print("digits log :", digits)
        print("letters log :", letters)

        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        print("letters log sorted:", letters)

        return letters + digits





if __name__ == "__main__":
    T = Solution()

    logs = ["dig1 8 1 5 1", "let4 xrt can", "dig2 3 4 2", "let3 case power"]

    T.reorderLogfile(logs)