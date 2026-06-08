
# Sistema de Prognóstico e Predição de Anomalias

## Visão Geral

O módulo `PredictiveAnalyzer` implementa um mecanismo de prognóstico para telemetria espacial baseado em aprendizado supervisionado e inferência determinística.

O sistema utiliza **Regressão Linear Simples** para estimar o comportamento futuro de métricas operacionais e aplica um conjunto de **regras lógicas de classificação** para determinar o risco operacional e o estado de saúde de cada subsistema monitorado.

Formalmente, o processo pode ser representado como:

\[
Dados \ Predição \ Classificação \ Avaliação
\]

---

## Regras de Pré-Processamento

### Remoção de Valores Ausentes

Antes da análise, o sistema remove todos os valores ausentes.

### Regra Formal

\[
S' = S - \{NaN\}
\]

### Regra Lógica

```text
SE valor = NaN
ENTÃO remover valor
```

---

## Casos Base

## Série Vazia

### Condição

\[
|S| = 0
\]

### Regra

```text
SE tamanho = 0
ENTÃO retornar (0.0, 0.0)
```

### Resultado

| Predição | Inclinação |
|-----------|-----------|
| 0.0 | 0.0 |

---

## Série Unitária

### Condição

\[
|S| = 1
\]

### Regra

```text
SE tamanho = 1
ENTÃO

predição = valor atual
inclinação = 0
```

### Resultado

| Predição | Inclinação |
|-----------|-----------|
| valor atual | 0.0 |

---

##  Modelo de Predição

O sistema utiliza **Regressão Linear Simples**.

A função aprendida possui a forma:

\[
f(x)=ax+b
\]

onde:

| Símbolo | Significado |
|----------|------------|
| a | Inclinação (slope) |
| b | Intercepto |

---

## Regra de Inferência

```text
SE quantidade de observações >= 2

ENTÃO

treinar regressão linear
calcular valor futuro
```

---

## Regra de Tendência

A inclinação da reta determina o comportamento da métrica.

## Crescimento

\[
a > 0
\]

```text
TENDÊNCIA = CRESCENTE
```

---

## Estabilidade

\[
a = 0
\]

```text
TENDÊNCIA = ESTÁVEL
```

---

## Decaimento

\[
a < 0
\]

```text
TENDÊNCIA = DECRESCENTE
```

---

## Sistema de Classificação de Risco

O risco é calculado através da diferença relativa entre o valor previsto e o valor atual.

\[
V =
\frac{|P-C|}
{|C|}
\]

onde:

| Símbolo | Significado |
|----------|------------|
| P | Valor previsto |
| C | Valor atual |

---

## Regra Especial

### Divisão por Zero

\[
C = 0
\]

```text
SE valor atual = 0

ENTÃO risco = LOW
```

---

## Árvore de Decisão de Risco

## Alto Risco

### Condição

\[
V > 0.30
\]

### Regra

```text
SE variação > 30%

ENTÃO HIGH
```

---

## Médio Risco

### Condição

\[
0.15 < V \le 0.30
\]

### Regra

```text
SE variação > 15%

ENTÃO MEDIUM
```

---

## Baixo Risco

### Condição

\[
V \le 0.15
\]

### Regra

```text
CASO CONTRÁRIO

LOW
```

---

## Sistema Especialista de Saúde

Após a classificação de risco, o sistema converte o risco em um índice de saúde.

## Função

\[
Health = f(Risk)
\]

---

## Tabela de Decisão

| Risco | Score |
|---------|---------|
| LOW | 95 |
| MEDIUM | 75 |
| HIGH | 45 |

---

## Regras

### LOW

```text
SE risco = LOW

ENTÃO score = 95
```

### MEDIUM

```text
SE risco = MEDIUM

ENTÃO score = 75
```

### HIGH

```text
SE risco = HIGH

ENTÃO score = 45
```

---

## Processo de Inferência

Para cada métrica numérica do dataset:

```text
1. Extrair série temporal

2. Remover valores ausentes

3. Executar regressão linear

4. Calcular valor previsto

5. Determinar risco

6. Calcular score de saúde

7. Gerar PredictionResult
```

Formalmente:

\[
Métrica
\
Predição
\
Risco
\
Saúde
\]

---

# Regras de Seleção de Métricas

O algoritmo ignora atributos não relacionados à telemetria quantitativa.

## Colunas Ignoradas

```text
phase
status
eva
burn
touchdown
```

### Regra

```text
SE coluna pertence ao conjunto ignorado

ENTÃO não analisar
```

---

## Regra de Tipo

```text
SE coluna é numérica

ENTÃO analisar

SENÃO ignorar
```

---

# Agregação de Saúde da Fase

Após a análise individual das métricas:

\[
Health_1,
Health_2,
...
Health_n
\]

é calculada a média aritmética.

\[
PhaseScore=
\frac{
\sum_{i=1}^{n}
Health_i
}{n}
\]

---

## Regra

```text
SE existem métricas válidas

ENTÃO

phase_score =
média(scores)
```

---

## Caso Especial

```text
SE nenhuma métrica foi analisada

ENTÃO

retornar
([], 0)
```

---

# Fluxo Algorítmico Completo

```text
PARA cada métrica numérica

    remover NaN

    SE tamanho < 2
        ignorar

    prever valor futuro

    calcular variação

    SE variação > 30%
        risco = HIGH

    SENÃO SE variação > 15%
        risco = MEDIUM

    SENÃO
        risco = LOW

    converter risco em score

    gerar PredictionResult

calcular média dos scores

retornar resultados
```

---

# Classificação 

O módulo pode ser formalmente classificado como:

- Sistema Baseado em Regras (Rule-Based System)
- Sistema Especialista Determinístico
- Pipeline de Machine Learning Supervisionado
- Motor de Inferência Heurística
- Sistema de Prognóstico Operacional
- Analisador de Séries Temporais Univariadas
- Sistema de Avaliação de Saúde de Missão
- Framework de Predição para Telemetria Aeroespacial