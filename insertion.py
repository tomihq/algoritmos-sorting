"""
Insertion Sort
Algoritmo estable, su complejidad en peor caso es O(n^2) (esta todo desordenado) y el mejor caso es O(n) cuando ya está ordenado.
Tengo que ir comparando cada elem con todos los anteriores, y si encontre uno que es menor, entonces tengo que ir swappeando.
[3, 2, 1] => [3, 1, 2] => [1, 3, 2] => [1, 2, 3]
"""

def main():
    arr = [3, 2, 1];
    i = 1;
    while(i<len(arr)):
        j = i
        while(j>0 and arr[j-1] > arr[j]):
            val = arr[j];
            val2 = arr[j-1]
            arr[j] = val2;
            arr[j-1] = val;
            j = j-1;
        i+=1;
    return arr;

print(main());