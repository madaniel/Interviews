import sys
import random
import subprocess
from argparse import ArgumentParser
from multiprocessing import Pool, Manager

# Defines
PROCESS_MIN_SECONDS = 1
PROCESS_MAX_SECONDS = 1
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

    def start_process(self, args):
        """
        Starts a single process
        """
        pid, data_dict, lock = args[:]
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




class Analyze(object):
    pass


if __name__ == "__main__":
    runner = Runner()
    runner.get_process_amount()
    manager = Manager()
    shared_dict = manager.dict()
    shared_dict["latency_list"] = []
    shared_dict["throughput_list"] = []
    shared_lock = manager.Lock()

    with Pool(runner.process_amount) as pool:
        pool.map(runner.start_process, [(pid, shared_dict, shared_lock) for pid in range(runner.process_amount)])

    print(str(shared_dict))