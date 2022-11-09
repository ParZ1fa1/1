import os
import time
count=1
i=0
n=0
finalbuffer= ""
buffer_len = 1
tempk=0
preview=""
a=1
start = time.time()
try:
    with open("testfile.txt", 'r') as file:
        buffer = file.read(buffer_len)
        if not buffer:
            print("\nФайл .txt в директории проекта пустой.\nДобавьте не пустой файл в директорию или переименуйте существующий *.txt файл.")
        while buffer:
            a=-a
            while buffer == "0":
                tempk+=1
                buffer=file.read(buffer_len)
                count=tempk
                preview=""
            n += 1
            if n//2 == count:
                n=0
                if preview.isdigit() == True and buffer.isdigit() == False:
                    finalbuffer += str(preview)
                    buffer = file.read(buffer_len)
                elif preview.isdigit() == True and buffer.isdigit() == True:
                    finalbuffer += buffer + preview
                    buffer = file.read(buffer_len)
                    preview=buffer

            elif count > 1 and n > 1:
                if preview.isdigit() == True and buffer.isdigit() == False:
                    finalbuffer += str(preview)
                    buffer = file.read(buffer_len)
                elif preview.isdigit() == True and buffer.isdigit() == True:
                    finalbuffer += preview + buffer
                    buffer = file.read(buffer_len)
                preview = buffer
                buffer = file.read(buffer_len)
                n+=1
            else:
                preview = buffer
                buffer = file.read(buffer_len)

            tempk = 0
        if a == 1:
            finalbuffer+=preview
        finalbuffer=finalbuffer.replace("0","")
        print(finalbuffer)
except ValueError:
    print("Файл .txt содержит недопустимые символы. Откорректируйте файл text.txt в директории или переименуйте существующий *.txt файл")
except FileNotFoundError:
    print("Файл не обнаружен.Добавьте файл в директорию или переименуйте существующий *.txt файл")
finish=time.time()
print("Время работы программы: ",finish-start," seconds")
