# FT8 Spy

[![pypresence](https://img.shields.io/badge/using-pypresence-00bb88.svg?style=for-the-badge&logo=discord&logoWidth=20)](https://github.com/qwertyquerty/pypresence)

## Overview

This Python script integrates Discord Rich Presence with the popular amateur radio software WSJT-X. By using the pypresence library, it communicates with the Discord API to display real-time information about your WSJT-X activity as your Discord status.

## Prerequisites

- Python 3.x installed on your system.
- Discord account.
- WSJT-X software installed and running.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/your-repo.git
    ```

2. Install required Python packages:

    ```bash
    pip install pypresence
    ```

## Usage

1. Run the script:

    ```bash
    python your_script.py
    ```

2. Make sure WSJT-X is running.

3. The script will connect to Discord RPC and start updating your Discord status based on the WSJT-X activity.

## Customization

Adjust the `IP_ADDRESS` and `PORT` variables in the script to match your WSJT-X UDP server configuration.

## Notes

- Discord Rich Presence is typically limited in how frequently it can be updated. The script is set to update every 5 seconds, but you may adjust this based on Discord's rate-limiting policies.
- Please be aware that Discord application IDs are public information and not considered sensitive like tokens. However, ensure not to expose your Discord token or any other sensitive information in your code.
- This integration uses the `pypresence` library for Discord RPC communication and `server` and `wsjtx_decoder` for handling WSJT-X UDP packets.

## Acknowledgments

- [pypresence](https://github.com/qwertyquerty/pypresence): A Python library for Discord Rich Presence.
- [WSJT-X](https://wsjt.sourceforge.io/wsjtx.html): The popular software for amateur radio communication using weak signal propagation modes.
- [pywsjtx](https://github.com/bmo/py-wsjtx) by Brian Moran: Source of the decoder and server modules.
