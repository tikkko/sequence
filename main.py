
import statistics

def sequence(i, f, g):
    s = int(input('Введіть ціле число '))
    while s > 0:
        i.append(s)
        s = int(input('Введіть ціле число '))
        if s % 2 == 0:
            f.append(s)
        else:
            g.append(s)
    else:
        print('Кількість введених чисел:', len(i))
        print('Сума введених чисел:', sum(i))
        print('Середнє арифметичне всіх введених чисел:', statistics.mean(i))
        print('Мінімум', min(i), 'Максимум', max(i))
        print(len(f), 'Парних')
        print(len(g), 'Непраних')


if __name__ == '__main__':
    print(sequence([], [], []))

