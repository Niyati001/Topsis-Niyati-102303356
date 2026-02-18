# Topsis-Niyati-102303356  
Predictive Analysis assignment 1 on TOPSIS by Dr.PS Rana
[topsis.py](https://github.com/user-attachments/files/25379279/topsis.py)
[college_numeric.csv](https://github.com/user-attachments/files/25379272/college_numeric.csv)
[result.csv](https://github.com/user-attachments/files/25379071/result.csv)
[Topsis_Niyati_102303356.ipynb](https://github.com/user-attachments/files/25379038/Topsis_Niyati_102303356.ipynb)
[README.md](https://github.com/user-attachments/files/25379080/README.md)

# TOPSIS Implementation – College Admission Dataset

## Subject
Predictive Analysis  

## Name
Niyati  

## Roll Number
102303356  

---

# Introduction

TOPSIS (Technique for Order Preference by Similarity to Ideal Solution) is a Multi-Criteria Decision Making (MCDM) method used to rank alternatives based on their distance from an ideal solution.

The best alternative should:

- Have the shortest distance from the Ideal Best solution
- Have the farthest distance from the Ideal Worst solution

This project implements TOPSIS using Python and applies it to a College Admission dataset to rank students based on multiple quantitative criteria.

---

# Objective

To rank students using the TOPSIS method based on the following criteria:

- Age
- Entrance Score
- Board Percentage
- Extracurricular Score
- Admission Probability

---

# Dataset Description

The dataset used contains the following columns:

| Column Name | Description |
|-------------|-------------|
| student_id | Unique identifier |
| age | Age of student |
| entrance_score | Entrance examination score |
| board_percentage | Board exam percentage |
| extracurricular | Extracurricular performance score |
| admission_probability | Probability of admission |

Only numerical columns were selected for TOPSIS since the method requires quantitative criteria.

---

# Methodology

The TOPSIS algorithm follows these steps:

## Step 1: Construct Decision Matrix

A matrix is formed using alternatives (students) and criteria.

## Step 2: Normalize the Decision Matrix

\[
r_{ij} = \frac{x_{ij}}{\sqrt{\sum x_{ij}^2}}
\]

Normalization removes scale differences among criteria.

## Step 3: Construct Weighted Normalized Matrix

\[
v_{ij} = w_j \cdot r_{ij}
\]

Equal weights were assigned to all criteria in this implementation.

## Step 4: Determine Ideal Best and Ideal Worst

- Ideal Best (A⁺): Maximum value for benefit criteria
- Ideal Worst (A⁻): Minimum value for benefit criteria

## Step 5: Calculate Separation Measures

\[
S_i^+ = \sqrt{\sum (v_{ij} - A_j^+)^2}
\]

\[
S_i^- = \sqrt{\sum (v_{ij} - A_j^-)^2}
\]

## Step 6: Calculate TOPSIS Score

\[
C_i = \frac{S_i^-}{S_i^+ + S_i^-}
\]

## Step 7: Ranking

Higher TOPSIS score indicates better ranking.

---

# Results

- Each student is assigned a TOPSIS Score.
- Students are ranked based on descending TOPSIS Score.
- Rank 1 represents the best candidate.

A bar graph was generated to visualize TOPSIS score distribution.

---

# Result Visualization

The graph shows variation in TOPSIS scores across students.  
Higher bars indicate stronger overall performance considering all criteria.

---

# Command Line Implementation

The project also includes a command-line implementation:

python topsis.py college_numeric.csv "1,1,1,1,1" "+,+,+,+,+" result.csv


This generates:

- Topsis Score column
- Rank column

---

# Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Google Colab

---

# Conclusion

The TOPSIS method successfully ranks students using multiple performance criteria.

It provides:

- Objective decision-making
- Multi-criteria evaluation
- Mathematical ranking system

This demonstrates how decision-support models can be applied in predictive analytics for ranking and evaluation problems.

---

# Repository Structure

Topsis-Assignment
│
├── topsis.py
├── college_numeric.csv
├── result.csv
├── Topsis_Analysis.ipynb
├── README.md



# Key Learning Outcomes

- Implementation of Multi-Criteria Decision Making
- Mathematical modeling using Python
- Data normalization techniques
- Ranking systems
- Visualization of decision results
- Command-line application development
- Python package creation

