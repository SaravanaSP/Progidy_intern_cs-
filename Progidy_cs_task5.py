import os
import sys
from scapy.all import *

# Disclaimer and terms of use
def display_disclaimer():
    print("------------------------ Packet Sniffer Tool Disclaimer ---------------------------")
    print("This packet sniffer tool is intended for educational and ethical purposes only.")
    print("Unauthorized use, distribution, or modification of this tool is strictly prohibited.")
    print("By using this tool, you agree to the following terms and conditions:")
    print("\n1. You will only use this tool on networks and systems for which you have explicit permission.")
    print("2. You will not use this tool to violate any laws, regulations, or terms of service.")
    print("3. You will not use this tool to harm, disrupt, or exploit any networks or systems.")
    print("4. You will not use this tool to intercept, collect, or store any sensitive or confidential information.")
    print("5. You will not redistribute or sell this tool without the express permission of the author.")
    print("6. The author is not responsible for any damages or losses incurred as a result of using this tool.")
    print("7. You will respect the privacy and security of all networks and systems you interact with using this tool.")

    accept_terms = input("\nDo you accept these terms and conditions? (y/n): ")

    if accept_terms.lower() != 'y':
        print("You must accept the terms and conditions before using this tool.")
        sys.exit()

# Function to analyze and display packet information
def packet_sniff(packet):
    # Check for IP layer in packet
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        protocol = packet[IP].proto
        
        output_string = f"\n[+] Packet Captured:\n"
        output_string += f"Source IP: {src_ip}\n"
        output_string += f"Destination IP: {dst_ip}\n"

        # Check for TCP layer
        if TCP in packet:
            src_port = packet[TCP].sport
            dst_port = packet[TCP].dport
            payload = str(packet[TCP].payload)
            output_string += f"Protocol: TCP\n"
            output_string += f"Source Port: {src_port}\n"
            output_string += f"Destination Port: {dst_port}\n"
            output_string += f"Payload: {payload[:50]}...\n"
        
        # Check for UDP layer
        elif UDP in packet:
            src_port = packet[UDP].sport
            dst_port = packet[UDP].dport
            payload = str(packet[UDP].payload)
            output_string += f"Protocol: UDP\n"
            output_string += f"Source Port: {src_port}\n"
            output_string += f"Destination Port: {dst_port}\n"
            output_string += f"Payload: {payload[:50]}...\n"
        
        # Check for ICMP layer
        elif ICMP in packet:
            output_string += f"Protocol: ICMP\n"
            output_string += f"Type: {packet[ICMP].type}\n"
            output_string += f"Code: {packet[ICMP].code}\n"
            output_string += f"Payload: {str(packet[ICMP].payload)[:50]}...\n"

        # Print and save the captured packet info
        print(output_string)
        with open(output_file, 'a') as f:
            f.write(output_string)

# Main function to run the sniffer tool
if __name__ == "__main__":
    # Display the disclaimer and terms
    display_disclaimer()

    print("\n--------------- Packet Sniffing Tool ---------------")
    
    # Set the path and filename for the output text file
    output_file = "packet_sniffer_results.txt"
    
    # Start packet sniffing
    print("[*] Starting packet capture... (press Ctrl+C to stop)")
    try:
        sniff(filter="ip", prn=packet_sniff, store=0)
    except KeyboardInterrupt:
        print("\n[!] Stopping packet capture...")
        print(f"\n[+] Results saved to: {output_file}")
        sys.exit()
