def normalize(values: list[float]) -> list[float]:
    if not values:
        return []
    minimum = min(values)
    maximum = max(values)
    value_range = maximum - minimum
    if value_range == 0:
        return [0.0 for _ in values]
    return [(v - minimum) / value_range for v in values]
