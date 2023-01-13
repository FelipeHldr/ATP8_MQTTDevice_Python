import paho.mqtt.client as mqtt
import time
from hal2 import temperatura2, aquecedor2
from definitions2 import user2, password2, client_id2, server2, port2


def mensagem2(client2, userdata2, msg2):
    vetor2 = msg2.payload.decode().split(',')
    aquecedor2('on' if vetor2[1] == '1' else 'off')
    client2.publish(f'v1/{user2}/things/{client_id2}/response', f'ok,{vetor2[0]}')
    print(vetor2)


# Conexão inicial
client2 = mqtt.Client(client_id2)
client2.username_pw_set(user2, password2)
client2.connect(server2, port2)

client2.on_message = mensagem2
client2.subscribe(f'v1/{user2}/things/{client_id2}/cmd/1')
client2.loop_start()

# Comportamento do sistema
while True:
    client2.publish('v1/' + user2 + '/things/' + client_id2 + '/data/0', temperatura2())

    time.sleep(5)

# client.disconnect()
