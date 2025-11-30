# todo56-calculator



##  Features

- Basic arithmetic operations (add, subtract, multiply, divide)
- Built-in logging for every operation
- Unit tests using **pytest**
- Static analysis with **flake8** and **pre-commit**
- Reference documentation auto-generated using **pdoc**
- MIT open-source license
- Simple and clean project structure






---

##  Installation

Clone the repository and create a virtual environment:

```bash
git clone https://github.com/newjack12/todo56.git
cd todo56

# Create & activate virtual environment
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Install pre-commit hooks
pip install pre-commit
pre-commit install
````

---

##  Usage

### Import the calculator in your Python code

```python
from app.calculator import add, subtract, multiply, divide

print(add(3, 5))
print(subtract(10, 4))
print(multiply(3, 7))
print(divide(10, 2))
```

### Division by zero handling

```python
try:
    divide(5, 0)
except ValueError as e:
    print(e)
```

### Run the main example script

```bash
python -m app.main
```

---

##  Run Tests

```bash
pytest tests/
```

---

##  Static Code Analysis

Manual run:

```bash
flake8 app/ tests/
```

Trigger all pre-commit checks:

```bash
pre-commit run --all-files
```

---

## Generate Reference Documentation

```bash
python -m pdoc --html app --output-dir docs/reference --force
```

Open the generated HTML documentation:

```
docs/reference/index.html
```

---

##  License

This project is released under the **MIT License**.
See the `LICENSE` file for full details.

```
