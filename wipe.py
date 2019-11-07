#!/bin/python
import subprocess
import os
import sys
import signal


def main_function():
    os.system('clear')
    adv_list = input('Show advanced disk list? (y/N)> ')

    if adv_list[0].lower() == 'y':
        os.system('fdisk -l')
    else:
        fdisk_lines = subprocess.run(
            ['/sbin/fdisk', '-l'], stdout=subprocess.PIPE).stdout.decode().split('\n')
        for line in fdisk_lines:
            if line.startswith('Disk /'):
                print(line)

    count_sel = input('How many cycles of wiping?> ')

    disk_sel = input(
        'Which disks to erase? (separate multiple drives with , Eg: /dev/sda,/dev/sdb,...)\nTo wipe all drives above 32 GB in size write "all"\n> ')
    if disk_sel[0].lower() == "a":
        pass  # TODO: erase all drives above 32 GB in size
    else:
        disks = disk_sel.rstrip().split(',')
        for disk in disks:
            print(f'Wiping {disk}...')
            for i in range(int(count_sel)):
                os.system(
                    f'dd if=/dev/urandom of={disk} bs=512 status=progress')
            os.system(
                f'dd if=/dev/zero of={disk} bs=512 status=progress')
            print(f'Done with {disk}')
    return 0


def signal_handler(sig, frame):
    print('You pressed Ctrl+C!')
    sys.exit(0)


if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    main_function()
    os.system("sudo poweroff")
