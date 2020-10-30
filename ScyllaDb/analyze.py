
import sys
import math
import random
import subprocess
from argparse import ArgumentParser
from multiprocessing import Process, Manager

# Defines
PERCENTILE = 0.95
PROCESS_MIN_SECONDS = 2
PROCESS_MAX_SECONDS = 2
THROUGHPUT_INDEX = 1
LATENCY_INDEX = 4


class Runner(object):
    """
    This will a launch processes based on user argument
    """

    def __init__(self):
        self.process_amount = None

    def get_process_amount(self):
        """
        Get the amount of stress process that should run
        """
        parser = ArgumentParser(description="Amount of Stress processes")
        parser.add_argument("ProcessAmount", metavar="process_amount", type=int, help="Total number of processes that should run")
        args = parser.parse_args()
        process_amount = args.ProcessAmount

        if process_amount < 1:
            print("1 is the minimum value for process_amount")
            sys.exit(1)

        self.process_amount = process_amount

    def start_process(self, pid, data_dict, lock):
        """
        Starts a single process
        """
        seconds = random.randint(PROCESS_MIN_SECONDS, PROCESS_MAX_SECONDS)
        print(f"<debug> pid={pid}, seconds={seconds}")
        command = ["python", "stress.py", str(seconds), str(pid)]
        stress_process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)

        while True:
            realtime_output = stress_process.stdout.readline()

            if realtime_output == b'' and stress_process.poll() is not None:
                break

            if realtime_output:
                realtime_output = realtime_output.decode('ascii')
                realtime_output_list = realtime_output.split()
                pid = int(realtime_output_list[-1])
                throughput = int(realtime_output_list[THROUGHPUT_INDEX])
                latency = int(realtime_output_list[LATENCY_INDEX])
                print(f"<debug> throughput={throughput} latency={latency} pid={pid}")

                with lock:
                    # update stats per process
                    latency_list = data_dict["latency_list"]
                    throughput_list = data_dict["throughput_list"]
                    latency_list.append(latency)
                    throughput_list.append(throughput)
                    data_dict["latency_list"] = latency_list
                    data_dict["throughput_list"] = throughput_list
                    data_dict["update_counter"] = data_dict.get("update_counter", 0) + 1

            if data_dict["update_counter"] == self.process_amount:
                # print stats
                print("All completed !")
                data_dict["update_counter"] = 0

    def run_stress_process(self):
        """
        Start all the stress process
        """
        manager = Manager()
        shared_dict = manager.dict()
        worker_list = []
        shared_dict["latency_list"] = []
        shared_dict["throughput_list"] = []
        shared_dict["update_counter"] = 0
        shared_lock = manager.Lock()

        for pid in range(self.process_amount):
            process = Process(target=self.start_process, args=(pid, shared_dict, shared_lock))
            worker_list.append(process)
            process.start()

        for worker in worker_list:
            worker.join()

        print(f"<debug> {str(shared_dict)}")


class Stats(object):

    """
    Class for statistics calculations
    """

    def __init__(self):
        self.min = math.inf
        self.max = -1
        self.sum = 0
        self.count = 0
        self.percentile = None
        self._average = None

    @property
    def average(self) -> float:
        """
        Calculates average of values
        """
        return self.sum / self.count

    def _update_percentile(self, data_list: list, percentile: float):
        """
        Calculates percentile of values in list based on float value
        """
        assert 0 <= percentile <= 1, "percentile should be float between 0 and 1"
        size = len(data_list)
        sorted(data_list)
        index_of_percentile = int(round(size * percentile)) - 1
        assert 0 < index_of_percentile < len(data_list), f"index {index_of_percentile} is out of range of data_list {data_list}"

        self.percentile = data_list[index_of_percentile]

    def update_stats(self, new_value: int, data_list: list):
        """
        Update all statistics values per new value
        """
        if new_value < self.min:
            self.min = new_value

        if new_value > self.max:
            self.max = new_value

        self.sum += new_value
        self.count += 1
        self._update_percentile(data_list=data_list, percentile=PERCENTILE)

    def __repr__(self):
        return f"Average={self.average}, Min={self.min}, Max={self.max}, 95th Percentile={self.percentile}"


if __name__ == "__main__":
    runner = Runner()
    runner.get_process_amount()
    runner.run_stress_process()
