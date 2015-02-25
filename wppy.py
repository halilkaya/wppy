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
from random import randint
from builtins import input  # Support for Python 2 & 3

if __name__ != '__main__':
	print("Not a module!!!")
	sys.exit(1)

parser = OptionParser()
parser.add_option('-n', '--name', dest="folder_name", help="Wordpress folder name", action="store")
options, args = parser.parse_args()

if not options.folder_name:
	print("[ERROR] Enter a folder name to get Wordpress into. You can use -n or --name parameter to determine it")
	sys.exit(1)

print("[INFO] Cloning the latest version of Wordpress")
os.system('wget -c http://wordpress.org/latest.zip')

print("[INFO] Extracting compressed file")
rndmfolder = 'wordpress' + str(randint(0,99));
os.system('unzip latest.zip -d ' + rndmfolder)

print("[INFO] Folder renaming as", options.folder_name)
os.system('mv ' + rndmfolder + '/wordpress ' + options.folder_name)

print("[INFO] Deleting latest.zip file and temporary wordpress directory")
os.system('rm latest.zip')
os.system('rm -r ' + rndmfolder)

print("[INFO] Copying wp-config-sample.php as wp-config.php")
os.system('cp ' + options.folder_name + '/wp-config-sample.php ' + options.folder_name + '/wp-config.php')

print("\n")

site_url = input('Enter site URL that you are currently installing Wordpress on: http://')
database_name = input('Enter your database name: ')
database_username = input('Enter username for this database: ')
database_password = input('Enter password: ')
database_host = input('Enter hostname (leave blank for localhost): ')

print("[INFO] Configuring database...")
os.system('vi -c "%s/database_name_here/' + database_name + '/g|wq" ' + options.folder_name + '/wp-config.php')
os.system('vi -c "%s/username_here/' + database_username + '/g|wq" ' + options.folder_name + '/wp-config.php')
os.system('vi -c "%s/password_here/' + database_password + '/g|wq" ' + options.folder_name + '/wp-config.php')

if not database_name:
	print("[WARN] You have typed an empty database name!")

if not database_username:
	print("[WARN] You have typed an empty username for database!")

if not database_password:
	print("[WARN] You have not typed a password!")

if not database_host:
	database_host = 'localhost'

os.system('vi -c "%s/localhost/' + database_host + '/g|wq" ' + options.folder_name + '/wp-config.php')

print("[INFO] Configured database config file successfully!\n")

if 'http://' not in site_url:
	home = 'http://' + site_url
	# @todo: httpS?
user_name = input('Enter a username for admin panel: ')
password = input('Enter a password for admin panel: ')
weblog_title = input('Enter site title: ')
blogdescription = input('Enter blog description: ')
admin_email = input('Enter admin e-mail: ')

print("[INFO] Connecting to MySQL and creating and configuring database...")
print("Enter your MySQL password the line below again.\n")
if not database_password:
	os.system('echo "create database ' + database_name + '" | mysql -u ' + database_username)
else:
	os.system('echo "create database ' + database_name + '" | mysql -u ' + database_username + ' -p')

os.system('curl --data "weblog_title=' + weblog_title + '&user_name=' + user_name + '&admin_password=' + password + '&admin_password2=' + password + '&admin_email=' + admin_email + '&blog_public=1&language=" ' + home + '/' + options.folder_name + '/wp-admin/install.php?step=2 -o "curl_output.txt"')

os.system('mv curl_output.txt ' + options.folder_name + '/')

print("[INFO] Your blog is ready! Just go to %s/%s" % (home, options.folder_name))