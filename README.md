# ⚙️ AVA – Adaptive Virtual Assistant for Industrial Diagnostics

## 💡 Philosophical Purpose

AVA bridges the gap between human intuition and machine precision. It handles the natural ambiguity of human operators—shorthand, incomplete descriptions, or high-level requests—and translates them into structured, executable operations for industrial IoT and predictive maintenance systems.

The outcome: clear, actionable diagnostics that reduce friction and accelerate decision-making.

---

## 🧭 Table of Contents

* [Key Features](#-key-features)
* [Core Philosophy](#-core-philosophy)
* [Architecture and Data Flow](#-architecture-and-data-flow)
* [Module Breakdown](#-module-breakdown)
* [Getting Started](#-getting-started)
* [Sample Interaction](#-sample-interaction)
* [Future Roadmap](#-future-roadmap)

---

## 🛠️ Key Features

AVA is a modular reasoning engine designed for flexibility, extendability, and rapid experimentation across industrial diagnostics.

* **Adaptive Input**: Processes natural human language (e.g., `"Check temp on Machine 4"`) and structured telemetry data.
* **Actionable Insights**: Converts requests into specific diagnostic actions (`vibration_analysis`, `rul_estimate`).
* **Structured Output**: Returns results as human-readable summaries and machine-readable JSON.
* **Decoupled Design**: Modules can be independently developed, tested, or swapped (e.g., replace an intent classifier without affecting the pipeline).

---

## ✨ Core Philosophy

<<<<<<< HEAD
- **Alignment:** Ensure human goals match machine actions.
- **Faithful Interpretation:** Preserve intent and context without “over-correcting” the user.
- **Structured Clarity:** Turn uncertainty into deterministic results.
- **Modular Exploration:** Each component can be tested and expanded independently.
=======
| Principle                   | Description                                                                               |
| --------------------------- | ----------------------------------------------------------------------------------------- |
| **Alignment**               | Ensure the human's goal is perfectly matched by the machine's executed action.            |
| **Faithful Interpretation** | Preserve the user's original intent and context without over-correction or hallucination. |
| **Structured Clarity**      | Convert ambiguous inputs into deterministic and reliable results.                         |
| **Modular Exploration**     | Enable independent testing and expansion of every component for rapid iteration.          |
>>>>>>> c2f5c5000b52a89f45f476bacf5dcfbd16fc7e7a

---

## 🧠 Architecture and Data Flow

AVA follows a linear, decoupled pipeline that separates logic from execution:

**Flow Summary**

1. **Input Layer**: Captures raw commands (text) or telemetry data.
2. **Analysis Layer**: Extracts intent, parameters, target machine ID, and confidence score.
3. **Permission Layer**: Validates request safety and authorization.
4. **Tooling Layer**: Maps intent to the appropriate diagnostic tool, retrieves data, and runs analysis (ML model, calculation, or script).
5. **Output Layer**: Produces concise, human-readable summaries and structured JSON for downstream systems.

---

## 🧩 Module Breakdown

| Layer                   | Responsibility                                         | Key Technical Location                                                            |
| ----------------------- | ------------------------------------------------------ | --------------------------------------------------------------------------------- |
| **Input Handler**       | Capture raw input (text, API call, or telemetry)       | `_core/input_handler.py`                                                          |
| **Intent Analysis**     | Classify intent, extract parameters, assign confidence | `_core/input_analyser.py`, `_core/intent_classifier.py`                           |
| **Permissions & Scope** | Validate request safety and authorization              | `_utils/permissions.py`                                                           |
| **Tool Selector**       | Map classified intent to execution module              | `_core/tool_selector.py`, `_tools/registry.py`                                    |
| **Tool Executor**       | Execute diagnostics, ML models, data retrieval         | `_core/tool_executor.py`, `_tools/*.py`, `_data/*`, `_library/machine_profiles/*` |
| **Response Generator**  | Summarize results, generate structured JSON            | `_core/response_generator.py`                                                     |
| **Output Handler**      | Deliver results to CLI, dashboard, or agent            | `_core/output_handler.py`                                                         |

---

## 🚀 Getting Started

### Requirements

* Python 3.10 or higher

### Installation

```bash
git clone https://github.com/kidmpukane/ava
cd ava
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Running AVA

Start the main CLI or dashboard simulator:

```bash
python main.py
```

### Testing Intents

Examples to try after startup:

* `vibration_analysis`
* `temperature_monitoring`
* `rul_estimate`

---

## 📝 Sample Interaction

**Input (via API or Agent)**

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

**Output (JSON + Summary)**

```json
{
  "status": "success",
  "summary": "Machine 4 ran 'vibration_analysis' using Sensor_12 data. All vibration metrics are nominal and within baseline tolerances.",
  "raw_output": {
    "machine_id": 4,
    "intent": "vibration_analysis",
    "results": {
<<<<<<< HEAD
      "RMS": 4.2,
      "peaks": [5.1, 4.8],
      "anomalies": 0
=======
      "RMS_velocity": 4.2,
      "spectral_peaks": [5.1, 4.8],
      "anomalies_detected": 0
>>>>>>> c2f5c5000b52a89f45f476bacf5dcfbd16fc7e7a
    }
  }
}
```

---

## 🛣️ Future Roadmap

* **Machine Learning Integration**: Deploy predictive models (vibration, temperature, RUL).
* **Real-Time Telemetry**: Connect to live sensors via message queues (Kafka) or industrial APIs.
* **Interactive Dashboard**: Visualize streaming results with Plotly or similar tools.
* **Agent Orchestration**: Enable multi-step reasoning for complex requests.
* **Expanded Toolset**: Add advanced predictive maintenance diagnostics and industrial analytics tools.

<<<<<<< HEAD
## Requirements

- Python 3.10 or higher

## Installation

- Clone the repository

```bash
git clone <https://github.com/kidmpukane/aval>
cd <avaa>
```

- Create a virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

- Install dependencies

```bash
pip install -r requirements.txt
```

```

```

```bash
python main.py
```

4. Test different intents:

- `vibration_analysis`
- `temperature_monitoring`
- `rul_estimate`

5. Extend modules independently without breaking the rest of the system.

---

## **Future Directions**

- **Machine Learning Integration:** Real predictive models for vibration, temperature, and RUL.
- **Real-Time Telemetry:** Connect to industrial sensors via API or message queues.
- **Interactive Dashboard:** Live Nevo or Plotly-based visualization.
- **Agent Orchestration:** Enable AVA to handle multi-step requests or coordinate multiple machines.
- **Expanded Toolset:** Add more predictive maintenance diagnostics and industrial analytics tools.

---

## **Philosophical View**

AVA is a loop: human ambiguity → machine precision → human clarity. Every layer exists to reduce friction between intention and execution. It’s modular, transparent, and built for experimentation as much as production.
=======

>>>>>>> c2f5c5000b52a89f45f476bacf5dcfbd16fc7e7a
