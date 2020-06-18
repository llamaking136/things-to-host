#!/usr/bin/python3

from sys import argv

cmd = {
    "libterm":
    "Libetrm Version 5.2.2 (1)",
    "version":
    "man version 0.5.0",
    "man": 
    """
NAME
    man
USAGE
    man <name_of_command>
DESCRIPTION
    man is a command that allows you to see the usage and
    definition of a command. You can specify which
    command you wish to see by using
    man <name_of_command>.
    """,
    
    "ls":
    """
NAME
    ls
USAGE
    ls <-ABCFGHLOPRSTUW@abcdefghiklmnopqrstuwx1%> <optional_path_to_dir>
DESCRIPTION
    ls is a command that allows you to see the files
    or directories in the current directory or other files.
    """,
    "cd":
    """
NAME
    cd
USAGE
    cd <path_to_dir>
DESCRIPTION
    cd is a command that allows you to go to a
    specific directory to change your current
    working directory.
    """,
    "pwd":
    """
NAME
    pwd
USAGE
    pwd<-L / -P>
DESCRIPTION
    pwd is a command that allows you to view
    your current working directory.
    -L will display the logical working directory.
    -P will display the physical working directory.
    """,
    "python":
    """
NAME
    python
USAGE
    python <path_to_file>
DESCRIPTION
    python is the regular python intreperter for running
    py files and running commands in the interpreter.
SEE ALSO
    python3, python2
    """,
    "python3":
    """,
NAME
    python3
USAGE
    python3 <path_to_file>
DESCRIPTION
    python3 is the regular python intreperter for running
    py files and running commands in the interpreter.
    This is the same as the python command.
SEE ALSO
    python2, python
    """,
    "python2":
    """
NAME
    python2
USAGE
    python2 <path_to_file>
DESCRIPTION
    python2 is the regular python intreperter for running
    py files and running commands in the interpreter.
    This is the 2.7 interpreter, for those that use it.
SEE ALSO
    python3, python
    """,
    "curl":
    """
NAME
    curl
USAGE
    curl <-aEKCbcdDfFPGgHIh0ik46jlLmMn:No#xUpQreJORXSsYy23tz1TBuAvVw> <url_to_download>
DESCRIPTION
    curl is a command that downloads files from the internet,
    such as https://www.apple.com.
SEE ALSO
    download
    """,
    "download":
    """
NAME
    download
USAGE
    download <url_file>
DESCRIPTION
    download is a command that downloads files from the internet.
    curl is the same as this, but this is written in Python.
SEE ALSO
    curl
    """,
    "touch":
    """
NAME
    touch
USAGE
    touch <filename/path_to_filename_to_make>
DESCRIPTION
    touch makes files.
    """,
    "mkdir":
    """
NAME
    mkdir
USAGE
    mkdir <name/path_of_dir_to_make>
DESCRIPTION
    mkdir makes directories.
    """,
    "rm":
    """
NAME
    rm
USAGE
    rm <-fidPRrvW> <path_to_file>
DESCRIPTION
    rm removes files.
    Note: With the -r argument, you can remove
    directories with files in them.
SEE ALSO
    rmdir
    """,
    "rmdir":
    """
NAME
    rmdir
USAGE
    rmdir <-p> <path_to_dir>
DESCRIPTION
    rmdir removes directories.
    Note: You can only delete empty direcories.
SEE ALSO
    rm
    """,
    "cat":
    """
NAME
    cat
USAGE
    cat <path_to_file>
DESCRIPTION
    cat is a command that prints out the data inside
    of a file.
    """,
    "echo":
    """
NAME
    echo
USAGE
    echo <-n> <message>
DESCRIPTION
    echo echos back your message you said.
    Works on system vairables like $PATH or $SHELL.
    """,
    "uname":
    """
NAME
    uname
USAGE
    uname <-amnprsv>
DESCRIPTION
    uname gives a description of your device's specs, such
    as the kernel name, kernel version, and device name.
SEE ALSO
    systeminfo
    """,
    "systeminfo":
    """
NAME
    systeminfo
USAGE
    systeminfo
DESCRIPTION
    systeminfo is just like uname, but goes into more hardware
    and software specs.
SEE ALSO
    uname
    """,
    "exit":
    """
NAME
    exit
USAGE
    exit
DESCRIPTION
    exit exits the current shell.
    """,
    "open":
    """
NAME
    open
USAGE
    open <path_to_file>
DESCRIPTION
    open opens files to share by using iOS to share.
    """,
    "cp":
    """
NAME
    cp
USAGE
    cp <-RHLPfinapvXc> <path_to_file>
DESCRIPTION
    cp is a command that copies files from one directory
    to the other.
    Note: Use the argument -r to copy directories.
    """,
    "edit":
    """
NAME
    edit
USAGE
    edit <path_to_file>
DESCRIPTION
    edit edits files, the LibTerm equivelent to vim.
    """
}

if len(argv) != 2:
    print("What manual page do you want?")
    exit(0)

try:
    print(cmd[argv[1]])
except:
    print("No manual entry for " + argv[1])
    exit(1)