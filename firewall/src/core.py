# -*- coding: utf-8 -*-

from util import getIpAddress, getPort, isSrc
from tcp_packet import tcp_packet
from udp_packet import udp_packet
from rule_engine import rule_engine

# Assuming the previous imports and functions are already included (getIpAddress, getPort, etc.)

# Assuming the previous imports and functions are already included (getIpAddress, getPort, etc.)

def main(f):
    while True:
        # Skip the first two lines (assumed headers)
        f.readline()  # Read the first line (assuming it's not needed)
        f.readline()  # Read the second line (assuming it's not needed)

        s = f.readline()  # Read the next line

        # Debugging: Print the raw line
        print("Raw line read from file:", repr(s))

        # Skip empty lines
        if not s.strip():
            print("Warning: Empty line encountered, skipping...")
            continue

        # Slice and split the string to extract packet details
        if len(s) < 8:
            print("Error: Line too short to process:", repr(s))
            continue

        s = s[6:len(s)-2].split("|")

        # Check if the list is large enough
        if len(s) < 12:
            print("Error: Not enough elements in the list s:", s)
            continue

        # Create MAC address from the split list
        MACaddress = s[6] + ":" + s[7] + ":" + s[8] + ":" + s[9] + ":" + s[10] + ":" + s[11]

        # Process TCP or UDP packet based on protocol
        if len(s) > 23 and s[23] == "06":  # TCP packet
            packet = tcp_packet(
                MACaddress,
                getIpAddress(s[26:30]),
                getIpAddress(s[30:34]),
                getPort(s[34:36]),
                getPort(s[36:38])
            )
        elif len(s) > 23 and s[23] == "11":  # UDP packet
            packet = udp_packet(
                MACaddress,
                getIpAddress(s[26:30]),
                getIpAddress(s[30:34]),
                getPort(s[34:36]),
                getPort(s[36:38])
            )
        else:
            print("Error: Unknown or unsupported packet type")
            continue

        # Debugging: Print packet information
        print(packet.String())

        # Skip the next line (assuming it's not needed)
        f.readline()

        # Create a RuleEngine instance
        r = rule_engine()

        # Assuming the packet is outgoing from the server
        isSuccess = False
        if isSrc(['f8', '34', '41', '21', '87', '7a'], s[6:12]):
            print("Packet going out of our server...")
            print(f"Source IP: {packet.getSrcIP()} and port: {packet.getSrcPort()} will {r.checkOutboundRules(packet.getSrcIP(), packet.getSrcPort())}")
            print(f"Destination IP: {packet.getDstIP()} and port: {packet.getDstPort()} will {r.checkOutboundRules(packet.getDstIP(), packet.getDstPort())}")

            isSuccess = r.checkOutboundRules(packet.getSrcIP(), packet.getSrcPort()) == 'Accept' and \
                        r.checkOutboundRules(packet.getDstIP(), packet.getDstPort()) == 'Accept'

        else:
            print("Packet comes to our server...")
            print(f"Source IP: {packet.getSrcIP()} and port: {packet.getSrcPort()} will {r.checkInboundRules(packet.getSrcIP(), packet.getSrcPort())}")
            print(f"Destination IP: {packet.getDstIP()} and port: {packet.getDstPort()} will {r.checkInboundRules(packet.getDstIP(), packet.getDstPort())}")

            isSuccess = r.checkInboundRules(packet.getSrcIP(), packet.getSrcPort()) == 'Accept' and \
                        r.checkInboundRules(packet.getDstIP(), packet.getDstPort()) == 'Accept'

        # Check if both source and destination are allowed
        if isSuccess:
            print("Packet transmission successful.")
        else:
            print("Packet transmission failed. Rejected.")
