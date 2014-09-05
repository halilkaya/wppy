wppy
====

wppy is a tool to get the latest version of Wordpress and install and configure it for you in one-line command.



Requirements
====

PHP (>=5.0)<br>
MySQL<br>
Python
curl

Runs on only Linux for now.



Installation
====

1. Clone this repository or download a zip.
2. Run wppy-installer.py with root privileges:<br>
    ```$ sudo python wppy-installer.py```
3. That's all!



Usage
====

1. Go to the directory that you want to install Wordpress. Ex:<br>
    ```$ cd /var/www/```<br>
   (PS: You don't need to create a directory. wppy will do it for you)
2. Just run ```wppy``` with ```--name``` parameter. This parameter will be your folder name.<br>
    ```$ wppy -n myblog```
3. Your Wordpress is ready on ex. ```http://localhost/myblog```



Contact
====

Please notice me if you have bugs or recommendation:<br>
kayahalil@gmail.com - GPG: 0x0FA83C53
