from scipy.stats import entropy
p = [0.5, 0.5]
q = [0.8, 0.2]
print("Entropy:", entropy(p))
print("KL Divergence:", entropy(p, q))
