from Analysise import check_code_quality
source_code = """
def example_function():
    a = 10
    b = 20
    c = a + b
    return c

def unused_variable_function():
    x = 5  # This variable is never used
    return 10

def short_function():
    pass
"""

warnings = check_code_quality(source_code)
for warning in warnings:
    print(warning)
