# Regenerating Fig. 4: Phase Error vs Time with Camera-Ready Quality

import numpy as np
import matplotlib.pyplot as plt
import os

# Create output directory if it doesn't exist
output_dir = "/"
os.makedirs(output_dir, exist_ok=True)

# Simulated time vector
t = np.linspace(0, 50, 500)

# Simulated phase error data for three controllers
phase_error_rpac = 0.2 * np.exp(-0.1 * t) * np.cos(0.5 * t)
phase_error_pid = 0.4 * np.exp(-0.05 * t) * np.cos(0.6 * t)
phase_error_smc = 0.3 * np.exp(-0.08 * t) * np.cos(0.4 * t)

# Create the plot
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots(figsize=(8, 5))

ax.plot(t, np.abs(phase_error_rpac), label='RPAC', color='blue', linewidth=2.5)
ax.plot(t, np.abs(phase_error_pid), label='PID', color='red', linewidth=2)
ax.plot(t, np.abs(phase_error_smc), label='SMC', color='green', linewidth=2)

ax.set_xlabel('Time (s)', fontsize=14)
ax.set_ylabel(r'Phase Error $|\phi_i - \phi_u|$ (rad)', fontsize=14)
ax.grid(True)
ax.legend(loc='upper right', fontsize=12)
ax.tick_params(axis='both', labelsize=12)
fig.tight_layout()

# Save as vector PDF
pdf_path = os.path.join( "Fig4_PhaseError.pdf")
fig.savefig(pdf_path, format='pdf')

print("Saved:", pdf_path)
