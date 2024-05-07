<<<<<<< HEAD
=======
#!/usr/bin/python3
"""
Fabric script to clean up old archives of web static files from deployment.
This script keeps only a specified number of the most recent archives both locally and on remote servers.
"""

from fabric.api import *
from fabric.contrib import files
import os

# Define the default user, host IPs and the SSH key location
env.user = 'ubuntu'
env.hosts = ['IP_web-01', 'IP_web-02']  # Replace with actual IPs of the servers
env.key_filename = 'path_to_my_ssh_private_key'  # Optional, depends on your setup

def do_clean(number=0):
    """
    Cleans up old archives. By default, or if number is 0 or 1, it keeps only the most recent archive.
    If number is greater than 1, it will keep the specified number of the most recent archives.
    """
    number = int(number)
    if number == 0:
        number = 1

    # Clean up local archives in the 'versions' directory
    local('ls -t versions/*.tgz | tail -n +{} | xargs rm -rf'.format(number + 1))

    # Clean up archives in the '/data/web_static/releases' directory on remote servers
    with cd('/data/web_static/releases'):
        run('ls -t | grep "web_static_" | tail -n +{} | xargs rm -rf'.format(number + 1))

    # Check if the current symlink is intact; warn if it appears to be broken
    if not files.exists('/data/web_static/current'):
        print("Warning: The current symlink is broken. You may need to redeploy the static content.")

# Additional deployment tasks can be defined here as needed
>>>>>>> fb14dd277d08a082f2f5c3dd72d499c12f8df1b6
