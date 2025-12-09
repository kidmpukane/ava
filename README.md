# **AVA – Adaptive Virtual Assistant for Industrial Diagnostics**

**Philosophical Purpose**
AVA exists to shrink the gap between human intention and machine understanding. It takes the messiness of human thought — shorthand, incomplete descriptions, intuition — and translates it into structured operations that machines can execute, delivering clarity back to the human operator.

---

## **Table of Contents**

1. [Overview](#overview)
2. [Core Philosophy](#core-philosophy)
3. [High-Level Architecture](#high-level-architecture)
4. [Module Breakdown](#module-breakdown)
5. [Sample Input / Output](#sample-input--output)
6. [Getting Started](#getting-started)
7. [Future Directions](#future-directions)

---

## **Overview**

AVA is a modular reasoning engine for industrial IoT and predictive maintenance. It can process human language or structured telemetry, translate it into actionable insights, and provide machine-readable and human-readable outputs.

It is designed to be flexible, extendable, and decoupled, allowing developers to experiment with each module independently.

---

## **Core Philosophy**

* **Alignment:** Ensure human goals match machine actions.
* **Faithful Interpretation:** Preserve intent and context without “over-correcting” the user.
* **Structured Clarity:** Turn uncertainty into deterministic results.
* **Modular Exploration:** Each component can be tested and expanded independently.

---

## **High-Level Architecture**

```
User Input
   ↓
_core/input_handler.py
   ↓
_core/input_analyser.py
_core/intent_classifier.py
   ↓
_utils/permissions.py
   ↓
_core/tool_selector.py
_tools/registry.py
   ↓
_core/tool_executor.py
_tools/*.py
_data/telemetry.py
_library/machine_profiles/*
   ↓
_core/response_generator.py
   ↓
_core/output_handler.py
   ↓
Returned Result
```

**Flow Summary:**

1. **Input Layer:** Capture raw commands and telemetry.
2. **Intent Analysis Layer:** Extract intent, parameters, confidence scores.
3. **Permission & Scope Layer:** Validate that requests are allowed and safe.
4. **Tool Selection Layer:** Map intent to appropriate diagnostic tool.
5. **Tool Execution Layer:** Run diagnostics, models, or analyses.
6. **Response Generation Layer:** Convert raw output into human-readable summaries and structured JSON.
7. **Output Layer:** Deliver results to CLI, dashboard, API, or another agent.

---

## **Module Breakdown**

| Layer               | Responsibility                                                 | Technical Location                                                             |
| ------------------- | -------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| Input Handler       | Capture raw input (text or telemetry)                          | `_core/input_handler.py`                                                       |
| Intent Analysis     | Classify intent, extract parameters, machine ID, confidence    | `_core/input_analyser.py` `_core/intent_classifier.py`                         |
| Permissions & Scope | Validate request safety, authorization                         | `_utils/permissions.py`                                                        |
| Tool Selector       | Map intent → tool/module                                       | `_core/tool_selector.py` `_tools/registry.py`                                  |
| Tool Executor       | Execute diagnostics/ML/analysis                                | `_core/tool_executor.py` `_tools/*.py` `_data/*` `_library/machine_profiles/*` |
| Response Generator  | Summarize results, generate human-readable & structured output | `_core/response_generator.py`                                                  |
| Output Handler      | Deliver result to dashboard, API, CLI                          | `_core/output_handler.py` `_utils/logger.py`                                   |

---

## **Sample Input / Output**

**Input (via CLI or agent):**

```json
{
  "intent": "vibration_analysis",
  "machine_id": 4,
  "params": {
    "sensor": "Sensor_12",
    "window": "17:42:31"
  }
}
```

**Output (JSON + Summary):**

```json
{
  "status": "success",
  "summary": "Machine 4 ran 'vibration_analysis' → All vibration metrics nominal.",
  "raw_output": {
    "machine_id": 4,
    "intent": "vibration_analysis",
    "results": {
        "RMS": 4.2,
        "peaks": [5.1, 4.8],
        "anomalies": 0
    }
  }
}
```

---

## **Getting Started**

1. Clone the repository.
2. Install dependencies (if any Python libraries are required for ML models or visualization).
3. Run the CLI or dashboard simulator:

```bash
python main.py
```

4. Test different intents:

* `vibration_analysis`
* `temperature_monitoring`
* `rul_estimate`

5. Extend modules independently without breaking the rest of the system.

---

## **Future Directions**

* **Machine Learning Integration:** Real predictive models for vibration, temperature, and RUL.
* **Real-Time Telemetry:** Connect to industrial sensors via API or message queues.
* **Interactive Dashboard:** Live Nevo or Plotly-based visualization.
* **Agent Orchestration:** Enable AVA to handle multi-step requests or coordinate multiple machines.
* **Expanded Toolset:** Add more predictive maintenance diagnostics and industrial analytics tools.

---

## **Philosophical View**

AVA is a loop: human ambiguity → machine precision → human clarity. Every layer exists to reduce friction between intention and execution. It’s modular, transparent, and built for experimentation as much as production.

