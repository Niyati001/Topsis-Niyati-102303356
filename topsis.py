import sys
import os
import pandas as pd
import numpy as np


def error_exit(message):
    print(f"Error: {message}")
    sys.exit(1)


def topsis(input_file, weights_str, impacts_str, output_file):

    # ✅ File existence check
    if not os.path.exists(input_file):
        error_exit("File not found.")

    # ✅ Read file
    try:
        data = pd.read_csv(input_file)
    except Exception:
        error_exit("Unable to read the input file.")

    # ✅ Minimum column check
    if data.shape[1] < 3:
        error_exit("Input file must contain three or more columns.")

    # ✅ Extract criteria columns (2nd to last)
    criteria = data.iloc[:, 1:]

    # ✅ Check numeric values
    try:
        criteria = criteria.astype(float)
    except ValueError:
        error_exit("From 2nd to last columns must contain numeric values only.")

    # ✅ Split weights and impacts
    weights = weights_str.split(',')
    impacts = impacts_str.split(',')

    # ✅ Check comma separation
    if len(weights) < 1 or len(impacts) < 1:
        error_exit("Impacts and weights must be separated by ',' (comma).")

    # ✅ Check length match
    if len(weights) != criteria.shape[1] or len(impacts) != criteria.shape[1]:
        error_exit("Number of weights, impacts and criteria columns must be same.")

    # ✅ Convert weights to float
    try:
        weights = np.array(weights, dtype=float)
    except ValueError:
        error_exit("Weights must be numeric.")

    # ✅ Validate impacts
    for impact in impacts:
        if impact not in ['+', '-']:
            error_exit("Impacts must be either '+' or '-'.")

    # ------------------------------
    # 🔹 STEP 1: Normalize matrix
    # ------------------------------
    norm_matrix = criteria / np.sqrt((criteria ** 2).sum())

    # ------------------------------
    # 🔹 STEP 2: Weighted matrix
    # ------------------------------
    weighted_matrix = norm_matrix * weights

    # ------------------------------
    # 🔹 STEP 3: Ideal best & worst
    # ------------------------------
    ideal_best = []
    ideal_worst = []

    for i in range(len(impacts)):
        if impacts[i] == '+':
            ideal_best.append(weighted_matrix.iloc[:, i].max())
            ideal_worst.append(weighted_matrix.iloc[:, i].min())
        else:
            ideal_best.append(weighted_matrix.iloc[:, i].min())
            ideal_worst.append(weighted_matrix.iloc[:, i].max())

    ideal_best = np.array(ideal_best)
    ideal_worst = np.array(ideal_worst)

    # ------------------------------
    # 🔹 STEP 4: Distance calculation
    # ------------------------------
    dist_best = np.sqrt(((weighted_matrix - ideal_best) ** 2).sum(axis=1))
    dist_worst = np.sqrt(((weighted_matrix - ideal_worst) ** 2).sum(axis=1))

    # ------------------------------
    # 🔹 STEP 5: Topsis score
    # ------------------------------
    topsis_score = dist_worst / (dist_best + dist_worst)

    # Add results
    data['Topsis Score'] = topsis_score
    data['Rank'] = topsis_score.rank(method='max', ascending=False).astype(int)

    # Save output
    data.to_csv(output_file, index=False)

    print("Success: Result written to", output_file)


# ===============================
# 🔹 MAIN FUNCTION (CLI PART)
# ===============================

if __name__ == "__main__":

    # ✅ Correct number of parameters check
    if len(sys.argv) != 5:
        print("Usage: python topsis.py <InputDataFile> <Weights> <Impacts> <OutputResultFileName>")
        sys.exit(1)

    input_file = sys.argv[1]
    weights = sys.argv[2]
    impacts = sys.argv[3]
    output_file = sys.argv[4]

    topsis(input_file, weights, impacts, output_file)
