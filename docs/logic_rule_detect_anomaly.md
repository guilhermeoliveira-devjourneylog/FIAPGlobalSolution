# Regras Lógicas de Detecção de Anomalias

## Visão Geral

O sistema utiliza regras determinísticas para identificar comportamentos anormais nas telemetrias de cada fase da missão.

Cada regra segue a estrutura:

```text
IF condição
THEN gerar anomalia
```

As anomalias possuem dois níveis de severidade:

- WARNING → comportamento suspeito.
- CRITICAL → falha operacional ou violação física relevante.

---

## Launch Detector

## ALTITUDE_DROP

```text
IF altitude_delta < -0.5
THEN ALTITUDE_DROP
```

**Severidade:** CRITICAL

Detecta redução significativa de altitude durante o lançamento.

---

## VELOCITY_DROP

```text
IF velocity_delta < -10
THEN VELOCITY_DROP
```

**Severidade:** CRITICAL

Detecta perda abrupta de velocidade durante a ascensão.

---

## ALTITUDE_STALL

```text
IF altitude_delta <= 0
THEN ALTITUDE_STALL
```

**Severidade:** WARNING

Detecta interrupção do ganho de altitude.

---

## VELOCITY_STALL

```text
IF velocity_delta <= 0
THEN VELOCITY_STALL
```

**Severidade:** WARNING

Detecta interrupção do ganho de velocidade.

---

## LEO Detector

## ORBITAL_DRIFT

```text
IF abs(altitude - média_altitude)
   > 3 * desvio_padrão
THEN ORBITAL_DRIFT
```

**Severidade:** WARNING

Detecta desvios orbitais fora da faixa estatística esperada.

---

## Translunar Detector

## FUEL_INCREASE

```text
IF fuel_delta > 0
THEN FUEL_INCREASE
```

**Severidade:** CRITICAL

Detecta aumento impossível da quantidade de combustível.

---

## EXCESSIVE_FUEL_CONSUMPTION

```text
IF abs(fuel_delta) > 0.5
THEN EXCESSIVE_FUEL_CONSUMPTION
```

**Severidade:** WARNING

Detecta consumo excessivo de combustível entre amostras consecutivas.

---

## POWER_OUTLIER

```text
IF abs(power_kw - média_power)
   > 3 * desvio_padrão_power
THEN POWER_OUTLIER
```

**Severidade:** WARNING

Detecta valores anormais de potência elétrica.

---

## NRHO Detector

## ORBITAL_DRIFT

```text
IF abs(altitude - média_móvel)
   > 3 * desvio_padrão_móvel
THEN ORBITAL_DRIFT
```

**Severidade:** WARNING

Detecta desvios orbitais utilizando estatística local em janela deslizante.

---

## Rendezvous Detector

## DISTANCE_INCREASE

```text
IF distance_delta > 0
THEN DISTANCE_INCREASE
```

**Severidade:** CRITICAL

Detecta aumento da distância durante a aproximação entre veículos.

---

## DOCKING_FAILURE

```text
IF status_final != "DOCKED"
THEN DOCKING_FAILURE
```

**Severidade:** CRITICAL

Detecta falha no acoplamento ao final da operação.

---

## Landing Detector

## ALTITUDE_RISE

```text
IF altitude_delta > 0
THEN ALTITUDE_RISE
```

**Severidade:** CRITICAL

Detecta aumento de altitude durante a descida.

---

## SURFACE_NOT_REACHED

```text
IF altitude_final > 0
THEN SURFACE_NOT_REACHED
```

**Severidade:** CRITICAL

Indica que a superfície não foi alcançada.

---

## LANDING_FAILURE

```text
IF touchdown IS NULL
THEN LANDING_FAILURE
```

**Severidade:** CRITICAL

Indica ausência de confirmação de pouso.

---

## Surface Detector

## POWER_LOSS

```text
IF solar_power_kw
   < média_power - 3 * desvio_padrão_power
THEN POWER_LOSS
```

**Severidade:** WARNING

Detecta perda anormal de geração de energia solar.

---

# Resumo das Regras

| Fase | Regra | Condição |
|--------|--------|--------|
| Launch | ALTITUDE_DROP | altitude_delta < -0.5 |
| Launch | VELOCITY_DROP | velocity_delta < -10 |
| Launch | ALTITUDE_STALL | altitude_delta <= 0 |
| Launch | VELOCITY_STALL | velocity_delta <= 0 |
| LEO | ORBITAL_DRIFT | abs(altitude - média) > 3σ |
| Translunar | FUEL_INCREASE | fuel_delta > 0 |
| Translunar | EXCESSIVE_FUEL_CONSUMPTION | abs(fuel_delta) > 0.5 |
| Translunar | POWER_OUTLIER | abs(power - média) > 3σ |
| NRHO | ORBITAL_DRIFT | abs(altitude - média_móvel) > 3σ |
| Rendezvous | DISTANCE_INCREASE | distance_delta > 0 |
| Rendezvous | DOCKING_FAILURE | status_final != DOCKED |
| Landing | ALTITUDE_RISE | altitude_delta > 0 |
| Landing | SURFACE_NOT_REACHED | altitude_final > 0 |
| Landing | LANDING_FAILURE | touchdown IS NULL |
| Surface | POWER_LOSS | power < média - 3σ |

## Complexidade Computacional

Todos os detectores realizam uma única varredura sobre os dados de telemetria.

```text
Complexidade Temporal: O(n)

Complexidade Espacial: O(n)
```

onde:

- n = número de amostras analisadas.