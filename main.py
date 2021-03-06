from framework import bottle
from framework.bottle import Bottle, TEMPLATE_PATH, route, template, error, request, debug, post, redirect, url, SimpleTemplate, static_file
from google.appengine.ext.webapp.util import run_wsgi_app

#Instead of supplying url in every handler, set up a template default
SimpleTemplate.defaults["url"] = lambda x, **kwargs: SETTINGS.URL_BASE + url(x, **kwargs)

app = Bottle()
TEMPLATE_PATH.insert(0,"views")	

def main():
	run_wsgi_app(bottle.default.app())

if __name__=="__main__":
	main()

@app.route("/")
def home():
	debug(True) #remove when in production
	if True: #ei kirjautunut
		redirect("/introduction")
	else: #kirjautunut
		redirect("/browse")

@app.route("/introduction")
def introduction():
	debug(True) #remove when in production
	return template("views/introduction.tpl")

@app.route("/browse")
def browse():
	debug(True)
	return template("views/browse.tpl")

@app.route("/help")
def help():
	return template("views/help.tpl")

@app.route("/contact")
def contact():
	return template("views/contact.tpl")

@app.route("/providerdemo")
def contact():
	return template("views/providerdemo.tpl")	
	
@app.error(404)
def error404(error):
    return template("404.tpl")

@app.route("/misc/<filename:path>")
def serve_misc(filename):
	return static_file(filename, root="misc")

@app.route("/css/<filename:path>", name="css")
def serve_css(filename):
	return static_file(filename, root="css")

@app.route("/js/<filename:path>", name="js")
def serve_js(filename):
    return static_file(filename, root="js")

@app.route("/fonts/<filename:path>", name="fonts")
def serve_fonts(filename):
    return static_file(filename, root="fonts")

@app.route("/less/<filename:path>", name="less")
def serve_less(filename):
    return static_file(filename, root="less")

@app.route("/scss/<filename:path>", name="scss")
def serve_scss(filename):
    return static_file(filename, root="scss")

# This isn"t exactly ideal because all images must be placed in the root of img/, but it works for now.
@app.route("<path:re:.*>/<filename:re:.*\.(jpg|gif|png|ico)>")
def serve_images(filename, path):
	return static_file(filename, root="img/")