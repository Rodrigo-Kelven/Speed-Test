import speedtest
import time

# Cria um objeto Speedtest
st = speedtest.Speedtest()

# Mostra os servidores de teste mais próximos
print("Servidores de teste mais próximos:")
st.get_servers()
print()

# Seleciona o servidor de teste mais rápido
print("Selecionando o servidor de teste mais rápido...")
st.get_best_server()
print()

# Realiza o teste de velocidade
print("Realizando o teste de velocidade...")
download_speed = st.download()
upload_speed = st.upload()
ping = st.results.ping

# Converte as velocidades para Mbps
download_speed_mb = download_speed / 10**6
upload_speed_mb = upload_speed / 10**6

# Mostra os resultados
print("\n")
print("########################")
print("Resultados:")
print(f"Download: {download_speed_mb:.2f} Mbps")
print(f"Upload: {upload_speed_mb:.2f} Mbps")
print(f"Ping: {ping:.2f} ms")

# Mostra o tempo de execução do teste
print(f"Tempo de execução: {time.time()} segundos")