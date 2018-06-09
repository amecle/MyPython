def dadao():
    print('我是dadao()，我在__all__前')

__all__ = ['p01']

def inInit():
    print('哈哈！I am in init of package！')