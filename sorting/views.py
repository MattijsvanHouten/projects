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

    def insertion_sort(self, arr):
        n = len(arr)
        for i in range(n):
            cursor = arr[i]
            pos = i

            while pos > 0 and arr[pos - 1] > cursor:
                arr[pos] = arr[pos - 1]
                pos = pos - 1

            arr[pos] = cursor

        return arr

    def merge_sort(self, arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            left = arr[:mid]
            right = arr[mid:]

            #    on each half
            merge_sort(left)
            merge_sort(right)

            # Two iterators for traversing the two halves
            i = 0
            j = 0
            
            # Iterator for the main list
            k = 0
            
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                  # The value from the left half has been used
                  arr[k] = left[i]
                  # Move the iterator forward
                  i += 1
                else:
                    arr[k] = right[j]
                    j += 1
                # Move to the next slot
                k += 1

            # For all the remaining values
            while i < len(left):
                arr[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                arr[k]=right[j]
                j += 1
                k += 1




random = randomizer()
sort = sort()

nums = random.randomize(start=0, n=12, end=100)

print(nums)               
print(sort.merge_sort(nums))