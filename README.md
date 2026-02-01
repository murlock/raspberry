#

## Preparation

- Raspberry Pi 2 with Debian Bookworm
- Install packages 
```
apt install sudo python3-dev build-essential i2c-tools curl git
``` 
- **root user has not password but can't be used with SSH**; an user must be created manually
  - add user to sudo and i2c groups
- Add i2c-dev to /etc/modules to be loaded on boot (could be loaded manually with `modprobe i2c-dev`)
- Check with `i2cdetect -y 1`:
```
     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:                         -- -- -- -- -- -- -- --
10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
70: -- -- -- -- -- -- -- 77
```

## Note:
- curl -LsSf https://astral.sh/uv/install.sh | sh

## Save SD Card
- Configure journald to avoid save log files, in `/etc/systemd/journald.conf`:
```
Storage=volatile
RuntimeMaxUse=30M
```
- Add to `/etc/fstab`
```
tmpfs /tmp tmpfs defaults,noatime,nosuid,size=100m 0 0
```

## Check BME280

Run `uv run example_bm280.py`

```
CHIP ID BCM2XXX
Température: 20.8°C
Humidité: 52.6%
Pression: 1005.2hPa
```

*Note:* Current code force platform because Revision is not set in `/proc/cpuinfo`

## Save metrics