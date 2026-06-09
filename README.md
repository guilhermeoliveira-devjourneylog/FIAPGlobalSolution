# FIAPGlobalSolution
Sistema de Monitoramento Operacional Espacial

**RM:** rm573419  
Versão: 1.0
Projeto: Artemis Mission Control System
Área: Engenharia Aeroespacial, Sistemas Críticos e Operações Espaciais
Data: Junho de 2026

## Resumo Executivo

O Artemis Mission Control System (AMCS) é uma plataforma de monitoramento operacional desenvolvida para supervisionar, analisar e apoiar a tomada de decisão durante todas as fases das missões do programa Artemis.

O sistema foi concebido para atuar como uma camada central de observabilidade e consciência situacional, integrando informações provenientes de veículos espaciais, habitats lunares, sistemas de energia, navegação, suporte à vida e infraestrutura de superfície.

O principal objetivo é fornecer aos operadores uma visão consolidada da missão, permitindo identificar riscos operacionais, acompanhar indicadores críticos e apoiar a execução segura de operações lunares de longa duração.

## 1. Cenário

Após décadas concentrando esforços em órbita terrestre baixa, a humanidade retorna à exploração do espaço profundo através do programa Artemis.

O programa Artemis busca:

- Retornar astronautas à Lua.
- Estabelecer presença humana permanente.
- Desenvolver tecnologias para Marte.
- Explorar recursos lunares.
- Construir infraestrutura espacial sustentável.

Diferentemente das missões Apollo, que possuíam curta duração, Artemis exige operações contínuas, envolvendo:

- Veículos Orion.
- Foguete SLS.
- Human Landing System (HLS).
- Gateway.
- Bases lunares.
- Rovers.
- Sistemas ISRU.

Essa complexidade gera enormes desafios operacionais.

## 2. Problema 

Crescimento da Complexidade Operacional

Uma missão lunar moderna produz milhares de eventos por segundo.

Os operadores precisam monitorar simultaneamente:

- Estado da nave.
- Consumo energético.
- Telemetria orbital.
- Integridade estrutural.
- Saúde da tripulação.
- Comunicações.
- Sistemas ambientais.
- Operações de superfície.

A ausência de uma plataforma integrada gera:

**Sobrecarga Cognitiva**

Operadores precisam consultar múltiplos sistemas.

**Risco Operacional**

Eventos críticos podem passar despercebidos.

**Falta de Consciência Situacional**

Informações ficam fragmentadas.

**Tomada de Decisão Lenta**

Situações de emergência exigem respostas imediatas.

## 3. Solução Proposta

O AMCS centraliza todas as informações relevantes da missão em um único ambiente operacional.

O sistema fornece:

- Monitoramento em tempo real.
- Consolidação de telemetria.
- Visualização hierárquica da missão.
- Gestão de subsistemas.
- Análise de estados operacionais.
- Avaliação contínua de riscos.

## 4. Benefícios

**Segurança**

Detecção precoce de anomalias e predição de falhas.

**Consciência Situacional**

Visão integrada da missão.

**Eficiência Operacional**

Menor carga cognitiva dos operadores.

**Escalabilidade**

Suporta futuras expansões:

- Moon Base
- Gateway
- Marte

**Tomada de Decisão**

Informações consolidadas em tempo real.

## 5. Fluxo Operacional da Missão

**Fase 1 — Lançamento SLS**

Objetivo: Inserção segura da cápsula Orion.

**Fase 2 — Órbita Terrestre**

Objetivo: Preparação para a Transferência Translunar.

**Fase 3 — Transferência Cislunar**

Objetivo: Alcançar órbita lunar.

**Fase 4 — Rendezvous com HLS**

Objetivo: Transferência segura da tripulação.

**Fase 5 — Pouso Lunar**

Objetivo: Realizar touchdown seguro.

**Fase 6 — Operações de Superfície**

Objetivo: Garantir sustentabilidade da missão.

**Fase 7 — Retorno**

Objetivo: Retorno seguro da tripulação.


## 7. Subsistemas Monitorados

**Energia**

Responsável pela geração e distribuição energética.

**Componentes:**

- Painéis solares
- Baterias
- Reatores nucleares
- Conversores de potência

**Indicadores:**

- Estado de carga
- Potência disponível
- Consumo instantâneo
- Autonomia

**Navegação**

Responsável pelo posicionamento e controle orbital.

**Componentes:**

- GN&C
- Sensores inerciais
- Star Trackers
- Computadores de bordo

**Indicadores:**

- Órbita atual
- Inclinação orbital
- Delta-V
- Erro de atitude

**Comunicações**

Mantém o elo entre Terra e Lua.

**Componentes:**

- Deep Space Network
- Antenas de alto ganho
- Gateway
- Redes lunares

**Indicadores:**

- Latência
- Banda disponível
- Perda de pacotes
- Disponibilidade

**Life Support**

Mantém condições habitáveis.

**Componentes:**

- Oxigênio
- Água
- Pressurização
- Controle térmico

**Indicadores:**

- Pressão
- Temperatura
- Umidade
- Níveis de CO₂

**Surface Operations**

Coordena operações na superfície.

**Componentes:**

- Rovers
- Habitats
- Equipamentos ISRU
- Infraestrutura energética

**Indicadores:**

- Estado dos ativos
- Missões em execução
- Cobertura operacional

**Safety**

Responsável pela segurança da missão.

**Monitora:**

- Radiação
- Micrometeoritos
- Falhas críticas
- Emergências médicas

## 8. Fundamentos Técnicos

O AMCS utiliza conceitos da mecânica orbital para interpretação da telemetria.

**Órbita NRHO**

Near Rectilinear Halo Orbit.

Órbita altamente elíptica ao redor da Lua.

Vantagens:

- Baixo consumo de combustível.
- Excelente cobertura do polo sul lunar.
- Ideal para o Gateway.

**Delta-V**

Variação de velocidade necessária para realizar manobras espaciais.

Quanto maior o Delta-V disponível:

- Maior capacidade de correção orbital.
- Maior flexibilidade operacional.

**Apogeu**

Ponto mais distante da Terra em uma órbita.

**Perigeu**

Ponto mais próximo da Terra em uma órbita.

**Inclinação Orbital**

Ângulo entre o plano orbital e o equador terrestre.

Determina quais regiões podem ser sobrevoadas.

**Rendezvous Orbital**

Procedimento de aproximação entre dois veículos espaciais.

Exemplo: Orion Human Landing System. Exige extrema precisão em:

- Velocidade relativa
- Distância relativa
- Sincronização orbital

**Transferência de Hohmann**

Manobra orbital de baixo consumo energético utilizada para mover uma espaçonave entre duas órbitas circulares. Baseia-se em uma órbita elíptica intermediária e minimiza o consumo de combustível, sendo amplamente utilizada em planejamento de missões espaciais

**ISRU**

In-Situ Resource Utilization.

Utilização de recursos encontrados localmente.

Exemplos:

- Produção de oxigênio.
- Extração de água.
- Produção de combustível.

Reduz dependência da Terra.

## Design Patterns
[Design Patterns](./docs/design_patterns.md)

## Estrutura de Dados
[Estrutura de Dados](./docs/data_structure.md)

## Regras Lógicas

[Predição](./docs/logic_rule_predictive.md)
[Detector de Anomalias](./docs/logic_rule_detect_anomaly.mddocs/)
[DataSet](./docs/logic_rule_dataset.md)

## Técnica de Previsão

[Técnica de Previsão](predictive.md)

## Como Executar

### Instalar dependências 

```
pip install -r requirements.txt
```
```
& [root]/FIAPGlobalSolution/.venv/Scripts/python.exe [root]/FIAPGlobalSolution/src/sistema.py
```

### Executar via terminal 

## Input e Output

[Input Output](./docs/in_out_md)

## Link Video do Youtube

[video youtube](./docs/link_video.txt)

