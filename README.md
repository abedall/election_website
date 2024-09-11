## Description

If you are not familiar with how elections work in the UK, please see this short BBC video https://www.youtube.com/watch?v=cRxUhGetEPQ

The results website presents a simple elections result service.

### Domain
The domain for the election represents some key concepts:
- _**constituencyId**_ a unique integer id to identify a location. E.g "Brent Central" is 90
- _**party**_ is a short 3, or 4, letter code for a party for instance LAB = Labour, CON = Conservative etc.
- _**votes**_ the number of votes gained by a party in a constituency
- _**share**_ the % share of the total votes the party received

### API
The API has 3 endpoints:
- GET `/` serves the index.html file.
- GET `/result/{id}` to get an elections result for a given id.
- GET `/scoreboard` to get the running totals. This is unimplemented.

### Task
Display the election results in the resources folder to the user. The election results are stored in ./resources/sample-election-results folder. The minimum information to display is each constituency's name, and which party had the majority vote for that constituency.

A random constituency's results is changed every 5 to 10 seconds, the new results will be stored by the same name in the ./resources/updated-election-results folder. The information displayed to the user has to be updated accordingly with the ones on the server.

- You can use whichever javascript library you'd like (as long as it's actually needed.)
- Do not change the updater.py file.
- You can change the main.py file as long as you don't change it's current functionality.
- You can change anything else (Like the API end points, or create new python files.)

## Prerequisites
- python 3.9 or higher

### To Build
`pip install -r requirements.txt`

### To Run
- go to src folder.
- python ./main.py

or if you need to run it on another port,
`PORT=**** python ./main.py`

