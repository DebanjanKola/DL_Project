# DL
DL Project
# [cite_start]Graph Neural Networks for Approximating Vertex Cover and Matching Problems [cite: 1]

[cite_start]**Team:** Neurox [cite: 2]  
[cite_start]**Members:** Debanjan Kola & Debrup Chatterjee [cite: 2]  
[cite_start]**Institution:** Ramakrishna Mission Vivekananda Educational and Research Institute [cite: 3]  
[cite_start]**Date:** February 2026 [cite: 4]  

---

## 📌 Project Overview
[cite_start]This project explores the use of Graph Neural Networks (GNNs) to approximate solutions for two classic graph problems: **Minimum Vertex Cover** and **Maximum Matching**[cite: 151, 152, 153, 154]. 

[cite_start]Because exact classical optimization for NP-hard problems (like Minimum Vertex Cover) becomes computationally expensive on large graphs [cite: 159, 160, 165][cite_start], we leverage GNNs to learn optimization heuristics directly from the graph's structural patterns[cite: 171, 172, 173].

## 🎯 Objectives
* [cite_start]**Vertex Cover:** Formulated as a node classification problem (outputting the probability of each node being in the cover)[cite: 239, 240, 241].
* [cite_start]**Maximum Matching:** Formulated as an edge classification problem (predicting whether an edge belongs to the matching)[cite: 250, 251, 252].
* [cite_start]**Generalization:** Train the GNN on smaller graphs where optimal solutions can be computed, and test its generalization capabilities on larger, unseen graphs[cite: 354, 355, 356].

## 🛠 Methodology
1.  [cite_start]**Dataset Generation:** Generating diverse synthetic datasets using Python's `NetworkX` library[cite: 291, 293]. [cite_start]This includes d-regular graphs, small-world graphs, and random graphs[cite: 294, 295, 296, 297]. [cite_start]We initially focus on d-regular graphs for a controlled testing environment[cite: 156, 157].
2.  [cite_start]**Label Generation:** Computing exact optimal solutions for small graphs to serve as training labels[cite: 209, 210].
3.  [cite_start]**Feature Extraction:** Converting NetworkX graphs to adjacency formats and extracting node features (e.g., degrees, embeddings) for PyTorch Geometric[cite: 302, 303, 304, 309].
4.  [cite_start]**Model Training:** Passing features through neighborhood aggregation layers to update embeddings, followed by supervised classification for nodes and edges[cite: 264, 265, 279, 280, 283].

## 👥 Division of Work
* [cite_start]**Debanjan Kola:** Focuses on the Vertex Cover dataset preparation, designing the node-based GNN prediction model, and analyzing structured (d-regular) graphs[cite: 367, 368, 369, 370].
* [cite_start]**Debrup Chatterjee:** Focuses on the Matching dataset preparation, edge-based GNN prediction model design, and implementing matching constraints[cite: 371, 372, 373, 374].
* [cite_start]**Joint Efforts:** NetworkX dataset generation, overarching GNN architecture design, model training pipelines, and experimental analysis[cite: 375, 376, 377, 378].
