'''
Piotr Malinowski
Insert Sort
18.10.23
Źródło: https://www.codingcreativo.it/en/python-insertion-sort/
'''

def insert(n):
    for i in range(1,len(n)):
        j = i
        while n[j] < n[j-1] and j > 0:
            n[j], n[j-1] = n[j-1], n[j]
            j -= 1
    return n

n = [4, 2, 5, 7, 8, 9, 2, 0, 3, 6]
n = insert(n)  
print(f"Posortowane liczby: {n}")

