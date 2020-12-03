from typing import List

class Solution:

    def reverseSting_2pointer(self, s):
        left, right = 0, len(s) - 1

        print("Input Str:", s)

        list_str = list(s)
        print("list_str:", list_str)

        while left < right:
            # switch left & right
            list_str[left] , list_str[right] = list_str[right], list_str[left]

            left += 1
            right -= 1

        print("reversed Str:", list_str)

        return "".join(list_str)

    def reverseString_func(self, s: List[str]):

        # reverse 함수는 list 에서만 사용가
        # list(s).reverse()
        return s[::-1]

if __name__ == "__main__":
    T = Solution()

    print('reverseSting_2pointer : ', T.reverseSting_2pointer('Apple is delicious'))

    S = 'Apple is delicious'

    print("reverseString_func : ", T.reverseString_func(S))



