# Generating Fig. 7: Monte Carlo simulation with 100 x₁(t) trajectories and mean envelope

import numpy as np
import matplotlib.pyplot as plt
import os

# Set plot style
plt.style.use('seaborn-v0_8')
font_size = 14

# Simulation parameters
num_trials = 100
time = np.linspace(0, 10, 1000)
x1_trajectories = []

# Generate synthetic trajectories (e.g., decaying sinusoids with noise)
for _ in range(num_trials):
    decay = np.exp(-0.3 * time)
    freq = 2 * np.pi * 1.0
    phase = np.random.uniform(0, 2*np.pi)
    noise = np.random.normal(0, 0.05, size=time.shape)
    x1 = decay * np.sin(freq * time + phase) + noise
    x1_trajectories.append(x1)

x1_trajectories = np.array(x1_trajectories)
mean_trajectory = np.mean(x1_trajectories, axis=0)

# Create plot
fig, ax = plt.subplots(figsize=(10, 6))
for traj in x1_trajectories:
    ax.plot(time, traj, color='gray', linewidth=0.5, alpha=0.6)

ax.plot(time, mean_trajectory, color='blue', linewidth=2.5, label='Mean Trajectory')

ax.set_title('Monte Carlo Simulation: $x_1(t)$ Envelope', fontsize=font_size + 2)
ax.set_xlabel('Time (s)', fontsize=font_size)
ax.set_ylabel('$x_1(t)$', fontsize=font_size)
ax.grid(True)
ax.legend(fontsize=font_size)
ax.tick_params(labelsize=font_size)

# Save as PDF
output_path = "Fig7_MonteCarlo_x1.pdf"
fig.savefig(output_path, format='pdf', bbox_inches='tight')

print("Saved:", output_path)
