#!/usr/bin/env python3
"""
Enhanced Multi-Service Socket Server
Demonstrates: TCP/UDP sockets, threading, multiple services, protocol handling
"""
import socket
import threading
import time
import json
from datetime import datetime

class MultiServiceServer:
    def __init__(self):
        self.running = True
        self.clients = {}
        self.message_history = []
        
    def tcp_chat_server(self, port=9001):
        """TCP Chat Service - Multiple clients can chat"""
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind(('localhost', port))
        sock.listen(5)
        print(f"📱 TCP Chat Server running on port {port}")
        
        while self.running:
            try:
                client, addr = sock.accept()
                thread = threading.Thread(target=self.handle_chat_client, args=(client, addr))
                thread.daemon = True
                thread.start()
            except:
                break
        sock.close()
    
    def handle_chat_client(self, client, addr):
        """Handle individual chat client"""
        username = None
        try:
            # Get username
            client.send("USERNAME:".encode())
            username = client.recv(1024).decode().strip()
            self.clients[client] = username
            
            # Send recent messages
            for msg in self.message_history[-5:]:
                client.send(f"HISTORY:{msg}".encode())
            
            # Broadcast join
            join_msg = f"{username} joined the chat"
            self.broadcast_message(join_msg, exclude=client)
            print(f"👤 {username} connected from {addr}")
            
            # Handle messages
            while self.running:
                data = client.recv(1024).decode().strip()
                if not data:
                    break
                    
                message = f"[{username}] {data}"
                self.message_history.append(message)
                self.broadcast_message(message, exclude=client)
                print(f"💬 {message}")
                
        except:
            pass
        finally:
            if client in self.clients:
                del self.clients[client]
                if username:
                    leave_msg = f"{username} left the chat"
                    self.broadcast_message(leave_msg)
                    print(f"👋 {username} disconnected")
            client.close()
    
    def broadcast_message(self, message, exclude=None):
        """Send message to all connected clients"""
        for client in list(self.clients.keys()):
            if client != exclude:
                try:
                    client.send(f"MSG:{message}".encode())
                except:
                    if client in self.clients:
                        del self.clients[client]
    
    def udp_info_server(self, port=9002):
        """UDP Info Service - Returns server stats"""
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind(('localhost', port))
        print(f"📊 UDP Info Server running on port {port}")
        
        while self.running:
            try:
                data, addr = sock.recvfrom(1024)
                request = data.decode().strip()
                
                if request == "STATUS":
                    response = {
                        "active_clients": len(self.clients),
                        "messages_sent": len(self.message_history),
                        "server_time": datetime.now().isoformat(),
                        "uptime": "Running"
                    }
                elif request == "TIME":
                    response = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                elif request == "USERS":
                    response = list(self.clients.values())
                else:
                    response = "Available commands: STATUS, TIME, USERS"
                
                sock.sendto(str(response).encode(), addr)
                print(f"📡 UDP request from {addr}: {request}")
                
            except:
                break
        sock.close()
    
    def tcp_file_server(self, port=9003):
        """TCP File Service - Simple file upload/download"""
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind(('localhost', port))
        sock.listen(5)
        print(f"📁 TCP File Server running on port {port}")
        
        while self.running:
            try:
                client, addr = sock.accept()
                thread = threading.Thread(target=self.handle_file_client, args=(client, addr))
                thread.daemon = True
                thread.start()
            except:
                break
        sock.close()
    
    def handle_file_client(self, client, addr):
        """Handle file upload/download requests"""
        try:
            # Simple protocol: UPLOAD:filename:content or DOWNLOAD:filename
            data = client.recv(4096).decode()
            
            if data.startswith("UPLOAD:"):
                parts = data.split(":", 2)
                if len(parts) == 3:
                    filename = parts[1]
                    content = parts[2]
                    with open(f"server_{filename}", "w") as f:
                        f.write(content)
                    client.send(f"File {filename} uploaded successfully".encode())
                    print(f"📤 File uploaded: {filename} from {addr}")
                
            elif data.startswith("DOWNLOAD:"):
                filename = data.split(":", 1)[1]
                try:
                    with open(f"server_{filename}", "r") as f:
                        content = f.read()
                    client.send(f"FILE:{content}".encode())
                    print(f"📥 File downloaded: {filename} to {addr}")
                except FileNotFoundError:
                    client.send("ERROR:File not found".encode())
        except:
            pass
        finally:
            client.close()
    
    def start(self):
        """Start all services"""
        print("🚀 Enhanced Multi-Service Server Starting...")
        print("=" * 50)
        
        # Start TCP Chat Server
        chat_thread = threading.Thread(target=self.tcp_chat_server)
        chat_thread.daemon = True
        chat_thread.start()
        
        # Start UDP Info Server  
        info_thread = threading.Thread(target=self.udp_info_server)
        info_thread.daemon = True
        info_thread.start()
        
        # Start TCP File Server
        file_thread = threading.Thread(target=self.tcp_file_server)
        file_thread.daemon = True
        file_thread.start()
        
        print("\n✅ All services started!")
        print("📱 TCP Chat: localhost:9001")
        print("📊 UDP Info: localhost:9002") 
        print("📁 TCP Files: localhost:9003")
        print("\nPress Ctrl+C to stop")
        
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("\n🛑 Shutting down server...")
            self.running = False

if __name__ == "__main__":
    server = MultiServiceServer()
    server.start()