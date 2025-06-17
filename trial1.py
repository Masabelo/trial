def trial_function():
    print("✅ Git Trial Test: Code is running successfully!")

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def run_tests():
    assert add(2, 3) == 5, "Addition test failed"
    assert subtract(5, 2) == 3, "Subtraction test failed"
    print("✅ All tests passed.")

if __name__ == "__main__":
    trial_function()
    run_tests()
