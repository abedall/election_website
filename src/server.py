import requests
from flask import Flask, request, render_template
from werkzeug.exceptions import abort

from src.results_controller import ResultsController
from src.results_service import ResultStore,ElectionResultsService
from flask import Flask, render_template, jsonify
import os
import json

# Define a function to get the winning party for a constituency
def get_winning_party(constituency):
    parties = {}
    for candidate in constituency['partyResults']:
        party = candidate['party']
        votes = candidate['votes']
        if party in parties:
            parties[party] += votes
        else:
            parties[party] = votes
    return max(parties, key=parties.get)

# function to return a list of results of all the constituencies info(name-id-winning party)
def display_constituency_results_id():
    # Define the directory where the JSON files are stored
    directory = './resources/sample-election-results'

    # Create an empty list to store the results
    results = []

    # Loop over all the JSON files in the directory
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            # Read in the JSON file
            with open(os.path.join(directory, filename)) as f:
                constituency = json.load(f)

            # Get the winning party for the constituency
            winning_party = get_winning_party(constituency)

            # Add the constituency name and winning party to the results list
            results.append({'Constituency ID':constituency['id'],'Constituency Name': constituency['name'], 'the winning_party': winning_party})

    return results

app: Flask = Flask(__name__)
controller: ResultsController = ResultsController()

# Define the route for homepage to choose from two options(Show All Results,Show Results for a Constituency ID)
@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


# Define the route for displaying constituency results by his ID
@app.route("/result", methods=["GET"])
def result_by_id():
  return render_template("result_id.html")


# Define the route for displaying all constituency results
@app.route("/scoreboard", methods=["GET"])
def display_constituency_results_html():
    # Call the JSON API to get the constituency results
    response = app.test_client().get('/all_result')
    results = response.get_json()

    # Render the HTML template with the constituency results
    return render_template('constituencies.html', results=results)


# Define the route to get the constituency results from the server up to date
@app.route("/all_result")
def display_constituency_results():
    # Define the directory where the JSON files are stored
    directory = './resources/sample-election-results'

    # Create an empty list to store the results
    results = []

    # Loop over all the JSON files in the directory
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            # Read in the JSON file
            with open(os.path.join(directory, filename)) as f:
                constituency = json.load(f)

            # Get the winning party for the constituency
            winning_party = get_winning_party(constituency)

            # Add the constituency id and the constituency name and winning party to the results list
            results.append({'ID':constituency['id'],'constituency': constituency['name'], 'winning_party': winning_party})

        # Return the results as a JSON response
    return jsonify(results)


# Define the route for get constituency ID from the user and return the result of this ID
@app.route("/constituency/<constituency_id>")
def constituency(constituency_id):
    # Get the constituency results for the entered ID
    results= display_constituency_results_id()
    election_result= ElectionResultsService()
    result = election_result.get_result(constituency_id,results)
    if result:
        # Return the results as a JSON response
        return jsonify(result)
    else:
        # Return a 404 error if the entered ID is not found
        return abort(404)

