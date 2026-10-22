from flask_app import app 
from flask import redirect

@app.route('/')
def home():
   return redirect('/usuarios')

if __name__=="__main__": 

   app.run(debug=True)