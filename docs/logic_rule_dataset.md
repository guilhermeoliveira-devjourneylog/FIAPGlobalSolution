# Regras Lógicas de Geração do Dataset da Missão Artemis

## Visão Geral

O dataset da missão é gerado por meio da composição sequencial de múltiplas fases operacionais. Cada fase produz um conjunto independente de observações sintéticas e, ao final, todos os conjuntos são consolidados em um único dataset.

A arquitetura utiliza os padrões de projeto **Factory** e **Builder**, garantindo modularidade, extensibilidade e desacoplamento entre a geração das fases e a construção do dataset final.

---

## Arquitetura de Geração

## Seleção da Fase

A criação das fases é realizada pela `PhaseFactory`.

### Regra Lógica

```text
SE nome_da_fase estiver registrado
ENTÃO instanciar a fase correspondente

SENÃO
GERAR erro
```

### Mapeamento de Fases

| Identificador | Classe |
|--------------|---------|
| launch | LaunchPhase |
| leo | LEOPhase |
| translunar | TranslunarPhase |
| nrho | NRHOPhase |
| rendezvous | RendezvousPhase |
| landing | LandingPhase |
| surface | SurfacePhase |

---

## Contrato de Geração

Todas as fases devem implementar a interface abstrata `MissionPhase`.

### Regra Lógica

```text
Toda fase deve implementar:

generate() → DataFrame
```

### Restrição

```text
SE generate() não for implementado
ENTÃO a fase não pode ser instanciada
```

---

## Construção Incremental

O `MissionBuilder` mantém uma coleção de datasets gerados.

### Estrutura

```text
datasets = [
    DataFrame_Fase_1,
    DataFrame_Fase_2,
    ...
    DataFrame_Fase_N
]
```

### Regra de Processamento

```text
PARA cada fase adicionada

1. Criar fase via Factory
2. Executar generate()
3. Armazenar DataFrame
```

---

## Consolidação Final

Após a geração de todas as fases:

### Regra Lógica

```text
Dataset_Final =
concat(
    datasets,
    ignore_index=True,
    sort=False
)
```

### Resultado

```text
Dataset_Final =
Fase1 ∪ Fase2 ∪ Fase3 ∪ ... ∪ FaseN
```

Onde:

```text
∪ = concatenação vertical de registros
```

---

## Regras por Fase

---

## Launch Phase

## Objetivo

Simular a ascensão inicial do veículo lançador.

## Domínio Temporal

```text
t ∈ [0, 600] segundos
```

## Altitude

```text
altitude_km = t × 0.45
```

## Velocidade

```text
velocity_ms = t × 20
```

## Característica Computacional

Modelo determinístico linear.

```text
f(t) = a × t
```

Sem componentes aleatórios.

---

## LEO Phase

## Objetivo

Simular a permanência em órbita baixa da Terra.

## Domínio Temporal

```text
t ∈ [0, 180] minutos
```

## Altitude Orbital

```text
altitude_km ~ N(185, 1)
```

## Velocidade Orbital

```text
velocity_kmh ~ N(28000, 50)
```

## Característica Computacional

Modelo estocástico baseado em distribuição normal.

---

## Translunar Phase

## Objetivo

Simular a transferência da Terra para a Lua.

## Domínio Temporal

```text
t ∈ [0, 4320] minutos
```

(72 horas)

---

## Distância Percorrida

```text
distance_km =
linspace(
    200000,
    384400
)
```

### Regra

```text
distance(t+1) ≥ distance(t)
```

A distância sempre aumenta.

---

## Combustível

```text
fuel_pct:
100% → 65%
```

### Regra

```text
fuel(t+1) ≤ fuel(t)
```

O combustível nunca aumenta.

---

## Energia

```text
power_kw =
PowerModel.power_kw(n)
```

Representa a telemetria energética da espaçonave.

---

## Eventos de Propulsão

```text
burn =
BurnEvent.generate(n)
```

### Regra

```text
Cada instante temporal
recebe um estado operacional
de propulsão
```

---

## NRHO Phase

## Objetivo

Simular a órbita lunar NRHO.

## Domínio Temporal

```text
t ∈ [0, 10080] minutos
```

(7 dias)

## Altitude

```text
altitude_km ~ N(70000, 500)
```

## Característica Computacional

Modelo estocástico de perturbação orbital.

---

## Rendezvous Phase

## Objetivo

Simular aproximação e acoplamento orbital.

## Domínio Temporal

```text
t ∈ [0, 1800] segundos
```

## Distância Relativa

```text
distance_m =
linspace(
    1000,
    0
)
```

### Regra

```text
distance(t+1) ≤ distance(t)
```

A distância nunca aumenta.

---

## Estado Operacional

```text
status =
DockingEvent.status(n)
```

### Regra

```text
O estado do docking
depende do progresso temporal
da aproximação
```

---

## Surface Phase

## Objetivo

Simular operações na superfície lunar.

## Domínio Temporal

```text
t ∈ [0, 5000]
```

## Geração de Energia

```text
solar_power_kw ~ N(95, 5)
```

## Atividades EVA

```text
eva =
EVAEvent.activity(n)
```

### Regra

```text
Cada instante temporal
recebe uma atividade
operacional de superfície
```

---

# Pipeline Completa de Geração

```text
INÍCIO

↓
Selecionar fase

↓
PhaseFactory.create()

↓
Instanciar fase

↓
generate()

↓
Produzir DataFrame

↓
Adicionar ao Builder

↓
Existem mais fases?

├── SIM → repetir processo
│
└── NÃO

↓
Concatenar DataFrames

↓
Dataset Final

↓
FIM
```

---

# Estruturas de Dados Utilizadas

| Estrutura | Finalidade |
|------------|------------|
| Dictionary | Registro das fases na Factory |
| List | Armazenamento incremental dos datasets |
| DataFrame | Representação tabular dos dados gerados |
| Array NumPy | Séries temporais e variáveis numéricas |

---

# Complexidade Computacional

Considerando:

```text
n = número total de registros gerados
```

## Geração

```text
O(n)
```

Cada amostra é produzida uma única vez.

## Consolidação

```text
O(n)
```

Devido à concatenação dos DataFrames.

## Complexidade Total

```text
O(n)
```

---

# Resumo Formal

O sistema implementa uma pipeline de geração sintética de dados temporais baseada em fases da missão espacial.

Cada fase atua como um gerador independente responsável pela produção de:

- Séries temporais;
- Variáveis físicas;
- Eventos discretos;
- Estados operacionais;
- Telemetria de missão.

A composição dos datasets é realizada através dos padrões:

```text
Factory Pattern
+
Builder Pattern
+
Abstract Interface Pattern
```

resultando em um dataset único, cronologicamente organizado e adequado para análises de telemetria, detecção de anomalias, prognóstico e visualização operacional.