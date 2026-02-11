# Linear Algebra Foundations with Python (NumPy Implementation)


This repository contains hands-on practice notebooks and scripts focused on **NumPy fundamentals**, **array manipulation**, and core concepts required for **linear algebra and data analysis in Python**.

The work is structured as small, progressive notebooks that build up from basic NumPy usage to axis operations, statistics, and linear algebra utilities.

---

## 📌 Contents

### ✅ Notebooks

#### 1) `01_numpy_intro_lists_vs_arrays.ipynb`
Introduces the difference between Python lists and NumPy arrays:
- Vectorization
- Performance comparison
- dtype inference
- Multidimensional arrays

#### 2) `02_numpy_indexing_slicing_manipulation.ipynb`
Covers core array operations:
- Indexing and slicing (1D/2D)
- Boolean indexing
- Broadcasting
- Reshape / flatten / transpose
- Array concatenation

#### 3) `03_numpy_axis_statistics_linalg.ipynb`
Focuses on mathematical and analytical operations:
- Dimensions (`ndim`), `shape`, and axis explanation
- Axis-based aggregation (2D + 3D)
- Statistical operations
- Linear algebra (`np.linalg`)

#### 4) `04_numpy_grayscale_image_simulation.ipynb`
Simulates a grayscale image using a 2D NumPy array:
- Pixel intensities (0–255)
- Brightness and contrast analysis
- Brightness and contrast adjustment using clipping

#### 5) `05_numpy_dataset_analysis_student_scores.ipynb`
Mini dataset analysis using NumPy:
- Student test scores dataset
- Per-student and per-test averages
- Filtering using boolean masks

#### 6) `06_numpy_linear_independence-and_span.ipynb`

Explores core linear algebra concepts through implementation:

- Matrix rank using `np.linalg.matrix_rank`
- Linear independence testing
- Span and dimension interpretation
- Geometric meaning of rank
- Matrix as a linear transformation (`@` operator)

Includes examples of:
- Dependent vs independent vectors
- Standard basis in ℝ³
- Interpreting rank geometrically


---

### ✅ Python Scripts

#### 6) `numpy-practice1.py`
Basic NumPy array creation and operations practice.

#### 7) `numpy-practice2.py`
Array initialization helpers:
- `zeros`, `ones`, `arange`, `linspace`, `eye`, random arrays

#### 8) `numpy-practice3.py`
Arithmetic operations with NumPy:
- element-wise math
- dot product
- transpose
- aggregation along axes

---

### ✅ Environment File

#### 9) `numpy-practice.yml`
Conda environment configuration file for installing dependencies consistently.

---

## 🧠 Learning Outcomes

By completing this repository, I practiced:

- Creating and manipulating NumPy arrays efficiently
- Writing vectorized operations instead of loops
- Understanding `ndim`, `shape`, and axis-based computation
- Using NumPy for statistics and linear algebra workflows
- Applying NumPy to real-world style tasks like images and datasets
- Matrix rank and linear independence
- Dimension of span and geometric interpretation
- Using `np.linalg` tools in structured mathematical workflows

---

## 🛠 Requirements

- Python 3.9+
- NumPy

Install dependencies:

```bash
pip install numpy
```

For running notebooks:

```bash
pip install jupyter
jupyter notebook
```

---


## 📈 Linear Algebra Progression

This repository now transitions from NumPy fundamentals toward
structured linear algebra concepts required for robotics and engineering:

- Rank and independence
- Basis and dimension
- Linear transformations
- Eigenvalues (upcoming)
- Decompositions (SVD, QR — upcoming)

Future notebooks will build toward robotics-specific mathematics
used in kinematics, control, and estimation.

