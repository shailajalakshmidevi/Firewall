import configparser
class rule_engine:
    def __init__(self):
        # Rules include accepting source and destination IP-port pairs
        self.rules = {
            '40.91.120.196:443': 'Accept',  # Accept source IP and port
            '192.168.1.6:63451': 'Accept',  # Accept destination IP and port
            '54.192.151.48:443': 'Accept',  # Example of another rule
            # Add any additional rules you may need
        }

    def checkInboundRules(self, ip, port):
        ip_port = f"{ip}:{port}"
        print(f"Checking inbound rule for {ip_port}...")
        # Return 'Accept' if a rule matches, otherwise reject
        if ip_port in self.rules:
            print(f"Rule found: {self.rules[ip_port]}")
            return self.rules[ip_port]
        else:
            print(f"No rule found for {ip_port}, rejecting.")
            return "Reject"

    def checkOutboundRules(self, ip, port):
        ip_port = f"{ip}:{port}"
        print(f"Checking outbound rule for {ip_port}...")
        # Return 'Accept' if a rule matches, otherwise reject
        if ip_port in self.rules:
            print(f"Rule found: {self.rules[ip_port]}")
            return self.rules[ip_port]
        else:
            print(f"No rule found for {ip_port}, rejecting.")
            return "Reject"
