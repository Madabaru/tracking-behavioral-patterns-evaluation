import matplotlib.pyplot as plt
import numpy as np


with open("test.txt", "rb") as f:
    d1 = f.read().decode()

with open("test2.txt", "rb") as f:
    d2 = f.read().decode()

d1 = d1.split(",")[:-1]
d1 = [float(i) for i in d1]

d2 = d2.split(",")[:-1]
d2 = [float(i) for i in d2]

plt.style.use('ggplot')
fig, (ax1, ax2) = plt.subplots(1, 2, sharey=True, figsize=(8,4))
ax1.patch.set_facecolor('#e0e0e0')
ax2.patch.set_facecolor('#e0e0e0')

ax1.hist(d1, [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5], color="#3f51b5")
ax1.set(ylabel="Frequency")
ax1.set(xlabel="Duration [h]")
ax1.set_xticks([0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5])
ax1.set_title("Browsing Dataset", fontsize=12)

ax2.hist(d2, [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5], color="#3f51b5")
ax2.set(xlabel="Duration [h]")
ax2.set_xticks([0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5])
ax2.set_title("Mobility Dataset", fontsize=12)

plt.yticks([0, 10000, 20000, 30000, 40000, 50000, 60000, 70000])

plt.tight_layout()
plt.show()
# plt.savefig(f"images/duration_distribution.pdf", format="pdf")

