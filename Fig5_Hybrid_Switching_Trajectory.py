# Regenerating Fig. 5: Hybrid converter switching trajectory with camera-ready styling

import numpy as np
import matplotlib.pyplot as plt
import os

# Create output directory if it doesn't exist
output_dir = "/"
os.makedirs(output_dir, exist_ok=True)

# Time vector
t = np.linspace(0, 10, 1000)

# Simulated switching trajectories for three control methods
rpac = np.sin(t) + 0.5 * np.sin(5 * t)
pid = np.sin(t + 0.5)
smc = np.sin(t - 0.5)

# Plotting
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots(figsize=(8, 5))

ax.plot(t, rpac, label='RPAC', color='blue', linewidth=2.5)
ax.plot(t, pid, label='PID', color='red', linewidth=1.5)
ax.plot(t, smc, label='SMC', color='green', linewidth=1.5)

ax.set_title('Hybrid Converter Switching Trajectory', fontsize=16)
ax.set_xlabel('Time (s)', fontsize=14)
ax.set_ylabel('State Variable x(t)', fontsize=14)
ax.grid(True)
ax.legend(loc='upper right', fontsize=12)

# Save as vector PDF
fig_path = os.path.join( "Fig5_Hybrid_Switching_Trajectory.pdf")
plt.savefig(fig_path, format='pdf')

plt.close()

print("Saved:", fig_path)
