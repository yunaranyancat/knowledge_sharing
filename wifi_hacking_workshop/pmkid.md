https://github.com/OscarAkaElvis/PMKID_PoC

# PMKID_PoC

This repository contains the necessary files used for a **PMKID vulnerability Proof of Concept**.

It is based on a modified copy of the original [hostapd project](http://w1.fi/hostap/) that has been **intentionally patched** to introduce the PMKID vulnerability.

For background information on this vulnerability, see this detailed write-up: [PMKID Attacks: Debunking the 802.11r Myth](https://www.nccgroup.com/es/research-blog/pmkid-attacks-debunking-the-80211r-myth/)

---

## Dependencies

To compile this PoC on Debian-based distributions (e.g. Parrot, Kali, Ubuntu), install the required packages:

```
sudo apt update
sudo apt install build-essential libnl-3-dev libnl-genl-3-dev libssl-dev pkg-config
```

## Installation

```
git clone https://github.com/OscarAkaElvis/PMKID_PoC
cd PMKID_PoC
cp .config hostap/hostapd/
cd hostap
make -C hostapd
```

## Configuration

Create a `hostapd.conf` file in the same directory with the following content, replacing `wlan0` with your wireless interface and adjusting other fields as needed:

```
interface=wlan0
ssid=vulnPMKID
driver=nl80211
hw_mode=g
bssid=00:11:22:33:44:55
channel=1
logger_syslog=0
wpa=2
wpa_passphrase=Wh4teverPassw0rd
wpa_key_mgmt=WPA-PSK
rsn_pairwise=CCMP
```

## Usage

`./hostapd/hostapd -K hostapd.conf`

Remember to launch this from `hostap` dir. Otherwise, adjust to point to the compiled hostapd binary.

If successful, your system will act as a vulnerable access point (AP), allowing PMKID capture. You can now use [hcxdumptool](https://github.com/ZerBea/hcxdumptool), [airgeddon](https://github.com/v1s1t0r1sh3r3/airgeddon), or any other tool that automates the capture process.

## ⚠️ Disclaimer

This repository is intended for educational and research purposes only. Unauthorized access to networks is illegal. Use responsibly and only on networks you own or have permission to audit.
