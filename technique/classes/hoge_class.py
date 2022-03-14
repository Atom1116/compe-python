class Hoge:
    def __init__(self, name):
        self.name = name

    def call_name(self):
        print('I am {}'.format(self.name))


class FugaMixin:
    def call_hello(self,):
        print('Hello!')
        self.call_name()


class HogeFuga(Hoge, FugaMixin):
    def __init__(self, name):
        super().__init__(name)

    def call(self):
        self.call_hello()


if __name__ == '__main__':
    hoge_fuga = HogeFuga('hikaru')
    hoge_fuga.call()
