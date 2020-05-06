from django.shortcuts import render
import numpy as np

class randomizer():
    def randomize(self, start, n, end=None):
        return np.random.randint(low=start, high=end, size=n)

class sort():
    def swap(self, arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]
        return arr

    def bubble_sort(self, arr):
        n = len(arr)
        swapped = True

        x = -1
        while swapped:
            swapped = False
            x = x + 1
            for i in range(1, n-x):
                if arr[i - 1] > arr[i]:
                    sort.swap(arr, i - 1, i)
                    swapped = True

        return arr  

    def selection_sort(self, arr):
        n = len(arr)
        for i in range(n):
            minimum = i

            for j in range(i + 1, n):
                if arr[j] < arr[minimum]: 
                    minimum = j

            sort.swap(arr, i=minimum, j=i)
        
        return arr

random = randomizer()
sort = sort()

nums = random.randomize(0, 100, 20)

print(nums)               
print(sort.selection_sort(nums))