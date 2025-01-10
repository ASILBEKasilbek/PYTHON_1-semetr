1
my_list = [3, 1, 4, 1, 5, 9]
my_list.sort()
print(my_list)


2
my_list = [3, 1, 4, 1, 5, 9]
sorted_list = sorted(my_list)
print(sorted_list)


3
import heapq
my_list = [3, 1, 4, 1, 5, 9]
heapq.heapify(my_list)
print(my_list)  # Bu o'sish tartibidagi min-heap bo'ladi


4
import bisect
my_list = [1, 2, 4, 5]
bisect.insort(my_list, 3)  # 3 ni tartibda joylashtiradi
print(my_list)


5
my_list = [3, 1, 4, 1, 5, 9]
sorted_list = sorted(my_list, reverse=False)
print(sorted_list)


6
my_list = [(1, 4), (2, 3), (3, 2)]
sorted_list = sorted(my_list, key=lambda x: x[0])  # Birinchi elementga ko'ra
print(sorted_list)


7
my_list = [3, 1, 4, 1, 5, 9]
for i in range(len(my_list)):
    for j in range(0, len(my_list)-i-1):
        if my_list[j] > my_list[j+1]:
            my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
print(my_list)



8
my_list = [3, 1, 4, 1, 5, 9]
for i in range(1, len(my_list)):
    key = my_list[i]
    j = i - 1
    while j >= 0 and key < my_list[j]:
        my_list[j + 1] = my_list[j]
        j -= 1
    my_list[j + 1] = key
print(my_list)



9
my_list = ['apple', 'banana', 'cherry', 'kiwi']
sorted_list = sorted(my_list, key=lambda x: len(x))  # So'z uzunligiga qarab
print(sorted_list)


10
import numpy as np
my_list = [3, 1, 4, 1, 5, 9]
sorted_list = np.sort(my_list)
print(sorted_list)



11
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

my_list = [64, 25, 12, 22, 11]
selection_sort(my_list)
print(my_list)




12
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

my_list = [12, 11, 13, 5, 6, 7]
merge_sort(my_list)
print(my_list)



13
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less_than_pivot = [x for x in arr[1:] if x <= pivot]
        greater_than_pivot = [x for x in arr[1:] if x > pivot]
        return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)

my_list = [10, 7, 8, 9, 1, 5]
sorted_list = quick_sort(my_list)
print(sorted_list)




14
def shell_sort(arr):
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2

my_list = [12, 34, 54, 2, 3]
shell_sort(my_list)
print(my_list)




15
def counting_sort(arr):
    max_val = max(arr)
    m = max_val + 1
    count = [0] * m

    for a in arr:
        count[a] += 1
    i = 0
    for a in range(m):
        for c in range(count[a]):
            arr[i] = a
            i += 1

my_list = [4, 2, 2, 8, 3, 3, 1]
counting_sort(my_list)
print(my_list)




16
def counting_sort_for_radix(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(len(arr)):
        arr[i] = output[i]

def radix_sort(arr):
    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        counting_sort_for_radix(arr, exp)
        exp *= 10

my_list = [170, 45, 75, 90, 802, 24, 2, 66]
radix_sort(my_list)
print(my_list)






17
def insertion_sort(bucket):
    for i in range(1, len(bucket)):
        up = bucket[i]
        j = i - 1
        while j >= 0 and bucket[j] > up:
            bucket[j + 1] = bucket[j]
            j -= 1
        bucket[j + 1] = up
    return bucket

def bucket_sort(arr):
    max_val = max(arr)
    size = max_val / len(arr)

    buckets = [[] for _ in range(len(arr))]
    for i in range(len(arr)):
        j = int(arr[i] / size)
        if j != len(arr):
            buckets[j].append(arr[i])
        else:
            buckets[len(arr) - 1].append(arr[i])

    for i in range(len(arr)):
        buckets[i] = insertion_sort(buckets[i])

    result = []
    for i in range(len(arr)):
        result = result + buckets[i]

    return result

my_list = [0.897, 0.565, 0.656, 0.123, 0.665, 0.343]
sorted_list = bucket_sort(my_list)
print(sorted_list)





18
class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return TreeNode(key)
    else:
        if root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

def inorder_traversal(root, res):
    if root:
        inorder_traversal(root.left, res)
        res.append(root.val)
        inorder_traversal(root.right, res)

def tree_sort(arr):
    if len(arr) == 0:
        return arr

    root = TreeNode(arr[0])
    for i in range(1, len(arr)):
        insert(root, arr[i])

    res = []
    inorder_traversal(root, res)
    return res

my_list = [5, 4, 7, 2, 11, 8, 6]
sorted_list = tree_sort(my_list)
print(sorted_list)



19
my_list = [3, 1, 4, 1, 5, 9]
my_list.sort()  # Tim Sort ishlatiladi
print(my_list)




20
def comb_sort(arr):
    gap = len(arr)
    shrink = 1.3
    sorted = False

    while not sorted:
        gap = int(gap / shrink)
        if gap > 1:
            sorted = False
        else:
            gap = 1
            sorted = True

        i = 0
        while i + gap < len(arr):
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                sorted = False
            i += 1

my_list = [8, 4, 1, 56, 3, -44, 23, -6, 28, 0]
comb_sort(my_list)
print(my_list)
