# Técnicas de Predição

## Objetivo

O módulo `PredictiveAnalyzer` realiza análises preditivas sobre métricas de telemetria para estimar comportamentos futuros, identificar tendências e calcular riscos operacionais antes da ocorrência de falhas.

---

# Fluxo de Predição

Para cada métrica numérica do dataset:

1. Coleta da série histórica.
2. Remoção de valores ausentes (`NaN`).
3. Treinamento de um modelo de regressão linear.
4. Projeção de um valor futuro.
5. Cálculo da tendência da métrica.
6. Avaliação do risco operacional.
7. Cálculo do índice de saúde.
8. Geração do resultado preditivo.

---

# Regressão Linear

## Técnica Utilizada

O sistema utiliza o algoritmo:

```python
LinearRegression
```

A regressão linear modela a relação entre tempo e valor da métrica para identificar tendências futuras.

### Modelo Matemático

\[
y = \beta_0 + \beta_1x
\]

Onde:

- `x` = tempo
- `y` = valor da métrica
- `β₀` = intercepto
- `β₁` = inclinação da tendência

---

# Pré-processamento dos Dados

## Conversão Numérica

Todas as amostras são convertidas para valores do tipo `float`.

```python
np.asarray(values, dtype=float)
```

---

## Remoção de Valores Ausentes

Valores `NaN` são descartados antes do treinamento.

```python
values = values[~np.isnan(values)]
```

Objetivo:

- Evitar erros de treinamento.
- Garantir consistência estatística.

---

# Horizonte de Previsão

O sistema realiza projeções para:

```python
FORECAST_STEPS = 30
```

Isso significa que a previsão é calculada para 30 amostras à frente da última observação disponível.

---

# Cálculo da Tendência

Após o treinamento, o coeficiente angular da reta é extraído:

```python
slope = model.coef_[0]
```

## Interpretação

| Slope | Significado |
|---------|---------|
| > 0 | Tendência de crescimento |
| < 0 | Tendência de queda |
| ≈ 0 | Estabilidade |

---

# Forecasting

O valor futuro é obtido por extrapolação da reta ajustada:

```python
prediction = model.predict(future_x)
```

Resultado:

```text
Valor esperado da métrica após 30 amostras futuras.
```

---

# Avaliação de Risco

O risco é calculado comparando o valor atual com o valor previsto.

## Variação Percentual

\[
\text{Variação} =
\frac{|Previsto - Atual|}
{|Atual|}
\]

---

## Regras de Classificação

| Variação | Risco |
|-----------|--------|
| ≤ 15% | LOW |
| > 15% e ≤ 30% | MEDIUM |
| > 30% | HIGH |

---

# Health Score

O risco é convertido em uma pontuação de saúde operacional.

| Risco | Score |
|---------|---------|
| LOW | 95 |
| MEDIUM | 75 |
| HIGH | 45 |

Objetivo:

- Facilitar monitoramento.
- Permitir agregação de indicadores.

---

# Seleção de Métricas

Somente colunas numéricas são analisadas.

## Colunas Ignoradas

```text
phase
status
eva
burn
touchdown
```

Essas colunas representam estados ou eventos e não séries temporais contínuas.

---

# Resultado Preditivo

Cada análise gera um objeto:

```text
PredictionResult
```

## Campos

| Campo | Descrição |
|---------|---------|
| metric | Nome da métrica |
| current_value | Último valor observado |
| predicted_value | Valor previsto |
| risk | Classificação de risco |
| health_score | Índice de saúde |

---

# Score da Fase

Após analisar todas as métricas, é calculada a média dos índices de saúde.

\[
PhaseScore =
\frac{\sum HealthScore}{N}
\]

Onde:

- `N` = quantidade de métricas analisadas.

O resultado representa a saúde operacional geral da fase da missão.

---

# Técnicas de Ciência da Computação Aplicadas

| Área | Técnica |
|--------|----------|
| Machine Learning | Regressão Linear |
| Time Series Analysis | Forecasting |
| Predictive Analytics | Prognóstico de métricas |
| Data Cleaning | Remoção de NaN |
| Feature Selection | Filtragem de atributos numéricos |
| Risk Analysis | Classificação por limiares |
| Health Monitoring | Cálculo de indicadores operacionais |

---

# Resumo

O sistema implementa um mecanismo de **forecasting baseado em regressão linear**, capaz de:

- Prever valores futuros.
- Identificar tendências.
- Detectar possíveis desvios operacionais.
- Classificar riscos.
- Calcular indicadores de saúde.
- Produzir uma visão consolidada do estado da missão.