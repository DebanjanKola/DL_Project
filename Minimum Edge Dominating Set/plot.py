import matplotlib.pyplot as plt
import numpy as np

# ── Replace these with your ACTUAL hybrid results ──────────────────────────
results = {
    'Barabasi\nAlbert': {
        'hybrid_mean': 9.20,  'hybrid_std': 2.80,   # GNN + Greedy
        'approx_mean': 10.73, 'approx_std': 3.15,
    },
    'Erdos\nRenyi': {
        'hybrid_mean': 11.10, 'hybrid_std': 3.10,
        'approx_mean': 12.90, 'approx_std': 3.94,
    },
    'Bipartite': {
        'hybrid_mean': 10.00, 'hybrid_std': 2.50,
        'approx_mean': 11.43, 'approx_std': 3.12,
    },
    'Watts\nStrogatz': {
        'hybrid_mean': 11.20, 'hybrid_std': 3.00,
        'approx_mean': 13.39, 'approx_std': 3.92,
    },
}

# ── Setup ─────────────────────────────────────────────────────────────────
graph_types = list(results.keys())
x = np.arange(len(graph_types))
w = 0.35

hyb_m = [results[g]['hybrid_mean'] for g in graph_types]
ap_m  = [results[g]['approx_mean'] for g in graph_types]

hyb_s = [results[g]['hybrid_std'] for g in graph_types]
ap_s  = [results[g]['approx_std'] for g in graph_types]

# ── Plot ──────────────────────────────────────────────────────────────────
plt.style.use('default')  # WHITE BACKGROUND

fig, ax = plt.subplots(figsize=(8, 5))

ax.bar(x - w/2, hyb_m, w, yerr=hyb_s, label='GNN + Greedy (Hybrid)', capsize=4)
ax.bar(x + w/2, ap_m,  w, yerr=ap_s,  label='2-Approximation', capsize=4)

ax.set_xticks(x)
ax.set_xticklabels(graph_types)
ax.set_ylabel('Mean EDS Size')
ax.set_title('Hybrid (GNN + Greedy) vs 2-Approx (Lower = Better)')
ax.legend()

plt.tight_layout()
plt.savefig('hybrid_vs_approx.png', dpi=150)
plt.show()

print("Saved → hybrid_vs_approx.png")