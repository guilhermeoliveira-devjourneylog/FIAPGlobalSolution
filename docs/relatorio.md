# FIAP Global Solution

# Relatório Técnico
## Artemis Mission Control System (AMCS)

**RM:** rm573419  
**Versão:** 1.0  
**Projeto:** Artemis Mission Control System  
**Data:** Junho de 2026  
**Área:** Engenharia Aeroespacial, Sistemas Distribuídos, Sistemas Críticos e Ciência de Dados

---

# 1. Visão Geral

O **Artemis Mission Control System (AMCS)** é uma plataforma computacional desenvolvida para monitoramento operacional, análise de telemetria, detecção de anomalias e suporte à tomada de decisão em missões espaciais do programa Artemis.

O sistema foi projetado para operar em ambientes de alta criticidade, onde falhas podem comprometer ativos bilionários e colocar vidas humanas em risco.

A solução centraliza informações provenientes de múltiplos subsistemas espaciais e fornece mecanismos de observabilidade operacional, análise preditiva e avaliação contínua de riscos.

---

# 2. Motivação do Projeto

Missões lunares modernas possuem uma complexidade significativamente superior às missões Apollo.

Entre os fatores responsáveis por essa complexidade destacam-se:

- Operações de longa duração
- Bases permanentes na superfície lunar
- Sistemas autônomos
- Veículos tripulados e não tripulados
- Infraestrutura energética distribuída
- Produção local de recursos (ISRU)
- Integração entre múltiplos veículos espaciais

Essa realidade gera grandes volumes de telemetria e eventos operacionais que precisam ser processados em tempo real.

O AMCS foi desenvolvido para reduzir:

- Sobrecarga cognitiva
- Fragmentação da informação
- Tempo de resposta operacional
- Risco de falhas não detectadas

---

# 3. Arquitetura Conceitual

A arquitetura foi organizada em cinco camadas principais.

```text
┌───────────────────────────┐
│      Data Generation      │
└─────────────┬─────────────┘
              │
┌─────────────▼─────────────┐
│     Telemetry Dataset     │
└─────────────┬─────────────┘
              │
┌─────────────▼─────────────┐
│   Anomaly Detection Layer │
└─────────────┬─────────────┘
              │
┌─────────────▼─────────────┐
│   Predictive Analytics    │
└─────────────┬─────────────┘
              │
┌─────────────▼─────────────┐
│ Operational Visualization │
└───────────────────────────┘
```

### Responsabilidades

| Camada | Responsabilidade |
|----------|------------------|
| Data Generation | Simulação e geração de telemetria |
| Telemetry Dataset | Armazenamento estruturado dos dados |
| Anomaly Detection | Identificação de comportamentos anormais |
| Predictive Analytics | Projeção de estados futuros |
| Visualization | Exibição operacional e suporte à decisão |

---

# 4. Estruturas de Dados

## 4.1 DataFrame

Estrutura principal utilizada para armazenamento e processamento dos dados de missão.

### Finalidade

- Telemetria temporal
- Métricas operacionais
- Eventos da missão
- Estados dos subsistemas

### Características

- Estrutura tabular
- Indexação temporal
- Processamento vetorizado
- Alta eficiência analítica

---

## 4.2 Dataclasses

Utilizadas para encapsular resultados de processamento.

### Exemplos

```python
PredictionResult
AnomalyResult
```

### Benefícios

- Tipagem forte
- Clareza semântica
- Facilidade de serialização
- Melhor manutenção

---

## 4.3 Dicionários

Utilizados para armazenar:

- Limites operacionais
- Configurações
- Mapeamentos
- Regras de negócio

### Exemplo

```python
{
    "POWER": 95,
    "OXYGEN": 80,
    "TEMPERATURE": 35
}
```

---

## 4.4 Enumerações

Representam estados discretos.

### Exemplo

```python
NORMAL
WARNING
CRITICAL
```

### Benefícios

- Eliminação de valores mágicos
- Maior legibilidade
- Maior segurança lógica

---

# 5. Modelo Operacional da Missão

O sistema representa a missão através de fases operacionais.

| Fase | Objetivo |
|--------|-----------|
| Launch | Inserção orbital |
| Earth Orbit | Preparação translunar |
| Translunar Transfer | Transferência Terra-Lua |
| Lunar Orbit | Inserção em órbita lunar |
| Rendezvous | Acoplamento orbital |
| Lunar Landing | Pouso lunar |
| Surface Operations | Operações na superfície |
| Return | Retorno terrestre |

Cada fase possui:

- Eventos específicos
- Métricas monitoradas
- Critérios de risco
- Regras operacionais

---

# 6. Regras Lógicas do Dataset

A geração do dataset segue regras determinísticas.

## Regra 1 — Sequenciamento Temporal

Toda observação deve respeitar a ordem cronológica.

```text
T0 < T1 < T2 < T3
```

### Objetivo

Garantir consistência temporal dos dados.

---

## Regra 2 — Continuidade da Missão

Cada fase deve possuir duração válida.

```text
duracao > 0
```

### Objetivo

Evitar fases vazias ou inconsistentes.

---

## Regra 3 — Consistência Física

Os valores simulados devem respeitar limites físicos.

### Exemplos

```text
0 ≤ bateria ≤ 100

temperatura > -273.15

oxigenio ≥ 0
```

### Objetivo

Garantir plausibilidade física dos dados.

---

## Regra 4 — Dependência de Fase

O comportamento das variáveis depende da fase operacional.

### Exemplo

Durante o pouso lunar:

```text
consumo_energia ↑

delta_v ↓
```

---

# 7. Sistema de Detecção de Anomalias

## Objetivo

Identificar:

- Falhas
- Degradações
- Comportamentos anormais
- Situações de risco

---

## Fluxo Lógico

```text
Receber Telemetria
        ↓
Validar Dados
        ↓
Remover Valores Inválidos
        ↓
Aplicar Detectores
        ↓
Classificar Severidade
        ↓
Gerar Alerta
```

---

## Regras de Validação

### Colunas Obrigatórias

```text
timestamp
mission_phase
metric
value
```

---

### Tratamento de Valores Ausentes

```text
NaN → Ignorado
```

ou

```text
NaN → Interpolado
```

---

### Ordenação Temporal

```python
sort(timestamp)
```

Objetivo:

Evitar falsos positivos.

---

### Persistência da Anomalia

Uma anomalia só é confirmada após múltiplas ocorrências.

```text
mínimo = 3 ocorrências consecutivas
```

Objetivo:

Reduzir alarmes falsos.

---

## Classificação de Severidade

| Nível | Significado |
|---------|-------------|
| INFO | Evento informativo |
| WARNING | Atenção necessária |
| CRITICAL | Risco operacional elevado |

---

# 8. Sistema Preditivo

## Objetivo

Antecipar:

- Falhas futuras
- Exaustão de recursos
- Tendências operacionais
- Condições críticas

---

## Técnica Utilizada

### Regressão Linear

Modelo matemático:

```text
y = β₀ + β₁x
```

Onde:

- x = tempo
- y = valor previsto

---

## Fluxo Preditivo

```text
Histórico
    ↓
Treinamento
    ↓
Estimativa
    ↓
Previsão
    ↓
Avaliação de Risco
```

---

## Saídas Geradas

### Valor Previsto

```text
87.4%
```

### Tendência

```text
CRESCENTE
```

ou

```text
DECRESCENTE
```

### Horizonte de Previsão

```text
30 min
60 min
120 min
```

### Confiança

```text
0.0 → 1.0
```

---

# 9. Fundamentos Aeroespaciais

## Delta-V

Representa a capacidade de execução de manobras orbitais.

### Regra Operacional

```text
delta_v ↓
risco ↑
```

---

## NRHO

**Near Rectilinear Halo Orbit**

Órbita utilizada pelo Gateway.

### Características

- Alta estabilidade orbital
- Baixo consumo energético
- Cobertura do polo sul lunar

---

## Rendezvous Orbital

Procedimento de aproximação entre veículos espaciais.

### Métricas Monitoradas

- Distância relativa
- Velocidade relativa
- Janela de acoplamento

---

## Transferência de Hohmann

Manobra orbital de baixo consumo energético.

```text
Órbita Inicial
      ↓
Transferência Elíptica
      ↓
Órbita Final
```

### Benefício

Minimização do consumo de combustível.

---

# 10. Decisões Técnicas

## Pandas

### Motivos

- Processamento eficiente
- Manipulação temporal
- Análise vetorizada

---

## Scikit-Learn

### Motivos

- Algoritmos consolidados
- Facilidade de integração
- Confiabilidade

---

## Arquitetura Modular

Cada componente possui responsabilidade específica.

### Benefícios

- Baixo acoplamento
- Alta coesão
- Facilidade de manutenção
- Escalabilidade

---

# 11. Design Patterns

## Builder

Responsável pela construção incremental do dataset.

```text
MissionBuilder
```

### Benefícios

- Flexibilidade
- Reutilização
- Organização do fluxo

---

## Factory

Responsável pela criação das fases da missão.

```text
PhaseFactory
```

### Benefícios

- Desacoplamento
- Extensibilidade

---

## Strategy

Permite troca dinâmica de algoritmos.

```text
AnomalyDetectorStrategy

PredictionStrategy
```

### Benefícios

- Modularidade
- Evolução simplificada

---

# 12. Benefícios Operacionais

## Segurança

- Detecção antecipada de falhas
- Monitoramento contínuo

## Consciência Situacional

- Visão integrada da missão
- Redução da fragmentação da informação

## Escalabilidade

Suporte para:

- Gateway
- Moon Base
- Missões para Marte
- Missões cislunares futuras

## Eficiência Operacional

- Menor carga cognitiva
- Melhor coordenação operacional

## Apoio à Decisão

- Informações consolidadas
- Análises preditivas
- Avaliação contínua de riscos

---

# 13. Conclusão

O **Artemis Mission Control System (AMCS)** constitui uma plataforma de observabilidade operacional voltada para missões espaciais modernas.

A solução integra conceitos de:

- Engenharia Aeroespacial
- Ciência de Dados
- Sistemas Distribuídos
- Sistemas Críticos
- Mecânica Orbital
- Inteligência Analítica

A combinação de estruturas de dados robustas, regras lógicas determinísticas, algoritmos preditivos e arquitetura modular baseada em padrões de projeto permite oferecer monitoramento contínuo, detecção de anomalias, previsão de comportamento futuro e suporte à tomada de decisão em ambientes operacionais de alta criticidade.

O sistema foi concebido para apoiar não apenas as missões Artemis, mas também futuras operações de exploração lunar permanente e missões de espaço profundo.