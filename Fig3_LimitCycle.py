# Regenerating Fig. 3: Van der Pol oscillator limit cycle with camera-ready quality

import numpy as np
import matplotlib.pyplot as plt
import os

# Ensure output directory exists
output_dir = "/"
os.makedirs(output_dir, exist_ok=True)

# Simulated data for demonstration (replace with actual simulation results)
t = np.linspace(0, 20, 1000)
x_rpac = np.sin(t)
y_rpac = np.cos(t)

x_pid = np.sin(t + 0.5)
y_pid = np.cos(t + 0.5)

x_smc = np.sin(t + 1.0)
y_smc = np.cos(t + 1.0)

# Plotting
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots(figsize=(8, 6))

ax.plot(x_rpac, y_rpac, label='RPAC', color='blue', linewidth=2.5)
ax.plot(x_pid, y_pid, label='PID', color='red', linewidth=1.5)
ax.plot(x_smc, y_smc, label='SMC', color='green', linewidth=1.5)

ax.set_xlabel('x₁ (Position)', fontsize=14)
ax.set_ylabel('x₂ (Velocity)', fontsize=14)
ax.grid(True)
ax.legend(loc='upper right', fontsize=12)

plt.title('Limit Cycle of Van der Pol Oscillator', fontsize=16)
plt.tight_layout()

# Save as vector PDF
pdf_path = os.path.join( "Fig3_LimitCycle.pdf")
plt.savefig(pdf_path, format='pdf')

print("Saved:", pdf_path)
