import paramiko
import time

# Variáveis de ambiente
switch_ip = "192.168.15.20"
tftp_server = "192.168.15.100"
switch_username = "admin"
switch_password = "admin123"
port = 22
config_file = "poc-config"

# Comando para copiar o arquivo de configuração do TFTP para o switch
copy_command = f"copy tftp://{tftp_server}/{config_file} running-config"

# Função para enviar comandos via SSH
def send_command(channel, command, delay=2):
    channel.send(command + '\n')
    time.sleep(delay)
    output = channel.recv(2048).decode()
    print(output)
    return output

# Autenticação SSH
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    print(f"Conectando ao switch {switch_ip}...")
    ssh.connect(switch_ip, port, switch_username, switch_password)
    channel = ssh.invoke_shell()
    time.sleep(1)

    # Enviar comandos para o switch
    print("Enviando comandos para o switch...")
    # send_command(channel, "enable")
    send_command(channel, copy_command, delay=5)  # Aumentar o delay para o comando de cópia
    send_command(channel, "write memory", delay=3)  # Salvar a configuração no switch

    print("Configuração aplicada com sucesso!")

except Exception as e:
    print(f"Erro ao aplicar configuração: {e}")

finally:
    channel.close()
    ssh.close()
    print("Conexão encerrada.")