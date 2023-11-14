def odwracanie_iterative(L, left, right):
    if left < 0 or right >= len(L) or left > right:
        return

    while left < right:
        L[left], L[right] = L[right], L[left]
        left += 1
        right -= 1


def odwracanie_recursive(L, left, right):
    if left < 0 or right >= len(L) or left > right:
        return

    if left < right:
        L[left], L[right] = L[right], L[left]
        odwracanie_recursive(L, left + 1, right - 1)


# example use:
lista = [1, 2, 3, 4, 5, 6, 7]
odwracanie_iterative(lista, 2, 5)
print("list after switching:", lista)
odwracanie_recursive(lista, 2, 5)
print("list after switching again:", lista)
