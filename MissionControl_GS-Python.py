'''
GLOBAL SOLUTION 2026.1 | FIAP | CIÊNCIA DA COMPUTAÇÃO
MISSION CONTROL AI - POSEIDON SENTINEL
EQUIPE NETUNO: 
RM 571836 - Bruna Yukimy Hada
RM 571562 - Denize Ferrante
RM 572395 - Gabriel Dias Menezes
'''

# Dados da Missão 
# dados_missao = [temperatura, comunicacao, bateria, oxigenio, estabilidade]

dados_missao = [
    [17, 95, 85, 98, 92], #Ciclo 1
    [27, 88, 18, 94, 85], #Ciclo 2
    [37, 75, 45, 75, 82], #Ciclo 3
    [36, 12, 40, 91, 78], #Ciclo 4
    [30, 15, 20, 85, 60], #Ciclo 5
    [36, 29, 35, 83, 39] #Ciclo 6
]

# Funções - Condições de Análise de cada parâmetro da missão para cada Ciclo

# Análise da Temperatura do Ciclo
def analisar_temperatura(temperatura):
  if temperatura < 18:
    return "ATENÇÃO | Temperatura abaixo do ideal", 1, "Verificar controle térmico da missão" # classificacao, pontos, recomendacao
  elif 18 <= temperatura <= 30:
    return "NORMAL", 0, "ok" # classificacao, pontos
  elif 30 < temperatura <= 35:
    return "ATENÇÃO | Temperatura elevada", 1, "Verificar controle térmico da missão" # classificacao, pontos, recomendacao
  else:
    return "CRÍTICO | Risco de superaquecimento", 2, "Verificar controle térmico da missão" # classificacao, pontos, recomendacao

# Análise da Comunicação do Ciclo
def analisar_comunicacao(comunicacao):
  if comunicacao < 30:
    return "CRÍTICO | Comunicação em nível crítico", 2, "Tentar restabelecer contato com a base"
  elif 30 <= comunicacao <= 59:
    return "ATENÇÃO", 1, "Monitorar sistema de comunicação"
  else:
    return "NORMAL", 0, "ok"
  
# Análise da Bateria do Ciclo
def analisar_bateria(bateria):
  if bateria < 20:
    return "CRÍTICO | Bateria em nível crítico", 2, "Ativar modo de economia de bateria"
  elif 20 <= bateria <= 49:
    return "ATENÇÃO | Bateria abaixo do recomendado", 1, "Monitorar sistema de bateria"
  else:
    return "NORMAL", 0, "ok"

# Análise do Oxigênio do Ciclo
def analisar_oxigenio(oxigenio):
  if oxigenio < 80:
    return "CRÍTICO | Oxigênio em nível crítico", 2, "Acionar protocolo de suporte à vida"
  elif 80 <= oxigenio <= 89:
    return "ATENÇÃO | Oxigênio abaixo do ideal", 1, "Monitorar sistema de oxigênio"
  else:
    return "NORMAL", 0, "ok"

# Análise da Estabilidade do Ciclo
def analisar_estabilidade(estabilidade):
  if estabilidade < 40:
    return "CRÍTICO | Estabilidade operacional crítica", 2, "Reduzir operações não essenciais"
  elif 40 <= estabilidade <= 69:
    return "ATENÇÃO | Estabilidade operacional reduzida", 1, "Monitorar sistema de Estabilidade"
  else:
    return "NORMAL", 0, "ok"

def classificacao_ciclo(pontuacao_total_ciclo):
    if pontuacao_total_ciclo < 3: 
      return "MISSÃO ESTÁVEL"
    elif 3 <= pontuacao_total_ciclo <= 5: 
      return "MISSÃO EM ATENÇÃO"
    else: 
      return "MISSÃO CRÍTICA"

print(f'=============================================================================================================================')
print(f'MISSION CONTROL AI')
print(f'=============================================================================================================================')
print(f'Missão: Poseidon Sentinel')
print(f'Missão: Equipe Netuno ')
print(f'Quantidade de ciclos analisados: {len(dados_missao)}')
print(f'=============================================================================================================================')

#Lista pontuação
ciclos_pontuacao = []

# Análise das 5 áreas para cada Ciclo

# Posição de cada Área na coluna
# Classifição da área e pontos da área 
for ciclo in range(len(dados_missao)):
  temperatura = dados_missao[ciclo][0] 
  classificacao_temperatura, pontos_temperatura, rec_temp = analisar_temperatura(temperatura)

  comunicacao = dados_missao[ciclo][1]
  classificacao_comunicacao, pontos_comunicacao, rec_com = analisar_comunicacao(comunicacao)

  bateria = dados_missao[ciclo][2]
  classificacao_bateria, pontos_bateria, rec_bat = analisar_bateria(bateria)

  oxigenio = dados_missao[ciclo][3]
  classificacao_oxigenio, pontos_oxigenio, rec_oxi = analisar_oxigenio(oxigenio)

  estabilidade = dados_missao[ciclo][4]
  classificacao_estabilidade, pontos_estabilidade, rec_est = analisar_estabilidade(estabilidade)

  # Total por Ciclo de Pontos por Ciclo
  pontuacao_total_ciclo = int(pontos_temperatura + pontos_comunicacao + pontos_bateria + pontos_oxigenio + pontos_estabilidade)

  ciclos_pontuacao.append(pontuacao_total_ciclo)
  
  # Recomendação por Ciclo
  rec_ciclo = [rec_temp, rec_com, rec_bat, rec_oxi, rec_est]
  rec_ciclo = [v for v in rec_ciclo if v != "ok"]  


  print()
  print(f'CLICO {ciclo+1}')
  print(f'-----------------------------------------------------------------------------------------------------------------------------')
  print(f'Temperatura: {temperatura}°C | {classificacao_temperatura}')
  print(f'Comunicação: {comunicacao} | {classificacao_comunicacao}')
  print(f'Bateria: {bateria} | {classificacao_bateria}')
  print(f'Oxigênio: {oxigenio} | {classificacao_oxigenio}')
  print(f'Estabilidade: {estabilidade} | {classificacao_estabilidade}')
  print()
  print(f'Pontuação de risco do Ciclo: {pontuacao_total_ciclo}')
  print(f'Classificação do Ciclo: {classificacao_ciclo(pontuacao_total_ciclo)}')
  print(f'Recomendação do Ciclo: {', '.join(map(str, rec_ciclo))}')
  print(f'-----------------------------------------------------------------------------------------------------------------------------')

# Relatório final da Missão 
print()
print(f'=============================================================================================================================')
print(f'RELATÓRIO FINAL DA MISSÃO')
print(f'=============================================================================================================================')
print(f'Missão: Poseidon Sentinel')
print(f'Missão: Equipe Netuno ')
print()
print(f'Quantidade de ciclos analisados: {len(dados_missao)}')
print()
# Calcular médias
media_temperatura = sum([ciclo[0] for ciclo in dados_missao]) / len(dados_missao)
print(f'Média de temperatura: {media_temperatura:.2f}C')

media_comunicacao = sum([ciclo[1] for ciclo in dados_missao]) / len(dados_missao)
print(f'Média de comunicação: {media_comunicacao:.2f}%')

media_bateria = sum([ciclo[2] for ciclo in dados_missao]) / len(dados_missao)
print(f'Média de bateria: {media_bateria:.2f}%')

media_oxignio = sum([ciclo[3] for ciclo in dados_missao]) / len(dados_missao)
print(f'Média de oxigênio: {media_oxignio:.2f}%')

media_estabilidade = sum([ciclo[4] for ciclo in dados_missao]) / len(dados_missao)
print(f'Média de estabilidade: {media_estabilidade:.2f}%')
print()
# Ciclo mais Crítico 
print(f'Lista de pontuação dos ciclos {ciclos_pontuacao}')
print()

# Encontrar o ciclo mais crítico
ciclo_mais_critico = ciclos_pontuacao.index(max(ciclos_pontuacao)) + 1
pontuacao_maxima = max(ciclos_pontuacao)
print(f'Ciclo mais crítico: CICLO {ciclo_mais_critico}')
print(f'Maior pontuação de risco: {pontuacao_maxima}')

# Calcular risco médio da missão
risco_medio_missao = sum(ciclos_pontuacao) / len(ciclos_pontuacao)
print(f'Risco médio da missão: {risco_medio_missao:.2f}')

# Contar ciclos críticos
ciclos_criticos = [p for p in ciclos_pontuacao if p > 5]  # Acima de 5 é crítico
quantidade_ciclos_criticos = len(ciclos_criticos)
print(f'Quantidade de ciclos críticos: {quantidade_ciclos_criticos}')

# Tendência da missão
primeiro_ciclo = ciclos_pontuacao[0]
ultimo_ciclo = ciclos_pontuacao[-1]
diferenca = ultimo_ciclo - primeiro_ciclo

if diferenca > 0:
    tendencia = "apresentou tendência de piora"
elif diferenca < 0:
    tendencia = "apresentou tendência de melhora"
else:
    tendencia = "permaneceu estável"

print(f'A missão {tendencia}')

print()
#Pontuação acumulada por área 
areas_monitoradas = [
    "Temperatura interna",
    "Comunicação com a base",
    "Sistema de energia",
    "Suporte de oxigênio",
    "Estabilidade operacional"
]

pontuacao_por_area = [0, 0, 0, 0, 0]

for ciclo in range(len(dados_missao)):
    temperatura, comunicacao, bateria, oxigenio, estabilidade = dados_missao[ciclo]
    
    _, p1, _ = analisar_temperatura(temperatura)
    _, p2, _ = analisar_comunicacao(comunicacao)
    _, p3, _ = analisar_bateria(bateria)
    _, p4, _ = analisar_oxigenio(oxigenio)
    _, p5, _ = analisar_estabilidade(estabilidade)
    
    pontuacao_por_area[0] += p1
    pontuacao_por_area[1] += p2
    pontuacao_por_area[2] += p3
    pontuacao_por_area[3] += p4
    pontuacao_por_area[4] += p5

print(f'Pontuação acumulada por área:')
for i in range(len(areas_monitoradas)):
    print(f"{areas_monitoradas[i]}: {pontuacao_por_area[i]} pontos")

#Área mais afetada
print()
area_mais_afetada = areas_monitoradas[pontuacao_por_area.index(max(pontuacao_por_area))]
pontuacao_maxima = max(pontuacao_por_area)
print(f'Área mais afetada: {area_mais_afetada}')

# Classificação final da missão
pontuacao_total_missao = sum(pontuacao_por_area)

if pontuacao_total_missao >= 10:
    classificacao_final = "MISSÃO CRÍTICA"
elif pontuacao_total_missao >= 6:
    classificacao_final = "MISSÃO EM ATENÇÃO"
else:
    classificacao_final = "MISSÃO ESTÁVEL"

print()
print(f'Classificação final da missão: {classificacao_final}')
print(f'=============================================================================================================================')