import json
import sys

def load(path):
    with open(path, "r") as f:
        return json.load(f)

def drift_score(current, baseline):
    diffs = []
    for k in baseline:
        if k in current:
            b = baseline[k]
            c = current[k]
            if b == 0:
                continue
            diffs.append(abs(c - b) / abs(b))
    return sum(diffs) / len(diffs) if diffs else 0.0

def classify(score):
    if score < 0.2:
        return "PASS"
    elif score < 0.5:
        return "WARN"
    else:
        return "FAIL"

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: gv_check.py <metrics.json> <baseline.json>")
        sys.exit(0)

    current = load(sys.argv[1])
    baseline = load(sys.argv[2])

    score = drift_score(current, baseline)
    status = classify(score)

    print(f"GV_SANITY: {status}")
    print(f"drift_score: {round(score, 3)}")

    if status == "FAIL":
        sys.exit(1)
