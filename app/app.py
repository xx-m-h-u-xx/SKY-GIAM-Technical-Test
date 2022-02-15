# -*- coding: utf-8 -*-
# @script : app.py 
# @requirements: pip install Flask
# @requirements: pip install prometheus-flask-exporter

import json, re, time
from flask import Flask, render_template, request, redirect, url_for, flash
from prometheus_flask_exporter import PrometheusMetrics


# Create Flask app instance
app = Flask(__name__)

# Initialises duration metrics and request counters, path is disable since it prevents access externally 
metrics = PrometheusMetrics(app, path=None)
metrics.info('app_info', 'Application info', version='1.0.3')
metrics.register_endpoint('/metrics')

# Global variable declared 
input_name = None

# Basic manual clock timer
def begin_time():
    request.start_time = time.time()


# Flask webapp server/ "webform"
# static information as metric starts from the moment user enters on website
@app.route("/")
@app.route("/webform", methods = ['GET', 'POST'])
@metrics.gauge('in_progress', 'Long running requests in progress')
def webform():

    # Checks HTTP request method and retrieves raw form data
    if request.method == "POST":
        request_data = request.get_data()
        request_json = json.loads(request_data)
        print(">>> JSON passed data: {}".format(request_json))

        # Checks the existence of dict keys from passed JSON user data '''
        if 'inputName' in request_json:
            input_name = request_json["inputName"]
            flash("You have entered, '{}'".format(input_name))

            # Validates user's input
            if input_name == None:
                flash("Error! You must submit something!")
                return render_template("webform.html")

            # if input name has been entered but not within valid range
            elif not(4 <= len(input_name) <= 40):
                flash("Your input entry must be between 4 and 40 characters long in length !!, 'error'")
                return render_template("webform.html")
             
            # checks entry if it doesn't contain any lower/uppercase characters (including white spaces)
            elif not(re.match(r'^([a-zA-Z ])+$', input_name)):
                
                flash(" @!?£*-+=/$%^&()<>`¬ Not Accepted !!\n\
                    Your input entry must only contain alphabetic characters !!!")
                
                return render_template("webform.html")

            # when inputName is validated correctly
            # displays response screen with results shown
            else:
                input_name = request_json["inputName"]
                flash("Submission Success!")
                return results(input_name)

    if request.method == "GET":
        return render_template("webform.html")


# Consideration: metric observations/info needs to associate with specific HTTP endpoint
# Consideration: metric info need to contain relevant statistics & metadata
# Summarises informational stats onto histogram graph for visible observations
# Allows ways to troubleshoot performance factors for the site
# Should a site's capacity be scaled up or down
# Should a site be effected with its server's hardware/software modifications
# Should a site experience unexpected behaviour
# Should a site track its gauge (number of requests hits per day)
# Should a site track its counter metrics (number of hits user has checked in over time)
@app.route('/status/<int:status>')

@metrics.do_not_track()

@metrics.summary('requests_by_status', 'request latencies by status', 
                    labels={'status': lambda r:r.status_code})

@metrics.histogram('requests_by_status_and_path', 'request latencies by status and path',
                    labels={'status': lambda r: r.status_code, 'path': lambda: request.path})

def echo_status(status):
    return 'Status: %s' % status, status


# @app.route('/metrics')
# def metrics():
#     return Response(prometheus_client.generate_latest(), mimetype=CONTENT_TYPE_LATEST)

# Basic manual stop clock timer
def end_time(results):
    
    # basic convertion into ms
    elapsed = (time.time() - request.start_time) * 1000
    return results


# Flask webapp /results page
@app.route("/results/<string:input_name>", methods = ['GET', 'POST'])
def results(input_name):
    return render_template("results.html", input_name=input_name)

# Customised error handler page
@app.errorhandler(404)
def page_not_found(e):
    return "Sorry there's been an error :(", 404


# Manual metric reporter
def configure_metrics(app):
    app.before_request(begin_time)      # before a request is processed
    app.after_request(end_time)        # before response is made



if __name__ == "__main__":
    # Launch Flask dev server
    metrics.start_http_server(5000) # link to endpoint to a HTTP port
    app.run(debug=True)