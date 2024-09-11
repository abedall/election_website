from threading import Timer
import random as r
import json
import os
import math as m

_num_of_constituinties: int = 650


class Updater:
    file_dir: str = os.path.dirname(os.path.realpath(__file__))

    def __init__(self) -> None:
        self.timer: Timer = None

        for file in os.listdir("./resources/updated-election-results"):
            os.remove(os.path.join(".", "resources", "updated-election-results", file))

        self.initialized = False
        # File updating every interval between 0 and 10000 millies.
        self.interval_start: int = 5
        self.interval_end: int = 10

    def update_file(self, file_num: int):
        file_name = "result" + str(file_num).zfill(3) + ".json"
        updated_result = "{}"
        with open(f"{Updater.file_dir}/resources/sample-election-results/{file_name}", "r") as f:
            result = json.load(f)
            votes_sum = 0
            parties = result["partyResults"]

            for party in parties:
                votes_sum += party["votes"]
            
            rest: int = votes_sum
            for par_id in range(len(parties)):
                party = parties[par_id]
                if par_id == len(result) - 1:
                    rand_votes: int = rest
                    rest = 0
                else:
                    rand_votes: int = int(r.random() * rest + 1)
                    rest -= rand_votes
                
                party["votes"] = rand_votes
                party["share"] = round(rand_votes / votes_sum * 100, 1)
            updated_result = result

        with open(f"{Updater.file_dir}/resources/updated-election-results/{file_name}", "w+") as f:
            json.dump(updated_result, f)
            

    def exec(self):
        print("execed")
        random_file_num: int = int(r.random() * _num_of_constituinties + 1)
        self.update_file(random_file_num)

        if self.timer:
            self.timer.cancel()

        time_to_exec: int = self._rand_interval()
        print(time_to_exec)
        self.timer = Timer(time_to_exec, self.exec)
        self.timer.start()

    def start(self):
        print("Started")
        if not self.initialized:
            self.initialized = True
            self.exec()
        
    def _rand_interval(self) -> int:
        return int(r.random() * (self.interval_end - self.interval_start) + self.interval_start + 1)