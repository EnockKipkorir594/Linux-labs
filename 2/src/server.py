import socket 
import sys

def run_server(host='0.0.0.0', port=5000):
	#create a TCP socket 
	server_socket= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	#Enable address reuse to avoid "Address already in use"  errors on quick restarts 
	server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)


	try:
		server_socket.bind((host, port))
		print(f"[*] server bound to {host}:{port}")

		server_socket.listen(5)

		print(f"[*] server listening for incoming connections...")

		client_conn, client_address = server_socket.accept()

		print(f"[+] Accepted connection from {client_address[0]}:{client_address[1]}")

		raw_data = client_conn.recv(1024)

		if raw_data: 
			
			
			message = raw_data.decode('utf-8')

			print(f"[<] received message from client '{message}'")

			response = f"ACK: Server received '{message}'"

			client_conn.sendall(response.encode('utf-8'))

			print(f"[>] Sent response back to client '{response}'")

		print("[*] closing client connection")

		client_conn.close()


	except Exception as e: 
		print(f"[!] Error: {e}", file=sys.stderr)

	finally:

		print("[*] closing server listening socket")
		
		server_socket.close()


if __name__ == '__main__':
	run_server()
