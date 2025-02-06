# Scrivete una funzione sum_list(my_list) che sommi tutti gli elementi di una lista.
# Poi, scaricate il vostro script Python e testatelo su Autograding
# (se la lista passata da sommare è vuota, la funzione deve tornare None - la somma di una lista vuota non è definita!)
my_list = [1, 2, 3, 4, 5]
def sum_list(my_list):
    somma = 0
    for number in my_list:
        somma += number
    return somma
print('Somma totale: {}'.format(sum_list(my_list)))

# Esercizio 1: Stampare l'equivalente di 538 minuti nel formato 12h:32min.   
print("L'equivalente di {} minuti è: {}:{} ore".format(538, 538//60, 538%60))

# Esercizio 2: Definire una funzione che prende come argomento una parola e una lettera. 
# Ritorna quante volte quella lettera è contenuta nella parola.  
lettera='e'
parola='casereccio'
def funz(parola, lettera):
    count = 0
    for char in parola:
        if char==lettera:
            count += 1
    return count
print('Quante volte la lettera "{}" è presente nella parola "{}": {}'.format(lettera, parola, funz(parola, lettera)))

# Esercizio 3: Scrivere una funzione che prende in input una stringa 
# e ritorna True se è un palindromo, False altrimenti
def stringa(striknjak):
    return striknjak == striknjak[::-1]
print(stringa(striknjak='oppo'))

# Esercizio 4: Definire una funzione che dati 3 numeri interi stabilisce 
# se possono essere i valori di 3 lati di un triangolo
def triangolo(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False
print(triangolo(a=4, b=5, c=1))

# Esercizio 5: Definire una funzione che prende in input una lista A, 
# gli indici i e j, e scambia il valore di A[i] con A[j].
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
def scambia(A, i, j):
    tmp=A[i]
    A[i]=A[j]
    A[j]=tmp
    return A
print("Lista scambiata: {}". format(scambia(A, i=4, j=10)))

# Esercizio 6: Definiere la funzione fattoriale
n=4
def fact_ric(n):
    if n == 1 or n ==0:
        return 1
    else:
        return n * fact_ric(n-1)
print("Fattoriale ricorsivo di {}: {}".format(n, fact_ric(n)))

def fact_it(n):
    molt=1
    for i in range(1, n+1):
        molt *= i
    return molt
print("Fattoriale iterativo di {}: {}".format(n, fact_it(n)))

# Esercizio 7: Scrivere una funzione che prende in input due liste 
# e ritorna `True` se le due liste hanno almeno un elemento in comune
lista_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lista_2 = ['uno', 9, 'tre', 'quattro', 'cinque']
def uguale(lista_1, lista_2):
    for numero in lista_1:
        if numero in lista_2:
            return True
print(uguale(lista_1, lista_2))

# Esercizio 8: Definire una funzione che prende in input una lista di numeri interi in [0, 9]
# e ritorna una lista di stringhe, corrispondenti ai numeri scritti in Italiano, 
# es. [1,0,7,9,8] ->["uno","zero","sette","nove","otto"]
interi = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
def itas(interi):
    nuova = []
    dizio = {0:'zero', 1:'uno', 2:'due', 3:'tre', 4:'quattro', 5:'cinque', 6:'sei', 7:'sette', 8:'otto', 9:'nove'}
    for number in interi:
        nuova.append(dizio[number])
    return nuova
print("Numeri convertiti: {}".format(itas(interi)))