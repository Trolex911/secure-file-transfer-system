# Secure File Transfer System

## Overview
This project demonstrates a basic secure file transfer system built using Python socket programming. It simulates a client-server architecture with an added layer of encryption for secure communication.

## Features
- Client-server communication using sockets
- File transfer over network
- XOR-based encryption and decryption
- Handles binary data transmission

## Technologies Used
- Python
- Socket Programming

## How It Works
1. The server listens for incoming connections.
2. The client connects and sends a file.
3. Data is encrypted before transmission.
4. The server decrypts and saves the file.

## How to Run

### Run Server
```bash
python server.py
