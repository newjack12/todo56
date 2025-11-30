from app.calculator import add, subtract, multiply, divide

if __name__ == "__main__":
    print(add(3, 5))
    print(subtract(10, 2))
    print(multiply(4, 6))
    try:
        print(divide(10, 0))
    except ValueError:
        pass
