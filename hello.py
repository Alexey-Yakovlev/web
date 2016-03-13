bind = "0.0.0.0:8080"
pythonpath= "/home/barlog/web"

def app(environ, start_response):
	data = environ["QUERY_STRING"].replace('&','\n')
	start_response("200 OK", [("Content-Type", "text/plain"),("Content-Length", str(len(data)))])
	return data
