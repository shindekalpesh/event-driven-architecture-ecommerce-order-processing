from collections import defaultdict
from time import perf_counter


class MetricsCollector:

    def __init__(self):
        self.counters = defaultdict(int)
        self.timings = defaultdict(list)

    def increment(self, metric_name):
        self.counters[metric_name] += 1

    def record_time(self, metric_name, duration):
        self.timings[metric_name].append(duration)

    def display(self):

        print("\n===== APPLICATION METRICS =====")

        print("\nCounters:")

        for name, value in self.counters.items():
            print(f"{name}: {value}")

        print("\nTimings: ")

        for name, values in self.timings.items():
            average = sum(values) / len(values)

            print(
                f"{name}: "
                f"average={average:.6f}s"
            )