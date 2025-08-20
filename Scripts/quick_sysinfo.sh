#!/usr/bin/env bash
# quick_sysinfo.sh - Print basic system information (Linux/macOS)
echo "Hostname: $(hostname)"
echo "OS: $(uname -s) $(uname -r)"
echo "Uptime: $(uptime)"
echo "Users logged in:"
who