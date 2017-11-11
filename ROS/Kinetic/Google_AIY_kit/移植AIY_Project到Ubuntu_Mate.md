##  移植AIY_Project到Ubuntu_Mate
- 安装Ubuntu Mate
    - 下载树莓派镜像 https://ubuntu-mate.org/raspberry-pi/
    - sudo dd bs=16m if=~/ubuntu-mate-16.04.2-desktop-armhf-raspberry-pi.img of=/dev/disk3
    - 升级内核到4.9  sudo rpi-update
```bash
    pi@pi-desktop:~$ sudo rpi-update
[sudo] password for pi:
 *** Raspberry Pi firmware updater by Hexxeh, enhanced by AndrewS and Dom
 *** Performing self-update
 *** Relaunching after update
 *** Raspberry Pi firmware updater by Hexxeh, enhanced by AndrewS and Dom
 *** We're running for the first time
 *** Backing up files (this will take a few minutes)
 *** Remove old firmware backup
 *** Backing up firmware
 *** Remove old modules backup
 *** Backing up modules 4.4.38-v7+
#############################################################
This update bumps to rpi-4.9.y linux tree
Be aware there could be compatibility issues with some drivers
Discussion here:
https://www.raspberrypi.org/forums/viewtopic.php?f=29&t=167934
##############################################################
 *** Downloading specific firmware revision (this will take a few minutes)
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   168    0   168    0     0     89      0 --:--:--  0:00:01 --:--:--    89
100 54.1M  100 54.1M    0     0   144k      0  0:06:24  0:06:24 --:--:--  105k
 *** Updating firmware
 *** Updating kernel modules
 *** depmod 4.9.60+
 *** depmod 4.9.60-v7+
 *** Updating VideoCore libraries
 *** Using HardFP libraries
 *** Updating SDK
 *** Running ldconfig
/sbin/ldconfig.real: /usr/lib/arm-linux-gnueabihf/libavutil.so.55.34.100 is not an ELF file - it has the wrong magic bytes at the start.

/sbin/ldconfig.real: /usr/lib/arm-linux-gnueabihf/libavutil.so is not an ELF file - it has the wrong magic bytes at the start.

/sbin/ldconfig.real: /usr/lib/arm-linux-gnueabihf/libavutil.so.55 is not an ELF file - it has the wrong magic bytes at the start.

 *** Storing current firmware revision
 *** Deleting downloaded files
 *** Syncing changes to disk
 *** If no errors appeared, your firmware was successfully updated to 754029b1cb414a17dbd786ba5bee4fc936332255
 *** A reboot is needed to activate the new firmware
```

- 安装 AIY
    - https://github.com/google/aiyprojects-raspbian/blob/voicekit/HACKING.md
    - 我在配置AIY hat 碰到问题，到GitHub论坛上提问
        - https://github.com/google/aiyprojects-raspbian/issues/168
    - 他提示我要 changing default to plug:micboost in  [_recorder.py](https://github.com/google/aiyprojects-raspbian/blob/3332a45591e64095c7a6d2d349cd13114d8962ef/src/aiy/_drivers/_recorder.py#L42)
    - 能正常使用AIY hat
    - 但Network proxy还没有解决。
        - https://github.com/google/aiyprojects-raspbian/issues/169