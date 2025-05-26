import os
from scapy.all import rdpcap
from sklearn.ensemble import IsolationForest
import numpy as np

def extract_features(packets):
    return np.array([[len(packet)] for packet in packets])

def analyse_traffic(packet_queue, analysis_queue):
    if not os.path.exists('capture.pcap'):
        print("Error: 'capture.pcap' file not found.")
        return []

    packets = rdpcap('capture.pcap')
    features = extract_features(packets)

    analysis_results = []
    model = IsolationForest(contamination=0.05)
    model.fit(features)
    predictions = model.predict(features)

    for i, packet in enumerate(packets):
        protocol = packet.payload.name.upper()
        result = f"Packet: {packet.summary()} - Protocol: {protocol}"
        if predictions[i] == -1:
            result += " - Intrusion detected!"
        analysis_results.append(result)
        analysis_queue.put(result)

    return analysis_results
