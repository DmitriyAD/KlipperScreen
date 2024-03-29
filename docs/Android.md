# Android

This article describes how to use KlipperScreen from an android device

!!! important
    The experience may not be equal to run KlipperScreen natively,
    depending on the device there maybe performance degradation or other issues

1. [First installl KlipperScreen on the Pi](Installation.md)
2. Install [XServer-XSDL](https://play.google.com/store/apps/details?id=x.org.server) on the android device
3. Choose [USB(ADB)](#adb) or [WIFI](#wifi)

### ADB

!!! warning
    Leaving the phone always connected it's not recommended, remove the battery to avoid issues.

* Install ADB on the Pi
```bash
sudo apt-get install android-tools-adb
```
* Put your Android phone/tablet in Debug mode.

Usually it involves enabling developer mode and "USB debugging" but this varies on different vendors and versions of the device
search "how to enable android debugging on device-model-and-brand"

* Copy the launcher script

```bash
cd ~/KlipperScreen/scripts
cp android-adb.sh launch_KlipperScreen.sh
chmod +x launch_KlipperScreen.sh
```

* Go to [Startup](#startup)

### WIFI

* Create a launcher script

```bash
cd ~/KlipperScreen/scripts
touch launch_KlipperScreen.sh
chmod +x launch_KlipperScreen.sh
nano launch_KlipperScreen.sh
```

* Paste this into the script (edit the IP for example: 192.168.1.2:0)
```bash
DISPLAY=(ip address from blue screen):0 $KS_XCLIENT
```

!!! important
    It's recommended to use a static address, because if the address changes your connection will stop working.

* Go to [Startup](#startup)

## Startup

Start Xserver-XSDL On the android device

On the splash-screen of the app go to:
```
“CHANGE DEVICE CONFIGURATION”
└──Mouse Emulation Modde
    └──Desktop, No Emulation
```
if you missed it, restart the app.

on the Pi
```bash
sudo service KlipperScreen stop
sudo service KlipperScreen start
```

## Migration from other tutorials

KlipperScreen says error option "service" is not supported anymore.

Stop the other service and Remove it, for example if the service is `KlippyScreenAndroid`:

```bash
sudo service KlippyScreenAndroid stop
sudo rm /etc/systemd/system/KlippyScreenAndroid.service
```

Follow this guide on how to setup the new launcher script with [USB(ADB)](#adb) or [WIFI](#wifi) and restart KS.

## Help

[The Discourse thread has old instructions but you may get some help if needed](https://klipper.discourse.group/t/how-to-klipperscreen-on-android-smart-phones/1196)

[#klipper-screen channel on Discord](https://discord.klipper3d.org/)

