import paramiko
import time

# Configurações do switch
switch_ip = "192.168.15.20"
username = "admin"
password = "admin123"

# Comandos para configurar o switch
commands = [
    "configure terminal",
    "interface 1/1/1",
    "description Configurado via SSH",
    "vlan 10",
    "name RODEI O ACTION",
    "exit",
    "write memory"
]

# Conectar ao switch via SSH
try:
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(switch_ip, username=username, password=password)

    print(f"Conectado ao switch {switch_ip}")

    # Abrir um shell e enviar comandos
    shell = ssh.invoke_shell()
    for command in commands:
        shell.send(command + "\n")
        time.sleep(1)  # Aguarde o comando ser processado

    print("Configuração aplicada com sucesso!")
    ssh.close()

except Exception as e:
    print(f"Erro ao conectar ao switch: {e}")