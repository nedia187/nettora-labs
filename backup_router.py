# connect to a router and save its config to a file
from netmiko import ConnectHandler
router = {"device_type": "cisco_ios", "ip": "192.168.1.1", "username": "admin", "password": "password"}
try:
    connection = ConnectHandler(**router)
    connection.enable()
    output = connection.send_command("show running-config")
    print(output)
    with open("R1_backup.txt","w") as f:
        f.write(output)
    print("backup saved successfully!")
except Exception as e:
print("failed to connect to", router["ip"], "error", e)