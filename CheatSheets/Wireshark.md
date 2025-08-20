# Wireshark Cheat Sheet (Quick)

- Start capture: `Capture -> Options`
- Display filter examples:
  - `http` / `tcp.port == 443` / `ip.addr == 192.168.1.10`
  - `dns && ip.src == 8.8.8.8`
- Right click -> Follow -> TCP Stream
- Save packets: `File -> Save As`
- Export objects: `File -> Export Objects -> HTTP`