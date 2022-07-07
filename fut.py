#!/bin/python3
#!/bin/bash

import sys
import pandas as pd


def Script():
    POS = float(sys.argv[3])
    SIDE = sys.argv[1]
    SIZE = float(sys.argv[2])
    PERC = 0.85
    if SIDE == "-l":
        long = ((POS * SIZE) / 100 + POS)
        long1 = str(long)
        long2 = long1[0:7]
        print(long2)
        df = pd.DataFrame([long2])
        df.to_clipboard(index=False, header=False)
        tt = float(long2)
        stoploss = ((tt * PERC) / 100 - POS)

        tt0 = str(stoploss)

        print("\nStop Loss:")
        print(tt0[1:7])

    elif SIDE == "-s":
        short = ((POS * SIZE) / 100 - POS)
        short1 = str(short)
        short2 = short1[1:8]
        print(short2)
        df1 = pd.DataFrame([short2])
        df1.to_clipboard(index=False, header=False)

        tt = float(short2)
        stoploss1 = ((tt * PERC) / 100 + POS)

        tt1 = str(stoploss1)

        print("\nStop Loss:")
        print(tt1[0:7])


try:
    Script()
except IndexError:
    print("Первый аргумент: (Сторона позиции) \n\tПример: -l (long) / -s (short)")
    print()
    print("Второй аргумент: (Процент от цены входа): \n\tПример: 0.19 (Процент который нужно добавить к цене входа, если заходим в long позицию ИЛИ отнимаем 0.19% от цены входа, если заходим в -s (short)) ")
    print()
    print("Третий аргумент: (Цена входа) \n\tПример: 1001 (цена в USD / ETH)")
    print("---" * 15)
    print("Пример работы скрипта:")
    print("fut -l 0.20 1100 (заходим в лонг, добавляем к цене входа 0.20%, цена входа: 1100)")
    print("Итого: 1102.2")
    print("fut -s 0.20 1100 (всё тоже самое, только отнимаем от цены входа 0.20%)")
    print("Итого: 1097.8")
