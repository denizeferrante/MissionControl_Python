# 🚀 Mission Control AI - Poseidon Sentinel

## 🌊 Sobre o Projeto

O **Mission Control AI** é um sistema inteligente de monitoramento desenvolvido para a Global Solution 2026.1. O objetivo é simular o centro de controle de uma missão espacial experimental, garantindo a segurança operacional da cápsula por meio da análise contínua de dados de telemetria.

O sistema processa ciclos de monitoramento, identifica riscos, calcula tendências e gera relatórios automáticos para apoiar a tomada de decisão em ambientes extremos.

## 🛠️ Dados da Missão

A missão **Poseidon Sentinel** opera em zonas abissais, onde a precisão dos dados é o único fator que separa o sucesso do desastre operacional. Abaixo, os dados identificadores do projeto:

- **Nome da Missão:** Poseidon Sentinel
- **Equipe Responsável:** Equipe Netuno
- **Contexto:** Indústria Espacial e Monitoramento de Cápsula

## 👥 Integrantes

- **RM 571836** - Bruna Yukimy Hada
- **RM 571562** - Denize Ferrante
- **RM 572395** - Gabriel Dias Menezes

## 📊 Áreas Monitoradas

O sistema monitora cinco variáveis críticas em cada ciclo de operação:

1. **Temperatura Interna (°C):** Monitoramento térmico do módulo.
2. **Qualidade da Comunicação (%):** Estabilidade do sinal com a base.
3. **Nível da Bateria (%):** Nível de energia disponível nos sistemas de suporte à vida e propulsão.
4. **Suporte de Oxigênio (%):** Concentração de O2 disponível para suporte à vida.
5. **Estabilidade Operacional (%):** Integridade estrutural do casco contra a pressão hidrostática.

## ⚙️ Regras de Alerta e Pontuação

Cada sensor atribui uma pontuação baseada no nível de risco detectado: **Normal (0 pontos)**, **Atenção (1 ponto)** e **Crítico (2 pontos)**.

| Variável | Normal (0 pts) | Atenção (1 pt) | Crítico (2 pts) |
| :--- | :--- | :--- | :--- |
| **Temperatura** | 18°C a 30°C | <18°C ou 30-35°C | >35°C |
| **Comunicação** | ≥60% | 30% a 59% | <30% |
| **Bateria** | ≥50% | 20% a 49% | <20% |
| **Oxigênio** | ≥90% | 80% a 89% | <80% |
| **Estabilidade** | ≥70% | 40% a 69% | <40% |

## 🧠 Lógica de Processamento

O código foi estruturado com os seguintes requisitos obrigatórios:

- **Matriz dados_missao:** Armazena pelo menos 6 ciclos de monitoramento.
- **Funções de Análise:** O sistema possui funções específicas para cada sensor, classificação de ciclo e análise de tendência.
- **Cálculo de Risco:** A soma dos pontos de cada sensor define a classificação do ciclo.

### Classificação do Ciclo

O sistema classifica o estado imediato da missão:

- **0 a 2 pontos:** ESTÁVEL (Operação normal)
- **3 a 5 pontos:** ATENÇÃO (Necessita monitoramento rigoroso)
- **6 a 10 pontos:** CRÍTICA (Protocolo de emergência ativado)

### Classificação Final da Missão

A classificação final é determinada pela soma de todas as pontuações de todos os ciclos processados:

- **Soma < 6:** MISSÃO ESTÁVEL
- **Soma entre 6 e 9:** MISSÃO EM ESTADO DE ATENÇÃO
- **Soma ≥ 10:** MISSÃO CRÍTICA (Falha sistêmica detectada)

## 📈 Análise de Tendência

Compara o primeiro e o último ciclo para informar se a missão está melhorando, piorando ou estável.

## 📍 Identificação da Área Mais Afetada
O algoritmo acumula a pontuação individual de cada sensor ao longo de todos os ciclos. Ao final do processamento, o sistema identifica qual das 5 variáveis (Temperatura, Comunicação, Bateria, Oxigênio ou Estabilidade) obteve a maior pontuação acumulada, apontando-a como a área crítica da missão.

## 🛠️ Tecnologias Utilizadas

- **Python 3.10+**: Linguagem base para o desenvolvimento da lógica.
- **Estruturas de Dados**: Listas compostas e dicionários para armazenamento de ciclos.
- **Modularização**: Funções específicas para cálculo de risco e exibição de relatórios.
- **Matemática Computacional**: Implementação de somatórios e médias ponderadas.

## 🎥 Vídeo Demonstrativo 

Confira o funcionamento do sistema e a explicação técnica no vídeo abaixo:

https://www.youtube.com/watch?v=9758mITlr0w
