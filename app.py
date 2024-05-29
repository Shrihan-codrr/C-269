
# Import Libraries
import os
from Flask import Flask , render_template , request , redirect , url_for , send_file 
from twilio.rest import Client
# Initilize the Flask
app = Flask(__name__)


# Route and define the index function to render the home.html.
@app.route('/')
def index():
    return render_template('index.html')
    if _name__=='__main__':
        app.run()

# Call the app.run()



