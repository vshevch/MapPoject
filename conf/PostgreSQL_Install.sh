# Update the package list
sudo apt-get update
# Install new versions of packages
sudo apt-get upgrade
# Install PostgreSQL-contrib (package that adds some additional utilities and functionality)
sudo apt-get -y install postgresql postgresql-contrib
# Switch over to the postgres account on your server by typing
# Create user and db
sudo -u postgres createuser vladshev 
sudo -u postgres createdb vladshev 
