## Arquitetura e Design Patterns – Artemis Mission Control System

**Visão Geral**

O Artemis Mission Control System foi projetado utilizando princípios de Engenharia de Software, SOLID e Design Patterns para garantir:

- Baixo acoplamento
- Alta coesão
- Escalabilidade
- Reutilização de código
- Facilidade de manutenção
- Extensão para futuras missões espaciais

A arquitetura foi construída para representar as diferentes fases operacionais de uma missão lunar Artemis, desde o lançamento até as operações de superfície.

**Estrutura da Solução**

mission/ 
├── phases/ 
├── telemetry/ 
├── events/ 
├── factory/ 
├── builders/ 
├── exporters

src/ 
├── sistema

Cada módulo possui uma responsabilidade específica seguindo o princípio Single Responsibility Principle (SRP).

**Design Patterns Utilizados**

1. Template Method Pattern

**Objetivo**

Definir um fluxo padrão para geração de datasets de missão, permitindo que cada fase implemente apenas seu comportamento específico.

**Problema**

Todas as fases da missão possuem uma sequência semelhante:

- Gerar tempo
- Gerar telemetria
- Gerar eventos
- Construir DataFrame

Sem um padrão comum haveria duplicação de código.

**Benefícios**

- Padronização
- Reutilização
- Extensibilidade

2. Factory Method Pattern

**Objetivo**

Centralizar a criação das fases da missão.

**Benefícios**

- Baixo acoplamento
- Facilidade para adicionar novas fases
- Criação centralizada

3. Strategy Pattern

**Objetivo**

Permitir diferentes estratégias de geração de telemetria para cada fase.

**Problema**

Cada fase possui comportamento completamente diferente.

Exemplos:

- Launch → motores RS-25
- LEO → parâmetros orbitais
- Translunar → correções de trajetória
- Landing → telemetria de descida

Implementação

Cada fase é uma estratégia independente:

- LaunchPhase
- LEOPhase
- TranslunarPhase
- NRHOPhase
- LandingPhase
- SurfacePhase

Todas compartilham a mesma interface:

generate()

**Benefícios**

- Extensibilidade
- Substituição transparente
- Baixo acoplamento

4. Builder Pattern

**Objetivo**

Construir uma missão completa composta por várias fases.

**Problema**

Uma missão Artemis é composta por múltiplos datasets.

- Launch
- LEO
- Translunar
- NRHO
- Rendezvous
- Landing
- Surface

**Benefícios**

- Construção incremental
- Fluent API
- Organização do fluxo da missão

5. Facade Pattern

**Objetivo**

Fornecer uma interface simplificada para geração da missão.

Exemplo

O arquivo principal atua como uma fachada.

O usuário não precisa conhecer detalhes internos.

Benefícios

- Simplicidade
- Menor curva de aprendizado
- Isolamento da complexidade

6. Domain Model Pattern

A estrutura segue conceitos de Domain Driven Design (DDD).

**Fases**

Representam o domínio operacional.

- Launch
- LEO
- Translunar
- NRHO
- Landing
- Surface
- Telemetry

Representa modelos físicos.

- Propulsion
- Power
- Thermal
- Communications
- GNC
- Events

Representa eventos discretos.

- Burns
- Docking
- Landing
- EVA

**Aplicação dos Princípios SOLID**

Single Responsibility Principle

Cada módulo possui apenas uma responsabilidade.

**Open/Closed Principle**

Novas fases podem ser adicionadas sem alterar código existente.

**Liskov Substitution Principle**

Qualquer fase pode substituir outra.

MissionPhase é a abstração comum.

**Interface Segregation Principle**

Cada componente implementa apenas o necessário.

**Dependency Inversion Principle**

O sistema depende de abstrações.

MissionPhase e não de implementações concretas.

Fluxo de Execução

- MissionBuilder
- PhaseFactory
- MissionPhase

 LaunchPhase

 LEOPhase

 TranslunarPhase

 NRHOPhase

 RendezvousPhase

 LandingPhase

 SurfacePhase

- DataFrame
- Exporter

 CSV

 Parquet

 Kafka

**Benefícios da Arquitetura**

- Escalável
- Modular
- Testável
- Reutilizável
- Orientada a domínio
- Compatível com Data Engineering
- Compatível com Event-Driven Architecture
- Compatível com Machine Learning Pipelines