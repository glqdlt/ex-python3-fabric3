from fabric.api import run, env, sudo

env.hosts =['some-user-id@127.0.0.1:10112']
env.password = 'some-user-password'

def pwd():
    run('pwd')

def shutdown():
    sudo('shutdown -P 00')







