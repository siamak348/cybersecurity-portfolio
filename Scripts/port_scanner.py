#!/usr/bin/env python3
"""Simple TCP port scanner for learning purposes.

Usage:
    python3 port_scanner.py --host example.com --ports 20-1024
"""
import argparse
import socket

def scan_port(host: str, port: int, timeout: float = 0.5) -> bool:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(timeout)
        try:
            return s.connect_ex((host, port)) == 0
        except Exception:
            return False

def parse_ports(port_spec: str):
    parts = port_spec.split(',')
    for p in parts:
        p = p.strip()
        if '-' in p:
            a, b = p.split('-')
            for x in range(int(a), int(b)+1):
                yield x
        else:
            yield int(p)

def main():
    parser = argparse.ArgumentParser(description="Simple TCP port scanner (educational)")
    parser.add_argument("--host", required=True, help="Hostname or IP to scan")
    parser.add_argument("--ports", default="22,80,443", help="Comma-separated list or ranges, e.g., 20-25,80,443")
    args = parser.parse_args()

    print(f"Scanning {args.host} ...")
    for port in parse_ports(args.ports):
        if scan_port(args.host, port):
            print(f"[OPEN] {port}")
    print("Done. Use responsibly and only on hosts you own or have permission to test.")

if __name__ == "__main__":
    main()