# ── Paste this cell into any notebook after running all 4 experiments ──────
import matplotlib.pyplot as plt
import numpy as np

# ── Results from your experiments (hardcoded from output) ───────────────────
results = {
    'Barabasi\nAlbert': {
        'gnn_mean': 11.24, 'gnn_std': 4.19,
        'greedy_mean': 9.67,  'greedy_std': 2.94,
        'approx_mean': 10.73, 'approx_std': 3.15,
        'gnn_ratio': 1.145,   'ap_ratio': 1.121,
        'f1': 0.180, 'precision': 0.173, 'recall': 0.189,
        'score_std': 0.0739,
        'beats_greedy': 8.0,  'beats_approx': 28.5,
    },
    'Erdos\nRenyi': {
        'gnn_mean': 14.32, 'gnn_std': 5.20,
        'greedy_mean': 11.54, 'greedy_std': 3.70,
        'approx_mean': 12.90, 'approx_std': 3.94,
        'gnn_ratio': 1.224,   'ap_ratio': 1.130,
        'f1': 0.114, 'precision': 0.105, 'recall': 0.125,
        'score_std': 0.0393,
        'beats_greedy': 0.5,  'beats_approx': 10.5,
    },
    'Bipartite': {
        'gnn_mean': 11.79, 'gnn_std': 3.84,
        'greedy_mean': 10.35, 'greedy_std': 2.65,
        'approx_mean': 11.43, 'approx_std': 3.12,
        'gnn_ratio': 1.124,   'ap_ratio': 1.105,
        'f1': 0.157, 'precision': 0.152, 'recall': 0.164,
        'score_std': 0.0563,
        'beats_greedy': 7.5,  'beats_approx': 16.5,
    },
    'Watts\nStrogatz': {
        'gnn_mean': 13.40, 'gnn_std': 4.28,
        'greedy_mean': 11.32, 'greedy_std': 3.36,
        'approx_mean': 13.39, 'approx_std': 3.92,
        'gnn_ratio': 1.179,   'ap_ratio': 1.189,
        'f1': 0.144, 'precision': 0.134, 'recall': 0.155,
        'score_std': 0.0372,
        'beats_greedy': 1.5,  'beats_approx': 32.0,
    },
}

graph_types  = list(results.keys())
n            = len(graph_types)
x            = np.arange(n)
w            = 0.25

C_GNN    = '#e74c3c'
C_GREEDY = '#3498db'
C_APPROX = '#2ecc71'
C_F1     = '#9b59b6'
C_PRE    = '#f39c12'
C_REC    = '#1abc9c'

plt.style.use('dark_background')
plt.rcParams.update({'font.family': 'monospace', 'axes.grid': True,
                     'grid.alpha': 0.2, 'grid.linestyle': '--'})

fig, axes = plt.subplots(2, 3, figsize=(17, 10))
fig.patch.set_facecolor('#0d0d1a')
for ax in axes.flatten():
    ax.set_facecolor('#12122a')

# ── 1. EDS Size comparison ──────────────────────────────────────────────────
ax = axes[0, 0]
gnn_m  = [results[g]['gnn_mean']    for g in graph_types]
gr_m   = [results[g]['greedy_mean'] for g in graph_types]
ap_m   = [results[g]['approx_mean'] for g in graph_types]
gnn_s  = [results[g]['gnn_std']     for g in graph_types]
gr_s   = [results[g]['greedy_std']  for g in graph_types]
ap_s   = [results[g]['approx_std']  for g in graph_types]

ax.bar(x - w, gnn_m, w, yerr=gnn_s, label='GNN',      color=C_GNN,    alpha=0.85, capsize=4, error_kw={'lw':1.5})
ax.bar(x,     gr_m,  w, yerr=gr_s,  label='Greedy',   color=C_GREEDY, alpha=0.85, capsize=4, error_kw={'lw':1.5})
ax.bar(x + w, ap_m,  w, yerr=ap_s,  label='2-Approx', color=C_APPROX, alpha=0.85, capsize=4, error_kw={'lw':1.5})
ax.set_xticks(x); ax.set_xticklabels(graph_types, fontsize=10)
ax.set_ylabel('Mean EDS Size'); ax.set_title('EDS Size  (lower = better)', fontweight='bold')
ax.legend(fontsize=9)

# ── 2. Approximation ratio ──────────────────────────────────────────────────
ax = axes[0, 1]
gnn_r = [results[g]['gnn_ratio'] for g in graph_types]
ap_r  = [results[g]['ap_ratio']  for g in graph_types]

ax.plot(graph_types, gnn_r, 'o-',  color=C_GNN,    lw=2.5, ms=9, label='GNN / Greedy')
ax.plot(graph_types, ap_r,  's--', color=C_APPROX, lw=2.5, ms=9, label='2-Approx / Greedy')
ax.axhline(1.0, color='white', lw=1.2, ls=':', label='Greedy = 1.0')
for i, (g, a) in enumerate(zip(gnn_r, ap_r)):
    ax.annotate(f'{g:.3f}', (graph_types[i], g), textcoords='offset points',
                xytext=(0, 8), ha='center', fontsize=8, color=C_GNN)
    ax.annotate(f'{a:.3f}', (graph_types[i], a), textcoords='offset points',
                xytext=(0, -14), ha='center', fontsize=8, color=C_APPROX)
ax.set_ylabel('Ratio'); ax.set_title('Approx Ratio vs Greedy  (< 1.0 = GNN wins)', fontweight='bold')
ax.legend(fontsize=9)

# ── 3. F1 / Precision / Recall ─────────────────────────────────────────────
ax = axes[0, 2]
f1_v  = [results[g]['f1']        for g in graph_types]
pre_v = [results[g]['precision'] for g in graph_types]
rec_v = [results[g]['recall']    for g in graph_types]

ax.bar(x - w, f1_v,  w, label='F1',        color=C_F1,  alpha=0.85)
ax.bar(x,     pre_v, w, label='Precision', color=C_PRE, alpha=0.85)
ax.bar(x + w, rec_v, w, label='Recall',    color=C_REC, alpha=0.85)
ax.set_xticks(x); ax.set_xticklabels(graph_types, fontsize=10)
ax.set_ylim(0, 0.35); ax.set_ylabel('Score')
ax.set_title('F1 / Precision / Recall vs Greedy Label', fontweight='bold')
ax.legend(fontsize=9)

# ── 4. Score STD (death spiral check) ──────────────────────────────────────
ax = axes[1, 0]
std_v  = [results[g]['score_std'] for g in graph_types]
colors = [C_GNN if s > 0.05 else '#ff6b6b' for s in std_v]
bars   = ax.bar(graph_types, std_v, color=colors, alpha=0.85, width=0.5, edgecolor='white', lw=0.5)
ax.axhline(0.05, color='#f39c12', lw=2, ls='--', label='0.05 threshold')
for bar, v in zip(bars, std_v):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.001,
            f'{v:.4f}', ha='center', va='bottom', fontsize=9,
            color='white' if v > 0.05 else '#ff6b6b')
ax.set_ylabel('Score STD'); ax.set_title('Score Diversity  (> 0.05 = no death spiral)', fontweight='bold')
ax.legend(fontsize=9)

# ── 5. GNN beats baselines (%) ─────────────────────────────────────────────
ax = axes[1, 1]
bg_v = [results[g]['beats_greedy']  for g in graph_types]
ba_v = [results[g]['beats_approx']  for g in graph_types]

ax.bar(x - w/2, bg_v, w, label='Beats Greedy',   color=C_GNN,    alpha=0.85)
ax.bar(x + w/2, ba_v, w, label='Beats 2-Approx', color=C_APPROX, alpha=0.85)
for i, (bg, ba) in enumerate(zip(bg_v, ba_v)):
    ax.text(i - w/2, bg + 0.5, f'{bg}%', ha='center', fontsize=8, color=C_GNN)
    ax.text(i + w/2, ba + 0.5, f'{ba}%', ha='center', fontsize=8, color=C_APPROX)
ax.set_xticks(x); ax.set_xticklabels(graph_types, fontsize=10)
ax.set_ylabel('% of test graphs'); ax.set_title('GNN Wins  (% of 200 test graphs)', fontweight='bold')
ax.legend(fontsize=9)

# ── 6. Summary radar-style bar (overall performance score) ─────────────────
ax = axes[1, 2]
# Composite score: lower ratio = better, higher beats% = better, higher F1 = better
# Normalise each to [0,1] and combine
ratio_score  = [max(0, 1 - (results[g]['gnn_ratio'] - 1) / 0.5)  for g in graph_types]
beats_score  = [results[g]['beats_greedy'] / 100                   for g in graph_types]
f1_score_n   = [results[g]['f1']                                   for g in graph_types]
std_score    = [min(results[g]['score_std'] / 0.1, 1.0)           for g in graph_types]

composite = [(r + b + f + s) / 4
             for r, b, f, s in zip(ratio_score, beats_score, f1_score_n, std_score)]

bar_colors = ['#e74c3c','#3498db','#2ecc71','#f39c12']
bars = ax.bar(graph_types, composite, color=bar_colors, alpha=0.88,
              width=0.5, edgecolor='white', lw=0.5)
for bar, v in zip(bars, composite):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.005,
            f'{v:.3f}', ha='center', fontsize=10, fontweight='bold')
ax.set_ylim(0, 0.6); ax.set_ylabel('Composite Score (higher = better)')
ax.set_title('Overall GNN Performance Score\n(ratio + beats% + F1 + score_std)', fontweight='bold')

# ── Final layout ────────────────────────────────────────────────────────────
fig.suptitle('GNN-EDS: Results Across All Graph Types  (1000 Train / 200 Test)',
             fontsize=15, fontweight='bold', y=1.01)
plt.tight_layout()
plt.savefig('gnn_eds_comparison.png', dpi=150, bbox_inches='tight',
            facecolor=fig.get_facecolor())
plt.show()
print('Saved → gnn_eds_comparison.png')
