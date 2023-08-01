# -*- coding: utf-8 -*-
"""
      Curso: Bacharelado em Física
      Disciplina: MAC0115 Introdução à Computação
      Turma: 24 - Yoshiko
      Exercício-Programa EP01

      DECLARO QUE SOU O ÚNICO AUTOR E RESPONSÁVEL POR ESSE PROGRAMA. 
      TODAS AS PARTES ORIGINAIS DESTE EXERCÍCIO-PROGRAMA FORAM
      DESENVOLVIDAS E IMPLEMENTADAS POR MIM SEGUINDO AS INSTRUÇÕES
      DESSE EP E QUE PORTANTO NÃO CONSTITUEM DESONESTIDADE ACADÊMICA
      OU PLÁGIO.
      DECLARO TAMBÉM QUE SOU RESPONSÁVEL POR TODAS AS CÓPIAS DESTE
      PROGRAMA E QUE EU NÃO DISTRIBUI OU FACILITEI A SUA DISTRIBUIÇÃO.
      ESTOU CIENTE QUE OS CASOS DE PLÁGIO E DESONESTIDADE ACADÊMICA
      SERÃO TRATADOS SEGUNDO OS CRITÉRIOS DIVULGADOS NA PÁGINA DA
      DISCIPLINA.
_______________________________________________________________________________
 Problema:

   Considere uma moeda cujas faces são “cara” e “coroa”, e suponha que essas
   faces têm igual probabilidade de ocorrer, quando essa moeda é lançada. 
   Uma sequência de lançamentos dessa moeda pode ser representada por uma 
   sequência de bits, onde 0 representa “cara” e 1 representa “coroa”. 
   Vamos chamar de padrão uma sequência de 3 a 8 bits (por exemplo, 110010).
   Dado um padrão, deseja-se saber quantas vezes, na média, precisamos 
   lançar essa moeda até que esse padrão ocorra.

"""

import random

def main():
    
    seq_dada = input("Digite uma sequência de bytes:\n",)               # Solicita uma sequência de bits (1s e 0s)
    n_testes_dados = int(input("Digite a quantidade de testes:\n",))    # Solicita um número de testes p/ a verificação de igualdade
   
    n_jogadas = 0                                                       # Soma do total de jogadas
    
    for n_testes_feitos in range(n_testes_dados):                       # Realiza a busca de igualdade p/ a qnt. de testes fornecidos
        
        seq_aleat = ""                                                  # String "nula" para iniciar a seq_aleat
        
        while(len(seq_aleat)!=len(seq_dada)):                           # Gera uma sequência aleatória de tamanho igual à sequência dada 
            bit_ger = random.randint(0, 1)                              # Gera um bit aleatório (0 ou 1)
            seq_aleat = seq_aleat + str(bit_ger)                        # Adiciona o bit à variável seq_alet
            n_jogadas += 1                                              # Adiciona +1 à n_jogadas
            
        while(seq_aleat!=seq_dada):                                     # Verifica se duas sequências são iguais até que o resultado seja positivo
            bit_acr = random.randint(0, 1)                              # Gera um bit aleatório (0 ou 1)
            seq_aleat = seq_aleat[1:] + str(bit_acr)                    # Remove o 1º bit da variável e substitui pelo novo bit gerado
            n_jogadas += 1                                              # Adiciona +1 à n_jogadas
            
        n_testes_feitos += 1                                            # Acresce à contagem de testes realizados
                    
    media =  n_jogadas/n_testes_dados                                   # Calcula a média de jogadas necessárias p/ se obter a igualdade de acordo com a qnt. de testes fornecidos 
     
    print("A média que relaciona jogadas e testes é: %f"%(media))
           
main()
