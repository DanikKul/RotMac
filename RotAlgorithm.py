from math import floor
from tkinter import *
from tkinter import scrolledtext
import random


incorrect = 'ДОРОГУША МОЯ!'
quotes = ['ОБ ЭТОМ Я ПОГОВОРЮ С ВАМИ НА СЕССИИ',
          'Чистилище не за горами',
          'Компиляторов начальник\n и АиЛОВТа командир',
          'Верю во всевидящий ноль',
          'КСиС, это выше, чем БГУИР',
          'Деятельность: Люблю компилировать',
          'Интересы: Отчислять студентов',
          'Те, кто знают, могли бы\n предвосхитить, а я предупреждаю!',
          'О себе:0,110101110101,010\n'
          '11101010100010011011001 10101010110.\n'
          '0101010100110111010110011010101101010101 ',
          'Сессия - моя любимая пора...',
          'Пройдемте на отчисление',
          'У меня мозг десятичный\n'
          'А че два показываете?\n'
          'Мозг же десятичный',
          'Программистов, как и разведчиков,\n'
          ' бывших не бывает.',
          'Каждый просто должен определиться с\n'
          ' областью, где он Рембрандт.',
          'Там двоичная система оценки:\n'
          ' либо девять либо три.',
          'Понимаете, на листочке бумаги с \n'
          '“компилятором Луцик” легче разговаривать,\n'
          ' чем с компилятором Microsoft.',
          'Главное ― не оставляйте ничего на потом,\n потома не будет',
          'Что тут непонятного, даже я понял']


def clicked():
    l_string = txt.get()
    n_string = txt1.get()
    if l_string == '':
        lbl1.configure(text="Неверно введены значения")
        label1.configure(text=incorrect)
        return
    for letter in l_string:
        if letter != ' ' and letter != '0' and letter != '1' and letter != 'x':
            lbl1.configure(text="Неверно введены значения")
            label1.configure(text=incorrect)
            return
    for letter in n_string:
        if letter != ' ' and letter != '0' and letter != '1' and letter != 'x':
            lbl1.configure(text="Неверно введены значения")
            label1.configure(text=incorrect)
            return
    l_list = l_string.split()
    inp = len(l_list[0])
    for elem in l_list:
        if len(elem) != inp:
            lbl1.configure(text="Неверно введены значения")
            label1.configure(text=incorrect)
            return
    n_list = n_string.split()
    for elem in n_list:
        if len(elem) != inp:
            lbl1.configure(text="Неверно введены значения")
            label1.configure(text=incorrect)
            return
    for elem in l_list:
        if elem in n_list:
            lbl1.configure(text="Неверно введены значения")
            label1.configure(text=incorrect)
            return
    lbl1.configure(text="Значения введены верно")
    label1.configure(text=(quotes[floor(random.random() * 18)] + '\n' + "©BY LUCIK"))
    try:
        font_size = int(txt2.get())
    except TypeError:
        font_size = 10
    scr_txt.configure(font=("Courier New", font_size),
                      width=round(250 / font_size * 10),
                      height=round(55 / font_size * 10))
    print(150 / font_size, 55 / font_size)
    rot_algo(l_list, n_list, inp)


def rot_algo(array1, array2, inputs):
    def multiplication(x1, x2):
        res = []
        for ind in range(len(x1)):
            if x1[ind] == x2[ind]:
                res.append(x1[ind])
            elif x1[ind] != x2[ind] and x1[ind] != 'x' and x2[ind] != 'x':
                res.append('y')
            elif x1[ind] != x2[ind] and x1[ind] == 'x' and x2[ind] != 'x':
                res.append(x2[ind])
            elif x1[ind] != x2[ind] and x1[ind] != 'x' and x2[ind] == 'x':
                res.append(x1[ind])
        return ''.join(res)

    def multiplication_table(arr1, arr2):
        res = []
        for ind in range(len(arr2)):
            res.append([])
        for ind in range(len(arr2)):
            for ind1 in range(len(arr1)):
                res[ind].append(multiplication(arr2[ind], arr1[ind1]))
        string_null = '-' * inputs
        for ind in range(len(arr2)):
            ind1 = ind
            while ind1 < len(arr1):
                res[ind][ind1] = string_null
                ind1 += 1
        return res

    def get_set_a(mult_table, mini, maxim):
        res = []
        for ind in range(len(mult_table)):
            for ind1 in range(len(mult_table[0])):
                counter = mult_table[ind][ind1].count('x') + mult_table[ind][ind1].count('y')
                if mult_table[ind][ind1].count('y') > 1:
                    continue
                if maxim + 1 >= counter >= mini + 1:
                    res.append(mult_table[ind][ind1])
        for ind in range(len(res) - 1):
            ind1 = ind + 1
            while ind1 < len(res):
                if res[ind] == res[ind1]:
                    res.pop(ind1)
                ind1 += 1
        for ind in range(len(res)):
            res[ind] = res[ind].replace('y', 'x')
        return res

    def get_set_b(set_c, set_z):
        res = []
        for ind in set_c:
            if ind not in set_z:
                res.append(ind)
        return res

    def get_set_z(mult_table, set_c, set_a):
        set_z = []
        for ind in range(len(mult_table[0])):
            new_arr_x = []
            new_arr_y = []
            for ind1 in range(len(mult_table)):
                if mult_table[ind1][ind].count('y') < 2:
                    new_arr_y.append(mult_table[ind1][ind].replace('y', 'x'))
                else:
                    new_arr_y.append('-' * inputs)
            for ind1 in range(len(mult_table[0])):
                if mult_table[ind][ind1].count('y') < 2:
                    new_arr_x.append(mult_table[ind][ind1].replace('y', 'x'))
                else:
                    new_arr_x.append("-" * inputs)
            flag = False
            for ind2 in range(len(set_a)):
                if set_a[ind2] in new_arr_x:
                    flag = True
                if set_a[ind2] in new_arr_y:
                    flag = True
            if not flag:
                set_z.append(set_c[ind])
        return set_z

    def maximum(arr):
        res = 0
        for item in arr:
            cur = item.count('x')
            if cur > res:
                res = cur
        return res

    def minimum(arr):
        res = 10
        for item in arr:
            cur = item.count('x')
            if cur < res:
                res = cur
        return res

    def are_same(x1, x2):
        for ind in range(len(x1)):
            if x1[ind] == x2[ind] or x2[ind] == 'x':
                continue
            else:
                return False
        return True

    def unite_sets(arr1, arr2):
        res = []
        for ind in range(len(arr1)):
            flag = False
            for ind1 in range(len(arr2)):
                if are_same(arr1[ind], arr2[ind1]):
                    flag = True
            if not flag:
                res.append(arr1[ind])

        for ind in arr2:
            res.append(ind)
        return res

    def additional_cubes(set_c, set_z, amount):
        res = []
        ind = 0
        while ind < len(set_z):
            if len(set_z) < ind or len(set_c) < ind:
                break
            if amount == set_z[ind].count('x') and set_z[ind] in set_c:
                res.append(set_z[ind])
                set_z.pop(ind)
            ind += 1
        return res

    def delete_duplicates(arr):
        new_arr = []
        for item in arr:
            if item not in new_arr:
                new_arr.append(item)
        return new_arr

    print("\nЭТАП УМНОЖЕНИЯ КУБОВ (C * C)\n")
    dashes = '-' * inputs
    scr_txt.delete(0.0, END)
    scr_txt.insert(INSERT, "ЭТАП УМНОЖЕНИЯ КУБОВ (C * C)\n")
    set_a1 = [0]
    set_c1 = unite_sets(array1, array2)
    minim = minimum(set_c1) + 1
    cubes = []
    full_set_z = []
    while set_a1:
        table = multiplication_table(set_c1, set_c1 + cubes)
        print("\nРезультат умножения")
        scr_txt.insert(INSERT, "\nРезультат умножения\n")
        print("-" * inputs, set_c1)
        tmp_str = ' '.join(set_c1)
        scr_txt.insert(INSERT, ' ' + dashes)
        scr_txt.insert(INSERT, '| ' + tmp_str)
        scr_txt.insert(INSERT, '\n')
        am = 0
        for i in range(len(table)):
            if len(set_c1) > i:
                print(set_c1[i], table[i])
                scr_txt.insert(INSERT, ' ' + set_c1[i])
                tmp_str = ' '.join(table[i])
                scr_txt.insert(INSERT, '| ' + tmp_str)
                scr_txt.insert(INSERT, '\n')
            else:
                print(cubes[am], table[i])
                scr_txt.insert(INSERT, ' ' + cubes[am])
                tmp_str = ' '.join(table[i])
                scr_txt.insert(INSERT, '| ' + tmp_str)
                scr_txt.insert(INSERT, '\n')
                am += 1
        set_a1 = delete_duplicates(get_set_a(table, minimum(set_c1), maximum(set_c1)))
        print("\nМножество А:", set_a1)
        tmp_str = ' '.join(set_a1)
        scr_txt.insert(INSERT, '\nМножество А:' + tmp_str + '\n')
        if not set_a1:
            full_set_z += cubes
        set_z1 = delete_duplicates(get_set_z(table, set_c1, set_a1))
        print("\nМножество Z:", set_z1)
        tmp_str = ' '.join(set_z1)
        scr_txt.insert(INSERT, '\nМножество Z:' + tmp_str + '\n')
        set_b1 = delete_duplicates(get_set_b(set_c1, set_z1))
        print("\nМножество B:", set_b1)
        tmp_str = ' '.join(set_b1)
        scr_txt.insert(INSERT, '\nМножество B:' + tmp_str + '\n')
        cubes = delete_duplicates(additional_cubes(set_c1, set_z1, minim))
        print("\nДополнительные кубы:", cubes)
        tmp_str = ' '.join(cubes)
        scr_txt.insert(INSERT, '\nДополнительные кубы:' + tmp_str + '\n')
        set_c1 = delete_duplicates(unite_sets(set_b1, set_a1))
        print("\nМножество C:", set_c1)
        tmp_str = ' '.join(set_c1)
        scr_txt.insert(INSERT, '\nМножество C:' + tmp_str + '\n')
        full_set_z += set_z1
        minim += 1
        scr_txt.insert(INSERT, '\n\n\n')
    full_set_z = delete_duplicates(full_set_z)
    print("\nКонечное множество Z:", full_set_z)
    tmp_str = ' '.join(full_set_z)
    scr_txt.insert(INSERT, '\nКонечное множество Z:' + tmp_str + '\n')
    review = []

    def substraction(set_z):
        result = []
        x = []
        for ind in range(len(set_z)):
            print("\nСледующее вычитание:", set_z[ind])
            scr_txt.insert(INSERT, "\nСледующее вычитание: " + set_z[ind] + '\n')
            tmp = set_z[ind]
            for ind1 in range(len(set_z)):
                if ind == ind1:
                    continue
                else:
                    x = sub(tmp, set_z[ind1])
                    print("Остаток:", x)
                    if x[0] is None:
                        tmp_st = 'Нет остатка'
                    else:
                        tmp_st = ' '.join(x)
                    scr_txt.insert(INSERT, "Остаток: " + tmp_st + '\n')
                    if len(x) == 1:
                        if x[0] is None:
                            break
                        else:
                            tmp = x[0]
                    else:
                        buff = x
                        for ind3 in range(len(x)):
                            ind2 = ind1
                            tmp = buff[ind3]
                            while ind2 < len(set_z):
                                if x[0] is None:
                                    break
                                if ind2 == ind:
                                    ind2 += 1
                                    continue
                                if ind3 >= len(x):
                                    break
                                x = sub(tmp, set_z[ind2])
                                tmp = x[ind3]
                                ind2 += 1
                            if x[0] is not None:
                                review.append([x, ind])
                            result += x
            print(x)
            if x and x[0] is not None:
                review.append([x, ind])
            result += x
        return result

    def replacer(s, newstring, index, nofail=False):
        if not nofail and index not in range(len(s)):
            raise ValueError("index outside given string")
        if index < 0:
            return newstring + s
        if index > len(s):
            return s + newstring
        return s[:index] + newstring + s[index + 1:]

    def sub(x1, x2):
        print("Дано:", x1, "#", x2)
        scr_txt.insert(INSERT, "Дано:" + x1 + '#' + x2 + '\n')
        res = []
        for ind in range(len(x1)):
            if x1[ind] == x2[ind]:
                res.append('z')
            elif x1[ind] != x2[ind] and x1[ind] == 'x':
                if x2[ind] == '0':
                    res.append('1')
                else:
                    res.append('0')
            elif x1[ind] != x2[ind] and x2[ind] == 'x':
                res.append('z')
            else:
                res.append('y')
        print("Результат вычитания:", ''.join(res))
        scr_txt.insert(INSERT, "Результат вычитания:" + ''.join(res) + '\n')
        if 'y' in res:
            return [x1]
        count_nums = 0
        count_z = 0
        for ind in res:
            if ind == 'z':
                count_z += 1
            elif ind == '1' or ind == '0':
                count_nums += 1
        if count_z == len(res):
            return [None]
        else:
            ret = []
            prev_ind = 0
            for ind in range(count_nums):
                tmp = x1
                ret.append([])
                ind1 = prev_ind
                while ind1 < len(tmp):
                    if res[ind1] == '1':
                        tmp = replacer(tmp, '1', ind1)
                        ret[ind].append(tmp)
                        prev_ind = ind1 + 1
                        break
                    elif res[ind1] == '0':
                        tmp = replacer(tmp, '0', ind1)
                        ret[ind].append(tmp)
                        prev_ind = ind1 + 1
                        break
                    ind1 += 1
            return sum(ret, [])

    def get_set_e(rev, set_z):
        set_e = []
        for ind in range(len(rev)):
            set_e.append(set_z[rev[ind][1]])
        return set_e

    print("\nВЫЧИТАНИЕ КУБОВ (z#(Z-z))\n")
    scr_txt.insert(INSERT, "\nВЫЧИТАНИЕ КУБОВ (z#(Z-z))\n" + '\n')
    subs_set = delete_duplicates(substraction(full_set_z))
    i = 0
    while i < len(subs_set):
        if subs_set[i] is None:
            i -= 1
            subs_set.remove(None)
        i += 1
    review = delete_duplicates(review)
    print("\nМножество Z:", full_set_z)
    tmp_str = ' '.join(full_set_z)
    scr_txt.insert(INSERT, "\nМножество Z:" + tmp_str + '\n')
    print("\nОстатки с индексами:", review)
    set_e1 = delete_duplicates(get_set_e(review, full_set_z))
    print("\nМножество Е:", set_e1)
    tmp_str = ' '.join(set_e1)
    scr_txt.insert(INSERT, "\nМножество E:" + tmp_str + '\n')

    def table_intersection(set_l, set_rem):
        res = []
        for ind in range(len(set_l)):
            res.append([])
        for ind in range(len(set_l)):
            for ind1 in range(len(set_rem)):
                res[ind].append(intersection(set_l[ind], set_rem[ind1][0][0]))
        return res

    def intersection(x1: str, x2: str):
        res = []
        for ind in range(len(x1)):
            if x1[ind] != x2[ind] and x1[ind] != 'x' and x2[ind] != 'x':
                return None
            elif x1[ind] == x2[ind]:
                res.append(x1[ind])
            elif x1[ind] != x2[ind] and x1[ind] == 'x':
                if x2[ind] == '1':
                    res.append('1')
                elif x2[ind] == '0':
                    res.append('0')
            elif x1[ind] != x2[ind] and x2[ind] == 'x':
                if x1[ind] == '1':
                    res.append('1')
                elif x1[ind] == '0':
                    res.append('0')
        return ''.join(res)

    def ret_same(x1, x2):
        res = []
        for ind in range(len(x1)):
            if x1[ind] == x2[ind] or x2[ind] == 'x' or x1[ind] == 'x':
                res.append(x1[ind])
            else:
                return False
        return ''.join(res)

    def get_rest(set_rem, rem, set_z):
        res = []
        for ind in range(len(set_rem)):
            for ind1 in range(len(rem)):
                if ret_same(rem[ind1], set_rem[ind][0][0]):
                    res.append(set_z[set_rem[ind][1]])
                    continue
        return res

    print("\nПЕРЕСЕЧЕНИЕ КУБОВ (z#(Z - z) ⋂ L)\n")
    scr_txt.insert(INSERT, "\nПЕРЕСЕЧЕНИЕ КУБОВ (z#(Z - z) ⋂ L)\n" + '\n')
    table1 = table_intersection(array1, review)
    rem1 = []
    for i in range(len(table1)):
        for j in range(len(table1[0])):
            if table1[i][j] is not None:
                rem1.append(table1[i][j])
    print("\nТаблица пересечения:")
    scr_txt.insert(INSERT, "\nТаблица пересечения:" + '\n')
    for i in range(len(table1)):
        print(array1[i], table1[i])
        tmp_str = ''
        for item in table1[i]:
            if item is None:
                tmp_str += "None "
            else:
                tmp_str += item + ' '
        scr_txt.insert(INSERT, array1[i] + '| ' + tmp_str + '\n')
    set_e1 = delete_duplicates(get_rest(review, rem1, full_set_z))
    print("\nМножество Е:", set_e1)
    tmp_str = ' '.join(set_e1)
    scr_txt.insert(INSERT, "\nМножество Е:" + tmp_str + '\n')

    def substraction1(set_l, set_e):
        result = []
        x = []
        for ind in range(len(set_l)):
            print("\nСледующее вычитание:", set_l[ind])
            scr_txt.insert(INSERT, "\nСледующее вычитание: " + set_l[ind] + '\n')
            tmp = set_l[ind]
            for ind1 in range(len(set_e)):
                x = sub(tmp, set_e[ind1])
                print("Остаток:", x)
                if x[0] is None:
                    tmp_st = 'Нет остатка'
                else:
                    tmp_st = ' '.join(x)
                scr_txt.insert(INSERT, "Остаток: " + tmp_st + '\n')
                if len(x) == 1:
                    if x[0] is None:
                        break
                    else:
                        tmp = x[0]
                else:
                    buff = x
                    for m in range(len(x)):
                        k = ind1
                        tmp = buff[m]
                        while k < len(set_e):
                            if x[0] is None:
                                break
                            if m >= len(x):
                                break
                            x = sub(tmp, set_e[k])
                            tmp = x[m]
                            k += 1
                        if x[0] is not None:
                            review.append([x, ind])
                        result += x
            if x and x[0] is not None:
                review.append([x, ind])
            result += x
        return result

    def get_uncovered_set(uncovered):
        res = []
        for item in uncovered:
            if item is not None:
                res.append(item)
        return res

    uncovered_set = get_uncovered_set(substraction1(array1, set_e1))
    print("\nНепокрытые остатки:", uncovered_set)
    if not uncovered_set:
        tmp_st = 'Нет непокрытых остатков'
    elif uncovered_set[0] is None:
        tmp_st = 'Нет непокрытых остатков'
    else:
        tmp_st = ' '.join(uncovered_set)
    scr_txt.insert(INSERT, "\nНепокрытые остатки: " + tmp_st + '\n')

    def get_new_set_z(set_z, set_e):
        res = []
        for item in set_z:
            if item not in set_e:
                res.append(item)
        return res

    def table_intersection1(set_l, set_rem):
        res = []
        for ind in range(len(set_l)):
            res.append([])
        for ind in range(len(set_l)):
            for ind1 in range(len(set_rem)):
                res[ind].append(intersection(set_l[ind], set_rem[ind1]))
        return res

    print("\nПЕРЕСЕЧЕНИЕ МНОЖЕСТВА Z И ОСТАТКОВ\n")
    scr_txt.insert(INSERT, "\nПЕРЕСЕЧЕНИЕ МНОЖЕСТВА Z И ОСТАТКОВ\n " + '\n')
    full_set_z = get_new_set_z(full_set_z, set_e1)
    print("Новое множество Z", full_set_z, "\n")
    tmp_str = ' '.join(full_set_z)
    scr_txt.insert(INSERT, "Новое множество Z: " + tmp_str + '\n')
    table = table_intersection1(full_set_z, uncovered_set)
    print('-' * inputs, uncovered_set)
    tmp_str = ' '.join(uncovered_set)
    scr_txt.insert(INSERT, dashes + '| ' + tmp_str + '\n')
    for i in range(len(table)):
        print(full_set_z[i], table[i])
        tmp_str = ''
        for item in table[i]:
            if item is None:
                tmp_str += "None "
            else:
                tmp_str += item + ' '
        scr_txt.insert(INSERT, full_set_z[i] + '| ' + tmp_str + '\n')
    print("\nМножество Е:", set_e1)
    tmp_str = ' '.join(set_e1)
    scr_txt.insert(INSERT, "\nМножество Е:" + tmp_str + '\n')
    func_list = []

    def get_func(tab, ind2, arr, iml):
        if ind2 >= len(tab[0]):
            tmp = []
            for x in arr:
                tmp.append(x)
            func_list.append(tmp)
            return
        for ind in range(len(tab)):
            if tab[ind][ind2] is not None:
                arr.append(iml[ind])
                get_func(tab, ind2 + 1, arr, iml)
                arr.pop()

    out = []
    if table:
        get_func(table, 0, out, full_set_z)

    if not set_e1:
        set_e1 = full_set_z

    for i in range(len(func_list)):
        func_list[i] = delete_duplicates(func_list[i])

    for i in range(len(func_list)):
        for j in range(len(set_e1)):
            func_list[i].append(set_e1[j])

    flag = False
    if not func_list:
        flag = True
        func_list.append([])
        for i in range(len(set_e1)):
            func_list[0].append(set_e1[i])

    for i in range(len(func_list)):
        for j in range(len(func_list[i])):
            string = ''
            for k in range(len(func_list[i][j])):
                if func_list[i][j][k] == '0':
                    string += ''.join('!' + f'x{k + 1}')
                elif func_list[i][j][k] == '1':
                    string += ''.join(f'x{k + 1}')
            func_list[i][j] = string

    print("\nИТОГОВЫЕ ФУНКЦИИ\n")
    scr_txt.insert(INSERT, "\nИТОГОВЫЕ ФУНКЦИИ\n" + '\n')

    print(func_list)
    if not flag:
        for i in range(len(func_list)):
            string = ''
            for j in range(len(func_list[i])):
                if j != len(func_list[i]):
                    string += ''.join(func_list[i][j] + ' v ')
                else:
                    string += ''.join(func_list[i][j])
            if string and string[-2] == 'v':
                string = string[:-2]
            print(f"F{i + 1} =", string)
            scr_txt.insert(INSERT, f"\n\nF{i + 1} =" + ' ' + string + '\n')
    else:
        string = 'F = '
        for i in range(len(func_list[0])):
            if i + 1 != len(func_list[0]):
                string += ''.join(func_list[0][i] + ' v ')
            else:
                string += ''.join(func_list[0][i])
        scr_txt.insert(INSERT, '\n' + string + '\n')
        print(string)


window = Tk()
window.state('zoomed')
window.title("Rot's Algorithm")
window.configure(background="#2e3032")
lbl = Label(window,
            text="Алгоритм Рота",
            font=("Arial Bold", 30),
            height=1, width=14,
            background="#2e3032",
            foreground='white')
lbl.place(x=20, y=0)
lbl = Label(window,
            text="Введите данные в таком формате",
            font=("Arial Bold", 13),
            height=1,
            width=29,
            background="#2e3032",
            foreground='white')
lbl.place(x=20, y=40)
lbl = Label(window,
            text="00x00 1x111 xx101 00010",
            font=("Courier New", 15),
            height=1,
            width=22,
            background="#202020",
            foreground='white')
lbl.place(x=23, y=70)
lbl = Label(window,
            text="L-наборы",
            font=("Arial Bold", 15),
            height=1,
            width=12,
            background="#2e3032",
            foreground='white')
lbl.place(x=20, y=120)
txt = Entry(window,
            width=25,
            font=("Courier New", 14),
            background="#202020",
            foreground='white')
txt.place(x=20, y=150)
lbl = Label(window,
            text="N-наборы",
            font=("Arial Bold", 15),
            height=1,
            width=12,
            background="#2e3032",
            foreground='white')
lbl.place(x=20, y=190)
txt1 = Entry(window,
             width=25,
             font=("Courier New", 14),
             background="#202020",
             foreground="white")
txt1.place(x=20, y=220)
lbl1 = Label(window,
             text="",
             font=("Arial Bold", 15),
             height=1,
             width=24,
             background="#2e3032",
             foreground='white')
lbl1.place(x=20, y=330)
lbl2 = Label(window,
             text="Размер шрифта",
             font=("Arial Bold", 15),
             height=1,
             width=14,
             background="#2e3032",
             foreground='white')
lbl2.place(x=20, y=264)
txt2 = Entry(window,
             width=6,
             background="#202020",
             foreground="white")
txt2.place(x=191, y=263)
txt2.insert(INSERT, '10')
btn = Button(window,
             text="Готово",
             font=("Arial Bold", 15),
             height=1,
             width=22,
             command=clicked,
             background='#202020',
             foreground='white',
             activebackground='#202020',
             bg="gray",
             fg="black",
             relief="ridge")
btn.place(x=21, y=360)
font_size = 10
scr_txt = scrolledtext.ScrolledText(window,
                                    width=round(250 / font_size * 10),
                                    height=round(55 / font_size * 10),
                                    font=("Courier New", 10),
                                    background='#202020',
                                    foreground='white')
scr_txt.place(x=280, y=0)
scr_txt.insert(INSERT, 'Здесь будет решение')
label1 = Label(window,
               text='ОБ ЭТОМ Я ПОГОВОРЮ С ВАМИ НА СЕССИИ',
               font=("Arial Bold", 10),
               foreground='white',
               background='#2e3032')
label1.place(x=20, y=400)
window.mainloop()
