import numpy as np
import matplotlib.pyplot as plt

# 시간 설정
t = np.linspace(0, 10, 1000)

# 예시 trajectory (실제 시뮬레이션 결과로 교체 필요)
x_rpac = np.exp(-0.5 * t) * np.sin(2 * np.pi * t)
x_pid = np.exp(-0.3 * t) * np.sin(2 * np.pi * t + 0.5)
x_smc = np.exp(-0.4 * t) * np.sin(2 * np.pi * t + 0.2)

# 그래프 설정
plt.figure(figsize=(8, 5))
plt.plot(t, x_pid, 'r--', label='PID')
plt.plot(t, x_smc, 'g-.', label='SMC')
plt.plot(t, x_rpac, 'b', linewidth=2.5, label='RPAC')

plt.xlabel('Time (s)', fontsize=14)
plt.ylabel('$x_1(t)$', fontsize=14)
plt.title('Duffing Oscillator: State Trajectory', fontsize=15)
plt.grid(True)
plt.legend(loc='upper right', fontsize=12)
plt.tight_layout()

# PDF로 저장
plt.savefig('fig1_duffing_trajectory.pdf')
plt.show()
