'''
https://hackmd.io/FfZ9tBxMSLiBcVka2pytlQ#-%E8%B3%87%E6%96%99%E5%9E%8B%E6%85%8BData-Type-%EF%BC%9A
變數與"資料型態"
'''
# 變數, 以下 a, b, Pi, _x 都是一個變數
a = 1
print(a)

b = a
print(b)

b = a + 1
print (b)

c = 'Hello World'
print (c)

Pi = 3.1415926535897
__x = Pi**2
print (__x)

#mikanchan 你隨便寫一個 變數
# 有什麼變數名稱是不可以的? 考你
# 試寫一個會錯的例子
# 成功了
'''
  File "main.py", line 36
    try = 2 * 5
        ^
SyntaxError: invalid syntax
'''

d = a + 2 - b
print(d)

'以下是一個 不可以用的 變數名稱 try'
#try = 2 * 5
#print(try)

##這樣？ (對, 不能用保留字)) 我用 # 符號將 37, 38 行錯誤先跳掉

# 還有其他不能用的嗎?
# 特殊符號也不能用 ? / ! 
#
# ?A = 1


# 639b = 7
# (對, 數字開頭也不能用) 

# list=[]
# 文法不會報錯, 但用到 list() 會錯誤, 所以不可以用.

b123 = 7 
# 可以用 數字當尾端

'''
 a = a + 1 這個等號, 跟數學裡的 = 符號 有點不一樣
 為什麼?
'''
#原因是, = 不是等式，而是 我讓前面的變數相當於後面的？ （對, 電腦程式的 = 都是這樣, 把 = 號左邊 置換成 右邊的結果)

小皮球 = 256
print(小皮球)
# > 256

# 小皮球 可以耶, 你好厲害
# 我試試看用中文 當 function 名稱,看可不可以?

def 印出(a):
  print (a)
  
印出(小皮球)
# > 256

# 中文 function name 也可以耶

'''
你覺得, 變數為何重要? 
跟計算機比, 很像就更能過做很多事, 那就是程式的目的?
它跟電腦的 CPU + 記憶體 構造也有關係
還有ㄋㄜ?
'''



'----------------------------------------'
'資料型態                                 '
'----------------------------------------'

# 整數跟 浮點數 (數學裡的 小數點), 如何轉換? 寫一個範例

a = int(Pi)
print (a)

# > 3

print (a + Pi)
# > 6.1415926535897
# 說明, 整數跟 浮點數 運算後, 希望能保留最精確的內容, 所以用 浮點數表示

# 如何 寫一個 b 是 浮點數, 是把 a 的值(整數) 轉型成 浮點數

b = float(a)
print(b)

# > 3.0  (答對了)

#mikanchan 那你會用 list 了嗎?
#有看完，但因為安裝有一點狀況，所以還沒有練習
'''
在這裡練習就好了啊? 學 Python 文法, 用這裡線上練習比較簡單
'''

'''
https://hackmd.io/tyZ4ce23Tv62dQ3zeYE00A

你覺得日常生活中, 有哪些是適合用 list 的變數來描述的？
'''
# 比如 排隊的人, 就是一種 list
# 還有哪些? 也是 list ? 舉 2 個以上常用的例子？
# 手機通訊錄、書架上的書 (對)

'mikanchan  list 相關的, 我們可以用 list.py 來練習'

'''
https://hackmd.io/0YyA0f_aTIOQtPiC3cbMiQ?view#-%E5%AD%97%E4%B8%B2%E9%81%8B%E7%AE%97%EF%BC%9A

為何會需要 字串這種形態的變數? 它可以拿來做什麼?
'''
# 比如 檔案名稱 "main.py", 就是一種字串
# 還有哪些? 也是字串? 舉 2 個以上常用的例子？
# 字串當作變數，把我們平常在用的語言轉換成電腦看得懂的語言，也可以讓電腦輸出的結果變成不懂程式語言的人也看得懂的。（對嗎？）

'''
總結

以上大家看到的 a, b, c 或 Pi, 或 小皮球, 都是 電腦程式語言中所謂的 "變數"
有了變數 = 某些變數或運算的結果, 讓電腦能夠幫我們做很多複雜的程式運作. 如果程式只能寫 1 + 100 = 101, 那買計算機就好了.

有了變數 我們還能定義一些 function, 可以帶參數進去, 那個參數也是一種變數, 所以所有形態的變數, 可以當參數傳給 function 裡面做處理, 處理後可以傳回值.
'''

'下一個練習, list.py'




'你有程式片段, 想要問的, 可以寫在 150 行以後'



'------------------------------- 自己可以貢獻 code '
'ming list 測試'
print ('--------------- ming (list) -----------------')
# list
from geeks import geeks
alist = []
aGeeks = geeks("Apple", 3)
bGeeks = geeks("Acer", 500)
alist.append(aGeeks)
alist.append(aGeeks)
alist.append(bGeeks)

print (alist[0].name, alist[0].roll, sep = ' ')

for item in alist:
  print (item.name, item.roll, sep = ' ')

print(alist[1].CONST)

print (alist[0].getPrivate())
# 文法錯誤
#print (list[0].__private)

print (type(alist))
print (dir(alist))

a = len(alist)
print(a)

aGreeks_count = alist.count(aGeeks)
print (aGreeks_count)

for item in alist:
  print (item.name, item.roll, sep = ' ')

alist.clear()
print (alist)

'------------------------------------------------'


# initialize list  
test_list = [1, 4, 6, 8, 9] 
  
# printing original list  
print("The original list : " + str(test_list)) 
  
# Convert Integral list to tuple list 
# using zip() + list() 
res = list(zip(test_list)) 
  
# printing result 
print("List after conversion to tuple list : " + str(res)) 

x = []
y = x
x.append(1)
y.append(2)

print (x)
if (id(x) == id(y)):
  print ('x = y')

print(type(3))
print(dir(3))
print(type(aGeeks))
def add(x, y):
  return x + y
print(add(1,5))
print(type(add))
print(dir(add))
print(type(len))

print('---------- test Class --------')
class Student:

  def __init__(self,name,ch_score, math_score): 

    self.name = name

    self.ch_score = ch_score

    self.math_score = math_score

  def average(self):

    return (self.ch_score + self.math_score)/2



student_lee = Student('李大中', 98, 90)



print('平均成績:', student_lee.average())

import inspect 
for i in inspect.getmembers(student_lee): 
    print(i)
    # to remove private and protected 
    # functions 
    if not i[0].startswith('_'): 
          
        # To remove other methods that 
        # doesnot start with a underscore 
        if not inspect.ismethod(i[1]):  
            print(i) 

print('---------- test a list of objects  --------')

alist = []

student_lee = Student('李大中', 98, 90)

ming = Student('王銘德', 58, 62)

alist.append (student_lee)

alist.append (ming)

b_list = [1, 'apple']
print(b_list)
c_tuple = (1, student_lee.name, 'a tuple')
print(c_tuple)

print(alist[0].name, alist[0].average(), sep = ' ')



for item in alist:
  print(item.name, item.average(), sep = ' ')
  
