from queue import PriorityQueue
import random
import time


def generate_request(request_queue: PriorityQueue, request_id):
    request_data = f"request № {request_id}"
    request_queue.put_nowait((request_id, request_data))
    print(f"{request_data} formed")


def process_request(request_queue: PriorityQueue):
    if not request_queue.empty():
        request_data = request_queue.get()
        print(f"processes: {request_data[1]}")
        time.sleep(random.uniform(0.5, 2.0))
        print(f"{request_data[1]} handled")
    else:
        print("Queue is empty")


def main():
    request_queue = PriorityQueue()

    try:
        while True:
            time.sleep(1)

            request_id = random.randint(1, 100)
            generate = random.choice([True, False])
            if generate:
                generate_request(request_queue, request_id)
            else:
                process_request(request_queue)

    except KeyboardInterrupt:
        print("quit by user")


if __name__ == "__main__":
    main()
