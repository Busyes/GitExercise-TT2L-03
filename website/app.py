from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def sum_numbers():
    if request.method == 'POST':
        number1 = float(request.form['number1'])
        number2 = float(request.form['number2'])
        result = number1 + number2
        return render_template_string('''
            <html>
                <body>
                    <h1>The sum is: {{ result }}</h1>
                </body>
            </html>
        ''', result=result)
    else:
        return render_template_string('''
            <html>
                <body>
                    <form method="post">
                        <label for="number1">Number 1:</label>
                        <input type="number" id="number1" name="number1" step="0.01" required><br>
                        <label for="number2">Number 2:</label>
                        <input type="number" id="number2" name="number2" step="0.01" required><br>
                        <input type="submit" value="Submit">
                    </form>
                </body>
            </html>
        ''')

if __name__ == '__main__':
    app.run(debug=True)