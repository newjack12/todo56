
# todo56-Tutorial

This tutorial will guide you step-by-step through installing, running, and using the **todo56-calculator** project.
It is designed for beginners and demonstrates basic operations, logging output, unit testing, static analysis, and documentation.

---

# Step 1 — Clone the Project & Set Up the Environment

Start by downloading the project from GitHub:

```bash
git clone https://github.com/newjack12/todo56.git
cd todo56
````

Create a virtual environment:

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

**macOS/Linux**

```bash
source venv/bin/activate
```

Install all dependencies:

```bash
pip install -r requirements.txt
pip install pre-commit
pre-commit install
```

Your environment is now ready.

---

#  Step 2 — Run the Calculator

Run the project’s main script:

```bash
python -m app.main
```

You should see log messages similar to:

```
INFO     Performing addition: 3 + 5
INFO     Performing subtraction: 10 - 4
INFO     Performing multiplication: 3 * 7
WARNING  Attempting division: 10 / 0
ERROR    Division by zero attempted
```

These messages demonstrate how the project uses multiple log levels.

---

#  Step 3 — Use the Calculator Programmatically

Import the functions in your own Python code:

```python
from app.calculator import add, subtract, multiply, divide

print(add(3, 5))        # 8
print(subtract(10, 4))  # 6
print(multiply(3, 7))   # 21
print(divide(10, 2))    # 5.0
```

## Handling Division by Zero

```python
try:
    divide(5,0)
except ValueError as e:
    print("Error:", e)
```

Expected output:

```
Error: Cannot divide by zero.
```

---

#  Step 4 — Run Unit Tests

All tests are located in `tests/test_calculator.py`.

Run them with:

```bash
pytest tests/
```

You should see output like:

```
3 passed in 0.15s
```

---

#  Step 5 — Run Static Code Analysis

### Manual analysis using flake8:

```bash
flake8 app/ tests/
```

### Automatic analysis using pre-commit:

```bash
pre-commit run --all-files
```

If your code violates style rules, flake8 will print messages such as:

```
app/calculator.py:12:1: E302 expected 2 blank lines, found 1
```

---

#  Step 6 — Generate Documentation

The project includes docstrings compatible with **pdoc**.

Generate HTML reference documentation:

```bash
python -m pdoc --html app --output-dir docs/reference --force
```

The documentation will be saved under:

```
docs/reference/
```

Open:

```
docs/reference/index.html
```

in a browser to explore it.

---
