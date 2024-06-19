"""
Selection Sort
Algoritmo inestable, su complejidad en peor/mejor caso es O(n^2).
Tengo que ir barriendo desde un indice j, hasta el ultimo e ir guardando el minimo de ese rango. Si encuentro un minimo lo intercambio con el indice exterior que estoy parado.
"""

def main():
    arr = [2, 3, 10, 15, 4, 9, 12, 13, 50, 48, 43];
    for i in range(0, len(arr)-1):
        min_index = i;
        for k in range(i+1, len(arr)):
            if arr[k] < arr[min_index]:
                min_index = k;
        arr[i], arr[min_index] = arr[min_index], arr[i];
    return arr;

print(main());