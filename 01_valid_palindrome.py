import re

class Solution:

    def isPalindrome_pop(self, s: str) -> bool:
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

    def isPalindrome_slicing(self, s: str) -> bool:

        # convert to lower char
        s = s.lower()

        # 정규식 : a-z0-9 : 소문자,숫자 형태 아닌 경우 '' 변환
        s = re.sub('[^a-z0-9]', '', s)

        # 역순으로 정렬
        s_rev = s[::-1]

        return s == s_rev


if __name__ == "__main__":
    T = Solution()

    str1 = 'is a palidrome?'
    str2 = 'superman am rep us'

    print("pop fn test")
    print('str1 is :', T.isPalindrome_pop(str1))
    print('str2 is :', T.isPalindrome_pop(str2))

    print("slicing fn test")
    print('str1 is :', T.isPalindrome_slicing(str1))
    print('str2 is :', T.isPalindrome_slicing(str2))


