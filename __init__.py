import os
import sys
from config import *
from packages.hpvs_module.hpWebFrame import *
from module_config import *
#parse in lists

mod_help = ["hpm-run"]
package_nameL =[]

def inputsOut(self=None):
	console("\n")
	console("Hip Pop Virtual Server currently running on a command line interface\n")
	console("Type hpm-run to begin(NOTE: This will start all Hip Pop Services)\n")
inputsOut(self=None)



grabberIn = runInput("")

if grabberIn!=mod_help[0]:
	console("command error")
	#this will start the machine over and over again
	exec(open("C:\\HPVS\\__init__.py").read())

else:
	
	console("All Hip Pop Services is now ON\n")
	console("Select a Service to Run:")
	console("WebFlask (to run this service type 'webFrame')\n")
	console("Package Install")
	console("Install a Package (to run this service type 'package')\n")

	grabberInz = runInput("hpm -")

	if grabberInz == "webFrame":
		console("WebFlask Frame Started......100%")
		console("go to this path on C:\\HPVS\\serving_static\\html\\main.py")
		console("to run the server")
		
		#this will start the machine over and over again
		exec(open("C:\\HPVS\\__init__.py").read())
	elif grabberInz == "package":
		console("Select a Type of Package Installer:")
		console("NodeJS Package Installer( type 'node')")
		console("Python Package Installer(Based on Hip Pop)(type 'base-install')")
		p_installer = runInput("hpm -")
		if p_installer == "node":
			console("We currently working on the NodeJS Installer")
			#this will start the machine over and over again
			exec(open("C:\\HPVS\\__init__.py").read())
		elif p_installer == "base-install":
			console("Enter a Package Name")
			p_run_package=runInput("hpm -install ")
	else:
		#this will start the machine over and over again
		exec(open("C:\\HPVS\\__init__.py").read())
	






