from flask import Flask, request, session as login_session, g, redirect, url_for, abort, render_template, flash, send_from_directory



app = Flask(__name__) # create the application instance :)
app.config.from_object(__name__) # load config from this file , flaskr.py


@app.route('/',)
def HomePage():
		return render_template("index.html")	#else:



if __name__ == "__main__":
	app.debug=True
	app.run()
