"""
Напишите проверку на то, является ли строка палиндромом. Палиндром — это слово или фраза, которые одинаково читаются слева направо и справа налево. Палиндром слова: тот -> тот потоп -> потоп көк -> көк Пример: palindrom_check("test") Возврат: Это не палиндром! palindrom_check("anna") Возврат: Это палиндром!def palindrom_check(word):

"""
def palindrom_check(word):
    word = str(input())
    a = word[::-1]
    if word == a:
      print(" Это палиндром!")
    else:
      print("Это не палиндром!")
print(palindrom_check('bob'))

