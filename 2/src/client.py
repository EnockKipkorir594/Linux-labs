import socket
import sys

def run_client(server_ip='172.24.0.10', server_port=5000):
    # 1. Create a TCP socket (AF_INET = IPv4, SOCK_STREAM = TCP)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # 2. Connect to the server
        print(f"[*] Attempting to connect to server at {server_ip}:{server_port}...")
        client_socket.connect((server_ip, server_port))
        print(f"[+] Connected successfully to {server_ip}:{server_port}")

        # 3. Send a message to the server
        message = "Hello from Lab 2 TCP Client!"
        print(f"[>] Sending message: '{message}'")
        client_socket.sendall(message.encode('utf-8'))

        # 4. Receive the server's response (buffer size 1024 bytes)
        raw_response = client_socket.recv(1024)
        server_response = raw_response.decode('utf-8')

        # 5. Display the response
        print(f"[<] Received response from server: '{server_response}'")

    except ConnectionRefusedError:
        print(f"[!] Connection refused. Ensure the server is actively listening on {server_ip}:{server_port}.", file=sys.stderr)
    except Exception as e:
        print(f"[!] An error occurred: {e}", file=sys.stderr)
    finally:
        # 6. Close the socket
        print("[*] Closing client socket.")
        client_socket.close()

if __name__ == '__main__':
    run_client()

