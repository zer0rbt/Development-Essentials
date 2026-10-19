"""Find the two smallest values of each list and save them to result.txt."""

from find_smallest import find_two_smallest
from int_lists import a, b, c, d

if __name__ == "__main__":
    with open("result.txt", "w", encoding="utf-8") as file:
        file.write(f"{a} -> {find_two_smallest(a)}\n")
        file.write(f"{b} -> {find_two_smallest(b)}\n")
        file.write(f"{c} -> {find_two_smallest(c)}\n")
        file.write(f"{d} -> {find_two_smallest(d)}\n")
