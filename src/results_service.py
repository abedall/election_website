from flask import jsonify
class ResultStore:

    def __init__(self) :
        self.store: list[dict] = []
    
    def get_result(self, id_to_get) -> str:
        result: list[dict] = list(filter(lambda result: result['id'] == int(id_to_get), self.store))
        print('this is result from function',result)
        return f"No result with id {id_to_get} found." if len(result) < 1 else result[0]

    def new_result(self, result) -> None:
        self.store.append(result)

    def get_all(self) -> list:
        return self.store

    def reset(self) -> None:
        self.store: list[dict] = []

import json
import os

class ElectionResultsService:

    def __init__(self):
        self.results = {}

    def load_results(self, filename):
        with open(filename) as f:
            self.results = json.load(f)

    def get_all_results(self):
        return self.results

    def get_result(self, constituency_id,results):
        for result in results:
            if not constituency_id.isdigit():
                return "Invalid constituency ID. Please enter a valid integer ID."
            if int( result['Constituency ID']) ==int( constituency_id):
                return result
        return   f"No result with id {constituency_id} found."