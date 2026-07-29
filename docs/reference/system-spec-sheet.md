---
title: "System Specification Sheet"
tags: ["hardware", "reference", "specifications", "power-supply"]
created_at: "2026-07-29"
last_updated_at: "2026-07-29"
---

# Hardware Specification and PSU Requirements

## Current System Hardware
* **Motherboard:** GIGABYTE B550 Gaming X Rev 1.0 (Standard ATX form factor).
* **CPU:** AMD Ryzen 7 5700X Enhanced (AM4 Socket, ~65W-105W TDP).
* **GPU:** AMD Radeon RX 580 (Polaris architecture, highly power-hungry, typically draws ~185W to 225W at peak load).
* **RAM:** 32GB (4x 8GB DDR4 modules).
* **Storage:** 
  * 2x M.2 NVMe SSDs (1TB and 2TB).
  * Variable SATA support (up to 6x HDDs/SSDs supported by the motherboard).
* **Cooling/Peripherals:** 
  * 6x Air Fans (3x 120mm front, 2x 90mm CPU, 1x 90mm rear). No RGB or liquid cooling.
  * 1x PCIe Wi-Fi Card (motherboard has extra PCI/PCIe slots, but unoccupied).
  * Standard low-power USB wireless dongles.
* **Previous PSU:** Corsair RM650 (650W, ATX Form Factor, definitively failed).
* **Operating System:** Windows 11.

## Estimated Power Draw (Wattage Calculation)
* **CPU (Peak Load):** ~105 Watts
* **RX 580 (Peak Load):** ~225 Watts
* **Base Platform (Motherboard/32GB RAM/Storage):** ~50 Watts
* **Cooling & PCIe Peripherals:** ~30 Watts (6x fans, Wi-Fi card).
* **Maximum Continuous Load:** ~410 Watts
* **Transient Spike Overhead:** Older Polaris GPUs can occasionally spike 50W-100W above their rated TDP for milliseconds, requiring a robust 12V rail.

## New Power Supply Requirements
* **Form Factor:** Standard ATX Power Supply (PS2).
* **Wattage:** **650W**. (While 500W could technically boot the machine, power supplies are most efficient and run coolest when operating at 50% to 60% of their maximum capacity. A 650W unit provides the exact necessary headroom to absorb older GPU transient spikes without tripping Over-Current Protection, and is the logical ceiling for this build).
* **Cables Required:**
    * 1x 24-Pin ATX (Motherboard Power).
    * 1x 8-Pin EPS12V (CPU Power).
    * 1x 8-Pin PCIe (Required by the RX 580, though ensuring the new PSU has at least two 8-pin PCIe cables is highly recommended for future GPU upgrades).
    * SATA Power Cables (Ensure the PSU has a sufficient number of SATA power connectors to support your intended number of 2.5"/3.5" drives, up to 6).

## Future-Proofing Considerations
* **Platform Migration:** The ATX power standard (24-pin motherboard, 8-pin EPS) is universal. A high-quality 650W PSU can be seamlessly migrated to a future Intel-based motherboard with zero physical or electrical compatibility issues.
* **GPU Upgrade Path:** Based on a strict mid-range budget ceiling (~$500 maximum, e.g., RTX 4070 Super or RX 7800 XT), a 650W PSU is definitively sufficient. Modern mid-range architectures are highly power-efficient (the RTX 4070 Super draws ~220W, identical to the older RX 580).
* **ATX 3.0 Standard:** When purchasing a new PSU, looking for one explicitly labeled as "ATX 3.0 Compatible" ensures it includes the newer `12VHPWR` cable natively. This cable is required by modern Nvidia 4000-series graphics cards, preventing the need for adapter dongles in the future.

## PSU Replacement Candidates (650W)

| Manufacturer | Model | OEM Platform | Warranty | Efficiency | Estimated Price | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Thermaltake** | Toughpower GF1 650W | CWT | 10 Years | 80+ Gold | ~$80 - $90 | Highly rated Tier-A unit built on a robust CWT platform. Excellent ripple suppression for the price. |
| **MSI** | MAG A650GL | CWT | 7 Years | 80+ Gold | ~$75 - $90 | Budget-friendly while retaining native ATX 3.0 / PCIe 5.0 support. Fully modular. |
| **Seasonic** | Focus GX-650 | Seasonic (In-House) | 10 Years | 80+ Gold | ~$100 - $110 | Retained on list as the "premium" alternative. The industry gold standard for power delivery and acoustics. |
