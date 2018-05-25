from fabric.api import run, env, sudo

env.hosts =['some-userid@127.0.0.1:10112']
env.password = 'some-password'


def pwd():
    run('pwd')


def shutdown(time='00'):
    sudo('shutdown -P '+time)


def rebooting(time='00'):
    sudo('shutdown -r '+time)


# fab smart_mon:/dev/sdb
def smart_mon(dev='/dev/sda'):
    sudo('smartctl --all ' + dev)


