# **Computer Networks Lab Theory & Viva Guide – Simplified Notes**

> Friendly, concise, exam-ready theory + quick viva Q&A for all **12** lab experiments.
> Each experiment follows the requested structure (Aim → Theory → Tools → Flow → Commands → Advantages → Observations → Troubleshooting → Viva Q&A).
> Source (lab manual): ADYPSOE Computer Network Laboratory — used to shape experiment steps and examples. 

---

## Experiment 1 — **Types of Topologies & Transmission Media (using Packet Tracer)**

### Title & Aim

**Aim:** Demonstrate different network topologies (bus, star, mesh) and transmission media using Cisco Packet Tracer.

### Concept / Theory

* **Topology** = logical/physical layout of network devices.

  * **Bus:** Single backbone; simple, cheap; collisions increase.
  * **Star:** Central switch/hub; easy to manage; single point of failure (central device).
  * **Mesh:** Direct links between nodes; high redundancy; expensive.
* **Transmission media:** UTP/STP (copper), Coaxial, Fiber-optic (single/multi-mode).
* **Why Packet Tracer:** Simulation to test without real hardware. 

**Mini diagram (ASCII)**

```
Bus: PC ---|--- PC ---|--- PC
Star:       Switch
           /  |   \
         PC  PC   PC
Mesh: PC--PC
     |\ / |
     | X  |
     |/ \ |
    PC--PC
```

### Key Components / Tools Used

* Cisco Packet Tracer, generic PCs, switches, routers, cables (straight/crossover).
* Commands: configuring IPs on PC GUI in Packet Tracer.

### Working Principle / Internal Flow

1. Place devices in Packet Tracer.
2. Connect using correct cable (straight for PC↔Switch, crossover for PC↔PC older devices).
3. Configure IPs/subnet masks on PCs.
4. Use **Simulation** mode to view frame/packet flow and show how frames traverse topology.

### Important Commands / Algorithms

* PC IP config (GUI) or CLI: `ip address 192.168.1.2 255.255.255.0` (on real devices).
* Packet Tracer: use simulation filters to inspect ARP/ICMP packets.

### Advantages / Applications

* Understand physical & logical behavior.
* Compare performance and redundancy.
* Useful for planning real deployments and teaching.

### Expected Output / Observation

* Pings succeed in correctly wired networks.
* Simulation shows ARP requests, Ethernet frames and ICMP echo packets.
* Mesh provides alternate paths when a link fails.

### Common Errors / Troubleshooting Tips

* Wrong IP/subnet → ping fails.
* Incorrect cable type for older devices.
* Switch ports administratively down — enable them.

### Viva Qs (8)

1. **Q:** What is a network topology?
   **A:** The arrangement of nodes and links in a network.
2. **Q:** Name three topologies.
   **A:** Bus, star, mesh.
3. **Q:** Advantage of star?
   **A:** Easy to manage and isolate faults.
4. **Q:** Disadvantage of mesh?
   **A:** Costly and cabling-heavy.
5. **Q:** When use fiber optic?
   **A:** For long-distance, high-speed, electromagnetic-noise areas.
6. **Q:** Straight vs crossover cable?
   **A:** Straight for host→switch; crossover for host→host (older NICs).
7. **Q:** What packet does Ping use?
   **A:** ICMP Echo Request/Reply.
8. **Q:** Why use Packet Tracer?
   **A:** Safe, low-cost simulation of networks.

*(Source: lab manual Packet Tracer exercises). *

---

## Experiment 2 — **Setup Wired LAN using Layer-2 Switch (cable prep, test, ping, Wireshark)**

### Title & Aim

**Aim:** Build a wired LAN using a Layer-2 switch, crimp/test cables, configure IPs, test with `ping`, and capture packets with Wireshark.

### Concept / Theory

* **LAN:** Network covering small area.
* **UTP/STP:** Twisted pairs; categories (Cat5e, Cat6) determine speed.
* **RJ-45 pinout:** T568B/T568A standards for wiring.
* **Ping (ICMP):** Tests reachability & RTT. 

**Mini ASCII – T568B order (left to right, clip down):**

```
1: White/Orange
2: Orange
3: White/Green
4: Blue
5: White/Blue
6: Green
7: White/Brown
8: Brown
```

### Key Components / Tools Used

* Hardware: PCs, NICs, Layer-2 switch, CAT-5/CAT-6 cable, RJ-45, crimping tool, cable tester.
* Software: Wireshark to capture packets.

### Working Principle / Internal Flow

1. Crimp RJ-45 to cable end (follow T568B).
2. Test continuity with cable tester.
3. Connect PC→Switch (straight cable).
4. Configure PC IPs (e.g., `192.168.1.2/24`).
5. Test with `ping 192.168.1.3`.
6. Run Wireshark on one host or mirror port on switch; capture ARP & ICMP frames.

### Important Commands / Algorithms

* Windows IP config: `ipconfig /all`
* Linux: `ifconfig eth0 192.168.1.2 netmask 255.255.255.0` or `ip addr add ...`
* Ping: `ping <IP>`
* Wireshark filter: `icmp` or `arp`
* Crimp steps (short algorithm): strip → untwist → order → trim → insert RJ-45 → crimp.

### Advantages / Applications

* Practical cabling skills.
* Understand frame-level troubleshooting.
* Verifying network connectivity and latency.

### Expected Output / Observation

* Cable tester shows all 8 wires good.
* `ping` replies with time (ms).
* Wireshark shows ARP then ICMP Echo request/reply packets.

### Common Errors / Troubleshooting Tips

* Mis-wired RJ-45 → no link or errors.
* Wrong subnet mask or gateway → no ping.
* Disabled NIC or switch port → no link light.

### Viva Qs (10)

1. **Q:** What is the purpose of a cable tester?
   **A:** Verify continuity and correct pin wiring.
2. **Q:** What is ARP?
   **A:** Address Resolution Protocol; maps IP → MAC.
3. **Q:** Which cable for PC→Switch?
   **A:** Straight-through (T568B both ends).
4. **Q:** What does `ping` measure?
   **A:** Round-trip time and packet loss.
5. **Q:** How to capture only ICMP in Wireshark?
   **A:** Use filter `icmp`.
6. **Q:** Why crimp carefully?
   **A:** Poor crimp → intermittent connectivity.
7. **Q:** What are Cat5e/Cat6 used for?
   **A:** Ethernet at different performance levels.
8. **Q:** How to check IP in Linux?
   **A:** `ip addr show` or `ifconfig`.
9. **Q:** What is duplex mismatch?
   **A:** One end full-duplex, other half → collisions/slow.
10. **Q:** What LED indicates link on NIC?
    **A:** Link/activity LED on the port.

*(Lab manual details on cabling & ping.) *

---

## Experiment 3 — **Configure 3-Router Network (RIP / OSPF / BGP) with Packet Tracer**

### Title & Aim

**Aim:** Use Packet Tracer to configure a 3-router network using a chosen routing protocol (RIP/OSPF/BGP) and verify routes.

### Concept / Theory

* **RIP:** Distance-vector; metric = hop count; max 15 hops; periodic updates (legacy).
* **OSPF:** Link-state IGP; builds LSDB via flooding; uses Dijkstra to compute shortest paths; supports areas.
* **BGP:** Path-vector protocol used between autonomous systems (internet scale) — more advanced. 

**Small ASCII of the lab:**

```
[LAN-A]---R1---R2---R3---[LAN-B]
         |
        ISP
```

### Key Components / Tools Used

* Packet Tracer routers (1841/2900), PC end hosts, serial/Ethernet links.
* Commands via router CLI: `enable`, `configure terminal`, `router rip`, `router ospf`, `network ...`.

### Working Principle / Internal Flow (example OSPF)

1. Enable OSPF process: `router ospf 1`.
2. Advertise interfaces: `network 192.168.1.0 0.0.0.255 area 0`.
3. Routers form adjacencies; exchange LSAs; run Dijkstra; populate routing table.
4. Verify with `show ip route` and `show ip ospf neighbor`.

### Important Commands / Algorithms

* **RIP sample:**

  ```
  R1> enable
  R1# conf t
  R1(config)# router rip
  R1(config-router)# version 2
  R1(config-router)# network 10.10.10.0
  ```
* **OSPF sample:** `router ospf 1` then `network <net> <wildcard> area 0`.
* Useful show commands: `show ip route`, `show ip ospf interface`, `show ip rip database`.

### Advantages / Applications

* Learn dynamic routing basics.
* See tradeoffs: simplicity (RIP) vs scalability (OSPF/BGP).
* Useful for designing resilient networks.

### Expected Output / Observation

* Routing tables showing learned networks.
* Successful cross-LAN pings.
* OSPF neighbors in `FULL` state.

### Common Errors / Troubleshooting Tips

* Wrong network/wildcard mask in `network` statement → interface not advertised.
* Mismatched OSPF area IDs → no adjacency.
* Missing `no shutdown` on interfaces.

### Viva Qs (10)

1. **Q:** Metric used by RIP?
   **A:** Hop count.
2. **Q:** Max hops in RIP?
   **A:** 15 (16 = unreachable).
3. **Q:** OSPF algorithm?
   **A:** Dijkstra (Shortest Path First).
4. **Q:** OSPF area 0 is called?
   **A:** Backbone area.
5. **Q:** Command to view routing table?
   **A:** `show ip route`.
6. **Q:** Why BGP used?
   **A:** Routing between autonomous systems (Internet scale).
7. **Q:** What is split horizon?
   **A:** Prevents routing loops in distance-vector protocols.
8. **Q:** How to enable RIP v2?
   **A:** `router rip` then `version 2`.
9. **Q:** What is an LSA?
   **A:** Link State Advertisement (OSPF).
10. **Q:** OSPF neighbor stuck in `INIT`?
    **A:** Check hello/dead timers or network connect.

*(RIP/OSPF configs and commands in lab manual). *

---

## Experiment 4 — **Implement Link-State / Distance-Vector Routing Program**

### Title & Aim

**Aim:** Write a program implementing distance-vector or link-state routing to compute suitable paths (e.g., Bellman-Ford for DVR, Dijkstra for LSR).

### Concept / Theory

* **Distance-Vector (Bellman-Ford):** Each node keeps distances to all nodes and exchanges with neighbors; updates based on neighbors’ distances. Problems: count-to-infinity.
* **Link-State (Dijkstra):** Each node knows full topology (via flooding LSAs) and runs Dijkstra to compute shortest paths. 

### Key Components / Tools Used

* Programming language (Python/C/Java), adjacency matrix/list, console I/O.

### Working Principle / Internal Flow (Distance-vector)

1. Initialize: distance to self = 0; others = ∞.
2. Exchange distance vectors with neighbors.
3. Update: `D_x(y) = min_v { C(x,v) + D_v(y) }`.
4. Repeat until no changes.

(For Link-state: build adjacency, flood LSAs, run Dijkstra.)

### Important Commands / Algorithms (Pseudo-code)

**Bellman-Ford (conceptual):**

```
for i in 1..(N-1):
  for each edge (u,v) with weight w:
    if dist[u] + w < dist[v]:
      dist[v] = dist[u] + w
```

**Dijkstra (conceptual):** Priority queue + relax neighbors.

### Advantages / Applications

* Understand routing internals.
* Simulate routing dynamics and convergence.
* Basis for real protocols (RIP vs OSPF).

### Expected Output / Observation

* Printed routing tables showing next hops and costs.
* Convergence after iterations; proper shortest paths.

### Common Errors / Troubleshooting Tips

* Not handling ∞ correctly → overflow.
* Forgetting to update on neighbor change.
* Not detecting or mitigating loops (split horizon, poison).

### Viva Qs (8)

1. **Q:** Algorithm for distance-vector?
   **A:** Bellman-Ford.
2. **Q:** Algorithm for link-state?
   **A:** Dijkstra’s algorithm.
3. **Q:** What is count-to-infinity?
   **A:** Slow incorrect increase of metric after failure.
4. **Q:** How to mitigate loops in DV?
   **A:** Split horizon and route poisoning.
5. **Q:** Flooding means?
   **A:** Send LSA to all routers.
6. **Q:** DV converges when?
   **A:** No updates change distances.
7. **Q:** Complexity of Dijkstra?
   **A:** O(E + V log V) with heap.
8. **Q:** When use DV vs LS in practice?
   **A:** Small/simple networks → DV; large/scalable → LS.

*(Theory and algorithm notes in lab manual). *

---

## Experiment 5 — **TCP Socket Programming: Hello & File Transfer**

### Title & Aim

**Aim:** Implement TCP client-server programs to (a) exchange “Hello” messages and (b) transfer files reliably.

### Concept / Theory

* **TCP:** Connection-oriented, reliable, ordered byte stream, uses 3-way handshake (SYN, SYN-ACK, ACK), retransmission, flow & congestion control.
* **Socket:** Endpoint for network I/O. 

**TCP 3-way handshake (ASCII)**

```
Client -> Server: SYN
Server -> Client: SYN,ACK
Client -> Server: ACK
```

### Key Components / Tools Used

* Programming language sockets API (Python `socket`, Java `Socket`/`ServerSocket`), terminal, two machines.

### Working Principle / Internal Flow

**Server:**

1. `socket()` → `bind()` → `listen()` → `accept()` → recv/send → close.
   **Client:**
2. `socket()` → `connect()` → send/recv → close.

File transfer: read file in chunks, `send()` on sender, write to file on receiver.

### Important Commands / Algorithms (Pseudo-code)

**Server (Python outline):**

```python
s = socket.socket()
s.bind((HOST, PORT))
s.listen()
conn, addr = s.accept()
data = conn.recv(4096)
# save data to file
conn.close()
```

**Client (send file):**

```python
s.connect((HOST, PORT))
with open('file','rb') as f:
  while chunk := f.read(4096):
    s.sendall(chunk)
s.close()
```

### Advantages / Applications

* Reliable file transfer.
* Understanding flow control and error handling.
* Base for HTTP, FTP server/client coding.

### Expected Output / Observation

* Console shows connection established.
* File received intact (compare checksums).
* Wireshark shows TCP SYN/SYN-ACK/ACK, data segments.

### Common Errors / Troubleshooting Tips

* Firewall blocks port — open firewall.
* Buffer sizes mismatched → partial read.
* Forgot to close socket → resource leak.

### Viva Qs (10)

1. **Q:** What is TCP handshake?
   **A:** SYN, SYN-ACK, ACK (3-way).
2. **Q:** Which socket type for TCP?
   **A:** `SOCK_STREAM`.
3. **Q:** How ensure full file received?
   **A:** Loop `recv()` until EOF marker or known size.
4. **Q:** What is `bind()`?
   **A:** Assign address/port to server socket.
5. **Q:** `listen()` purpose?
   **A:** Accept incoming connections queue.
6. **Q:** What is `sendall()`?
   **A:** Sends all bytes, handling partial sends.
7. **Q:** How to debug no connection?
   **A:** Check `telnet host port` or `netstat`.
8. **Q:** TCP vs UDP — reliability?
   **A:** TCP reliable (ACKs/retrans), UDP unreliable.
9. **Q:** How to terminate connection?
   **A:** FIN/ACK sequence.
10. **Q:** Which tool to view packets?
    **A:** Wireshark.

*(Server/client algorithms found in lab manual). *

---

## Experiment 6 — **UDP Socket File Transfer (script/text/audio/video)**

### Title & Aim

**Aim:** Implement UDP-based file transfer for different file types between two machines.

### Concept / Theory

* **UDP:** Connectionless, best-effort, no guarantees on order or delivery. Good for streaming where speed matters. Packets are datagrams with 8-byte header. 

### Key Components / Tools Used

* UDP sockets (`SOCK_DGRAM`), sender/receiver programs, test files (script, txt, audio, video).

### Working Principle / Internal Flow (reliable UDP approach)

1. Sender: split file into chunks, number them, send datagrams.
2. Receiver: `recvfrom()`, store by sequence number, send ACK for each chunk (to add reliability).
3. Sender retransmits unACKed chunks within timeout.
4. Reassemble chunks in order and write file.

(You may implement a simple stop-and-wait or sliding window to increase efficiency.)

### Important Commands / Algorithms

* Socket creation: `socket(PF_INET, SOCK_DGRAM, 0)`
* `sendto()` / `recvfrom()`
* Simple stop-and-wait pseudo:

```
for seq, chunk in enumerate(chunks):
  sendto(packet(seq,chunk))
  wait for ack(seq); if timeout -> resend
```

### Advantages / Applications

* Real-time streaming (audio/video) where small losses acceptable.
* Lower overhead vs TCP.
* Useful for custom unreliable protocols.

### Expected Output / Observation

* Files received (maybe with custom reliability code) matching original if ACK/resend implemented.
* Wireshark shows UDP datagrams; no handshake packets.

### Common Errors / Troubleshooting Tips

* Packet loss: implement ACKs and retransmit.
* Out-of-order: include sequence numbers and reorder.
* MTU size exceed → fragmentation; use appropriate chunk size (~1400 bytes).

### Viva Qs (8)

1. **Q:** UDP socket type?
   **A:** `SOCK_DGRAM`.
2. **Q:** Why UDP for audio streaming?
   **A:** Lower latency; tolerate some loss.
3. **Q:** How ensure packet order?
   **A:** Add sequence numbers and reorder at receiver.
4. **Q:** How to detect missing packets?
   **A:** Sequence gaps; request retransmit.
5. **Q:** What is `recvfrom()`?
   **A:** Receive UDP packet and sender address.
6. **Q:** Should you use checksums?
   **A:** Yes, to detect corruption.
7. **Q:** How to avoid fragmentation?
   **A:** Use chunk < MTU (e.g., 1400 bytes).
8. **Q:** When NOT to use UDP?
   **A:** When reliable delivery is required (e.g., bank transactions).

*(UDP programming examples in lab manual). *

---

## Experiment 7 — **Study & Analyze HTTP, HTTPS, FTP using Packet Tracer**

### Title & Aim

**Aim:** Analyze HTTP, HTTPS, and FTP behavior (file upload/download, web serving) in Packet Tracer.

### Concept / Theory

* **HTTP:** Stateless application-level protocol (TCP port 80).
* **HTTPS:** HTTP over TLS (TCP port 443); ensures confidentiality and integrity.
* **FTP:** File Transfer Protocol uses control (21) and data channels (20 or negotiated); sends credentials in plaintext unless FTPS/SFTP used. 

### Key Components / Tools Used

* Packet Tracer server with FTP/HTTP services, client PC, browser and terminal FTP client.

### Working Principle / Internal Flow

1. Configure static IPs for server and client.
2. Use FTP client to upload `myFile.txt` to server: `ftp <server-ip>` → login → `put myFile.txt`.
3. Upload HTML to server HTTP directory; access via browser `http://server-ip`.
4. For HTTPS — demonstrate TLS handshake (conceptually) or simulate via Wireshark.

### Important Commands / Algorithms

* FTP commands: `ftp <ip>`, `put <file>`, `get <file>`, `cd /http`.
* HTTP: browse `http://<server-ip>/index.html`.
* Use Packet Tracer Server GUI to enable services and check file manager.

### Advantages / Applications

* Learn file transfer methods and differences in security.
* Understand multi-channel FTP behavior.
* Practice web hosting tasks and troubleshooting.

### Expected Output / Observation

* Successful file upload visible in server file manager.
* Browser able to retrieve uploaded HTML file.
* Packet traces show TCP sessions and HTTP/FTP commands.

### Common Errors / Troubleshooting Tips

* Wrong directory on server → file not accessible via HTTP.
* Firewall or ACLs block ports.
* FTP passive vs active mode issues behind NAT.

### Viva Qs (10)

1. **Q:** FTP control port?
   **A:** 21 (control); data uses 20 or negotiated ports.
2. **Q:** Difference HTTP vs HTTPS?
   **A:** HTTPS is encrypted (TLS) while HTTP is not.
3. **Q:** How to upload a file via FTP?
   **A:** `put filename` after logging in.
4. **Q:** What does `GET` do?
   **A:** HTTP method to retrieve a resource.
5. **Q:** Why HTTPS important?
   **A:** Confidentiality, integrity, authentication.
6. **Q:** FTP sends credentials how?
   **A:** In plaintext (unless FTPS/SFTP).
7. **Q:** How to check HTTP headers?
   **A:** Developer tools or `curl -I`.
8. **Q:** What is passive FTP?
   **A:** Server listens for data connection; client connects to server-specified port.
9. **Q:** Which ports does HTTPS use?
   **A:** TCP 443.
10. **Q:** How to enable HTTP service in Packet Tracer server?
    **A:** Use Services → HTTP and add files.

*(FTP & HTTP lab steps in manual). *

---

## Experiment 8 — **Study SSL/TLS via Wireshark Packet Capture**

### Title & Aim

**Aim:** Capture and analyze SSL/TLS packets using Wireshark while visiting an SSL-protected website.

### Concept / Theory

* **SSL/TLS:** Provides confidentiality, authentication and integrity for application protocols (HTTPS). TLS is successor to SSL.
* **TLS Record Layer:** Contains content type, version, length; handshake establishes ciphers & keys. 

**Handshake overview**

```
ClientHello -> ServerHello -> Certificate -> (ClientKeyExchange) -> ChangeCipherSpec -> Encrypted Application Data
```

### Key Components / Tools Used

* Browser, Wireshark, target HTTPS site (or local HTTPS server), optional server private key for decryption (if available).

### Working Principle / Internal Flow

1. Start Wireshark; apply display filter `ssl` or `tls`.
2. Visit HTTPS URL; capture:

   * ClientHello and ServerHello (cipher suites, version).
   * Certificate message (server certificate).
   * ClientKeyExchange and ChangeCipherSpec.
   * Encrypted Application Data (cannot view without keys).
3. Inspect handshake fields and TLS record structure.

### Important Commands / Algorithms

* Wireshark filter: `ssl || tls`.
* To decrypt (if you have server key): Preferences → Protocols → TLS → (RSA keys list) or use session keys (pre-master secrets).

### Advantages / Applications

* Understand cryptographic negotiation and certificate exchange.
* Troubleshoot TLS failures (wrong cert, cipher mismatch).
* Learn how secure web traffic looks on the wire.

### Expected Output / Observation

* Packets labeled ClientHello, ServerHello, Certificate, ChangeCipherSpec, Encrypted Alert.
* Certificate chain visible in clear during handshake.

### Common Errors / Troubleshooting Tips

* Cannot decrypt application data without keys.
* Some modern TLS configs use ephemeral keys (ECDHE) — RSA key won't decrypt.
* Use correct Wireshark filter `tls` (modern) rather than `ssl`.

### Viva Qs (10)

1. **Q:** What TCP port does HTTPS use?
   **A:** 443.
2. **Q:** Which message contains the server’s certificate?
   **A:** Certificate message.
3. **Q:** What does ChangeCipherSpec mean?
   **A:** Signals switch to encrypted communication.
4. **Q:** Can you view HTTPS payload in Wireshark?
   **A:** Not without keys (and often not even then due to ECDHE).
5. **Q:** Why use TLS over SSL?
   **A:** TLS is a standardized, improved successor.
6. **Q:** What’s in ClientHello?
   **A:** Supported cipher suites, random, session id, extensions.
7. **Q:** What is `server_name` extension?
   **A:** SNI (Server Name Indication) – requests specific host cert.
8. **Q:** What's an Alert message?
   **A:** Signals errors or connection close.
9. **Q:** How to filter only TLS records?
   **A:** Use Wireshark filter `tls`.
10. **Q:** Why certificates are important?
    **A:** Authenticate server identity and enable trust chain.

*(Wireshark TLS lab content from manual). *

---

## Experiment 9 — **S/MIME Email Security Implementation via MS Outlook**

### Title & Aim

**Aim:** Implement S/MIME email security (digital signing and encrypting) using Microsoft Outlook.

### Concept / Theory

* **S/MIME:** Standards for digital signatures and encryption in email using X.509 certificates. Provides authentication, integrity, and confidentiality. 

### Key Components / Tools Used

* MS Outlook, certificate authority (or self-signed cert), steps to import digital ID/certificate.

### Working Principle / Internal Flow

1. Obtain a digital certificate (Get a Digital ID).
2. Configure Outlook: Trust Center → Email Security → Add Signing Certificate.
3. Digitally sign email (adds signature header).
4. Encrypt email: Options → More Options → Security Settings → Encrypt message content and attachments.
5. Recipient must have sender’s public certificate to verify signature and sender must have recipient’s public key to encrypt message to them.

### Important Commands / Algorithms

* High-level steps shown in Outlook menus (no CLI). Key algorithms used in S/MIME: RSA for signatures/key exchange, AES for symmetric encryption.

### Advantages / Applications

* Protects sensitive email content.
* Complies with regulations (HIPAA, corporate policies).
* Ensures non-repudiation.

### Expected Output / Observation

* Sent email shows digital signature and encryption indicators.
* Recipient can verify signature and decrypt if they have private key/permissions.

### Common Errors / Troubleshooting Tips

* Certificate not trusted → signature shows as invalid.
* Recipient lacks public key → cannot decrypt.
* Wrong certificate installed → unable to sign.

### Viva Qs (8)

1. **Q:** What is S/MIME?
   **A:** Protocol for signing and encrypting email using certificates.
2. **Q:** What do you need to send an encrypted email?
   **A:** Recipient's public key (certificate).
3. **Q:** How to get a digital ID in Outlook?
   **A:** Trust Center → Email Security → Get a Digital ID.
4. **Q:** Difference signing vs encryption?
   **A:** Signing provides integrity/authenticity; encryption provides confidentiality.
5. **Q:** What algorithm commonly used?
   **A:** RSA for keys; AES for data encryption.
6. **Q:** If signature invalid — likely cause?
   **A:** Certificate expired or not trusted.
7. **Q:** Is S/MIME compatible with Gmail?
   **A:** Gmail supports S/MIME if enabled for account.
8. **Q:** Where S/MIME used in enterprise?
   **A:** Secure corporate email, regulated industries.

*(Steps summarized from lab manual S/MIME section). *

---

## Experiment 10 — **Study IPsec (ESP and AH) by Packet Capture**

### Title & Aim

**Aim:** Capture and study IPsec (ESP and AH) packets using Wireshark.

### Concept / Theory

* **IPsec:** Suite providing IP layer security: **AH** (Authentication Header) – integrity/authentication of IP packets; **ESP** (Encapsulating Security Payload) – confidentiality and/or integrity of IP payload. Uses ISAKMP/IKE for key exchange (UDP 500). 

### Key Components / Tools Used

* Two hosts or VPN endpoints, IPsec tunnel configuration, Wireshark to capture ESP/AH packets.

### Working Principle / Internal Flow

1. IKE Phase 1: Establish secure channel and authenticate peers (ISAKMP on UDP 500).
2. IKE Phase 2: Negotiate IPsec SAs (ESP/AH parameters).
3. Data: packets encapsulated using ESP/AH and sent across tunnel (protocol numbers 50=ESP, 51=AH).
4. Wireshark shows ESP/AH headers (payload encrypted for ESP).

### Important Commands / Algorithms

* IPsec policies depend on OS (e.g., `setkey` on Linux, or use GUI VPN tool).
* Wireshark filters: `esp` or `ah` or `udp.port==500`.

### Advantages / Applications

* Secure site-to-site VPNs, remote access VPNs.
* Protects IP packets end-to-end or tunnel mode for networks.

### Expected Output / Observation

* ISAKMP negotiation packets (UDP 500).
* ESP packets (protocol 50) – payload not readable; shows SPI and sequence number.
* AH packets (protocol 51) – integrity info covering IP header/payload.

### Common Errors / Troubleshooting Tips

* NAT traversal requires NAT-T (UDP encapsulation).
* Firewalls blocking UDP 500 or protocol 50/51.
* Mismatched SA proposals → negotiation fails.

### Viva Qs (10)

1. **Q:** IPsec protocols?
   **A:** AH (51) and ESP (50).
2. **Q:** Port used by IKE/ISAKMP?
   **A:** UDP 500 (and 4500 for NAT-T).
3. **Q:** Which provides confidentiality?
   **A:** ESP (when encryption enabled).
4. **Q:** Which provides integrity of IP header?
   **A:** AH (protects header & payload).
5. **Q:** Why NAT traversal needed?
   **A:** NAT changes IP headers; use NAT-T to encapsulate ESP in UDP.
6. **Q:** Wireshark filter for ESP?
   **A:** `esp`.
7. **Q:** What is SPI?
   **A:** Security Parameter Index identifies SA.
8. **Q:** Tunnel vs transport mode?
   **A:** Tunnel encapsulates whole IP packet; transport protects payload only.
9. **Q:** What must be opened on firewall for IPsec?
   **A:** UDP 500, UDP 4500 (NAT-T), protocol 50/51 as needed.
10. **Q:** Can ESP be authenticated but not encrypted?
    **A:** Yes, ESP can provide integrity-only (rare).

*(IPsec lab description & details in manual). *

---

## Experiment 11 — **Install & Configure DHCP Server (assign IPs automatically)**

### Title & Aim

**Aim:** Install and configure DHCP server; assign IP addresses automatically to client machines.

### Concept / Theory

* **DHCP:** Dynamic Host Configuration Protocol automates IP assignment (IP, mask, gateway, DNS). Works via DORA: Discover → Offer → Request → Acknowledge. 

**DORA Flow (ASCII)**

```
Client --DHCPDISCOVER--> Broadcast
Server --DHCPOFFER--> Client
Client --DHCPREQUEST--> Server
Server --DHCPACK--> Client
```

### Key Components / Tools Used

* DHCP server software (e.g., isc-dhcp-server on Linux), client machines configured to obtain IP automatically.

### Working Principle / Internal Flow

1. Configure DHCP server config file with network, range, options.
2. Start DHCP service: `sudo service isc-dhcp-server start`.
3. Client set to Obtain IP automatically → sends DHCPDISCOVER -> receives DHCPOFFER -> DHCPREQUEST -> DHCPACK.
4. Client config applied; verify with `ipconfig`/`ip addr`.

### Important Commands / Algorithms

* Example `dhcpd.conf` snippet:

```
subnet 192.168.1.0 netmask 255.255.255.0 {
  range 192.168.1.10 192.168.1.50;
  option routers 192.168.1.1;
}
```

* Restart server: `sudo service isc-dhcp-server restart`

### Advantages / Applications

* Centralized IP management.
* Avoid manual config errors.
* Lease management and easy network scaling.

### Expected Output / Observation

* Client obtains IP in the specified range.
* `dhcpd` logs show DISCOVER/OFFER/ACK sequence.

### Common Errors / Troubleshooting Tips

* Incorrect subnet in config → no leases given.
* DHCP server not on same VLAN → broadcasts blocked (use DHCP relay).
* Existing static IP conflicts.

### Viva Qs (8)

1. **Q:** What does DHCP stand for?
   **A:** Dynamic Host Configuration Protocol.
2. **Q:** What is DORA?
   **A:** Discover, Offer, Request, Acknowledge (DHCP flow).
3. **Q:** Where DHCP operates in OSI?
   **A:** Application layer (uses UDP).
4. **Q:** Which UDP ports used?
   **A:** 67 (server), 68 (client).
5. **Q:** What is a DHCP lease?
   **A:** Time period IP assigned to a client.
6. **Q:** How to view assigned leases?
   **A:** Check `dhcpd.leases` file or server UI.
7. **Q:** What is DHCP relay?
   **A:** Forwards DHCP broadcasts across networks.
8. **Q:** Why static IPs still needed?
   **A:** For servers/printers requiring fixed addresses.

*(DHCP installation steps in lab manual). *

---

## Experiment 12 — **DNS Lookup Program (IP ⇄ URL)**

### Title & Aim

**Aim:** Write a program that performs DNS lookups — given an IP returns URL (reverse DNS) and given a domain returns IP (forward DNS).

### Concept / Theory

* **DNS:** Distributed hierarchical naming system mapping hostnames to IP addresses. Forward lookup: name → A/AAAA records. Reverse lookup: IP → PTR record in `in-addr.arpa` (IPv4) or `ip6.arpa` (IPv6). 

### Key Components / Tools Used

* Sockets or DNS libraries (e.g., Python `socket.gethostbyname()` / `socket.gethostbyaddr()` or `dnspython`).

### Working Principle / Internal Flow

1. **Forward:** `resolve(domain)` → query DNS resolver → get A/AAAA.
2. **Reverse:** `reverse_lookup(ip)` → construct reverse domain (e.g., `1.0.0.127.in-addr.arpa`) → query for PTR.

### Important Commands / Algorithms (Python example)

```python
import socket
ip = socket.gethostbyname('example.com')
name = socket.gethostbyaddr('93.184.216.34')  # returns (hostname, aliaslist, ipaddrlist)
```

For more control use `dnspython`:

```python
import dns.resolver
answers = dns.resolver.resolve('example.com','A')
```

### Advantages / Applications

* Understand how name resolution works.
* Useful for network tools, logs interpretation, security auditing.

### Expected Output / Observation

* Correct IP(s) for domain input.
* Correct canonical name(s) for IP input (if PTR exists).

### Common Errors / Troubleshooting Tips

* No PTR record → reverse lookup fails.
* DNS caching or propagation delay may show older records.
* Firewall blocks DNS (port 53 UDP/TCP).

### Viva Qs (8)

1. **Q:** DNS default port?
   **A:** UDP 53 (TCP 53 also for zone transfers).
2. **Q:** What’s a PTR record?
   **A:** Pointer record for reverse DNS lookup.
3. **Q:** What does `dig` do?
   **A:** Query DNS servers for records.
4. **Q:** What is TTL?
   **A:** Time To Live controlling caching duration.
5. **Q:** Why reverse DNS sometimes missing?
   **A:** PTR not configured by IP owner (ISP).
6. **Q:** Which record for IPv6?
   **A:** AAAA (forward) and `ip6.arpa` PTR (reverse).
7. **Q:** How to get host IP in Python?
   **A:** `socket.gethostbyname(hostname)`.
8. **Q:** Why CNAME used?
   **A:** To alias one name to another.

*(DNS basics referenced from lab manual and standard APIs). 

---

# Quick Appendix — Most-useful Commands & Filters (one-page cheat-sheet)

* **Ping (reachability):** `ping <IP/host>`
* **Show routes (Cisco):** `show ip route`
* **OSPF neighbor:** `show ip ospf neighbor`
* **RIP status:** `show ip rip database`
* **Wireshark filters:** `icmp`, `arp`, `http`, `tls`, `ip.addr==x.x.x.x`, `esp`, `ah`
* **Packet Tracer:** Use Simulation and Event List to inspect frames
* **Linux network:** `ip addr`, `ifconfig` (legacy), `netstat -rn` / `route -n`
* **Socket (Python):** `socket.socket()`, `bind()`, `listen()`, `accept()`, `connect()`, `sendall()`, `recv()`
* **DHCP:** `dhcpd.conf` edits → `sudo systemctl restart isc-dhcp-server`
* **DNS quick check:** `dig +short example.com` / `dig -x 1.2.3.4`

---

## Final Notes & Study Tips

* Memorize **flows**: TCP 3-way, DHCP DORA, DNS forward/reverse, TLS handshake — these are common viva points.
* Practice **one-liners**: `show` commands, `ping`, Wireshark filters.
* When in lab: **draw** quick ASCII diagrams to explain topology/routing in viva.
* Use Packet Tracer to **simulate** before applying to real devices.

---