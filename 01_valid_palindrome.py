class Solution:

    def isPalindrome(self, s: str) -> bool:
        # s : alphabet and numeric only

        check_str = []
        for char in s:
            # check type : alphabet & numeric
            if char.isalnum():
                check_str.append(char.lower())
            else:
                pass

        # Validate Palindrome
        # 첫글자 vs 마지막글자 : 문자열에서 하나씩 pop 해서 비교
        while len(check_str) > 1:
            if check_str.pop(0) != check_str.pop():
                return False

        return True


if __name__ == "__main__":
    T = Solution()

    str1 = 'is a palidrome?'
    str2 = 'superman am rep us'

    print('str1 is :', T.isPalindrome(str1))
    print('str2 is :', T.isPalindrome(str2))

