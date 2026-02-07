# Enhanced Socket Programming Project

A sophisticated yet concise client-server application demonstrating multiple socket programming concepts.

## 🎯 Features Demonstrated

- **TCP Socket Programming** - Reliable connection-based communication
- **UDP Socket Programming** - Fast connectionless communication
- **Multi-threading** - Concurrent client handling
- **Multiple Services** - Different protocols on different ports
- **Real-time Chat** - Multi-user messaging system
- **File Transfer** - Upload/download functionality
- **Server Information** - Status and monitoring queries

## 📁 Files

- `enhanced_server.py` - Multi-service server (TCP Chat + UDP Info + TCP Files)
- `enhanced_client.py` - Multi-purpose client with menu interface

## 🚀 Quick Start

1. **Start the server:**

   ```bash
   python3 enhanced_server.py
   ```

2. **Run client(s):**
   ```bash
   python3 enhanced_client.py
   ```

## 🔧 Services Available

### 1. TCP Chat Service (Port 9001)

- Multi-user real-time chat
- Message history for new users
- User join/leave notifications

### 2. UDP Info Service (Port 9002)

- `STATUS` - Server statistics
- `TIME` - Current server time
- `USERS` - List of connected users

### 3. TCP File Service (Port 9003)

- Upload files to server
- Download files from server
- Simple protocol implementation

## 💡 Key Concepts Shown

- **Socket Types**: Both TCP (reliable) and UDP (fast)
- **Concurrency**: Multiple clients handled simultaneously
- **Protocol Design**: Custom message formats
- **Error Handling**: Robust connection management
- **Threading**: Background message receiving
- **Client-Server Architecture**: Clear separation of concerns

## 🎮 Usage Examples

```bash
# Terminal 1: Start server
python3 enhanced_server.py

# Terminal 2: Chat client
python3 enhanced_client.py
# Choose option 1 (Chat)

# Terminal 3: Another chat client
python3 enhanced_client.py
# Choose option 1 (Chat)

# Terminal 4: Info requests
python3 enhanced_client.py
# Choose option 2 (Info Request)
```

This project demonstrates advanced socket programming in under 200 lines while showing real-world concepts like chat systems, file transfer, and server monitoring.
