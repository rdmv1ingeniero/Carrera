import paho.mqtt.client as mqtt

BROKER = "mqtt.eict.ce.pucmm.edu.do"
PORT = 1883
USER = "itt363-grupo3"
CLAVE = "CnFebqnjbq7F"
TOPIC_GENERAL = "/itt363-grupo3/estacion/#"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print(f"Suscriptor conectado escuchando en {TOPIC_GENERAL}...")
        client.subscribe(TOPIC_GENERAL)
    else:
        print(f"Error de conexion")

def on_message(client, userdata, msg):
    # Formateamos la salida para que sea legible
    print(f"Mensaje recibido en {msg.topic}: {msg.payload.decode()}")

client = mqtt.Client()
client.username_pw_set(USER, CLAVE)
client.on_connect = on_connect
client.on_message = on_message

print(f"Escuchando en {BROKER}...")
client.connect(BROKER, PORT)
client.loop_forever()