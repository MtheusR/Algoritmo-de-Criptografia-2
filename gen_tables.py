import random
import csv
import string
import os

def n_random(minimo, maximo):
    return random.randint(minimo, maximo)

def gerar_tamanho_tabelas(minimo, maximo):
    tamanho_tabelas_geradas = []
    n_tabelas = random.randint(minimo, maximo)

    for _ in range(n_tabelas):
        verificacao = True
        while verificacao:
            tamanho = n_random(5, 15)
            if tamanho in tamanho_tabelas_geradas:
                verificacao = True
            else:
                verificacao = False
        tamanho_tabelas_geradas.append(tamanho)

    return tamanho_tabelas_geradas

valores_totais = []

def gerar_valores_binarios(tamanho, n_tabelas_chaves):
    valores_binarios = []

    for i in range(tamanho):
        verificacao = True
        while verificacao:
            valor_binario = ''.join(random.choice('01') for _ in range(n_tabelas_chaves[i]))
            if (valor_binario not in valores_binarios) and (valor_binario not in valores_totais):
                valores_binarios.append(valor_binario)
                verificacao = False
    
    return valores_binarios


def gerar_arquivo_csv(file_name, caracteres, tabelas):
    valores = {}

    for char in caracteres:
        valores[char] = gerar_valores_binarios(len(tabelas), tabelas)

    with open(file_name + '.csv', 'w', newline='') as arquivo:
        escritor_csv = csv.writer(arquivo)
        escritor_csv.writerow(['Caractere'] + [f'Tabela {i+1}' for i in range(len(tabelas))])

        for char in valores:
            escritor_csv.writerow([char] + valores[char])

def gerar_tamanho_tabelas_tabs(num_tabelas_chaves):
    tamanho = n_random(8, 15)
    return [tamanho] * len(num_tabelas_chaves)