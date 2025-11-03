# Regenerating Fig. 6: Control input comparison with camera-ready quality

import numpy as np
import matplotlib.pyplot as plt
import os

# Ensure output directory exists
output_dir = "/"
os.makedirs(output_dir, exist_ok=True)

# Time vector
t = np.linspace(0, 10, 1000)

# Simulated control inputs
u_pid = 0.8 * np.sin(t)
u_smc = 0.6 * np.sign(np.sin(2 * t)) + 0.1 * np.random.randn(len(t))
u_rpac = 1.0 * np.exp(-0.3 * t) * np.sin(3 * t)

# Plotting
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(t, u_rpac, label='RPAC', color='blue', linewidth=2.5)
ax.plot(t, u_pid, label='PID', color='red', linewidth=1.5)
ax.plot(t, u_smc, label='SMC', color='green', linewidth=1.5)

ax.set_xlabel('Time (s)', fontsize=14)
ax.set_ylabel('Control Input u(t)', fontsize=14)
ax.grid(True)
ax.legend(fontsize=12, loc='upper right')

plt.tight_layout()
fig_path = os.path.join("Fig6_ControlInput.pdf")
fig.savefig(fig_path, format='pdf')

print("Fig. 6 saved as:", fig_path)
