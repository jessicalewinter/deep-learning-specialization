def accuracy(y_true: list[int], y_pred: list[int]) -> float:
    if len(y_true) != len(y_pred):
        raise ValueError("y_true and y_pred must have the same length.")
    if not y_true:
        return 0.0
    correct = sum(1 for t, p in zip(y_true, y_pred) if t == p)
    return correct / len(y_true)
