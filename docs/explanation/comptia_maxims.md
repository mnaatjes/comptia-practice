---
title: "CompTIA Exam Maxims"
tags: ["CompTIA", "A+", "exam", "maxims", "strategy"]
created_at: "2026-07-17"
last_updated_at: "2026-07-17"
---

While CompTIA doesn’t publish an official "Secret Handbook of Maxims," the entire exam architecture is built on an unwritten code of structural logic. If you know these internal rules, you can consistently predict the correct answer on complex situational questions.

Think of these as the unwritten design patterns of the CompTIA universe:

---

### 1. The Financial Maxims

* **The Maxim of Minimum Sufficiency ("Most Cost-Effective"):**
  * *The Rule:* Never buy a Ferrari when a bicycle gets you across the street. If the prompt asks for the "most cost-effective" or "best budget" solution, identify the absolute minimum technical requirement to solve the problem, and pick the *cheapest* option that meets it. Anything extra is a wrong answer.

* **The Sunk Cost Maxim:**
  * *The Rule:* Corporate efficiency beats technical curiosity. If an enterprise component (like a motherboard or a proprietary laptop screen) fails out of warranty, and the repair labor plus part cost approaches or exceeds the replacement value of the unit, the CompTIA answer is always **Replace the device**, never "solder the component" or "rebuild the board."

---

### 2. The Operational & Safety Maxims

* **The Maxim of Least Privilege:**
  * *The Rule:* Trust no one with more access than they need to do their job this minute. If a user needs to update a single record in a database, they get write access to that specific table—never database administrator (DBA) privileges, and never local admin rights on the server box.

* **The "Life Safety First" Hierarchy:**
  * *The Rule:* Human life $>$ Data integrity $>$ Uptime. If a question involves a fire, an electrical hazard, a structural threat, or a CRT monitor discharge risk, the correct answer *always* prioritizes physical human safety and evacuation protocols over saving the server data or running a backup.

---

### 3. The Technical Allocation Maxims

* **The Virtualization Core Calculation ($N + 1$):**
  * *The Rule:* As we calculated before, resources are always expressed as $Total = Host + Guest(s)$. You must account for the hypervisor's footprint first before slicing up CPU cores, RAM, or storage pools for virtual environments.

* **The SOHO Wireless Default:**
  * *The Rule:* In a Small Office/Home Office environment, if it isn't encrypted with the highest available consumer standard (historically WPA2, currently **WPA3**), it is considered completely insecure. If a question asks how to secure a basic wireless access point, the priority chain is always: *Strongest Encryption Standard $\rightarrow$ Disable SSID Broadcast $\rightarrow$ Configure MAC Filtering.*

---

### 4. The Diagnostic Maxims

* **The "Identify the Problem" Separation of Concerns:**
  * *The Rule:* Never fix what you haven't defined. The first step of the 6-step troubleshooting methodology requires you to gather information from the user *before* implementing a solution. If an exam question asks what to do first when a user walks in with a broken computer, the correct answer is almost always to **ask open-ended questions** or duplicate the issue, rather than cracking open the case or changing configurations.

* **The Layer Isolation Law:**
  * *The Rule:* Software cannot fix broken copper; hardware cannot fix a syntax error. Always map the symptom to its native tier (Hardware, Firmware, OS/Network Link). If a device fails to initialize at the hardware level, any answer suggesting a software patch, registry edit, or driver installation is a deliberate distractor.

Mastering these maxims is what bridges the gap between studying raw flashcards and actually understanding how to pass the exam scenarios.
