import sys
import subprocess

# implement pip as a subprocess:
subprocess.check_call([sys.executable, '-m', 'pip', 'install',
                       'robotframework==3.2.2'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install',
                       'robotframework-selenium2library==3.0.0'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install',
                       'robotframework-reportportal==5.0.4'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install',
                       'robotframework-databaselibrary==1.2.4'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install',
                       'robotframework-requests==0.6.5'])
# process output with an API in the subprocess module:
reqs = subprocess.check_output([sys.executable, '-m', 'pip',
                                'freeze'])
installed_packages = [r.decode().split('==')[0] for r in reqs.split()]

print(installed_packages)
