"""
Complete Python Error Handling Code
Demonstrates all common error types with try-except blocks
"""

def demonstrate_errors():
    """Demonstrates various Python error types"""
    
    print("=" * 60)
    print("PYTHON ERROR HANDLING DEMO")
    print("=" * 60)
    
    # 1. TypeError - Wrong data type operation
    print("\n1. TYPE ERROR DEMO:")
    try:
        result = "5" + 5  # Cannot add string and int
        print(f"Result: {result}")
    except TypeError as e:
        print(f"❌ Error: {type(e).__name__}")
        print(f"Message: {e}")
        print(f"Error Code: TypeError")
    
    # 2. ValueError - Invalid value for operation
    print("\n2. VALUE ERROR DEMO:")
    try:
        num = int("hello")  # Cannot convert string to int
        print(f"Result: {num}")
    except ValueError as e:
        print(f"❌ Error: {type(e).__name__}")
        print(f"Message: {e}")
        print(f"Error Code: ValueError")
    
    # 3. IndexError - List index out of range
    print("\n3. INDEX ERROR DEMO:")
    try:
        my_list = [1, 2, 3]
        result = my_list[10]  # Index 10 doesn't exist
        print(f"Result: {result}")
    except IndexError as e:
        print(f"❌ Error: {type(e).__name__}")
        print(f"Message: {e}")
        print(f"Error Code: IndexError")
    
    # 4. KeyError - Dictionary key not found
    print("\n4. KEY ERROR DEMO:")
    try:
        my_dict = {"name": "John", "age": 25}
        result = my_dict["city"]  # "city" key doesn't exist
        print(f"Result: {result}")
    except KeyError as e:
        print(f"❌ Error: {type(e).__name__}")
        print(f"Message: {e}")
        print(f"Error Code: KeyError")
    
    # 5. ZeroDivisionError - Division by zero
    print("\n5. ZERO DIVISION ERROR DEMO:")
    try:
        result = 10 / 0  # Cannot divide by zero
        print(f"Result: {result}")
    except ZeroDivisionError as e:
        print(f"❌ Error: {type(e).__name__}")
        print(f"Message: {e}")
        print(f"Error Code: ZeroDivisionError")
    
    # 6. FileNotFoundError - File not found
    print("\n6. FILE NOT FOUND ERROR DEMO:")
    try:
        with open("nonexistent_file.txt", "r") as f:
            content = f.read()
        print(f"Content: {content}")
    except FileNotFoundError as e:
        print(f"❌ Error: {type(e).__name__}")
        print(f"Message: {e}")
        print(f"Error Code: FileNotFoundError")
    
    # 7. AttributeError - Object attribute not found
    print("\n7. ATTRIBUTE ERROR DEMO:")
    try:
        my_str = "hello"
        result = my_str.nonexistent_method()
        print(f"Result: {result}")
    except AttributeError as e:
        print(f"❌ Error: {type(e).__name__}")
        print(f"Message: {e}")
        print(f"Error Code: AttributeError")
    
    # 8. NameError - Variable not defined
    print("\n8. NAME ERROR DEMO:")
    try:
        print(undefined_variable)
    except NameError as e:
        print(f"❌ Error: {type(e).__name__}")
        print(f"Message: {e}")
        print(f"Error Code: NameError")
    
    # 9. ImportError - Module not found
    print("\n9. IMPORT ERROR DEMO:")
    try:
        import nonexistent_module
    except ImportError as e:
        print(f"❌ Error: {type(e).__name__}")
        print(f"Message: {e}")
        print(f"Error Code: ImportError")
    
    # 10. Success case - No error
    print("\n10. SUCCESS CASE (No Error):")
    try:
        result = 10 + 5
        print(f"✅ Result: {result}")
        print("Error Code: None (Success)")
    
