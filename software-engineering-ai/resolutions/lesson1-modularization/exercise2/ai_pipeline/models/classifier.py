def classify(probabilities: list[float], threshold: float = 0.5) -> list[int]:
    return [1 if p >= threshold else 0 for p in probabilities]
