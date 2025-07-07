from ncclient import manager


router = {
    "host": "192.168.56.2",
    "port": 830,
    "username": "cisco",
    "password": "cisco123!",
    "hostkey_verify": False
}


config_hostname = """
<config>
  <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
    <hostname>cifuentes-lavin</hostname>
  </native>
</config>
"""


config_loopback = """
<config>
  <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
    <interface>
      <Loopback>
        <name>11</name>
        <ip>
          <address>
            <primary>
              <address>11.11.11.11</address>
              <mask>255.255.255.255</mask>
            </primary>
          </address>
        </ip>
      </Loopback>
    </interface>
  </native>
</config>
"""


with manager.connect(**router) as m:
    print("✅ Conectado al router CSR1000v vía NETCONF")


    response1 = m.edit_config(target="running", config=config_hostname)
    print("✅ Nombre del router cambiado a: cifuentes-lavin")
    print(response1)


    response2 = m.edit_config(target="running", config=config_loopback)
    print("✅ Loopback11 creada con IP 11.11.11.11/32")
    print(response2)

