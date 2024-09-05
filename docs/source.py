import os
import shutil 
import time
import csv
from rich.table import Table
from rich import print

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def center(s):
    width = shutil.get_terminal_size().columns
    return s.center(width)

def write():
    clear()
    print(center("------------------- GAME OF LIFE ------------------- "))
    print("This is a terminal game to elucidate the original Game of Life.")
    print("Here you'll have options to determine how big your population will be, by determining the size of the matrix,how many steps the population will evolute, and more.")
    print("To know more about this game, I recommend to read my readme on https://github.com/me15degrees")
    time.sleep(2.5)
    print(center("\nPress Enter to continue..."))
    input()
    
    clear()
    while True:
        try:
            size = int(input("Choose the matrix size (enter a number): "))
            break
        except ValueError:
            clear()
            print("Please enter a valid integer.")
    
    clear()
    while True:
        try:
            gen = int(input("Choose the number of generations (enter a number): "))
            break
        except ValueError:
            clear()
            print("Please enter a valid integer.")
    
    clear()
    while True:
        steps = input("Do you want to see all the steps? (Y/N): ").upper()
        if steps == "Y" or steps == "N":
            break
        else:
            clear()
            print("Please enter Y or N.")
    
    clear()
    while True:
        archive = input("Do you want to save to an archive? (Y/N): ").upper()
        if archive == "Y" or archive == "N":
            break
        else:
            clear()
            print("Please enter Y or N.")
    clear()
    return size, gen, steps, archive


def upper(i, j, matrix): # função para retornar o elemento acima da célula
    if i != 0:
        return matrix[i-1][j]

def down(i, j, matrix, n): # função para retornar o elemento abaixo da célula
    if i != (n-1):
        return matrix[i+1][j]

def left(i, j, matrix): # função para retornar o elemento à esquerda da célula
    if j != 0:
        return matrix[i][j-1]

def right(i, j, matrix, n): # função para retornar o elemento à direita da célula
    if j != (n-1):
        return matrix[i][j+1]

def diag1(i, j, matrix): # função para retornar o elemento que está na diagonal superior esquerda da célula
    if i != 0 and j != 0:
        return matrix[i-1][j-1]

def diag2(i, j, matrix, n): # função para retornar o elemento que está na diagonal superior direita da célula
    if i != 0 and j != (n-1):
        return matrix[i-1][j+1]

def diag3(i, j, matrix, n): # função para retornar o elemento que está na diagonal inferior esquerda da célula
    if i != (n-1) and j != 0:
        return matrix[i+1][j-1]

def diag4(i, j, matrix, n): # função para retornar o elemento que está na diagonal inferior direita da célula
    if i != (n-1) and j != (n-1):
        return matrix[i+1][j+1]

def change(i, j, matrix, neighbour): # para alterar o estado da célula baseada nas regras
    item = matrix[i][j]
    if item == 0 and sum(neighbour) == 3:
        item = 1
    elif item == 1 and (sum(neighbour) < 2 or sum(neighbour) > 3):
        item = 0
    return item

def step(q,n,matrix):
    table = Table()
    print(f"---------------- RESULT AFTER {q+1} GENERATIONS ----------------")
    for i in range(n):
        for j in range(n):
            table.add_column(matrix[i][j])
        print(table)

def save(matrix): # para escrever as matrizes no arquivo .csv
    filename = "game_of_life.csv"
    with open(filename, 'a', newline='') as arquivo_csv: 
        writer_csv = csv.writer(arquivo_csv)
        for line in matrix:
            writer_csv.writerow(line)
        writer_csv.writerow([])  
    
