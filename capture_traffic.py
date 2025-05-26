from scapy.all import sniff, wrpcap
import logging
from queue import Queue

def capture_network_traffic(packet_queue):
    packets = []

    def process_packet(packet):
        packets.append(packet)
        packet_queue.put(packet.summary())
        logging.info(f"Packet captured: {packet.summary()}")

    logging.basicConfig(filename='capture.log', level=logging.INFO, format='%(asctime)s - %(message)s')

    print("Starting packet capture...")
    sniff(count=150, prn=process_packet)
    wrpcap('capture.pcap', packets)
    print("Traffic capture completed. Data saved to capture.pcap")
