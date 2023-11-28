
import matplotlib.pyplot as plt

# 数据
cluster_labels = ['Cluster_Label: 0', 'Cluster_Label: 1', 'Cluster_Label: 2', 'Cluster_Label: 3', 'Cluster_Label: 4']
expert_counts = [151, 77, 116, 11, 25]
densities = [2.49, 2.05, 2.94, 0.32, 0.61]

# 创建图形
fig, ax1 = plt.subplots(figsize=(10, 6))

# 绘制专家数量（左 Y 轴）
ax1.bar(cluster_labels, expert_counts, color='b', alpha=0.7, label='The number of experts')
ax1.set_xlabel('Cluster_Label')
ax1.set_ylabel('The number of experts', color='b')
ax1.tick_params(axis='y', labelcolor='b')

# 创建第二个 Y 轴
ax2 = ax1.twinx()

# 绘制密度（右 Y 轴）
ax2.plot(cluster_labels, densities, color='r', marker='o', linestyle='-', label='density')
ax2.set_ylabel('density', color='r')
ax2.tick_params(axis='y', labelcolor='r')

# 添加图例
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(lines + lines2, labels + labels2, loc='upper right')

# 显示图形
plt.title('The number and density of experts')
plt.grid(axis='y')
plt.tight_layout()
plt.show()
