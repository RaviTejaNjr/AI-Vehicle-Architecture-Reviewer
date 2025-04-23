# Vehicle Architecture AI Reviewer

This project uses a Large Language Model (LLM) to review and comment on automotive vehicle architecture descriptions. It's tailored for applications in connected vehicle systems, where smart AI support can enhance tool development and design validation.

---

## 🚀 Features
- Accepts architecture specs in plain text or markdown
- Uses LLMs to generate structured feedback:
  - Design flaws or omissions
  - Suggestions on protocols (CAN, LIN, Ethernet)
  - Redundancy and fail-safe mechanisms
- Optional Streamlit UI for easy interaction

---

## 📁 Project Structure
```
vehicle-architecture-ai-reviewer/
├── README.md
├── data/
│   └── sample_architectures.md         # Example architecture descriptions
│   └── example_runner.py
│   ...
├── src/
│   ├── llm_commenter.py                # Core logic to prompt LLM and get comments
│   ├── format_architecture_input.py    # Input formatter for LLM context
│   └── example_runner.py               # CLI script to run the tool
├── prompts/
│   └── architecture_review_prompt.txt  # Prompt template for LLM
```

---

## 🧠 How It Works
1. You provide a vehicle architecture description (e.g., ECUs, sensors, buses).
2. The script formats it and uses a prompt template to query an LLM (like OpenAI GPT-4).
3. The LLM responds with comments in a structured format.

---

## 🛠️ Getting Started
```bash
# Run the example CLI
python src/example_runner.py --input data/sample_architectures.md
```

---

## 🔍 Example Output
```

🔎 INPUT DESCRIPTION:

A compact electric vehicle features:

- A lightweight battery management system (BMS) ECU monitoring cell voltage and temperature.
- Single Motor Controller connected via CAN to the BMS.
- HVAC system controlled by a LIN-connected HVAC ECU.
- Vehicle uses a single Gateway ECU, no mention of redundancy.
- No external diagnostic interface described.

✅ OUTPUT:
🧠 **LLM-Generated Review**
------------------------------
Design Quality: 7/10

The vehicle architecture appears to be well-structured and modular, with separate ECUs for the BMS, Motor Controller, HVAC system, and Gateway. This separation of concerns is a good practice in automotive systems design.

However, there are some potential issues that need attention:

1. **Lack of redundancy**: The single Gateway ECU raises concerns about system reliability and fault tolerance. A failure or malfunction of the Gateway could have significant consequences on the entire vehicle's operation. Consider adding redundant Gateways to ensure continued functionality in case one fails.
2. **No external diagnostic interface**: The absence of an external diagnostic interface makes it difficult for technicians to diagnose issues without accessing the vehicle's internal systems. This can lead to increased downtime and repair costs. Consider adding a dedicated diagnostic port or using a standardized protocol like J1939 or CAN bus with a diagnostic module.
3. **CAN bus connection between BMS and Motor Controller**: While using a single CAN bus for the BMS and Motor Controller is efficient, it may not be suitable for all applications. In case of a fault in one ECU, it could propagate to the other, potentially causing damage or malfunctioning. Consider adding redundancy or using separate CAN buses for critical systems.
4. **LIN connection for HVAC system**: The use of LIN (Local Interconnect Network) for the HVAC system may not be the most efficient choice, especially if the system requires high-speed data transfer. Consider upgrading to a more suitable protocol like CAN bus or Ethernet.

Suggestions:

1. **Add redundant Gateways**: Install at least one redundant Gateway ECU to ensure continued operation in case of a failure.
2. **Implement external diagnostic interface**: Add a dedicated diagnostic port, such as J1939 or a CAN bus with a diagnostic module, to facilitate easier diagnosis and troubleshooting.
3. **Use separate CAN buses for critical systems**: Consider adding separate CAN buses for the BMS and Motor Controller to prevent propagation of faults in case of a failure.
4. **Upgrade HVAC system protocol**: Consider upgrading the HVAC system to use a more efficient protocol like CAN bus or Ethernet, depending on the specific requirements of the system.

Overall, the architecture has good potential, but addressing these concerns will improve its reliability, maintainability, and diagnostic capabilities.


## 📂 Examples
See output folder for sample architecture files and LLM-reviewed output reports (PDF & Markdown).

```

---


## 🤖 Prompt Template
```
You are a senior automotive systems engineer reviewing the following vehicle architecture. Provide comments on design quality, potential issues, and suggestions:

{ARCHITECTURE_TEXT}
```

---

## 📈 Future Extensions
- Add anomaly detection via rule-based validators
- Connect to vehicle signal databases for deeper checks
- Host Online