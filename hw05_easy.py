# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os

#создать папки
def create_dir(number_dir = 9, dir = 'dir'):
    dir_name = [os.getcwd() + '/' + dir + '_' + str(i) for i in range(number_dir)]
    for i in dir_name:
        try:
            os.mkdir(path=i)
        except FileExistsError:
            pass
create_dir(number_dir=12)

#удалить папки
def remove_dir(number_dir = 9, dir = 'dir'):
    dir_name = [os.getcwd() + '/' + dir + '_' + str(i) for i in range(number_dir)]
    for i in dir_name:
        try:
            os.rmdir(path=i)
        except FileNotFoundError:
            pass
remove_dir(number_dir=12)
#-----конец----


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

def show_list():
    return(os.listdir())
show_list()
#-----конец----



# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

import shutil
 def copy_file():
    shutil.copy(__file__, 'copy_' + __file__)
copy_file()
#-----конец----