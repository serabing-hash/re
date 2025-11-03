# Phase-Aligned Resonant Control (RPAC) – Simulation Code

This repository contains all Python scripts used to generate the simulation figures in the paper:

**"Phase-Aligned Control Framework for Nonlinear Resonant Systems"**  
Accepted to IEEE [Access/TAC], 2025.

## 📊 Figures Included

| Figure | Description |
|--------|-------------|
| Fig. 1 | Duffing oscillator – \( x_1(t) \) trajectory comparison (PID, SMC, RPAC)  
| Fig. 2 | Duffing oscillator – Phase portrait \( x_1 \) vs \( x_2 \)  
| Fig. 3 | Van der Pol oscillator – Limit cycle visualization  
| Fig. 4 | Phase error \( |\phi_i - \phi_u| \) over time  
| Fig. 5 | Hybrid converter – Switching trajectory  
| Fig. 6 | Control input \( u(t) \) comparison  
| Fig. 7 | Monte Carlo simulation – 100 randomized initial conditions

All figures are rendered in **vector-quality PDF format** with grid lines, enlarged axis labels, and clear legends.

## 🧠 Requirements

- Python 3.8+
- `numpy`, `matplotlib`, `scipy`
- Optional: `seaborn` for enhanced styling

Install dependencies:
```bash
pip install -r requirements.txt
