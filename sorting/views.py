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

    def merge(self, left, right, merged):

        left_cursor, right_cursor = 0, 0
        while left_cursor < len(left) and right_cursor < len(right):
          
            # Sort each one and place into the result
            if left[left_cursor] <= right[right_cursor]:
                merged[left_cursor+right_cursor]=left[left_cursor]
                left_cursor += 1
            else:
                merged[left_cursor + right_cursor] = right[right_cursor]
                right_cursor += 1
                
        for left_cursor in range(left_cursor, len(left)):
            merged[left_cursor + right_cursor] = left[left_cursor]
            
        for right_cursor in range(right_cursor, len(right)):
            merged[left_cursor + right_cursor] = right[right_cursor]

        return merged

    def merge_sort(self, arr):
        # The last array split
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        # Perform merge_sort recursively on both halves
        left, right = self.merge_sort(arr[:mid]), self.merge_sort(arr[mid:])

        # Merge each side together
        return self.merge(left, right, arr.copy())


    



random = randomizer()
sort = sort()

nums = random.randomize(start=0, n=12, end=100)
print(nums)             
print(sort.merge_sort(nums))
