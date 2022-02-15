# SKY GIAM Junior Performance Engineer - Technical Test
# README Documentation

@script : main.py 
@author : Mohammed Healal Uddin
@language: Python 3.9.1


## Description
PrometheusMetric module was implemented as there were a lot of documentations about this module online. Along with default metrics resulted from the Prometheus, I could have the option to populate monitoring diagrams to help visualise different performance metrics for factors like: CPU/Memory/Disk usage, tasks, long-running processes, as well as Request duration and Response time.


### Functional Requirements:
- App should allow a user to submit a string text input 
- App should allow a response page to be displayed on-screen containing text input


### Non-Functional Requirements:
- App should summarises informational stats (onto histogram graph for visible observations is advantageous)
- App show allow insights into troubleshooting performance factors for the site
- Consideration: metric observations/info needs to associate with specific HTTP endpoint
- Consideration: metric info need to contain relevant statistics & metadata :
	- Should a site's capacity be scaled up or down
	- Should a site be effected with its server's hardware/software modifications
	- Should a site experience unexpected behaviour
	- Should a site track its gauge (number of requests hits per day)
	- Should a site track its counter metrics (number of hits user has checked in over time)
	- Should a site track/report request latency


## Prerequisites

i)   Please ensure you have a Python interpreter installed on your system
https://www.python.org/downloads/

ii)  Please ensure you have the latest Python version updated (prferably Python 3.9.1)
https://www.python.org/downloads/release/python-391/

iii) Please esnure you have a suitable IDE or console CLI to execute the program
Preferably Visual Studio Code Version: 1.64.0 
https://code.visualstudio.com/#alt-downloads 

iv) This program was programmed & executed on Microsoft Windows NT 11 (version 21H2)
Due to other commitments, I did not manage to test this on other operating systems



## Instructions

(1) Begin by unzipping the folder
- "SKY-GIAM-Technical-Test"

(2) Configuring virtual environment
- Open CLI and enter the key commands shown between backticks
	(i) Install 'virtualenv' package
		`pip install virtualenv`

	(ii) Create isolated virtual environment
		`virtualenv env`

	(iii) Activate virtual environment
		`venv\Scripts\activate.bat`

(3) Install project package
	(iv) Install Package Dependencies
		`pip install -r requirements.txt`

	(v) Record environment's package list into 'requirements.txt'
		`pip freeze > requirements.txt`

	(vi) 'app.py' is now running on a Flask Development Environment Server
	(vii) Copy localhost IP address from Command Prompt / Terminal Window
	(viii) Paste it on a web browser preferably Google Chrome

(3) Install project package
	(iv) Change into the project's directory & execute main script
		`cd app`
		`python  "app.py"`
