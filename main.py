'''
https://hackmd.io/FfZ9tBxMSLiBcVka2pytlQ#-%E8%B3%87%E6%96%99%E5%9E%8B%E6%85%8BData-Type-%EF%BC%9A
變數與"資料型態"
'''
# 變數
a = 1
print(a)

b = a
print(b)

b = a + 1
print (b)

c = 'Hello World'
print (c)

Pi = 3.1415926535897
_x = Pi**2
print (_x)

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

#try = 2 * 5
#print(try)

##這樣？ (對, 不能用保留字)) 我用 # 符號將 36, 37 行錯誤先跳掉

# 還有其他不能用的嗎?
# 特殊符號也不能用 ? / ! 
#
# ?A = 1


# 639b = 7
# (對, 數字開頭也不能用) 

# b123 = 7 
# 可以用 數字當尾端

'''
 a = a + 1 這個等號, 跟數學裡的 = 符號 有點不一樣
 為什麼?
'''
#不是等式，而是 我讓前面的變數相當於後面的？ （對, 電腦程式的 = 都是這樣, 把 = 號左邊 置換成 右邊的結果)

小皮球 = 256
print(小皮球)

# 小皮球 可以耶, 你好厲害
def 印出(a):
  print (a)
  
印出(小皮球)

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
# 說明, 整數跟 浮點數 運算後, 希望能保留最精確的內容, 所以用 浮點數表現

# 如何 寫一個 b 是 浮點數, 是把 a 的值(整數) 轉型過來

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


'''
總結

以上大家看到的 a, b, c 或 Pi, 或 小皮球, 都是 電腦程式語言中所謂的 "變數"
有了變數 = 某些變數或運算的結果, 讓電腦能夠幫我們做很多複雜的程式運作. 如果程式只能寫 1 + 100 = 101, 那買計算機就好了.

有了變數 我們還能定義一些 function, 可以帶參數進去, 那個參數也是一種變數, 所以所有形態的變數, 可以當參數傳給 function 裡面做處理, 處理後可以傳回值.
'''

'下一個練習, list.py'