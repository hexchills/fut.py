#!/bin/python3

import pandas as pd

print("size. (long - l / short - s)")
SIDE = input("> ")

print("---" * 9)

print("percent. (default - 0.165)")
SIZE = float(input("> ") or "0.165")

print("---" * 9)

print("price. (example: 1011) ETH/USD")
POS = float(input("> ").replace(",", ""))

PERC = 0.85

if SIDE == "l":
    long = ((POS * SIZE) / 100 + POS)
    long1 = str(long)
    long2 = long1[0:7]
    print("\nLimit Order:")
    print(long2)
    df = pd.DataFrame([long2])
    df.to_clipboard(index=False, header=False)
    tt = float(long2)
    stoploss = ((tt * PERC) / 100 - POS)

    tt0 = str(stoploss)

    print("\nStop Loss:")
    print(tt0[1:7])

elif SIDE == "s":
    short = ((POS * SIZE) / 100 - POS)
    short1 = str(short)
    short2 = short1[1:8]
    print("\nLimit Order:")
    print(short2)
    df1 = pd.DataFrame([short2])
    df1.to_clipboard(index=False, header=False)

    tt = float(short2)
    stoploss1 = ((tt * PERC) / 100 + POS)

    tt1 = str(stoploss1)

    print("\nStop Loss:")
    print(tt1[0:7])
