from browser import document, alert

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
echo()
