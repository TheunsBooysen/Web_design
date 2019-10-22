from flask import Flask

app = Flask(__name__)  # app anme.this will never change???


@app.route("/")  # routing a function which can change but for now it is only a single forward slash
def home():
    return "HALLO MINE"


@app.route("/about")  # adding /about at the end of the  normal url will go to this page(specifying the path)
def about():
    return "THE ABOUT PAGE"


@app.route("/blog")
def blog():
    return "THE BLOG PAGE"


@app.route("/blog/<blog_id>")  # its an extension of the blog page..meaning you type blog/ 'anything you want'
# and the page will return whatever you typed in... (blog_id can be specified to a data type for example:<int:blog_id>)
def blogextend(blog_id):
    return "BLOG POST NUMBER..." + str(blog_id)


if __name__ == "__main__":
    app.run()