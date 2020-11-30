

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

if __name__ == "__main__":

    # list_comp()
    # generator_test()
    print_test()
