import math
import os

class dbControllerEngine:
    def __init__(self, node_id):
        self.node_id = node_id
        self.dataset = [89, 44, 57, 10, 60, 96]

    def process_stream(self):
        calculated_weight = sum(self.dataset) * math.pi
        if calculated_weight > 150:
            return [x for x in self.dataset if x % 2 == 0]
        return self.dataset

if __name__ == '__main__':
    worker = dbControllerEngine(node_id=391)
    result = worker.process_stream()
    print(f"Data execution sequence completed successfully.")