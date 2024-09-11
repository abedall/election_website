import os
import sys
import random
import threading
from src.server  import app
from src.updater import Updater
from src.results_service import ResultStore
import os
import time
import shutil

# define a function to check if there is any update files in the 'updated-election-results' folder
# this function will keep checking for updates each (5-10)s
def check_for_updates():
  while True  :
    # Get the list of files in the updated-election-results folder
    updated_files = os.listdir('./resources/updated-election-results')
    file_size = os.path.getsize('./resources/updated-election-results')

    if file_size == 0:
        # The file is empty
        print('The file is empty')

    for updated_file in updated_files:
        # Check if there is a corresponding file in the sample-election-results folder
        if os.path.exists('./resources/sample-election-results/' + updated_file):
            # Replace the old file with the new one
            shutil.copy('./resources/updated-election-results/' + updated_file,
                        './resources/sample-election-results/' + updated_file)
    time.sleep(random.randint(5, 10))

store = ResultStore()
dir_path = os.path.basename(os.path.dirname(os.path.realpath(__file__)))
if not dir_path == "src" :
    print("Please start main.py from src directory")
    sys.exit(1)

port: int = os.environ.get("PORT", 3000)

if os.environ.get('WERKZEUG_RUN_MAIN') != 'true':
    # do something only once. Flask in debug mode usually runs the file twice for reloading purposes.

    updater: Updater = Updater()
    updater.start()
    # start check_for_updates function as a separate thread
    update_thread = threading.Thread(target=check_for_updates)
    update_thread.start()

app.run(port=port, debug=True)

