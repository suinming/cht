[tutorial_video](https://www.youtube.com/watch?v=V6m5ZPGIbcI)

1. `sudo fdisk -l` to check the location of the usb 
2. `mount | grep /dev/sd_x` check if your usb is mounted or not. If the grep result have partitions which are mounted use `sudo umount /dev/sd_x` to unmounted the partition
3. `sudo wipefs --all /dev/sd_x` wipe the file system of the usb
4. create partition table using `sudo cfdisk /dev/sd_x` (it will open a prompt and go through the procedure) 

  - select label type => dos 
  - press enter to create a partition(and use the default size which is the maximum size of the usb)
  - select write to create partition
  - quit

5. format the partition `sudo mkfs.vfat` -n 'SU_USB' /dev/sd_x (NOTICE: the name should be all capital case i.e. SU_USB)
6. check if the usb is ready to use 
