import paho.mqtt.client as mqtt
import random
import streamlit as st

data_list = []
time_list = []


def pub():
    with st.empty():
        def on_connect(client_1, userdata, flags, rc):
            if rc == 0:
                print("Connected to MQTT Broker!")
            else:
                print("Failed to connect, return code %d\n", rc)

        def on_message(client_1, userdata, msg):

            print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
            if len(data_list) >= 100:
                data_list.pop(0)
            data_list.append(float(msg.payload.decode()))
            st.line_chart(data_list)

        client_id = f'python-mqtt-{random.randint(0, 100)}'
        client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1, client_id)
        client.username = "root"
        client.password = "Whc@20010311"
        client.on_connect = on_connect
        client.connect("113.125.84.107", port=1883)
        topic = "/public/pz_esp32/1"
        client.subscribe(topic)
        client.on_message = on_message
        client.loop_forever()
        try:
            while True:
                pass
        except KeyboardInterrupt:
            print("Interrupted by user, exiting...")
        client.disconnect()


# streamlit run s
if __name__ == '__main__':
    pub()

