# -*- coding: utf-8 -*-
"""
  Curso: Bacharelado em Física
  Disciplina: MAC0115 Introdução à Computação
  Turma: 24 - Yoshiko
  Exercício-Programa EP03 - Aquecimento
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

"""

import math
const_grav = 6.67*(10**(-11)) # Constante gravitacional

def main():
     
# Área do Imput abaixo:________________________________________________________ 
 
# A ordem recebida será R_x, R_y, V_x, V_y e m
    

    b_i  = [ [[] for j in range(5)] for i in range(2)]
    for i in range(2): # leitura do do arquivo de entrada com dados sobre cada um dos 3 corpos
    		b_i[i] = [float(x) for x in input().split()]
    
    T = int(input()) # recebe o tempo de simulação
    dt = int(input()) # recebe o dt necessário para acrescer a cada ciclo de simulação
   
    
#Função principal que faz a "magia" acontecer:_________________________________
    
    bodys_at = [ [] for j in range(2)] # gera uma lista de 2 elementos que recebe as posições atualizadas p/ a Lua
    
    
    for n_time in range(0, T+dt, dt):
        
        bodys_at[0],bodys_at[1] = b_i[1][0],b_i[1][1] # Guarda as posições anteriores 
        
        
        dist_0_1 = dist(b_i[0], b_i[1]) # retorno da função dist
        
        forcas = fg(dist_0_1, b_i) # retorno da função fg
    
        new_posi_1 = atualiza(b_i[1], forcas, dt) # retorno da função 
            
        b_i[1][0],b_i[1][1] = new_posi_1[0], new_posi_1[1] # troca as posições em b_i para as retornadas
        
        print(" ".join(map(str , bodys_at))) # remove os colchetes e as vírgulas da lista criada e retorna os dados desejados
    
#Área das Funções______________________________________________________________

def dist(a, b):
    
   a # recebe o primeiro corpo
   b # recebe o segundo corpo
   
   dist_cubo = float((math.sqrt(((b[0] - a[0])**2) + ((b[1]-a[1])**2)))**3)
   # a variável acima calcula a distnância ao quadrado entre o primeiro e o segundo corpo

   return(dist_cubo) # retorna a distância ao cubo entre dois corpos

def fg(a,b): # Calcula e retorna a força gravitacional dado a dist_cubo
    
    a # recebe a dist_cubo
    b # recebe o corpo a ser calculado
    
    f_x = -(const_grav*(b[0][4]*b[1][4]))*((b[1][0]-b[0][0])/a) # Faz Fx = G * (m_1 * m*2)*(x_2 - x_1) / dist^3
    
    f_y = -(const_grav*(b[0][4]*b[1][4]))*((b[1][1]-b[0][1])/a) # Faz Fx = G * (m_1 * m*2)*(y_2 - y_1) / dist^3
    
    return (f_x, f_y) # retorna as componentes da força

def atualiza(a, b, c): # atualiza as componentes de movimento do corpo dada f_x, f_y, dt e o corpo que se deseja atualizar
    
    a # recebe um corpo
    b # recebe f_x, f_y
    c # recebe o valor de dt
    
    a_x, a_y = b[0]/a[4] , b[1]/a[4] # calcula a aceleração do corpo em x e y
        
    v_x, v_y = a_x*c + a[2] , a_y*c + a[3] # calcula a velocidade do corpo em x e y
    
    r_x, r_y = v_x*c + a[0] , v_y*c + a[1] # calcula a posição do corpo em x e y
    
    a[2], a[3] = v_x, v_y # troca as velocidades em b_i para as novas calculadas em dt
    
    return(r_x, r_y) # retorna as posições atualizadas em x e y

main()
