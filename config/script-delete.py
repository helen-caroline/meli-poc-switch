import paramiko
import os
import time

# Variáveis de ambiente
switch_ip = os.environ.get('RUNNER_SWITCH_IP')
tftp_server = os.environ.get('RUNNER_TFTP_SERVER')
switch_username = os.environ.get('RUNNER_SWITCH_USERNAME')
switch_password = os.environ.get('RUNNER_SWITCH_PASSWORD')
port = '22'
copy = 'copy tftp://' + tftp_server + '/poc-config startup-config'

# Autenticação SSH
ssh = paramiko.SSHClient()
ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(switch_ip, port, switch_username, switch_password)
channel = ssh.invoke_shell()
time.sleep(1)

# Execução de comandos no Switch
commands = [
    'enable',
    copy,
    'y',
    'reload',
    'y',
    'y'
]

for command in commands:
    channel.send (command + '\n')
    time.sleep(10)
    output = channel.recv(2048).decode()
    print (output)

channel.close()
ssh.close()