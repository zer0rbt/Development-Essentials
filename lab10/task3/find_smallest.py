"""Find the two smallest values of a list."""


def find_two_smallest(values: list[int]) -> tuple[int, ...]:
    """Return the two smallest values in ascending order."""
    return tuple(sorted(values)[:2])
