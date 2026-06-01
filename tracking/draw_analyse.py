import matplotlib.pyplot as plt
from matplotlib import rc
import numpy as np
import matplotlib

# x = np.linspace(0, 10, 501)
#
# fig = plt.figure()
# axes = fig.subplots(nrows=1, ncols=2)
# axes[0].plot(x, np.sin(x), color='k', label="sin(x)")
# axes[0].plot(x, np.tan(x), color='r', label="sin(x)")
# axes[1].plot(x, np.cos(x), color='b', label="cos(x)")
#
# lines = []
# labels = []
# for ax in fig.axes:
#     axLine, axLabel = ax.get_legend_handles_labels()
#     lines.extend(axLine)
#     labels.extend(axLabel)
#
# fig.legend(lines, labels,
#            loc='upper right')  # 图例的位置，bbox_to_anchor=(0.5, 0.92),
# plt.show()


# 创建数据


import matplotlib.lines as mlines


# def top_param():
#     import matplotlib.pyplot as plt
#     from matplotlib import rc

#     rc('font', family='serif')
#     rc('mathtext', default='regular')

#     # ===== 数据 =====
#     # K = ['4', '5', '6', '7']
#     K = ['1', '2', '3', '4', 'All']

#     SR_rgbt = [52.6, 53.7, 54.1, 53.6, 53.7]
#     SR_rgbd = [56.7, 59.4, 60.6, 57.8, 58.8]
#     SR_rgbe = [59.0, 58.8, 60.1, 59.4, 59.7]
#     # Trainable = [0.0, 0.0, 0.59, 0.0, 0.0]

#     # ===== 画布 =====
#     fig, ax = plt.subplots(figsize=(6.2, 5.2))

#     # ===== 左轴：性能 =====
#     l1, = ax.plot(
#         K, SR_rgbt, marker='o', color='#1f77b4',
#         linewidth=2.4, label='LasHeR (SR)'
#     )
#     l2, = ax.plot(
#         K, SR_rgbd, marker='s', color='#ff7f0e',
#         linewidth=2.4, label='DepthTrack (F)'
#     )
#     l3, = ax.plot(
#         K, SR_rgbe, marker='^', color='#2ca02c',
#         linewidth=2.4, label='VisEvent (MSR)'
#     )

#     ax.set_ylabel('Tracking Performance (%)', fontsize=15)
#     ax.set_ylim(52.5, 61.0)

#     # ===== 右轴：参数量 =====
#     ax2 = ax.twinx()
#     # l4, = ax2.plot(
#     #     K, Trainable, linestyle='-.', marker='d',
#     #     color='gray', linewidth=2.2, label='Trainable Params (M)'
#     # )
#     # ax2.set_ylabel('Parameters (Million)', fontsize=15)
#     # ax2.set_ylim(0.004, 0.05)

#     # ===== 统一 Legend =====
#     # lines = [l1, l2, l3, l4]
#     lines = [l1, l2, l3]
#     labels = [l.get_label() for l in lines]
#     # ax.legend(
#     #     lines, labels,
#     #     loc='upper left',
#     #     fontsize=12,
#     #     frameon=False
#     # )

#     ax.legend(
#     lines, labels,
#     loc='upper center',
#     bbox_to_anchor=(0.5, 1.18),
#     ncol=2,
#     fontsize=12,
#     frameon=False
#     )


#     # ===== 网格 & 坐标轴美化 =====
#     ax.grid(
#         axis='y',
#         linestyle='--',
#         linewidth=0.6,
#         alpha=0.6
#     )

#     ax.set_xlabel('Top-K', fontsize=16)

#     ax.tick_params(axis='both', labelsize=12)
#     ax2.tick_params(axis='y', labelsize=12)

#     # 去除多余边框
#     ax.spines['top'].set_visible(False)
#     ax2.spines['top'].set_visible(False)

#     plt.tight_layout()
#     # plt.show()
#     plt.savefig('top_k.pdf')

def top_param():
    import matplotlib.pyplot as plt
    from matplotlib import rc

    # ===== 全局字体风格（论文级）=====
    rc('font', family='serif')
    rc('mathtext', default='regular')

    # ===== 数据 =====
    K = ['1', '2', '3', '4', 'All']

    SR_rgbt = [52.6, 53.7, 54.1, 53.6, 53.7]
    SR_rgbd = [56.7, 59.4, 60.6, 57.8, 58.8]
    SR_rgbe = [59.0, 58.8, 60.1, 59.4, 59.7]

    # ===== 画布 =====
    fig, ax = plt.subplots(figsize=(6.6, 5.6))

    # ===== 折线 =====
    l1, = ax.plot(
        K, SR_rgbt,
        marker='o', markersize=8,
        linewidth=2.8,
        color='#1f77b4',
        label='LasHeR (SR)'
    )
    l2, = ax.plot(
        K, SR_rgbd,
        marker='s', markersize=8,
        linewidth=2.8,
        color='#ff7f0e',
        label='DepthTrack (F)'
    )
    l3, = ax.plot(
        K, SR_rgbe,
        marker='^', markersize=8,
        linewidth=2.8,
        color='#2ca02c',
        label='VisEvent (MSR)'
    )

    # ===== 轴标签（最大一档 + 加粗）=====
    ax.set_xlabel(
        'Top-K',
        fontsize=20,
        fontweight='bold'
    )
    ax.set_ylabel(
        'Tracking Performance (%)',
        fontsize=20,
        fontweight='bold'
    )

    ax.set_ylim(52.5, 61.0)

    # ===== Legend（显著但不抢主轴）=====
    ax.legend(
        loc='upper center',
        bbox_to_anchor=(0.5, 1.22),
        ncol=2,
        fontsize=16,
        frameon=False,
        handlelength=2.0
    )

    # ===== 网格 =====
    ax.grid(
        axis='y',
        linestyle='--',
        linewidth=0.7,
        alpha=0.6
    )

    # ===== Tick labels（关键放大点）=====
    ax.tick_params(
        axis='both',
        which='major',
        labelsize=15,
        width=1.2,
        length=6
    )

    # ===== 去除多余边框 =====
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    plt.tight_layout()
    # plt.show()
    plt.savefig('top_k.pdf', dpi=300, bbox_inches='tight')


def expert_num():
    import matplotlib.pyplot as plt
    from matplotlib import rc

    # ===== 全局字体风格（论文级）=====
    rc('font', family='serif')
    rc('mathtext', default='regular')

    # ===== 数据 =====
    K = ['4', '5', '6', '7']

    SR_rgbt = [53.4, 53.3, 54.1, 53.1]
    SR_rgbd = [57.7, 59.2, 60.6, 58.8]
    SR_rgbe = [59.7, 59.4, 60.1, 59.1]

    # ===== 画布 =====
    fig, ax = plt.subplots(figsize=(6.6, 5.6))

    # ===== 折线 =====
    l1, = ax.plot(
        K, SR_rgbt,
        marker='o', markersize=8,
        linewidth=2.8,
        color='#1f77b4',
        label='LasHeR (SR)'
    )
    l2, = ax.plot(
        K, SR_rgbd,
        marker='s', markersize=8,
        linewidth=2.8,
        color='#ff7f0e',
        label='DepthTrack (F)'
    )
    l3, = ax.plot(
        K, SR_rgbe,
        marker='^', markersize=8,
        linewidth=2.8,
        color='#2ca02c',
        label='VisEvent (MSR)'
    )

    # ===== 轴标签（最大一档 + 加粗）=====
    ax.set_xlabel(
        'Number of Experts',
        fontsize=20,
        fontweight='bold'
    )
    ax.set_ylabel(
        'Tracking Performance (%)',
        fontsize=20,
        fontweight='bold'
    )

    ax.set_ylim(53.0, 61.0)

    # ===== Legend（显著但不抢主轴）=====
    ax.legend(
        loc='upper center',
        bbox_to_anchor=(0.5, 1.22),
        ncol=2,
        fontsize=16,
        frameon=False,
        handlelength=2.0
    )

    # ===== 网格 =====
    ax.grid(
        axis='y',
        linestyle='--',
        linewidth=0.7,
        alpha=0.6
    )

    # ===== Tick labels（关键放大点）=====
    ax.tick_params(
        axis='both',
        which='major',
        labelsize=15,
        width=1.2,
        length=6
    )

    # ===== 去除多余边框 =====
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    plt.tight_layout()
    # plt.show()
    plt.savefig('expert_num.pdf', dpi=300, bbox_inches='tight')

if __name__ == '__main__':

    top_param()
    expert_num()