# Entradas e Saídas do Sistema

## Visão Geral

O **Artemis Mission Control System** é um pipeline computacional responsável por:

1. Construir um dataset de missão.
2. Persistir os dados em múltiplos formatos.
3. Executar análises preditivas.
4. Detectar anomalias operacionais.
5. Exibir relatórios e dashboards em console.

---

# Fluxo de Dados

```text
Definição das Fases
        │
        ▼
 MissionBuilder
        │
        ▼
 Dataset da Missão
        │
 ┌──────┼─────────┐
 ▼      ▼         ▼
CSV   Parquet  Visualização
        │
        ▼
Predição
        │
        ▼
Detecção de Anomalias
        │
        ▼
Relatórios Operacionais
```

---

# Entradas do Sistema

## 1. Configuração da Missão

### Origem

Definida pelo operador através da composição sequencial das fases da missão.

### Exemplo

```python
MissionBuilder()
.add_phase("launch")
.add_phase("leo")
.add_phase("translunar")
.add_phase("nrho")
.add_phase("rendezvous")
.add_phase("landing")
.add_phase("surface")
.build()
```

### Tipo de Dados

```text
List[String]
```

### Estrutura

| Campo | Tipo | Descrição |
|---------|---------|---------|
| phase | String | Nome da fase da missão |

### Valores Permitidos

| Fase | Descrição |
|--------|--------|
| launch | Lançamento |
| leo | Low Earth Orbit |
| translunar | Transferência Terra-Lua |
| nrho | Near Rectilinear Halo Orbit |
| rendezvous | Acoplamento |
| landing | Pouso Lunar |
| surface | Operações de Superfície |

---

## 2. Dataset de Telemetria

Após a execução do Builder é produzido um conjunto de dados contendo informações operacionais da missão.

### Tipo

```python
pandas.DataFrame
```

### Estrutura Esperada

| Campo | Tipo |
|---------|---------|
| timestamp | datetime |
| phase | string |
| altitude | float |
| velocity | float |
| fuel | float |
| battery | float |
| temperature | float |
| signal_strength | float |

### Exemplo

```text
timestamp              phase       altitude
2026-01-01 00:00:00    launch      0
2026-01-01 00:00:01    launch      120
2026-01-01 00:00:02    launch      450
```

---

# Saídas do Sistema

## 1. Dataset Consolidado

Resultado produzido pelo MissionBuilder.

### Variável

```python
mission
```

### Tipo

```python
pandas.DataFrame
```

### Finalidade

Representar toda a telemetria da missão em uma única estrutura de dados.

---

## 2. Exportação CSV

### Operação

```python
CSVExporter.export(
    mission,
    "./data/artemis_mission.csv"
)
```

### Saída

```text
data/artemis_mission.csv
```

### Formato

```text
CSV
```

### Utilização

- Compartilhamento de dados
- Auditoria
- Importação em ferramentas analíticas

---

## 3. Exportação Parquet

### Operação

```python
ParquetExporter.export(
    mission,
    "./data/artemis_mission.parquet"
)
```

### Saída

```text
data/artemis_mission.parquet
```

### Formato

```text
Apache Parquet
```

### Utilização

- Big Data
- Data Lake
- Analytics
- Processamento distribuído

---

## 4. Visualização da Missão

### Operação

```python
viewer.render_mission(
    mission
)
```

### Saída

```text
Mission Dashboard
```

### Conteúdo

- Estatísticas da missão
- Métricas operacionais
- Estado das fases
- Indicadores de desempenho

---

## 5. Sistema de Predição

### Entrada

```python
PredictiveAnalyzer.analyze(
    phase_df
)
```

### Tipo da Entrada

```python
pandas.DataFrame
```

Contendo apenas os registros de uma fase específica.

---

### Saída 1 — Predições

```python
predictions
```

### Tipo

```python
List[PredictionResult]
```

### Estrutura

| Campo | Tipo |
|---------|---------|
| metric | string |
| current_value | float |
| predicted_value | float |
| risk | string |
| health_score | int |

### Finalidade

Projetar tendências futuras das métricas monitoradas.

---

### Saída 2 — Índice de Saúde

```python
phase_score
```

### Tipo

```python
float
```

### Finalidade

Representar o estado geral da fase analisada.

---

### Visualização

```python
viewer.render_predictions_viewer(
    phase_name,
    predictions,
    phase_score
)
```

### Resultado

```text
Prediction Dashboard
```

### Conteúdo

- Tendências
- Projeções
- Riscos
- Health Score

---

## 6. Sistema de Detecção de Anomalias

### Entrada

```python
MissionAnomalyDetector.detect(
    phase_df
)
```

### Tipo

```python
pandas.DataFrame
```

---

### Saída

```python
List[Anomaly]
```

### Estrutura Conceitual

| Campo | Tipo |
|---------|---------|
| phase | string |
| anomaly_type | string |
| timestamp | datetime |
| severity | string |
| description | string |

### Finalidade

Identificar comportamentos fora do padrão esperado.

---

## 7. Consolidação de Anomalias

### Operação

```python
all_anomalies.extend(
    MissionAnomalyDetector.detect(
        phase_df
    )
)
```

### Resultado

```python
all_anomalies
```

### Tipo

```python
List[Anomaly]
```

### Finalidade

Centralizar todas as ocorrências anômalas detectadas ao longo da missão.

---

## 8. Relatório de Anomalias

### Operação

```python
viewer.render_anomaly_viewer(
    all_anomalies
)
```

### Saída

```text
Anomaly Report
```

### Conteúdo

- Eventos anômalos
- Fase da ocorrência
- Severidade
- Quantidade por categoria
- Incidentes críticos

---

# Resumo das Interfaces

| Componente | Entrada | Saída |
|------------|----------|--------|
| MissionBuilder | Lista de fases | Dataset da missão |
| CSVExporter | DataFrame | Arquivo CSV |
| ParquetExporter | DataFrame | Arquivo Parquet |
| MissionConsole | Dataset | Dashboards e relatórios |
| PredictiveAnalyzer | DataFrame da fase | Predições e Health Score |
| MissionAnomalyDetector | DataFrame da fase | Lista de anomalias |

---

# Contrato de Entrada e Saída

## Entrada Principal

```text
Lista de fases da missão
```

## Saídas Principais

```text
• Dataset consolidado da missão
• Arquivo CSV
• Arquivo Parquet
• Dashboard operacional
• Predições por fase
• Health Score por fase
• Lista de anomalias
• Relatório de anomalias
```

---

# Classificação em Ciência da Computação

| Categoria | Implementação |
|------------|---------------|
| Entrada de Dados | Configuração das fases da missão |
| Processamento | Construção do dataset |
| Persistência | CSV e Parquet |
| Análise Preditiva | Regressão e prognóstico |
| Detecção de Anomalias | Identificação de desvios operacionais |
| Visualização | Dashboards e relatórios em console |
| Saída de Dados | Arquivos e relatórios analíticos |

O sistema segue a arquitetura clássica **Input → Processing → Storage → Analytics → Output**, produzindo artefatos analíticos para monitoramento e suporte à tomada de decisão durante a execução da missão Artemis.