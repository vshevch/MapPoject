# Update the package list
sudo apt-get update
# Install new versions of packages
sudo apt-get upgrade
# Install PostgreSQL-contrib (package that adds some additional utilities and functionality)
sudo apt-get -y install postgresql postgresql-contrib
## if that does not work**
#1. Search for postgresql install files
apt search postgresql
#2. Find one that works (often it has a version as part of the install file)
#3. Run that the command but with the new install file name
## End ##
# Switch over to the postgres account on your server by typing
# Create user with password prompt -P and superuser -s
sudo -u postgres createuser -P -s <user>
root
root
# Create Database
sudo -u postgres createdb -O <user> <user>
