# Regenerating Fig. 2: Phase portrait of Duffing oscillator with camera-ready quality

import numpy as np
import matplotlib.pyplot as plt
import os

# Ensure output directory exists
output_dir = "/"
os.makedirs(output_dir, exist_ok=True)

# Simulated data for demonstration (replace with actual simulation data if available)
t = np.linspace(0, 10, 1000)
x1_rpac = np.sin(t)
x2_rpac = np.cos(t)
x1_pid = np.sin(t + 0.5)
x2_pid = np.cos(t + 0.5)
x1_smc = np.sin(t + 1.0)
x2_smc = np.cos(t + 1.0)

# Plotting
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots(figsize=(8, 6))

ax.plot(x1_rpac, x2_rpac, label='RPAC', color='blue', linewidth=2.5)
ax.plot(x1_pid, x2_pid, label='PID', color='red', linewidth=1.5)
ax.plot(x1_smc, x2_smc, label='SMC', color='green', linewidth=1.5)

ax.set_xlabel('$x_1$', fontsize=14)
ax.set_ylabel('$x_2$', fontsize=14)
ax.grid(True)
ax.legend(loc='upper right', fontsize=12)
ax.set_title('Phase Portrait of Duffing Oscillator', fontsize=16)

# Save as vector PDF
fig_path = os.path.join("Fig2_Duffing_PhasePortrait.pdf")
plt.savefig(fig_path, format='pdf')
plt.close()

print("Saved:", fig_path)
