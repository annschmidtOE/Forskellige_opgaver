from bottle import run, get, template
import requests
 
 
##############################
@get("/")
def _():
    html = requests.get("https://proff.dk").text
    html = html.replace("Vil du vide mere om hvad Proff", "Køb en MAC for 1.000 kr")
    return html
    # return template("index.html")
 
##############################
run(host="127.0.0.1", port=80, debug=True, reloader=True)