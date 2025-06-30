
from flask import Flask, render_template, redirect, url_for, request, session


app = Flask(__name__)
app.secret_key = "poiuhbsalaskcn"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/listings")
def show_list():
    return render_template("listings.html")

@app.route('/details')
def details():
    # Get the ID from query parameters
    detail_id = request.args.get('id')

    # Check if ID is a number between 1 and 6
    if detail_id and detail_id.isdigit():
        id_int = int(detail_id)
        if 1 <= id_int <= 6:
            template_name = f'details_{id_int}.html'
            return render_template(template_name)
    
    # If ID is invalid or out of range, return 404
    
    return '''
            <html>
            <head>
                <style>
                body {
                    display: flex;
                    height: 100vh;
                    margin: 0;
                    justify-content: center;
                    align-items: center;
                    font-size: 3rem;
                    font-family: Poppins, Arial, sans-serif;
                }
                </style>
            </head>
            <body>
                404 :(
            </body>
            </html>
    '''




if __name__ == "__main__":
    app.run(debug=True)