# Python Debian Package Parser

##### Prolog
This document is markdown format and best viewed using a markdown capable viewer, such as 
_pycharm_ or _visual studio code_. Alternatively copy/paste into an online markdown viewer 
such as [dillinger.io](https://dillinger.io)

### Introduction

This project uses python to show statistics of the debian packages (for a specific architecture) that have the most files associated with them.
It uses the online data from [debian](http://ftp.uk.debian.org/debian/dists/stable/main/.) to do so.  
See _[challenge.txt](./challenge.txt)_ for furter details.

## Terminology
[Listing File](http://ftp.uk.debian.org/debian/dists/stable/main/.)  
from here available contents files (see below) can be discerned

[Contents (index) File](http://ftp.uk.debian.org/debian/dists/stable/main/Contents-[Arch].gz) <br>
 "Architecture" specific (one->many) mapping of file->packages
eg [official documentation](https://wiki.debian.org/RepositoryFormat#A.22Contents.22_indices) 


## Prerequisites
    Python 3.12+
    If you have multiple versions of python installed, please make sure the correct one is being referenced in the files in _prj/script_ 

## Setup
    prj/script> ./venv_create.sh
    
This will create a virtual environment and install the required packages (as listed in **prj/pip_reqs.txt**)

- *Note*: on Ubuntu one may need to first separately **install python3-venv**


    > sudo apt install python3-venv

- *Note*: [Poetry](https://python-poetry.org/docs/) has superior dependency handling, and should be preferred in a 
production environment. Direct use of pip was chosen here, however, as poetry requires global modifications on the developers machine, 
and I wanted to avoid requiring this of anyone else, wishing to run/test this project
  - *Note*: If you are behind a proxy you may need to configure *https_proxy* (eg export as an environment var) appropriately 
   for pip to be able to download the packages, and the app to download the files. eg:

        > export http_proxy=http://10.10.1.10:3128
        > export https_proxy=http://10.10.1.10:1080
     

## Execute
    >  ./prj/script/venv/bin/python -m src.main udeb-all

    collating for 'Contents-udeb-all.gz' .... 
    downloading http://ftp.uk.debian.org/debian/dists/stable/main/ ...
    5.52kB [00:00, 7.63MB/s]
    .... download complete
    downloading http://ftp.uk.debian.org/debian/dists/stable/main/Contents-udeb-all.gz ...
    100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 13.2k/13.2k [00:00<00:00, 9.49MB/s]
    .... download complete
    extracting...
    
    Package statistics for 'udeb-all':
    |    | Package                                            |   Num Files |
    |---:|:---------------------------------------------------|------------:|
    |  1 | debian-installer/xkb-data-udeb                     |         293 |
    |  2 | debian-installer/fonts-noto-unhinted-udeb          |         270 |
    |  3 | debian-installer/ca-certificates-udeb              |         259 |
    |  4 | debian-installer/console-keymaps-at                |         128 |
    |  5 | debian-installer/debootstrap-udeb                  |          72 |
    |  6 | debian-installer/console-keymaps-acorn             |          57 |
    |  7 | debian-installer/console-setup-linux-charmaps-udeb |          56 |
    |  8 | debian-installer/debian-edu-profile-udeb           |          50 |
    |  9 | debian-installer/kickseed-common                   |          40 |
    | 10 | debian-installer/console-setup-freebsd-fonts-udeb  |          36 |


## Test
    ex_auto>  ./prj/script/venv/bin/pytest test/

    ========================================================================= test session starts ==========================================================================
    platform darwin -- Python 3.10.7, pytest-7.2.0, pluggy-1.0.0
    collected 15 items                                                                                                                                                     
    
    test/test__cts_arch.py .                                                                                                                                         [  6%]
    test/test__man_app.py ...                                                                                                                                        [ 26%]
    test/test__man_file.py ...                                                                                                                                       [ 46%]
    test/test__man_parser_.py ..                                                                                                                                     [ 60%]
    test/test__man_util.py ..                                                                                                                                        [ 73%]
    test/test__man_web.py ....                                                                                                                                       [100%]
    
    ========================================================================== 15 passed in 0.77s ==========================================================================


## Check Typing
    >  ./prj/script/venv/bin/mypy --check-untyped-defs -p test -p src

    Success: no issues found in 16 source files


## Check Lint
    > ./prj/script/venv/bin/python -m pylint src test

    --------------------------------------------------------------------
    Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)




Notes:
------
Some of the wording was ambiguous in this 
[contents file](https://wiki.debian.org/DebianRepository/Format?action=show&redirect=RepositoryFormat#A.22Contents.22_indices)

In any cases of ambiguity a reasonable best guess was made. For example:

    'The first row of the table SHOULD have the columns "FILE" and "LOCATION" '

Rows don't have columns, and it is not fully clear if a literal

            "FILE       LOCATION"

should be expected and ignored, or if this is just trying to describe schema (latter was presumed)

     'A filename relative to the root directory, without leading .'

Its actually a file path (filename cant contain "/")

      "possibly taking advantage of the fact that package names cannot include
             white space characters"

Its was furthermore presumed there can also be no spaces -between- package names

If any of the above presumptions are incorrect, then the code may need to be revised.
