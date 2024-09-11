## Description

If you are not familiar with how elections work in the UK, please see this short BBC video https://www.youtube.com/watch?v=cRxUhGetEPQ

The results website presents a simple elections result service.

### Domain
The domain for the election represents some key concepts:
- _**constituencyId**_ a unique integer id to identify a location. E.g "Brent Central" is 90
- _**party**_ is a short 3, or 4, letter code for a party for instance LAB = Labour, CON = Conservative etc.
- _**votes**_ the number of votes gained by a party in a constituency
- _**share**_ the % share of the total votes the party received

Endpoints (server.py)
GET /

Description: Serves the homepage allowing users to choose between "Show All Results" or "Show Results for a Constituency ID."
GET /result

Description: Displays results for a specific constituency by its ID. It renders the result_id.html page where users can input a constituency ID.
GET /scoreboard

Description: Displays the scoreboard of all constituencies’ results in an HTML template (constituencies.html). Calls /all_result to retrieve data.
GET /all_result

Description: Fetches all constituency results in JSON format. Displays the constituency ID, name, and the winning party for each.
GET /constituency/<constituency_id>

Description: Fetches and displays results for a specific constituency using the constituency_id. If the ID is invalid, it returns a 404 error.
Main Functions
display_constituency_results_id() (server.py):

Loops over all election result files and retrieves the constituency ID, name, and winning party.
get_winning_party(constituency) (server.py):

Determines the party with the most votes in a given constituency.
constituency(constituency_id) (server.py):

Retrieves election results for a specific constituency ID. If not found, it returns a 404 error.
Updater.exec() (updater.py)​(updater):

Periodically updates election results by randomly selecting a constituency and modifying its vote count. This update is then saved to the ./resources/updated-election-results folder.

## Prerequisites
- python 3.9 or higher

### To Build
`pip install -r requirements.txt`

### To Run
- go to src folder.
- python ./main.py

or if you need to run it on another port,
`PORT=**** python ./main.py`

