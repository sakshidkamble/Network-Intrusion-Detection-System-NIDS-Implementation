# Network-Intrusion-Detection-System-NIDS-Implementation
This project implements a Network Intrusion Detection System (NIDS) using Python,  Wireshark, and Scapy. It demonstrates the setup and configuration of a custom NIDS to detect various network attacks, including port scans, DoS attacks, and SQL injection attempts.
---
 DEVELOPMENT & IMPLEMENTATION

 SYSTEM DESIGN

Basic Modules:

The NIDS is divided into several modules, each responsible for a specific function:

Capture Module: This module is responsible for capturing network packets as they traverse the nerwork. It stores the packets for real-time analysis and future reference.

Analysis Module: The analysis module uses the Isolation Forest machine learning algorithm to detect anomalies in the captured network traffic. It flags any suspicious activity for further investigation.

GUI Module: The GUI module provides a user-friendly interface for interacting with the NIDS. Lisers can view real-time traffic logs, receive alerts, and generate reports. The interface is designed to be intuitive, making it easy for users to access critical information quickly.

Reporting Module: This module generates detailed reports on detected intrusions, including the type of threat, affected systems, and recommended actions. The reports are customizable, allowing users to focus on specific types of data or incidents.

---
Detailed system design:

1. Capture Module The Capture Module is the foundation of the NIDS, responsible for intercepting and recording network traffic as it traverses the network. It operates in real-time, capturing packets from the network interface and storing them for further analysis by other modules.

Library Used: The Capture Module utilizes the Scapy library in Python, which provides powerful tools for network packet manipulation. Scapy is capable of handling various network protocols and is flexible enough to adapt to different network environments.

- Efficiency Considerations: To ensure that the Capture Module can handle high volumes of traffic without causing bottlenecks, optimizations such as multi-threading and efficient memory management are employed.

Real-time Processing: The Capture Module is designed to work in real-time, ensuring that there is minimal delay between packet capture and analysis.

Functionality:

-Packet Capture: The module captures all packets transmitted over the network, regardless of their protocol. This includes packets sent over TCP, UDP, ICMP, and other common network protocols.

-Packet Storage: Once captured, packets are stored temporarily in memory or written to disk for analysis. The storage is designed to be efficient, ensuring minimal impact on system performance.

- Filtering: The module can be configured to filter traffic based on specific criteria such as IP addresses, ports, or protocols, enabling more focused analysis on relevant data.

Preprocessing Basic preprocessing of packets may be done at this stage, such as extracting headers, payloads, and other relevant metadata that will be used by the Analysis Module.

2. Analysis Module The Analysis Module is the brain of the NIDS, where the captured network traffic is examined to identify potential threats. This module leverages machine learning. specifically the Isolation Forest algorithm, to detect anomalies that could indicate malicious activity.

Isolation Forest Algorithm: The Isolation Forest is an unsupervised learning algorithis used for anomaly detection. It works by constructing random forests where outliers are isolated earlier in the process, making it efficient for detecting anomalies in large datasets

Model Training: The model is trained on normal network traffic to learn what constitutes typical behavior. Once deployed, it continuously monitors live traffic, comparing it against the learned model to detect anomalies.

Data Input: The Analysis Module receives preprocessed data from the Capture Module. It performs further processing as needed, such as feature extraction, to prepare the data for analysis by the Isolation Forest algorithin.

Scalability: The module is designed to scale with the network size and traffic volume. Techniques like distributed processing or cloud-based infrastructure can be employed to handle larger datasets.

Functionality

-Anomaly Detection: The primary function of the Analysis Module is to identify deviations from normal network behavior. The Isolation Forest algorithm is particularly effective for this purpose. as it is designed to identify outliers in data sets, which in the context of network traffic, are often indicative of intrusions.

- Alert Generation: Upon detecting a potential intrusion, the Analysis Module generates an alert, which is then passed on to the GUI Module for user notification.

3. GUI Module -The Graphical User Interface (GUI) Module is the user-facing component of the NIDS. It provides a visual interface through which users can interact with the system, view real-time traffic logs, receive alerts, and generate detailed reports.

Library Used: The GUI Module is developed using Tkinter, a standard Python library for creating graphical interfaces. Tkinter is chosen for its simplicity, cross-platform compatibility, and ease of integration with other Python modules.

- User Experience (UX) Design: The GUI is designed with the user in mind, featuring a clean

layout, easy navigation, and responsive controls. Visual elements like charts and graphs are used to make data interpretation straightforward.

Customization: The GUI provides options for users to customize their experience, such as setting thresholds for alerts, selecting specific network segments to menitor, and configuring report formats.

Real-time Data Updates: The interface updates in real-time, reflecting the latest network activity and analysis results. This ensures that users always have the most current information at their fingertips.

Functionality

- Real-time Monitoring: The GUI displays real-time network traffic information, including packet counts, types of traffic, and any detected anomalies. Users can view logs and track the system's performance.

-Alert Notificanon When the Analysis Module detects a potential threat, the GUI immediately notifies the user through visual and audible alerts. The alerts are categorized by severity, allowing users to prioritize their response

-Report Generation: Users can generate detailed reports on detected intrusions directly from the GUI. These reports can be customized to include specific data points, time ranges, and types of threats.

-User Interaction: The GUI allows users to internet with the system by setting filters, configuring alert preferences, and managing the system's operation. It is designed to be intuitive, minimizing the learning curve for new users

4. Reporting Module The Reporting Module is responsible for compiling and presenting the data collected and analyzed by the NIDS. It generates comprehensive reports that provide insights into network activity, detected threats, and recommended actions.

Library Used: Matplotlib, a popular Python library for data visualization, is used to generate graphs and charts in the reports. This ensures that the reports are not only informative but also visually appealing.

Data Aggregation: The Reporting Module aggregates data over time, allowing for the creation of summary reports that highlight trends and patterns in network activity. This long-term view is crocial for identifying persistent threats or recurring issues.

Automated Reporting: The module supports automated report generation based on predefined schedules or triggered by specific events, such as a detected intrusion. This feature ensures that reports are consistently produced and disseminated without manual intervention.

Interactive Reports. For advanced users, reports can include interactive elements that allow for deeper exploration of the data, such as drill-down capabilities on specific anomalies or traffic patterns.

Functionality:

- Report Compilation: The module gathers data from the Capture and Analysis modules, organizing it into a coherent report format. This includes information on the types of traffic observed, anomalies detected, and any actions taken by the system.

- Customizable Reports: Users can customize the reports to focus on specific data points, such as traffic from a particular IP address, or incidents occurring within a specific time frame. This flexibility allows users to tailor reports to their needs.

Visualization: The Reporting Module uses visual elements like charts, graphs, and tables to present data in an easily digestible format. This helps users quickly grasp the significance of the reported information.

- Export and Sharing. Reports can be exported in various formats (e.g., PDF, CSV) and shared with relevant stakeholders. This is particularly useful for compliance reporting or for sharing information with security teams.

 ---
 FUTURE WORK & ADVANCEMENTS

1 Future Work and Advancements

While the NIDS developed in this project meets its primary objectives, there are several areas for potential future enhancement:

Advanced Machine Learning Models:

Scope: Experiment with other machine learning models such as neural networks, Support Vector Machines (SVM), or ensemble methods to improve anomaly detection accuracy.

Advancements: Implement and train models on larger and more diverse datasets to increase detection capabilities and reduce false positives/negatives.

Real-Time Analysis:

Scope: Upgrade the system to handle real-time traffic analysis, allowing for immediate threat detection and response.

Advancements: Integrate with streaming data platforms like Apache Kafka or Apache Flink for handling high-speed network traffic.

User Interface Enhancements:

Scope: Improve the GUI to include more features like interactive dashboards, detailed visualization of traffic patterns, and user-configurable settings.

Advancements: Use advanced visualization libraries or frameworks like D3.js or Plotly for more interactive and insightful data representation.

Automated Response Mechanisms:

Scope: Develop automated response capabilities to take predefined actions in response to detected anomalies.

Advancements: Implement integration with firewall systems or Intrusion Prevention Systems (IPS) to block or mitigate threats automatically.

---
REFERENCES

Literature Review References:

1) Machine Learning-Based Network Intrusion Detection for Big and Imbalanced Data Using Oversampling. Stacking Feature Embedding, and Feature Extraction. Md. Alamin Talukder, Md. Manowarul Islam, Md Ashraf Uddin, Khondokar Fida Hasan, Selina Sharmin, Salem A. Alyami, Mohammad Ali Moni, 2024, Journal of Big Data

DOI: 10.1186/540537-024-00886-w

2) Using Machine Learning Algorithms in Intrusion Detection Systems: A Review, Mazin S.. Hasanien Ali Talib, June 2024 DOI: 10.25130/tips.v2913,1553 3) Hybrid Intrusion Detection Technique for Internet of Things, Jose, Jinsi Jose, Deepa V. 24

January 2024, Journal of Telecommunication Systems and Management

DOI: 10.1016/j.teler.2022.100030

4) Performance Enhancement of Intrusion Detection System Using Dimensionality Reduction. Techniques and Evaluation with Different Machine Learning Classifiers on Optimal Dataset, Surya Prakash J, Suguna R, 16 February 2023, Shodhganga Link: http://hdl.handle.net/10603/480115

5) Effective Modeling of Aggregated Intrusion Detection System for Performance Enhancement, Priya N, Vasantha S, 22 October 2020, Shodhganga

Link: http://hdl.handle.net/10603/303809

6) Feature Selection and Classification Techniques for Effective Intrusion Detection, Rajesh Kambattan, K, Manimegalai, R, 21 September 2021, International Journal of Computational Intelligence

DOI: 10.25195/ijci.v50i1.462

7) Study and Analysis of Network Behaviour for Anomaly Detection, Selvakumar B. Muneeswaran K, 2021, Shodhganga Link: http://hdl.handle.net/10603/459144

8) Network Intrusion Detection System Using Machine Learning, Riyazahmed A. Jamadar, 2018. Indian Journal of Science and Technology

Link: https://indist.org/articles/network-intrusion-detection-system-using-machine-learning

9) An Ontology-Based Multi-agent Framework for Network Intrusion Detection, Anusha K. Sathiyamoorthy E, 2 July 2018, Shodhganga

Link: http://hdl.handle.net/10603/207041

10) Machine Learning and Deep Learning Methods for Intrusion Detection Systems: A Survey, Hongyu Liu, Bo Lang, October 2019, MDPI - Applied Sciences DOI: 10.3390/app9204396

11) Design and Development Consideration for Intrusion Detection and Prevention Systems, Beigh Bilal Maqbool, Peer Mushtaq Ahmad, 16 May 2016, Shodhganga Link: http://hdl.handle.net/10603/90198

12) Design and Analysis of Efficient Multilevel Security Model Using Cryptology Intrusion Detection and Prevention Systems, Makani, Ritu; Chaba, Yogesh, 15 April 2016, Shodhganga Link: http://hdl.handle.net/10603/81961

---

![WhatsApp Image 2025-05-25 at 18 21 40_2ae760e4](https://github.com/user-attachments/assets/c5d2a3ff-3c87-4e36-876b-0e0b4c9dec9b)  ---
![WhatsApp Image 2025-05-25 at 18 20 32_5fd43750](https://github.com/user-attachments/assets/9b7e6aa8-fc96-494e-a749-2aa4007fa209) ---
![WhatsApp Image 2025-05-25 at 18 20 12_cbd0d7d0](https://github.com/user-attachments/assets/1c5ba8f5-1c5d-4cb8-a5c1-62783886b441) ---
![WhatsApp Image 2025-05-25 at 18 19 04_8cab601f](https://github.com/user-attachments/assets/b687fda8-4da2-49e8-9b4a-0561227c4a34) ---
![WhatsApp Image 2025-05-25 at 18 19 42_fefd7d63](https://github.com/user-attachments/assets/4e05ce7f-2252-48d6-ad23-af86fd428049)
