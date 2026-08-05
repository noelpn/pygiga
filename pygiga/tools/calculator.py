"""Calculator tool."""

import ast

class CalculatorTool:
    """Evaluate simple arithmetic expressions."""

    def calculate(self, expression):
        try:
            tree = ast.parse(expression, mode='eval')
            return eval(compile(tree, '<calc>', mode='eval'), {}, {})
        except Exception as exc:
            return {'error': str(exc)}
