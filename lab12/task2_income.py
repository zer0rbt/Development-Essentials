import numpy as np
np.random.seed(333)
i, t, _ = np.random.randint(10_000, 50_000, (3, 10)), np.r_[[.3] * 4, [.4] * 3, [.3] * 3], np.set_printoptions(linewidth=120)
print("income", i, "net, 30%", i * .7, "net, 40% in May-Jul", n := i * (1 - t), "Apr-Jun", n[:, 3:6], sep="\n")