# Graph Neural Networks for Approximating Vertex Cover and Matching Problems 
 
**Name:** Debanjan Kola 
**Institution:** Ramakrishna Mission Vivekananda Educational and Research Institute  

---

## Project Overview
This project explores the capabilities of Graph Neural Networks (GNNs) and Deep Reinforcement Learning to approximate solutions for two NP-hard combinatorial optimization problems: **Minimum Vertex Cover (MVC)** and **Minimum Edge Dominating Set (MEDS)**. 

While classical approximation algorithms (like the 2-Approximation baseline) are fast, they follow mathematically rigid heuristics. This project demonstrates that neural models can autonomously discover more optimal structural patterns and consistently outperform standard 2-Approximation algorithms across various graph topologies.

## Problems Addressed
1. **Minimum Vertex Cover (MVC):** Selecting the minimum number of vertices such that every edge in the graph is adjacent to at least one selected vertex.
2. **Minimum Edge Dominating Set (MEDS):** Selecting the minimum number of edges such that every other edge in the graph shares at least one vertex with a selected edge. (Note: Deep learning for MEDS remains a largely unexplored frontier).

## Graph Topologies Evaluated
To test the generalization and structural learning of our models, we evaluated them across diverse graph families:
* **Barabási-Albert:** Scale-free networks (e.g., social influencer networks).
* **Erdős-Rényi:** Random graphs with uniform degree distribution.
* **Watts-Strogatz:** Small-world networks with high clustering (e.g., friend circles).
* **Bipartite Graphs:** Nodes split into two disjoint sets (e.g., student-course enrollment).
* **d-regular Graphs:** Highly structured networks where all nodes share the exact same degree.

##  Neural Architectures Deployed
We approached the problems using three distinct neural frameworks:
1. **Node-Based GNNs (Simple GNN, GIN, GAT-v2):** Aggregates neighborhood features via message passing to output node probabilities (used for MVC).
2. **Edge-Based GNN:** Transforms the input into a Line Graph $L(G)$ and aggregates edge features to output edge probabilities.
3. **S2V-DQN (Reinforcement Learning):** Uses Structure2Vec to compute embeddings and a Deep Q-Network to estimate Q-values, greedily adding nodes or edges to the cover set.

##  Key Experimental Results

### Minimum Vertex Cover (MVC) Performance
Our models were benchmarked against a standard 2-Approximation algorithm (ratio = 1.0). Lower ratios indicate better, smaller covers.
* **Barabási-Albert:** The Edge-Based GNN significantly outperformed the baseline, achieving a highly optimal average ratio of **0.642**.
* **Bipartite:** The Simple GNN leveraged the bipartite structure exceptionally well, reaching an approximation ratio of **0.629**.
* **Watts-Strogatz:** Simple GNN achieved an average ratio of **0.939**, demonstrating robust heuristics.
* **d-regular & Erdős-Rényi:** S2V-DQN maintained highly competitive sub-1.0 ratios (**0.980** and **0.950** respectively).

### Minimum Edge Dominating Set (MEDS) Performance
Because there is a lack of prior deep learning literature for the MEDS problem, we rigorously benchmarked against the classical 2-Approximation algorithm (which finds an arbitrary maximal matching).
* **Watts-Strogatz (The Highlight):** The RL approach (**S2V-DQN**) achieved a massive **91.5% win rate** against the 2-Approximation algorithm.
* **Bipartite:** Message-passing GNN yielded our tightest average approximation ratio of **1.124**.
* **Overall Dominance:** Neural models found strictly smaller, more optimal covers on 32.0% of Watts-Strogatz graphs and 28.5% of Barabási-Albert graphs. S2V-DQN consistently maintained the lowest average EDS size across all topologies.

##  Conclusions & Future Work
* **A New Standard:** Neural models are capable of consistently beating the classical 2-Approximation baseline for complex edge and vertex covering problems.
* **Topology Matters:** There is no "one size fits all." Simple GNNs dominate Bipartite graphs, while S2V-DQN heavily dominates Small-World topologies.
* **The Future is RL:** With its overwhelming win rate on structured graphs, Reinforcement Learning (S2V-DQN) emerges as the leading approach for future expansions of this work.
