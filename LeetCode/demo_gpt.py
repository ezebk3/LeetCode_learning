import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# 生成随机数据
np.random.seed(42)  # 设置随机种子以保证结果可复现

group1 = np.random.normal(loc=20, scale=5, size=4)
group2 = np.random.normal(loc=22, scale=5, size=4)
group3 = np.random.normal(loc=25, scale=5, size=4)

data = [group1, group2, group3]

# 进行显著性检验
t_stat_12, p_value_12 = stats.ttest_ind(group1, group2)
t_stat_13, p_value_13 = stats.ttest_ind(group1, group3)
t_stat_23, p_value_23 = stats.ttest_ind(group2, group3)

# 打印显著性检验结果
print(f"Group1 vs Group2: t-statistic = {t_stat_12:.4f}, p-value = {p_value_12:.4f}")
print(f"Group1 vs Group3: t-statistic = {t_stat_13:.4f}, p-value = {p_value_13:.4f}")
print(f"Group2 vs Group3: t-statistic = {t_stat_23:.4f}, p-value = {p_value_23:.4f}")

# 创建柱状图
labels = ['Col1', 'Col2', 'Col3', 'Col4']
x = np.arange(len(labels))  # 标签位置
width = 0.25  # 柱宽

fig, ax = plt.subplots()
rects1 = ax.bar(x - width, group1, width, label='Group 1')
rects2 = ax.bar(x, group2, width, label='Group 2')
rects3 = ax.bar(x + width, group3, width, label='Group 3')

# 添加一些文本标签
ax.set_xlabel('Columns')
ax.set_ylabel('Values')
ax.set_title('Three Groups Comparison')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

# 添加显著性标记
def add_significance(ax, x1, x2, y, h, p):
    bar_x = [x1, x1, x2, x2]
    bar_y = [y, y+h, y+h, y]
    ax.plot(bar_x, bar_y, color='black')
    significance = 'n.s.'
    if p < 0.05:
        significance = '*'
    if p < 0.01:
        significance = '**'
    if p < 0.001:
        significance = '***'
    ax.text((x1+x2)*.5, y+h, significance, ha='center', va='bottom', color='black')

# 添加显著性检验结果到图表
y_max = max(max(group1), max(group2), max(group3)) + 2
add_significance(ax, x[0] - width, x[0], y_max, 1, p_value_12)
add_significance(ax, x[0] - width, x[0] + width, y_max + 2, 1, p_value_13)
add_significance(ax, x[0], x[0] + width, y_max + 4, 1, p_value_23)

fig.tight_layout()

plt.show()