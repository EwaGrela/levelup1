from flask import Flask, render_template, request

app = Flask(__name__)


# @app.route("/")
# def hello():
# 	return "Hello world!"

# if __name__ == '__main__':
#     app.run(debug=True)

@app.route("/")
def index():
	return render_template("index.html")




@app.route("/request")
def request_info():
	return "request method {}, request url: {}, request headers:{}".format(request.method, request.url, request.headers)

#this always at the end
if __name__ == '__main__':
    app.run(debug=True)