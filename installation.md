# Installation WSL

For the installation check the following url

[https://learn.microsoft.com/en-us/windows/wsl/install](https://learn.microsoft.com/en-us/windows/wsl/install)

1. check the windows Version and Build ( min windows 10 build +19043)
2. launch `Powershell` as Administrator
3. type `wsl --install`
4. reboot the system
5. finish the installation
6. create a username and password

## After installation

To enter the `WSL` system

1. launch `Powershell`
2. `wsl ~`

This will prompt you in Linux (Ubuntu) Bash command line


## Before working with Ubuntu

        $ sudo apt update
        $ sudo apt dist-upgrade


**NB**: 
`apt` is the Ubuntu package manager.


## Install Python

    $ sudo apt install python3.11-full python3-pip
    $ python -V
    $ pip -V

**NB**: 

`pip` is the  package manager for Python


## Install VS code