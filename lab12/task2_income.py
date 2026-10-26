import numpy as np; np.random.seed(333)
i = np.random.randint(10_000, 50_000, (3, 10))
t = np.r_[[.3] * 4, [.4] * 3, [.3] * 3]
n = i * (1 - t)

print("Income:\n", i,
      "\n\nNet income (30% tax):\n", i * .7,
      "\n\nNet income (updated tax):\n", n,
      "\n\nApr-Jun:\n", n[:, 3:6], sep="")