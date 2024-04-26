from flask import Flask,request,Response,jsonify
from flask import render_template
from predict import print_last_character_before_occurrences
app = Flask(__name__)


@app.route("/",methods=['GET', 'POST'])
def home():
    output=""
    if request.method == 'POST':
        # Get the input from the HTML form
        user_input = request.form.get('inputf')

        # Execute the process_function from predict.py with the user input
        output = print_last_character_before_occurrences(user_input)
        print(output)
        
        # Include output in the response dictionary
        
        
        # return Response(output, mimetype="text/plain")
        # Return the rendered template with the response dictionary
        return render_template('index.html', output=output, input=user_input)
    return render_template('index.html')


if __name__ == "__main__":
  app.run(debug=True)
