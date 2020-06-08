# coding=utf-8
import numpy as np


class Array(object):
    def __init__(self, number):
        self.array = np.random.randint(-100, 101, size=number)

    def show(self):
        print self.array

    def sort(self):
        self.array.sort()

    def __len__(self):
        return len(self.array)

    def __del__(self):
        print("Deleted object Array contains {}".format(self.array))

    def __getitem__(self, item):
        return self.array[item]

    def __setitem__(self, key, value):
        self.array[key] = value

    def binary_search(self, search):
        mid = len(self.array) // 2
        low = 0
        high = len(self.array) - 1

        while self.array[mid] != search and low <= high:
            if search > self.array[mid]:
                low = mid + 1
            else:
                high = mid - 1
            mid = (low + high) // 2

        if low > high:
            print("No value")
        else:
            print("ID =", mid)
            return mid


array = Array(30)
array.sort()
array.show()
n = int(input("Choose number to search in array: "))
array.binary_search(n)
del array
