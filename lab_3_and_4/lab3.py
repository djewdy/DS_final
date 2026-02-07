from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

class Calculator:
    @staticmethod
    def add(a, b): return a + b
    @staticmethod
    def subtract(a, b): return a - b
    @staticmethod
    def multiply(a, b): return a * b
    @staticmethod
    def divide(a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b


@app.route('/api/<operation>')
def operate(operation):
    try:
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))

        if operation == 'add':
            result = Calculator.add(a, b)
        elif operation == 'subtract':
            result = Calculator.subtract(a, b)
        elif operation == 'multiply':
            result = Calculator.multiply(a, b)
        elif operation == 'divide':
            result = Calculator.divide(a, b)
        else:
            return jsonify({"error": "Unknown operation"}), 400

        return jsonify({"result": result})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception:
        return jsonify({"error": "Invalid input"}), 400

@app.route('/')
def index():
    return render_template_string("""
<!DOCTYPE html>
<html>
<head>
    <title>Flask Calculator</title>
    <style>
        body { font-family: Arial; max-width: 400px; margin: 40px auto; text-align: center; }
        input, select, button { margin: 10px; padding: 8px; font-size: 1em; }
        #result { margin-top: 20px; font-weight: bold; font-size: 1.2em; }
    </style>
</head>
<body>
    <h2>Calculator</h2>
    <div>
        <input type="number" id="a" placeholder="Enter first number">
        <input type="number" id="b" placeholder="Enter second number"><br>
        <select id="operation">
            <option value="add">Add (+)</option>
            <option value="subtract">Subtract (−)</option>
            <option value="multiply">Multiply (×)</option>
            <option value="divide">Divide (÷)</option>
        </select><br>
        <button onclick="compute()">Compute</button>
    </div>
    <div id="result"></div>

    <script>
        async function compute() {
            const a = document.getElementById('a').value;
            const b = document.getElementById('b').value;
            const operation = document.getElementById('operation').value;

            if (a === '' || b === '') {
                alert('Please enter both numbers.');
                return;
            }

            const url = `/api/${operation}?a=${a}&b=${b}`;
            const response = await fetch(url);
            const data = await response.json();

            if (data.result !== undefined) {
                document.getElementById('result').textContent = "Result: " + data.result;
            } else {
                document.getElementById('result').textContent = "Error: " + data.error;
            }
        }
    </script>
</body>
</html>
    """)

if __name__ == '__main__':
    app.run(debug=True)