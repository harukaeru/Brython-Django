from browser import document, alert
import random

foo = "{{ foo }}"

print("OK")
class Hoge:
    def __init__(self, a):
        self.a = a

    def p(self):
       print(self.a)

def echo():
    # jQueryめいたこともできる
    print(dir(document["hoge"]))

    # alertも使える
    alert(document["hoge"].text)

# インスタンスも作れる
Hoge(a='aaa').p()

# コンソールに出力
print(foo)
print(random.randint(0, 1000))
echo()
