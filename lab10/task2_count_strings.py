"""Count the string elements in a list of mixed types."""

items = [list, "abba", "123", 123, "list", None, True, ["x"]]

checks = [isinstance(item, str) for item in items]
print(f"Number of strings: {checks.count(True)}")
