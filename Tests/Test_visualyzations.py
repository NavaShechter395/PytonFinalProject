import ast

def check_code_quality(source_code):
    tree = ast.parse(source_code)
    function_lengths = []
    warnings_count = {
        "long_function": 0,
        "missing_docstring": 0,
        "unused_variable": 0,
        "too_many_arguments": 0
    }

    # בדוק אורך הפונקלים
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            function_lines = node.end_lineno - node.lineno + 1
            function_lengths.append(function_lines)

            if function_lines > 20:
                warnings_count["long_function"] += 1
            if ast.get_docstring(node) is None:
                warnings_count["missing_docstring"] += 1
            if len(node.args.args) > 5:  # לדוגמה, יותר מדי פרמטרים
                warnings_count["too_many_arguments"] += 1

        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    used = False
                    for usage in ast.walk(tree):
                        if isinstance(usage, ast.Name) and usage.id == target.id:
                            used = True
                            break
                    if not used:
                        warnings_count["unused_variable"] += 1

    return function_lengths, warnings_count

# דוגמת שימוש
source_code = """
def example_function(a, b, c, d, e, f):
    total = a + b + c + d + e
    return total

def unused_function():
    x = 10  # משתנה לא בשימוש
"""

function_lengths, warnings = check_code_quality(source_code)
print("Function Lengths:", function_lengths)
print("Warnings Count:", warnings)
