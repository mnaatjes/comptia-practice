---
title: "CompTIA A+ Exam Structure"
tags: ["CompTIA", "A+", "Core 1", "Core 2", "exam structure"]
created_at: "2026-07-17"
last_updated_at: "2026-07-17"
---

CompTIA A+ is unique because it is explicitly split into **two separate exams**, commonly referred to as **Core 1** and **Core 2**. You must pass both exams within the same version series to earn the certification.

The structural split is designed around a very clean functional boundary: **Core 1 is the physical hardware, components, and wires exam**, while **Core 2 is the software, configuration, security, and process exam**.

---

## 1. Exam Domain Breakdown

CompTIA formally organizes both exams into distinct, weighted domains. The current curriculum (the **V15 / 1200 series**) features the following topic divisions:

### Core 1 (Exam Code: 220-1201)

*Focuses on physical technology, foundational connectivity, and hardware diagnostic skills.*

* **Domain 1: Mobile Devices (13%)** – Form factors, internal components, and connectivity features of laptops, smartphones, tablets, and wearables.
* **Domain 2: Networking (23%)** – Network protocols, common port numbers, Wi-Fi standard variations, SOHO (Small Office/Home Office) router configurations, and essential cabling types.
* **Domain 3: Hardware (25%)** – The core physical architecture of computers: motherboards, CPU sockets, RAM generations, power supplies, mass storage types (SATA vs. NVMe SSDs), and printers.
* **Domain 4: Virtualization and Cloud Computing (11%)** – Hypervisors (Type 1 and Type 2), virtual machines, and cloud service structures (IaaS, PaaS, SaaS).
* **Domain 5: Hardware and Network Troubleshooting (28%)** – The practical application of CompTIA's formal 6-step troubleshooting methodology to isolate and fix failing motherboards, storage errors, and network connectivity drops.

### Core 2 (Exam Code: 220-1202)

*Focuses on operating system management, endpoint security, and organizational desktop workflows.*

* **Domain 1: Operating Systems (28%)** – Installation, management, and optimization of major operating systems, emphasizing Windows utilities and CLI tools (cmd, PowerShell), along with basic Linux, macOS, Android, and iOS environments.
* **Domain 2: Security (28%)** – Mitigating malware, recognizing social engineering threats, implementing physical security controls, managing user permissions (least privilege), device encryption, and standard SOHO wireless security settings.
* **Domain 3: Software Troubleshooting (23%)** – Resolving OS boot failures, broken user profiles, misbehaving device drivers, application crashes, and malware remediation.
* **Domain 4: Operational Procedures (21%)** – Best practices for structural IT support teams: change management procedures, technical documentation, ticketing workflows, safety protocols (e.g., proper grounding and lifting), data compliance regulations (GDPR, HIPAA), and professional communication habits.

---

## 2. How the Study Material is Logically Organized

While the exam domains are listed above by percentage weight, third-party study platforms (like Professor Messer, Mike Meyers, Jason Dion) and official CompTIA CertMaster guides do not necessarily present information in that exact numerical order.

Instead, high-quality study pipelines organize the material into **progressive conceptual tiers**:

```
[ Tier 3: Troubleshooting & Application ]  <-- CompTIA's 6-Step Method, Command-Line tools
                   ▲
[ Tier 2: Languages & Protocols ]          <-- IP Addressing, Ports, OSI, Security Policy
                   ▲
[ Tier 1: Ground-Level Hardware ]          <-- RAM, CPU sockets, Motherboard form factors

```

* **Hardware First (The Blueprint):** Study guides almost always start with individual components (RAM, motherboards, storage controllers). It is impossible to troubleshoot a storage mapping failure or allocate hardware resources to a virtual machine without first mastering how physical buses and storage controllers work.
* **Networking and Infrastructure Next:** Once local hardware is established, the material scales up to structural communication protocols (IP addressing, routing, network ports, and cloud basics).
* **Software Layering:** Only after the entire infrastructure framework is covered do study tracks transition to Core 2 software concepts. This is where you learn to apply the operating system utilities and configuration frameworks built on top of that infrastructure layer.
* **The Troubleshooting Capstone:** The material finishes by introducing the strict **CompTIA 6-Step Troubleshooting Methodology**. Both exams dedicate nearly a third of their questions directly to scenarios that test your ability to apply these diagnostic steps in order.
