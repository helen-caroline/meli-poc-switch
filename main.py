import paramiko
import time

# Configurações do switch
switch_ip = "192.168.15.20"
username = "admin"
password = "admin123"

# Carregar comandos do arquivo poc-config
commands = []
with open("config/poc-config", "r") as file:
    for line in file:
        # Ignorar linhas de comentário ou vazias
        if not line.startswith("!") and line.strip():
            commands.append(line.strip())

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