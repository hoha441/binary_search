#!/usr/bin/env python

def insertion_sort (array) :
    for i in range (1,len(array)):
        for j in range(i-1,-1,-1):
            if (array[j] > array[i]):
                array[j],array[i]=array[i],array[j]
                i= i -1
    for i in range (len(array)):
           print array[i],

def selection_sort (array) :
    for i in range (len(array)):
        mini = i
        for j in range(i+1,len(array)):
            if (array[j] < array[mini]):
                mini = j
        array[i],array[mini]=array[mini],array[i]

    for i in range (len(array)):
      print array[i],
    print ("")
    return array

def binary_search (array,init,fin,numero_buscado) :
    half_array = (fin+init)/2
    
    print init,fin
    z=0
    z = int(raw_input("numero a buscar: "))

    if array[half_array] == numero_buscado:
        found = half_array
        print "Encontrado esta en el indice = %i" %(found+1)
    
    elif fin-init == 0:
        print ("No encontrado")

    elif array[half_array] < numero_buscado:        
        binary_search(array,half_array+1,fin,numero_buscado)            
    
    elif array[half_array] > numero_buscado:
        binary_search(array,init,half_array,numero_buscado)            
                    
if __name__ == '__main__':
    array=[-1,43,56,89,53,412,78,99]
    insertion_sort(array)
    print ("")
    array = selection_sort(array)
    numero_buscado = int(raw_input("numero a buscar: "))
    binary_search(array,0,len(array)-1,numero_buscado)
