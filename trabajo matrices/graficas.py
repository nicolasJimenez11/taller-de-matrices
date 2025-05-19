import matplotlib.pyplot as plt

def plot_alternating_solid_line(ax, x, y, color, marker, label):
    for i in range(len(x) - 1):
        ax.plot(x[i:i+2], y[i:i+2], color=color, marker=marker,
                linestyle='-', linewidth=2, markersize=5)
    ax.plot(x[-1], y[-1], color=color, marker=marker,
            linestyle='', markersize=5, label=label)

# Datos
tamanos = [128, 256, 512, 1024]
memoria_naive = [0.38, 1.5, 6, 24]
tiempo_naive = [770, 5826, 46540, 396615]
memoria_strassen = [1.312, 5.25, 21, 84]
tiempo_strassen = [1180, 8320, 59830, 440634]

fig, axes = plt.subplots(1, 3, figsize=(22, 6), sharey=False)

# --- Gráfica Naive ---
ax1 = axes[0]
ax1.set_xlabel('Tamaño de matriz (n)')
ax1.set_ylabel('Tiempo (ms)', color='tab:red')
ax1.plot(tamanos, tiempo_naive, color='tab:red', marker='o', linestyle='-', label='Tiempo Naive', linewidth=2)
ax1.tick_params(axis='y', labelcolor='tab:red')
ax1.set_xticks(tamanos)
ax1.set_title('Naive')

ax2 = ax1.twinx()
ax2.set_ylabel('Memoria (MB)', color='tab:green')
plot_alternating_solid_line(ax2, tamanos, memoria_naive, color='tab:green', marker='D', label='Memoria Naive')
ax2.tick_params(axis='y', labelcolor='tab:green')

lines_1, labels_1 = ax1.get_legend_handles_labels()
lines_2, labels_2 = ax2.get_legend_handles_labels()
ax1.legend(lines_1 + lines_2, labels_1 + labels_2, loc='upper left')

# --- Gráfica Strassen ---
ax3 = axes[1]
ax3.set_xlabel('Tamaño de matriz (n)')
ax3.set_ylabel('Tiempo (ms)', color='tab:blue')
ax3.plot(tamanos, tiempo_strassen, color='tab:blue', marker='o', linestyle='-', label='Tiempo Strassen', linewidth=2)
ax3.tick_params(axis='y', labelcolor='tab:blue')
ax3.set_xticks(tamanos)
ax3.set_title('Strassen')

ax4 = ax3.twinx()
ax4.set_ylabel('Memoria (MB)', color='tab:purple')
plot_alternating_solid_line(ax4, tamanos, memoria_strassen, color='tab:purple', marker='D', label='Memoria Strassen')
ax4.tick_params(axis='y', labelcolor='tab:purple')

lines_3, labels_3 = ax3.get_legend_handles_labels()
lines_4, labels_4 = ax4.get_legend_handles_labels()
ax3.legend(lines_3 + lines_4, labels_3 + labels_4, loc='upper left')

# --- Gráfica Comparativa ---
ax5 = axes[2]
ax5.set_xlabel('Tamaño de matriz (n)')
ax5.set_ylabel('Tiempo (ms)')
ax5.plot(tamanos, tiempo_naive, color='tab:red', marker='o', linestyle='-', label='Tiempo Naive', linewidth=2)
ax5.plot(tamanos, tiempo_strassen, color='tab:blue', marker='o', linestyle='-', label='Tiempo Strassen', linewidth=2)
ax5.set_xticks(tamanos)
ax5.set_title('Comparativa')

ax6 = ax5.twinx()
ax6.set_ylabel('Memoria (MB)')
ax6.plot(tamanos, memoria_naive, color='tab:green', marker='D', linestyle='-', label='Memoria Naive', linewidth=2, markersize=5)
ax6.plot(tamanos, memoria_strassen, color='tab:purple', marker='D', linestyle='-', label='Memoria Strassen', linewidth=2, markersize=5)

# Leyenda combinada para la comparativa
lines_5, labels_5 = ax5.get_legend_handles_labels()
lines_6, labels_6 = ax6.get_legend_handles_labels()
ax5.legend(lines_5 + lines_6, labels_5 + labels_6, loc='upper left')

plt.suptitle('Comparación Tiempo y Memoria - Naive vs Strassen (Python)')
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.subplots_adjust(wspace=0.35)  # Separación entre gráficas
plt.show()