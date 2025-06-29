import ast
import importlib.util
import sys

class CodeQualityChecker(ast.NodeVisitor):
    def __init__(self):
        self.function_length_warnings = []
        self.file_length_warnings = []
        self.unused_variables = []
        self.docstring_warnings = []
        self.function_lines = 0
        self.total_lines = 0
        self.source_code = ""

    def visit_FunctionDef(self, node):
        # בדיקת אורך הפונקציה
        if len(node.body) > 20:
            self.function_length_warnings.append(f'Warning: Function "{node.name}" exceeds 20 lines.')

        # בדיקה אם יש מחרוזת תיעוד
        if ast.get_docstring(node) is None:
            self.docstring_warnings.append(f'Warning: Function "{node.name}" has no documentation strings')

        # ספירת שורות הפונקציה
        self.function_lines += len(node.body)
        self.generic_visit(node)

    def visit_Assign(self, node):
        for target in node.targets:
            if isinstance(target, ast.Name):
                self.unused_variables.append(target.id)
        self.generic_visit(node)

    def visit_Module(self, node):
        # ספירת שורות בקובץ
        self.total_lines = self.source_code.count('\n') + 1
        self.generic_visit(node)

    def check_unused_variables(self, tree):
        # בדיקת משתנים שאינם בשימוש
        used_variables = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.Name) and isinstance(node.ctx, ast.Load):
                used_variables.add(node.id)

        for var in self.unused_variables:
            if var not in used_variables:
                print(f'Warning: Variable "{var}" is assigned but never used.')

    def report(self):
        # הדפסת התראות
        for warning in self.function_length_warnings:
            print(warning)
        for warning in self.docstring_warnings:
            print(warning)
        if self.total_lines > 200:
            print('Warning: The file exceeds 200 lines.')

# דוגמה לשימוש
file_path = r"E:\יד\קורסים שגמרנו\pyton\main.py"

spec = importlib.util.spec_from_file_location("main", file_path)
main_module = importlib.util.module_from_spec(spec)
sys.modules["main"] = main_module
spec.loader.exec_module(main_module)

checker = CodeQualityChecker()
with open(file_path, "r", encoding="utf-8") as source:
    checker.source_code = source.read()
    tree = ast.parse(checker.source_code)

checker.visit(tree)
checker.check_unused_variables(tree)
checker.report()
