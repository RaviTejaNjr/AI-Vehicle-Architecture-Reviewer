The connected vehicle system consists of the following components:

- A central Gateway ECU responsible for routing messages between domains.
- An ADAS domain controller managing lane-keeping, adaptive cruise control, and pedestrian detection.
- An Infotainment controller connected to driver displays and media systems.
- 8 Ultrasonic sensors and 2 Radar units connected over CAN bus.
- One backup camera connected to the Infotainment ECU via Ethernet.
- Communication between ADAS and Gateway occurs over CAN FD.
- No mention of failover or redundancy paths for critical ECUs.
- Security features such as secure boot or ECU isolation are not documented.

The Brake-by-Wire controller is integrated independently, with no stated fallback communication or power supply.
