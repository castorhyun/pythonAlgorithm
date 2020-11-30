
import collections

# List Comprehension
# 리스트 압축표현
def list_comp():
    list = [ n * 2 for n in range(0,10)]

    print("list_comp:",list)

# Generator
# yield - 함수 내에서 실행중인 값을 내보내고, return 과 다르게 함수는 끝까지 실행된다.
# 다음값을 생성하기 위해서는  next 함수 사용
# cf) range 함수도 제너레이터 역할을 하는 range 클래스를 리턴함.
def get_natural_num():
    n = 0
    while True:
        n+=1
        yield n

def generator_test():

    g = get_natural_num()
    for _ in range(0,10):
        print(next(g))


def print_test():

    # list 출력
    a = ['A', 'B']
    print('리스트출력 : ', ' '.join(a))

    print('{0} : {2}'.format(1, 'fruit', 'apple'))

    # f-string : 3.6+ 이상에서 지원
    idx = 1
    fruit = 'Melon'
    print(f'{idx+1}:  {fruit}')

# Tip Function annotation - 함수 annotation 은 주석같은 기능으로 코드에 영향을 주는 강제사항은 아님.
# :expression - 함수 매개변수
# -> expression - 함수 return
#def numMatchingSubseq(self, S: str, words: list[str]) -> int:
def numMatchingSubseq(S, words):
    matched_count = 0

    for word in words:
        pos = 0

        for i in range(len(word)):
            # Find matching position for each character
            found_pos = S[pos:].find(word[i])
            if found_pos < 0:
                matched_count -= 1
                break
            else:
                pos += found_pos + 1

        matched_count += 1

    return matched_count

def dictModule():

    # Counter
    a = [1,1,1,2,2,2,2,3,3,3,4,4,4,4,4,5,5,5]
    # Count a item and return Dict type
    b = collections.Counter(a)
    print(b)
    # return 2 items in dict
    print(b.most_common(2))

if __name__ == "__main__":

    # list_comp()
    # generator_test()
    # print_test()
    # S = 'hi hello world'
    # find_word = ['hi', 'world']
    # print(numMatchingSubseq(S, find_word))
    dictModule()



