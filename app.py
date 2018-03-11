from flask import Flask, render_template, request, url_for
import datetime

app = Flask(__name__)


# @app.route("/")
# def hello():
# 	return "Hello world!"

# if __name__ == '__main__':
#     app.run(debug=True)

@app.route("/")
def index():
	title ="Flask app"
	return render_template("index.html", title=title)




@app.route("/request")
def request_info():
	title ="Request"
	return render_template("request_info.html", title=title)

@app.route("/now")
def now():
	title ="Now"
	time = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S.%f")
	# datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S.%f")
	return render_template("now.html", time=time, title=title)

@app.route("/user_agent")
def user_agent():
	title = "User agent"
	return render_template("user_agent.html", title=title)

@app.route("/counter")
def count():
	with open("count.txt", "r") as g:
		count = g.read()
		count = int(count)
		print(type(count))
	with open("count.txt", "w") as h:
		h.write(str(count+1))
	return render_template("count.html", count=count)

#this always at the end
if __name__ == '__main__':
    app.run(debug=True) 