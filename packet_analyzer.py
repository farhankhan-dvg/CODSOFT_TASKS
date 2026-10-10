from scapy.all import sniff, IP, TCP, UDP, ICMP

def packet_callback(packet):
    if packet.haslayer(IP):
        src = packet[IP].src
        dst = packet[IP].dst
        proto = "TCP" if packet.haslayer(TCP) else ("UDP" if packet.haslayer(UDP) else ("ICMP" if packet.haslayer(ICMP) else "Other"))
        print(f"[{proto}] {src}  ===>  {dst}")

print("Capturing 15 network packets...")
sniff(prn=packet_callback, count=15)
print("Capture finished successfully!")