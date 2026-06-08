# Estruturas de Dados e Organização Computacional

## Visão Geral

O módulo `predictive.py` implementa um sistema de análise preditiva baseado em séries temporais e utiliza estruturas de dados clássicas da Ciência da Computação para armazenar, processar e retornar informações derivadas da telemetria da missão.

A arquitetura pode ser representada da seguinte forma:

```text
DataFrame
    │
    ▼
Filtragem de atributos numéricos
    │
    ▼
Séries temporais (Array)
    │
    ▼
Modelo de Regressão Linear
    │
    ▼
PredictionResult
    │
    ▼
Lista de PredictionResult
    │
    ▼
Tupla de Retorno
```

---

# 1. PredictionResult

## Classificação

**Estrutura de Dados:** Registro (Record)

**Implementação Python:** `dataclass`

Um registro é uma estrutura composta utilizada para agrupar múltiplos atributos heterogêneos sob uma única entidade lógica.

### Definição Conceitual

```text
PredictionResult
├── metric : String
├── current_value : Float
├── predicted_value : Float
├── risk : String
└── health_score : Integer
```

### Complexidade

| Operação             | Complexidade |
| -------------------- | ------------ |
| Acesso a campo       | O(1)         |
| Atualização de campo | O(1)         |
| Criação do objeto    | O(1)         |

### Papel no Sistema

Representa um único elemento do domínio:

> "Previsão de uma métrica de telemetria."

Cada instância encapsula completamente o resultado da análise de uma variável observada.

---

# 2. Série Temporal

## Classificação

**Estrutura de Dados:** Vetor (Array)

**Implementação:** `numpy.ndarray`

Após a remoção dos valores ausentes:

```python
values = np.asarray(values)
```

obtém-se uma sequência linear de elementos numéricos.

### Estrutura

```text
Array
┌─────┬─────┬─────┬─────┬─────┐
│v₀   │v₁   │v₂   │...  │vₙ   │
└─────┴─────┴─────┴─────┴─────┘
```

### Complexidade

| Operação          | Complexidade |
| ----------------- | ------------ |
| Acesso por índice | O(1)         |
| Percorrer série   | O(n)         |
| Filtrar NaN       | O(n)         |

onde:

```text
n = número de amostras da métrica
```

### Papel no Sistema

Representa uma série temporal discreta utilizada como entrada para o algoritmo de regressão linear.

---

# 3. Conjunto de Features

## Classificação

**Estrutura de Dados:** Matriz

**Implementação:** `numpy.ndarray`

```python
x = np.arange(
    len(values)
).reshape(-1, 1)
```

Produz:

```text
┌───┐
│ 0 │
├───┤
│ 1 │
├───┤
│ 2 │
├───┤
│...│
├───┤
│ n │
└───┘
```

### Tipo

```text
Matriz n × 1
```

### Papel

Representa o eixo temporal utilizado como variável independente para treinamento do modelo preditivo.

---

# 4. Coleção de Resultados

## Classificação

**Estrutura de Dados:** Lista Dinâmica

**Implementação:** `list`

```python
predictions = []
```

### Estrutura

```text
List
│
├── PredictionResult
├── PredictionResult
├── PredictionResult
└── ...
```

### Tipo Formal

```python
list[PredictionResult]
```

### Complexidade

| Operação          | Complexidade    |
| ----------------- | --------------- |
| Inserção no final | O(1) amortizado |
| Iteração          | O(n)            |
| Acesso por índice | O(1)            |

onde:

```text
n = quantidade de métricas analisadas
```

### Papel

Armazena todos os resultados produzidos pela análise preditiva da fase.

---

# 5. Conjunto de Colunas Ignoradas

## Classificação

**Estrutura de Dados:** Hash Set

**Implementação:** `set`

```python
ignored = {
    "phase",
    "status",
    "eva",
    "burn",
    "touchdown"
}
```

### Estrutura

```text
Hash Set
```

### Complexidade

| Operação | Complexidade |
| -------- | ------------ |
| Busca    | O(1)         |
| Inserção | O(1)         |
| Remoção  | O(1)         |

### Justificativa

A utilização de um conjunto evita buscas lineares durante a filtragem das colunas do DataFrame.

---

# 6. Dataset de Entrada

## Classificação

**Estrutura de Dados:** Tabela

**Implementação:** `pandas.DataFrame`

### Estrutura

```text
DataFrame

┌────┬─────────┬─────────┬─────────┐
│ t  │ metric1 │ metric2 │ metric3 │
├────┼─────────┼─────────┼─────────┤
│ 0  │   ...   │   ...   │   ...   │
│ 1  │   ...   │   ...   │   ...   │
│ 2  │   ...   │   ...   │   ...   │
└────┴─────────┴─────────┴─────────┘
```

### Modelo Abstrato

```text
Tabela Relacional
```

ou

```text
Matriz Rotulada
```

### Papel

Representa o repositório principal de telemetria consumido pelo sistema de prognóstico.

---

# 7. Valor de Retorno

## Classificação

**Estrutura de Dados:** Tupla

**Implementação:** `tuple`

### Estrutura

```python
(
    predictions,
    phase_score
)
```

### Tipo Formal

```python
tuple[
    list[PredictionResult],
    int
]
```

### Representação

```text
Tuple
│
├── List<PredictionResult>
│
└── Integer
```

### Complexidade

| Operação          | Complexidade |
| ----------------- | ------------ |
| Acesso a elemento | O(1)         |

### Papel

Fornece um retorno composto contendo:

1. Resultados detalhados por métrica.
2. Avaliação agregada da fase.

---

# Resumo das Estruturas Utilizadas

| Estrutura         | Tipo Computacional       | Implementação    |
| ----------------- | ------------------------ | ---------------- |
| PredictionResult  | Record                   | dataclass        |
| Série Temporal    | Array                    | numpy.ndarray    |
| Variável Temporal | Matrix                   | numpy.ndarray    |
| Resultados        | Dynamic Array            | list             |
| Colunas Ignoradas | Hash Set                 | set              |
| Dataset           | Tabela / Matriz Rotulada | pandas.DataFrame |
| Retorno Final     | Tuple                    | tuple            |

---

# Complexidade Global

Considerando:

```text
m = número de métricas

n = número de amostras por métrica
```

A execução do método:

```python
PredictiveAnalyzer.analyze(df)
```

possui custo aproximado:

```text
Tempo:
O(m · n)

Memória:
O(m + n)
```

onde:

* O(m·n) decorre da varredura das séries temporais e ajuste dos modelos.
* O(m) corresponde ao armazenamento dos objetos `PredictionResult`.
* O(n) corresponde às estruturas temporárias utilizadas durante a regressão.
  """

## anomaly_detection

O módulo `anomaly_detection.py` implementa uma arquitetura orientada a objetos para detecção de anomalias em séries temporais de telemetria. Do ponto de vista da Ciência da Computação, ele utiliza uma combinação de estruturas de dados abstratas e concretas para representar observações, regras de detecção e resultados analíticos.

---

# 1. Estruturas de Dados Fundamentais

## 1.1 DataFrame (Tabela Relacional em Memória)

A principal estrutura de entrada é:

```python
pd.DataFrame
```

O DataFrame pode ser interpretado como uma:

- Matriz bidimensional heterogênea
- Relação tabular
- Coleção indexada de registros

Formalmente:

```text
DataFrame
│
├── Índice (Index)
│
└── Colunas
     ├── altitude_km
     ├── velocity_ms
     ├── fuel_pct
     ├── power_kw
     └── ...
```

### Complexidade

| Operação | Complexidade |
|-----------|-------------|
| Acesso coluna | O(1) |
| Acesso linha | O(1) |
| `diff()` | O(n) |
| `mean()` | O(n) |
| `std()` | O(n) |
| `rolling()` | O(n) |

---

## 1.2 Estrutura de Anomalia

As anomalias são modeladas como:

```python
class Anomaly(TypedDict):
    phase: str
    index: int
    severity: str
    anomaly: str
```

Equivale a um registro estruturado:

```text
Anomaly
│
├── phase
├── index
├── severity
└── anomaly
```

Exemplo:

```python
{
    "phase": "LAUNCH",
    "index": 42,
    "severity": "CRITICAL",
    "anomaly": "VELOCITY_DROP"
}
```

### Tipo de Estrutura

```text
Dictionary (Hash Table)
```

### Complexidade

| Operação | Complexidade |
|-----------|-------------|
| Inserção | O(1) |
| Busca | O(1) |
| Atualização | O(1) |

---

## 1.3 Lista de Anomalias

Todos os detectores retornam:

```python
List[Anomaly]
```

Estrutura:

```text
Dynamic Array
```

Representação:

```text
[
    anomaly_1,
    anomaly_2,
    anomaly_3,
    ...
]
```

### Complexidade

| Operação | Complexidade |
|-----------|-------------|
| Append | O(1) amortizado |
| Iteração | O(n) |
| Busca linear | O(n) |

---

# 2. Estruturas de Controle

## 2.1 Tabela de Despacho (Dispatch Table)

A classe `MissionAnomalyDetector` mantém:

```python
DETECTORS = {
    "LAUNCH": LaunchDetector(),
    "LEO": LEODetector(),
    "TRANSLUNAR": TranslunarDetector(),
    ...
}
```

### Estrutura

```text
Hash Map
```

Representação:

```text
Phase
  ↓
Detector
```

Exemplo:

```text
"LAUNCH"      → LaunchDetector
"LEO"         → LEODetector
"TRANSLUNAR"  → TranslunarDetector
"NRHO"        → NRHODetector
```

### Complexidade

| Operação | Complexidade |
|-----------|-------------|
| Busca detector | O(1) |
| Inserção detector | O(1) |
| Remoção detector | O(1) |

### Benefício

Implementa o padrão:

```text
Dictionary-Based Dispatch
```

Eliminando grandes cadeias de:

```python
if/elif/else
```

---

## 2.2 Lista de Colunas Obrigatórias

Cada detector define:

```python
REQUIRED_COLUMNS
```

Exemplo:

```python
[
    "altitude_km",
    "velocity_ms"
]
```

### Estrutura

```text
Array / Lista Sequencial
```

Utilizada durante a validação:

```python
for column in REQUIRED_COLUMNS:
```

### Complexidade

```text
O(m)
```

onde:

```text
m = número de colunas obrigatórias
```

---

# 3. Estruturas para Análise Temporal

## 3.1 Vetores Delta

Exemplo:

```python
df["altitude_km"].diff()
```

Gera:

```text
ΔAltitude
```

Representação:

```text
[
  0,
  +0.3,
  +0.4,
  -0.6,
  +0.5
]
```

### Tipo

```text
Array Numérico
```

### Complexidade

```text
O(n)
```

---

## 3.2 Máscaras Booleanas

Exemplo:

```python
altitude_drop = (
    altitude_delta < -0.5
)
```

Resultado:

```text
[
 False,
 False,
 False,
 True,
 False
]
```

### Estrutura

```text
Bit Vector / Boolean Mask
```

Utilizada para:

```python
df[altitude_drop]
```

### Complexidade

```text
O(n)
```

---

# 4. Estruturas Estatísticas

## 4.1 Média

```python
mean()
```

Representa:

```text
Escalar Numérico
```

### Complexidade

```text
O(n)
```

---

## 4.2 Desvio Padrão

```python
std()
```

Representa:

```text
Escalar Estatístico
```

Utilizado em:

```python
3σ Rule
```

### Complexidade

```text
O(n)
```

---

## 4.3 Janela Deslizante (Sliding Window)

Utilizada no detector `NRHODetector`:

```python
rolling(window=120)
```

Estrutura lógica:

```text
Sliding Window
```

Representação:

```text
[t1 ... t120]
[t2 ... t121]
[t3 ... t122]
```

Aplicação:

```python
rolling_mean
rolling_std
```

### Complexidade

```text
O(n)
```

(com otimizações internas do Pandas)

---

# 5. Hierarquia de Classes

O sistema utiliza herança para especialização dos detectores:

```text
PhaseAnomalyDetector
│
├── LaunchDetector
├── LEODetector
├── TranslunarDetector
├── NRHODetector
├── RendezvousDetector
├── LandingDetector
└── SurfaceDetector
```

### Tipo de Estrutura

```text
Árvore de Herança (Inheritance Tree)
```

### Características

- Polimorfismo
- Encapsulamento
- Extensibilidade
- Reutilização de código

---

# 6. Fluxo de Dados

```text
                DataFrame
                     │
                     ▼
       MissionAnomalyDetector
                     │
                     ▼
            Hash Map Lookup
                     │
                     ▼
          Detector Específico
                     │
                     ▼
        Vetores Temporais (Δ)
                     │
                     ▼
         Máscaras Booleanas
                     │
                     ▼
       Lista de Anomalias
```

---

# 7. Classificação das Estruturas Utilizadas

| Estrutura | Categoria |
|------------|-----------|
| DataFrame | Estrutura Tabular |
| TypedDict | Registro |
| Dict | Tabela Hash |
| List | Vetor Dinâmico |
| Series | Vetor |
| Boolean Mask | Bit Vector |
| Rolling Window | Janela Deslizante |
| Inheritance Tree | Árvore |
| Dispatch Table | Hash Map |
| Detector Registry | Dicionário Associativo |

---

# 8. Complexidade Computacional Global

Considerando:

```text
n = número de amostras de telemetria
```

A maioria dos detectores realiza:

1. Percurso dos dados (`diff`, filtros, máscaras)
2. Cálculo de estatísticas (`mean`, `std`)
3. Geração da lista de anomalias

Portanto:

```text
Tempo: O(n)
Espaço: O(n)
```

A única exceção parcial é o detector `NRHODetector`, que utiliza janelas móveis, mas continua apresentando comportamento linear devido às otimizações vetorizadas do Pandas.

---

# Resumo Computacional

O módulo pode ser modelado como um sistema de processamento de séries temporais baseado em:

- **Tabelas relacionais em memória (DataFrames)** para armazenamento da telemetria.
- **Vetores numéricos** para cálculos de diferenças temporais.
- **Máscaras booleanas** para filtragem eficiente.
- **Tabelas hash** para roteamento de detectores.
- **Registros tipados** para representação das anomalias.
- **Árvores de herança** para organização das estratégias de detecção.
- **Janelas deslizantes (Sliding Windows)** para análise estatística local.

A arquitetura segue princípios clássicos de Engenharia de Software e Estruturas de Dados, combinando **Hash Maps**, **Vetores**, **Registros**, **Árvores de Herança** e **Processamento Vetorizado**, permitindo escalabilidade e extensibilidade para futuras fases da missão Artemis.