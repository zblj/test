from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
	return render_template('main.html')
	
@app.route("/login/")
def hello():
	return render_template('login.html')
	
@app.route("/new_account/")
def hello():
	return render_template('new account.html')

@app.route("/pwd_change/")
def hello():
	return render_template('pwd_change.html')
	
#neka sprememba


if __name__ == "__main__":
	app.run(host='0.0.0.0', port=5000, debug=True)
