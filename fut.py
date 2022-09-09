#!/bin/python3
import pyperclip
from colorama import Fore, Back, Style

print("[" + Fore.YELLOW + "?" + Fore.RESET + "] " +
      "Side | " + Fore.CYAN + "(long - l / short - s)" + Fore.RESET)
SIDE = input(Fore.LIGHTRED_EX + ">> " + Fore.RESET)

print(Fore.RED + "---" * 9 + Fore.RESET)
print()
print("[" + Fore.YELLOW + "?" + Fore.RESET + "] " +
      "Percent | " + Fore.CYAN + "(default - 0.089)" + Fore.RESET)
SIZE = float(input(Fore.LIGHTRED_EX + ">> " + Fore.RESET) or "0.089")

print(Fore.RED + "---" * 9 + Fore.RESET)
print()
print("[" + Fore.YELLOW + "?" + Fore.RESET + "] " +
      "Stop-Loss | " + Fore.CYAN + "(default - 0.41)" + Fore.RESET)
PERC = float(input(Fore.LIGHTRED_EX + ">> " + Fore.RESET) or "0.41")

print(Fore.RED + "---" * 9 + Fore.RESET)
print()
print("[" + Fore.YELLOW + "?" + Fore.RESET + "] " +
      "Price | " + Fore.CYAN + "(example: 1011 - ETH/USD)" + Fore.RESET)
POS = float(input(Fore.LIGHTRED_EX + ">> " + Fore.RESET).replace(",", ""))
print(Fore.RED + "---" * 9 + Fore.RESET)


if SIDE == "l":
    long = ((POS * SIZE) / 100 + POS)
    long1 = str(long)
    long2 = long1[0:7]
    print(Fore.YELLOW + "\nLimit Order:" + Fore.RESET)
    print(long2)
    df = pyperclip.copy(long2)
    tt = float(long2)
    stoploss = ((tt * PERC) / 100 - POS)

    tt0 = str(stoploss)

    print(Fore.YELLOW + "\nStop Loss:" + Fore.RESET)
    print(tt0[1:7])

if SIDE == "s":
    short = ((POS * SIZE) / 100 - POS)
    short1 = str(short)
    short2 = short1[1:8]
    print(Fore.YELLOW + "\nLimit Order:" + Fore.RESET)
    print(short2)
    df1 = pyperclip.copy(short2)

    tt = float(short2)
    stoploss1 = ((tt * PERC) / 100 + POS)

    tt1 = str(stoploss1)

    print(Fore.YELLOW + "\nStop Loss:" + Fore.RESET)
    print(tt1[0:7])
