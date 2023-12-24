# Ubuntu Command Line Interface (CLI)

## Before working with Ubuntu

        $ sudo apt update
        $ sudo apt dist-upgrade

## `APT` Ubunut package manager

To install a package

    $ sudo apt install package_name_1 package_name_2 ...etc

To remove a package

    $ sudo apt remove package_name

To search for a package

    $ sudo apt search a_name

## Working with Directories and Files

To check the working directory `pwd` = print working directory

    $ pwd

To create a file

    $ touch file_name

To create a directory `mkdir` = make directory

    $ mkdir dir_name

To delete a file `rm` = remove

    $ rm file_name

To delete a directory `-r` = recursive

    $ rm -r dir_name

To list the content of a directory

    $ ls
    $ ls -l

To list hidden files and directories

    $ ls -la 

To rename a file or directory `mv` = move, it can be used to move files & dirs

    $ mv test.txt my_test.txt 

To copy a file

    $ cp test.txt /home/smahi/project

To copy a directory

    $ cp -r test /home/smahi/project/