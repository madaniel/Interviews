
import sys
import math
import random
import subprocess
from argparse import ArgumentParser
from multiprocessing import Process, Manager

# Defines
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

    @staticmethod
    def start_process(pid, data_dict, lock):
        """
        Starts a single process
        """
        seconds = random.randint(PROCESS_MIN_SECONDS, PROCESS_MAX_SECONDS)
        print(f"<debug> pid={pid}, seconds={seconds}")
        command = ["python", "stress.py", str(seconds)]
        stress_process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)

        while True:
            realtime_output = stress_process.stdout.readline()

            if realtime_output == b'' and stress_process.poll() is not None:
                break

            if realtime_output:
                realtime_output = realtime_output.decode('ascii')
                realtime_output_list = realtime_output.split()
                throughput = int(realtime_output_list[THROUGHPUT_INDEX])
                latency = int(realtime_output_list[LATENCY_INDEX])
                print(f"<debug> throughput={throughput} latency={latency}")

                with lock:
                    latency_list = data_dict["latency_list"]
                    throughput_list = data_dict["throughput_list"]
                    latency_list.append(latency)
                    throughput_list.append(throughput)
                    data_dict["latency_list"] = latency_list
                    data_dict["throughput_list"] = throughput_list

    def run_stress_process(self):
        """
        Start all the stress process
        """
        manager = Manager()
        shared_dict = manager.dict()
        worker_list = []
        shared_dict["latency_list"] = []
        shared_dict["throughput_list"] = []
        shared_lock = manager.Lock()

        for pid in range(self.process_amount):
            process = Process(target=self.start_process, args=(pid, shared_dict, shared_lock))
            worker_list.append(process)
            process.start()

        for worker in worker_list:
            worker.join()

        print(f"<debug> {str(shared_dict)}")


class Report(object):

    """
    Class for printing summary statistics
    """

    def __init__(self):
        self.min = None
        self.max = None
        self.average = None
        self.percentile = None

    def __repr__(self):
        return f"Average={self.average}, Min={self.min}, Max={self.max}, 95th Percentile={self.percentile}"


class Stats(object):

    """
    Class for statistics calculations
    """

    def __init__(self):
        self.min = math.inf
        self.max = -1
        self._average = None

    @staticmethod
    def get_average(data_list: list) -> float:
        """
        Calculates average of values in list
        """
        return sum(data_list) / len(data_list)

    @staticmethod
    def get_percentile(data_list: list, percentile: float) -> int:
        """
        Calculates percentile of values in list based on float value
        """
        assert 0 <= percentile <= 1, "percentile should be float between 0 and 1"
        size = len(data_list)
        sorted(data_list)
        index_of_percentile = int(round(size * percentile)) - 1
        assert 0 < index_of_percentile < len(data_list), f"index {index_of_percentile} is out of range of data_list {data_list}"

        return data_list[index_of_percentile]

    def update_min(self, value):
        """
        Update minimum value
        """
        if value < self.min:
            self.min = value

    def update_max(self, value):
        """
        Update maximum value
        """
        if value > self.max:
            self.max = value


if __name__ == "__main__":
    runner = Runner()
    runner.get_process_amount()
    runner.run_stress_process()
