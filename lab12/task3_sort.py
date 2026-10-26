from random import randint as r
# quicksort: pick a random pivot, smaller numbers go left, the rest go right
# left and right don't touch each other so in theory they can be sorted in parallel
# returns the sorted list and how many comparisons it took
q = lambda v: (v, 0) if len(v) < 2 else (lambda p, L, R: [(L if x < p else R).append(x) for x in v] and (lambda a, b: (a[0] + [p] + b[0], len(v) + a[1] + b[1]))(q(L), q(R)))(v.pop(r(0, len(v) - 1)), [], [])
# comparisons:
#   worst case (pivot is always the min or max) - n(n-1)/2, so 5 -> 10, 10 -> 45
#   best case (pivot always splits in half) - 5 -> 6, 10 -> 19, roughly n*log2(n)
#   on average - 2(n+1)(1 + 1/2 + ... + 1/n) - 4n, so 5 -> 7.4, 10 -> 24.4
# output: size, comparisons, sorted list (for long lists just checks it's sorted)
[print(n, (s := q([r(-100, 100) for _ in range(n)]))[1], s[0] if n <= 10 else all(a <= b for a, b in zip(s[0], s[0][1:]))) for n in (0, 1, 5, 10, 100, 1000)]
