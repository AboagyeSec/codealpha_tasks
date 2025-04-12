from scapy.all import sniff, IP, TCP, UDP, DNS, wrpcap


packets = []

def capture_packet(packet):
    if packet.haslayer(IP):  
        print(f"Packet Captured: {packet.summary()}")  

        
        with open("captured_report.txt", "a") as f:
            f.write(f"{packet.summary()}\n")

        
        packets.append(packet)


sniff(count=50, prn=capture_packet)


wrpcap("captured_packets.pcap", packets)

print("\n Packets saved to captured_report.txt and captured_packets.pcap")
