class geeks:
    CONST = 'OK'
    def __init__(self, name, roll):
      self.name = name
      self.roll = roll
      # 測試 private 變數的寫法
      self.__private = "秘密, 要用 getPrivate() 才看得到"
    def getPrivate(self):
      return self.__private

