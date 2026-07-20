from preprocessing.normalization import normalize
from models.classifier import classify
from metrics.evaluation import accuracy


def main() -> None:
    raw_data = [10.0, 20.0, 30.0, 40.0, 50.0, 60.0, 70.0, 80.0]
    y_true = [0, 0, 0, 0, 1, 1, 1, 1]

    normalized_data = normalize(raw_data)
    y_pred = classify(normalized_data)
    score = accuracy(y_true, y_pred)

    print("Raw data:         ", raw_data)
    print("Normalized data:  ", [round(v, 4) for v in normalized_data])
    print("Predictions:      ", y_pred)
    print("True labels:      ", y_true)
    print(f"Model accuracy:    {score:.2%}")


if __name__ == "__main__":
    main()
