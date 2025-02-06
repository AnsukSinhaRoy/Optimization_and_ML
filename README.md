# Optimization and Machine Learning Lab

This repository contains various optimization algorithms implemented in Python, categorized based on their applicability to linear and nonlinear systems. The goal is to provide reusable and well-structured code following object-oriented principles.

## Repository Structure
```
📂 optimization-lab
│── 📂 linear_systems
│   ├── kaczmarz.py  # Vanilla & Randomized Kaczmarz Methods
│── 📂 nonlinear_systems
│   ├── gradient_descent.py  # GD, PGD, SGD
│   ├── newton_method.py  # Newton's Method
│── 📂 utils
│   ├── cost_functions.py  # Least Squares, Logistic Cost
│   ├── derivatives.py  # First and Second Derivatives
│   ├── plotting.py  # Error and Convergence Plots
│── main.py  # Runs experiments for all methods
│── README.md  # Documentation
```

## Implemented Methods
### Linear Systems
- **Kaczmarz Method**
  - Vanilla Kaczmarz (Sequential row selection, slow convergence)
  - Randomized Kaczmarz (Faster convergence with probability-based row selection)

### Nonlinear Systems
- **Gradient-Based Methods**
  - Gradient Descent (GD)
  - Projected Gradient Descent (PGD)
  - Stochastic Gradient Descent (SGD)
- **Second-Order Methods**
  - Newton's Method (Uses Hessian matrix for quadratic convergence)

## Setup & Usage
### Prerequisites
Ensure you have Python installed along with the required dependencies:
```bash
pip install numpy matplotlib
```

### Running Experiments
To run optimization experiments:
```bash
python main.py
```

## Future Improvements
- Implement adaptive learning rate strategies (Adam, RMSProp)
- Add constrained optimization methods
- Extend support for deep learning-based optimization

## Contributors
Feel free to contribute by improving existing methods or adding new ones!

