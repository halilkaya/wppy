#!/usr/bin/env python
#-*-coding: utf-8-*-

import os

os.system('cp wppy.py /usr/bin/')
os.system('mv /usr/bin/wppy.py /usr/bin/wppy')
os.system('chmod a+x /usr/bin/wppy')

print

print "wppy installed successfully!"
print "Just run wppy --name blogname in the folder that you want to install your WordPress blog!"

print
