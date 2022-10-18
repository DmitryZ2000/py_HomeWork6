# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

my_text = 'Скажика дядя ведь не даромабв Москва спалеабвнная пажаром французам отдана'
print(my_text)

musor = 'абв'

print(' '.join((filter(lambda x: not musor in x, [word for word in my_text.split()]))))
