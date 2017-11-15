# Python-Reporting-Script
Script that searches and returns 3 reports from a database

# Instructions 
**1.) Install VirtualBox 5.l.**

Newer versions do not work with the current release of Vagrant.
    
[Link to download v5.1](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1)
    
**2.) Install Vagrant**

Vagrant is the software that configures the VM and lets you share files between your host computer
and the VM's filesystem.
    
[Link to download Vagrant](https://www.vagrantup.com/downloads.html)
    
**3.) Download the Configuration Files for Project**

This download will be a zipped file, "FSND-Virtual-Machine"

Inside will be a file named vagrant
  
Unzip the vagrant file to any location desired
    
The new linux os will be downloaded into the vagrant file
    
[Link to Download Configuration Files](https://d17h27t6h515a5.cloudfront.net/topher/2017/August/59822701_fsnd-virtual-machine/fsnd-virtual-machine.zip)

**4.) Dowload the Database File**

[Link to download database](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
    
**5.) Setup The Virtual Machine**

Open bash compatable command prompt

cd into the vagrant file 
    
**Enter: vagrant up**
    
Wait for the new Linux OS to download
    
**Enter: vagrant ssh** to login into os
    
**Enter: cd /vagrant**

**6.) Clone This Repository Inside of /vagrant**

Make sure the database and repository files are in the same file!
   
**7.) Log Database Into OS**

cd to the file containing the python script and database 

Enter: psql -d news -f newsdata.sql**
    
Wait for database to load
    
**8.) Last Step**

Enter into command prompt: python reportsDB.py
    
    
