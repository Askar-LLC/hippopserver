from config import *
from hpWebFrame import(Flask, render_template)
from  serving_static import *
def gtest():
	console("This is a Working progress enviroment for the Hip Hop Server test \n")
	app = Flask(__name__)


	@app.route("/")
	def index(self=1):
	#self test
		consoleRun = "return"
		return "hello"
#returning to the default headers
	if __name__ == "__main__":
		app.config['DEBUG']=True
#cofiguration for the hip pop server

		host = ["127.0.0.1", "5000", "True"]
		hostURL = host[0]
		hostPORT = host[1]
		hostDEBUGGER = host[2]
		app.run(hostURL, hostPORT)
	
gtest()