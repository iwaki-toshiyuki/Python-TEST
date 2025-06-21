# 課題１
print("hello world")

# 課題2
def greet():
  print("こんにちは")

greet()


# 課題3
def print_name(name):
  return "私の名前は" + name + "です"

print(print_name("トイトイ"))

#課題4
def get_greet():
  return "おはようございます"

print(get_greet())

#課題5
def add(a,b):
  return a + b

print(add(6,21))


#課題6
import webbrowser
url = "file:///Users/iwakitoshiyuki/raretech/python/Python-TEST/example.html"
webbrowser.open_new_tab(url)
