import random
import time

def print_matrix(M, matr_name, tt):
    print("матрица " + matr_name + " промежуточное время = " + str(format(tt, '0.2f')) + " seconds.")
    for i in M: # делаем перебор всех строк матрицы
        for j in i: # перебираем все элементы в строке
            print("%5d" % j, end=' ')
        print()

print("\n-----Результат работы программы-------")
try:
    row_q = int(input("Введите количество строк (столбцов) квадратной матрицы в интервале от 6 до 100:"))
    while row_q < 6 or row_q > 100:
        row_q = int(input(
            "Вы ввели неверное число\nВведите количество строк (столбцов) квадратной матрицы в интервале от 6 до 100:"))
    K = int(input("Введите число К="))
    start = time.time()
    A, F, AF, AT = [], [], [], []  # задаем матрицы
    for i in range(row_q):
        A.append([0] * row_q)
        F.append([0] * row_q)
        AF.append([0] * row_q)
        AT.append([0] * row_q)
    time_next = time.time()
    print_matrix(F, "F", time_next - start)

    for i in range(row_q):                                   # заполняем матрицу А
        for j in range(row_q):
            A[i][j] = random.randint(-10, 10)

    time_prev = time_next
    time_next = time.time()
    print_matrix(A, "A", time_next - time_prev)
    for i in range(row_q):  # F
        for j in range(row_q):
            F[i][j] = A[i][j]
    time_prev = time_next
    time_next = time.time()
    print_matrix(F, "F", time_next - time_prev)

    C = []                                                   # задаем матрицу C
    size = row_q // 2
    for i in range(size):
        C.append([0] * size)

    for i in range(size):                                    # формируем подматрицу С
        for j in range(size):
            C[i][j] = F[size + row_q % 2 + i][size + row_q % 2 + j]
    time_prev = time_next
    time_next = time.time()
    print_matrix(C, "C", time_next - time_prev)



    kolv = 0
    nul = 0
    for i in range(size):                                        # обработка матрицы C
        for j in range(size):
            if i > size - j - 1 and i > j and i % 2 == 1 and C[i][j]==0:
                nul+=1
                #print(C[i][j],"3")
            elif i < j and i > size - j - 1 and j % 2 == 0 and C[i][j] % 2 == 1 and C[i][j] != 9 :
                kolv += 1
                #print(C[i][j],"2")

    print("кол-во нулей = ", nul)
    print("кол-во простых чисел = ", kolv)


    if kolv>nul:                                                         # формируем F по условию
        print(
            "количество простых чисел в нечетных столбцах в области 2 больше, чем количество нулевых  элементов в четных строках в области 3, поэтому меняем в С симметрично области 1 и 3 местами")
        for i in range(size + row_q % 2 + 1, row_q, 1):
            for j in range(size + row_q % 2 + 1, row_q, 1):
                if (i - size - row_q % 2) > (j - size - row_q % 2) and (i - size - row_q % 2) > size - (j - size - row_q % 2) - 1:
                    buffer = F[i][j]
                    F[i][j] = F[size-i-1][j]
                    F[size-i-1][j] = buffer
    else:
        print(
            "количество простых чисел в нечетных столбцах в области 2 меньше, чем количество нулевых  элементов в четных строках в области 3, поэтому меняем в С симметрично области 1 и 3 местами")
        for j in range(row_q // 2 + row_q % 2, row_q, 1):
            for i in range(row_q // 2):
                F[i][j], F[row_q // 2 + row_q % 2 + i][j] = F[row_q // 2 + row_q % 2 + i][j], F[i][j]
    time_prev = time_next
    time_next = time.time()
    print_matrix(F, "Измененная F", time_next - time_prev)

                                                                           # (К*A)*F– (K * A^T)
    print_matrix(A, "A", 0)

    for i in range(row_q):  # A^T
        for j in range(i, row_q, 1):
            AT[i][j], AT[j][i] = A[j][i], A[i][j]
    time_prev = time_next
    time_next = time.time()
    print_matrix(AT, "A^T", time_next - time_prev)

    for i in range(row_q):                 # K * A^T
        for j in range(row_q):
            AT[i][j] = K * AT[i][j]
    time_prev = time_next
    time_next = time.time()
    print_matrix(AT, "K*A^T", time_next - time_prev)

    for i in range(row_q):                  # K*A
        for j in range(row_q):
            A[i][j] = K * A[i][j]
    time_prev = time_next
    time_next = time.time()
    print_matrix(A, "K*A", time_next - time_prev)

    for i in range(row_q):                     # K*A*F
        for j in range(row_q):
            s = 0
            for m in range(row_q):
                s = s + A[i][m] * F[m][j]
            AF[i][j] = s
    time_prev = time_next
    time_next = time.time()
    print_matrix(AF, "K*A*F", time_next - time_prev)

#

    for i in range(row_q):                     # (К*A)*F – (K * AT)
        for j in range(row_q):
            AF[i][j] = AF[i][j] - AT[i][j]
    time_prev = time_next
    time_next = time.time()
    print_matrix(AF, "(К*A)*F – (K * A^T)", time_next - time_prev)

    finish = time.time()
    result = finish - start
    print("Program time: " + str(result) + " seconds.")


except ValueError:
    print("\nэто не число")
