5#!/usr/bin/env python3
"""
Enhanced Multi-Client for Multi-Service Server
Demonstrates different socket protocols and client types
"""
import socket
import threading
import time

class MultiServiceClient:
    def __init__(self):
        self.chat_running = False
    
    def tcp_chat_client(self, host='localhost', port=9001):
        """Connect to TCP chat service"""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((host, port))
            
            # Get username prompt
            response = sock.recv(1024).decode()
            if response.startswith("USERNAME:"):
                username = input("Enter username: ")
                sock.send(username.encode())
            
            self.chat_running = True
            
            # Start receiving messages
            receive_thread = threading.Thread(target=self.receive_chat_messages, args=(sock,))
            receive_thread.daemon = True
            receive_thread.start()
            
            print(f"💬 Connected to chat! Type messages (or 'quit' to exit)")
            
            # Send messages
            while self.chat_running:
                message = input()
                if message.lower() == 'quit':
                    break
                sock.send(message.encode())
            
        except Exception as e:
            print(f"❌ Chat error: {e}")
        finally:
            sock.close()
            self.chat_running = False
    
    def receive_chat_messages(self, sock):
        """Receive chat messages in background"""
        while self.chat_running:
            try:
                data = sock.recv(1024).decode()
                if data.startswith("MSG:"):
                    print(f"\r{data[4:]}")
                elif data.startswith("HISTORY:"):
                    print(f"📜 {data[8:]}")
                print("> ", end="", flush=True)
            except:
                break
    
    def udp_info_client(self, host='localhost', port=9002, command="STATUS"):
        """Send UDP info request"""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.sendto(command.encode(), (host, port))
            
            response, addr = sock.recvfrom(1024)
            print(f"📊 Server Info: {response.decode()}")
            sock.close()
            
        except Exception as e:
            print(f"❌ UDP error: {e}")
    
    def tcp_file_client(self, host='localhost', port=9003, action="upload", filename="test.txt"):
        """Upload or download files"""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((host, port))
            
            if action == "upload":
                # Create test content
                content = f"Test file created at {time.ctime()}\nSocket programming demo!"
                message = f"UPLOAD:{filename}:{content}"
                sock.send(message.encode())
                
                response = sock.recv(1024).decode()
                print(f"📤 Upload result: {response}")
                
            elif action == "download":
                message = f"DOWNLOAD:{filename}"
                sock.send(message.encode())
                
                response = sock.recv(4096).decode()
                if response.startswith("FILE:"):
                    content = response[5:]
                    print(f"📥 Downloaded content:\n{content}")
                else:
                    print(f"📥 Download result: {response}")
            
            sock.close()
            
        except Exception as e:
            print(f"❌ File error: {e}")
    
    def demo_all_services(self):
        """Demonstrate all services"""
        print("🎮 Multi-Service Client Demo")
        print("=" * 40)
        
        print("\n1. Testing UDP Info Service...")
        self.udp_info_client(command="STATUS")
        time.sleep(1)
        
        print("\n2. Testing File Upload...")
        self.tcp_file_client(action="upload", filename="demo.txt")
        time.sleep(1)
        
        print("\n3. Testing File Download...")
        self.tcp_file_client(action="download", filename="demo.txt")
        time.sleep(1)
        
        print("\n4. Getting server time...")
        self.udp_info_client(command="TIME")
        
        print("\n5. Starting chat client...")
        print("   (You can type messages or 'quit' to exit)")
        self.tcp_chat_client()

def main():
    client = MultiServiceClient()
    
    print("🎯 Enhanced Multi-Service Client")
    print("Choose an option:")
    print("1. Chat Client")
    print("2. Info Request (UDP)")
    print("3. File Upload")
    print("4. File Download") 
    print("5. Demo All Services")
    
    try:
        choice = input("\nEnter choice (1-5): ")
        
        if choice == "1":
            client.tcp_chat_client()
        elif choice == "2":
            cmd = input("Enter command (STATUS/TIME/USERS): ") or "STATUS"
            client.udp_info_client(command=cmd)
        elif choice == "3":
            filename = input("Enter filename: ") or "test.txt"
            client.tcp_file_client(action="upload", filename=filename)
        elif choice == "4":
            filename = input("Enter filename: ") or "test.txt"
            client.tcp_file_client(action="download", filename=filename)
        elif choice == "5":
            client.demo_all_services()
        else:
            print("Invalid choice")
            
    except KeyboardInterrupt:
        print("\n👋 Goodbye!")

if __name__ == "__main__":
    main()
