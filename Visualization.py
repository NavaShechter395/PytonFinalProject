import ast
import matplotlib.pyplot as plt

def check_code_quality(source_code):
    """
    בודק את איכות הקוד ומחזיר את אורך הפונקציות ומספר האזהרות.
    """
    tree = ast.parse(source_code)
    function_lengths = []
    warnings_count = {
        "long_function": 0,
        "missing_docstring": 0,
        "unused_variable": 0
    }

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            function_lines = node.end_lineno - node.lineno + 1
            function_lengths.append(function_lines)

            if function_lines > 20:
                warnings_count["long_function"] += 1
            if ast.get_docstring(node) is None:
                warnings_count["missing_docstring"] += 1

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

def create_histogram(function_lengths):
    """
    יוצר היסטוגרמה של אורכי הפונקציות.
    """
    plt.hist(function_lengths, bins=range(0, max(function_lengths) + 1, 1), alpha=0.7)
    plt.title('Function Lengths Distribution')
    plt.xlabel('Number of Lines')
    plt.ylabel('Frequency')
    plt.savefig('histogram.png')
    plt.clf()
    print("Histogram saved as 'histogram.png'") # הדפסה לאישור שמירת ההיסטוגרמה

def create_pie_chart(warnings_count):
    """
    יוצר תרשים עוגה של התפלגות האזהרות.
    """
    labels = warnings_count.keys()
    sizes = warnings_count.values()
    plt.pie(sizes, labels=labels, autopct='%1.1f%%')
    plt.title('Warnings Distribution')
    plt.savefig('pie_chart.png')
    plt.clf()
    print("Pie chart saved as 'pie_chart.png'") # הדפסה לאישור שמירת תרשים העוגה

def create_bar_chart(warnings_count):
    """
    יוצר תרשים עמודות של מספר הבעיות לפי סוג.
    """
    labels = warnings_count.keys()
    sizes = warnings_count.values()
    plt.bar(labels, sizes, alpha=0.7)
    plt.title('Number of Issues by Type')
    plt.ylabel('Count')
    plt.savefig('bar_chart.png')
    plt.clf()
    print("Bar chart saved as 'bar_chart.png'") # הדפסה לאישור שמירת תרשים העמודות
