---
title: "Diagnostic Report: Corsair RM650 Hardware Failure"
tags: ["hardware", "RMA", "Corsair", "PSU"]
created_at: "2026-07-29"
last_updated_at: "2026-07-29"
---

# Diagnostic Report: Corsair RM650 Hardware Failure

**Model:** Corsair RM650 (CP-9020194-NA)
**Purchase Date:** October 8, 2020 (Amazon)
**Warranty Status:** Active (10-Year Manufacturer Warranty)

## Primary Symptom
The system experiences catastrophic "black-screen" hard crashes under 3D load, which recently escalated to occurring at complete idle (both in the Windows OS and within the UEFI BIOS environment). During these events, the display instantly drops signal, but the motherboard and case fans remain partially powered, indicating a severe voltage drop rather than a thermal trip.

## Diagnostic Isolation Steps Completed

1. **Software & OS Elimination:** 
   * Windows System Logs (`windows_system_log.evtx`) were extracted and parsed. `Kernel-Power 41` events confirmed unexpected hard power losses.
   * Crashes persisted in Safe Mode and ultimately occurred while idling inside the UEFI BIOS, entirely eliminating Windows OS, background processes, and display drivers as the root cause.
   
2. **Firmware (fTPM) Elimination:**
   * The motherboard BIOS was updated to the latest stable, non-beta version (`F18`), successfully patching known AMD fTPM microcode voltage bugs that mimic power failures. The crashes persisted immediately after the update.

3. **GPU Isolation (The Control Test):**
   * The primary GPU (AMD Radeon RX 580) was physically removed from the system.
   * A known-working, highly stable secondary GPU (AMD Radeon HD 7870) was installed.
   * The system immediately reproduced the exact same black-screen crash at idle with the control GPU installed, definitively eliminating the graphics card as the point of failure.

4. **Hardware PSU Tester Validation:**
   * The Corsair RM650 was removed from the system and connected to a standalone LCD Power Supply Tester at a local diagnostic shop. 
   * The tester emitted continuous warning beeps across the voltage rails during the PG (Power Good) check, indicating a failure to maintain ATX specification tolerances even under a static, synthetic load.

## Conclusion
The Corsair RM650's internal voltage regulation has severely degraded. It is failing to provide a stable, continuous 12V current to the motherboard and PCIe cables. The resulting transient voltage drops instantly kill the display signal and lock the motherboard. A warranty replacement (RMA) is requested.
