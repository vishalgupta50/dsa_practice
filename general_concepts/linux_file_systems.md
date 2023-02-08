# Important Links

- https://www.geeksforgeeks.org/linux-file-hierarchy-structure/
- https://engineeringinterviewquestions.com/linux-file-systems-interview-questions-answers/
- https://www.wisdomjobs.com/e-university/linux-file-systems-interview-questions.html

## Linux File System Hierarchy Structure

1. /bin : Essential command binaries that need to be available in single-user mode; for all users, e.g., cat, ls, cp. 
2. /boot : Boot loader files, e.g., kernels, initrd. 
   - Kernel initrd, vmlinux, grub files are located under /boot
3. /dev : Essential device files, e.g., /dev/null. 
   - These include terminal devices, usb, or any device attached to the system.
4. /etc : Host-specific system-wide configuration files.
   - Contains configuration files required by all programs.
   - This also contains startup and shutdown shell scripts used to start/stop individual programs.
   - Example: /etc/resolv.conf, /etc/logrotate.conf.
5. /home : Users’ home directories, containing saved files, personal settings, etc.
6. /lib : Libraries essential for the binaries in /bin/ and /sbin/.
   - Library filenames are either ld* or lib*.so.*
7. /media : Mount points for removable media such as CD-ROMs (appeared in FHS-2.3).
8. /mnt : Temporarily mounted filesystems.
9. /opt : Optional application software packages.
   - Contains add-on applications from individual vendors.
   - Add-on applications should be installed under either /opt/ or /opt/ sub-directory.
10. /sbin : Essential system binaries, e.g., fsck, init, route. 
    - Just like /bin, /sbin also contains binary executables. iptables, reboot, fdisk, ifconfig, swapon
11. /srv : Site-specific data served by this system, such as data and scripts for web servers, data offered by FTP servers, and repositories for version control systems.
12. /tmp : Temporary files. Often not preserved between system reboots, and may be severely size restricted.
13. /usr : Secondary hierarchy for read-only user data; contains the majority of (multi-)user utilities and applications. 
    1. Contains binaries, libraries, documentation, and source-code for second level programs.
    2. /usr/bin contains binary files for user programs. 
    3. /usr/sbin contains binary files for system administrators. 
    4. /usr/lib contains libraries for /usr/bin and /usr/sbin
    5. /usr/local contains users programs that you install from source. 
    6. /usr/src holds the Linux kernel sources, header-files and documentation.
