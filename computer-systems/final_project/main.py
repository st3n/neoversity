import os
import logging
import http.server
import socketserver
import urllib.parse
import multiprocessing
from socket import socket, AF_INET, SOCK_STREAM
from datetime import datetime
from pymongo import MongoClient

PORT = 3000
SOCKET_SERVER_PORT = 5000

MONGO_URI = "mongodb://mongo:27017/"
DB_NAME = "messages_db"
COLLECTION_NAME = "messages"

client = MongoClient(MONGO_URI)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]

# Set up logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger()


class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.path = "/templates/index.html"
        elif self.path == "/message":
            self.path = "/templates/message.html"
        elif self.path.startswith("/static"):
            self.path = self.path
        else:
            self.path = "/templates/error.html"
            self.send_response(404)

        return http.server.SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        if self.path == "/message":
            length = int(self.headers["Content-Length"])
            field_data = self.rfile.read(length).decode("utf-8")
            fields = urllib.parse.parse_qs(field_data)

            username = fields.get("username")[0]
            message = fields.get("message")[0]

            data = f"{username}|{message}"
            with socket(AF_INET, SOCK_STREAM) as s:
                s.connect(("localhost", SOCKET_SERVER_PORT))
                s.sendall(data.encode("utf-8"))

            self.send_response(301)
            self.send_header("Location", "/")
            self.end_headers()
            logger.info(f"Form submitted: {username}, {message}")


def start_http_server():
    with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
        logger.info(f"HTTP server running on port {PORT}")
        httpd.serve_forever()


def start_socket_server():
    with socket(AF_INET, SOCK_STREAM) as server_socket:
        server_socket.bind(("0.0.0.0", SOCKET_SERVER_PORT))
        server_socket.listen(5)
        logger.info(f"Socket server running on port {SOCKET_SERVER_PORT}")

        while True:
            conn, addr = server_socket.accept()
            with conn:
                data = conn.recv(1024).decode("utf-8")
                if data:
                    username, message = data.split("|")
                    message_data = {
                        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"),
                        "username": username,
                        "message": message,
                    }
                    collection.insert_one(message_data)
                    logger.info(f"Message saved to MongoDB: {message_data}")


if __name__ == "__main__":
    p1 = multiprocessing.Process(target=start_http_server)
    p2 = multiprocessing.Process(target=start_socket_server)

    p1.start()
    p2.start()

    p1.join()
    p2.join()
