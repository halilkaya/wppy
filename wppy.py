#!/usr/bin/env python
#-*-coding: utf-8-*-

#
#	Halil Kaya
#	   www.halilkaya.net
#	   kayahalil@gmail.com
#	   GPG: 0x0FA83C53
#
#	wppy is licensed with GPL
#

import sys, os
from optparse import OptionParser

parser = OptionParser()
parser.add_option('-n', '--name', dest="folder_name", help="Wordpress folder name", action="store")
options, args = parser.parse_args()

if not options.folder_name:
	print "[ERROR] Enter a folder name to get Wordpress into. You can use -n or --name parameter to determine it"
	sys.exit(1)

print "[INFO] Cloning the latest version of Wordpress"
os.system('wget -c http://wordpress.org/latest.zip')

print "[INFO] Extracting compressed file"
os.system('unzip latest.zip')

print "[INFO] Folder creating as " + options.folder_name
os.system('mv wordpress ' + options.folder_name)

print "[INFO] Deleting latest.zip file"
os.system('rm latest.zip')

print "[INFO] Changing wp-config-sample.php tp wp-config,php"
os.system('mv ' + options.folder_name + '/wp-config-sample.php ' + options.folder_name + '/wp-config.php')

print

site_url = raw_input('Enter site URL that you are currently installing Wordpress on: http://')
database_name = raw_input('Enter your database name: ')
database_username = raw_input('Enter username for this database: ')
database_password = raw_input('Enter password: ')
database_host = raw_input('Enter hostname (leave blank for localhost): ')

print "[INFO] Configuring database..."
os.system('vi -c "%s/database_name_here/' + database_name + '/g|wq" ' + options.folder_name + '/wp-config.php')
os.system('vi -c "%s/username_here/' + database_username + '/g|wq" ' + options.folder_name + '/wp-config.php')
os.system('vi -c "%s/password_here/' + database_password + '/g|wq" ' + options.folder_name + '/wp-config.php')

if not database_name:
	print "[WARN] You have typed an empty database name!"

if not database_username:
	print "[WARN] You have typed an empty username for database!"

if not database_password:
	print "[WARN] You have not typed a password!"

if not database_host:
	database_host = 'localhost'

os.system('vi -c "%s/localhost/' + database_host + '/g|wq" ' + options.folder_name + '/wp-config.php')

print "[INFO] Configurated database successfully!"

print "[INFO] Connecting to MySQL and creating database..."
if not database_password:
	os.system('echo "create database ' + database_name + '" | mysql -u ' + database_username)
else:
	os.system('echo "create database ' + database_name + '" | mysql -u ' + database_username + ' -p')

print
print "[INFO] Last one more step! Just go to http://" + site_url + "/" + options.folder_name + " and get your Wordpress blog ready!"
