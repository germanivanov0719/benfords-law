import os
import sys

from Factorial import factorial


def blockPrint():
    sys.stdout = open(os.devnull, "w", encoding="utf-8")


def sum_squares(a: int, b: int) -> int:
    return (b + 3 * b**2 + 2 * b**3 - a + 3 * a**2 - 2 * a**3) // 6


def enablePrint():
    sys.stdout = sys.__stdout__


def Benfords_Law(start: int, end: int, silent: bool = False) -> bool:
    r = [0] * 10
    fact = factorial(start)
    for i in range(start, end):
        r[int(str(fact)[0]) - 1] += 1
        if not silent:
            print(
                f"{int(sum_squares(start, i) / sum_squares(start, end) * 100)}% done ({start}…{i}/{start}…{end}){' '*10}",
                sep="",
                end="\r",
            )
        fact *= i + 1
    if not silent:
        print("Total: ", r, sep="")
    for i in range(9):
        if r[i] <= r[i + 1]:
            if not silent:
                print("We couldn't prove Benford's law, try larger numbers.")
            return False
    if not silent:
        print("Benford's law proved!")
    return True


if __name__ == "__main__":
    Benfords_Law(int(input("Start: ")), int(input("End: ")))
