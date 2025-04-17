"""
This is just a simple script to scan a target using nmap and print the results.
It uses the nmap library to perform the scan and prints the results in a readable format.

It is important to note that this script is for educational purposes only and should not be used for any illegal activities.
Before using this script, make sure you have permission to scan the target.
Besides, this script is not a replacement for a full-fledged security assessment tool.
It is just a simple script to demonstrate how to use the nmap library in Python.
AND POCS ARE NOT ALLOWED TO BE USED FOR ILLEGAL ACTIVITIES.
This script is for educational purposes only.
"""

import socket
import nmap

scanner = nmap.PortScanner()
target = "home.cern"

# Realiza o scan com todos os scripts (-A) e detecção completa
scanner.scan(target, arguments='-sS -sV -O -p 1-1024 -T4')

# Verifica se algum host foi detectado
if not scanner.all_hosts():
    print(f"Nenhum host encontrado para {target}.")
    exit()

# Pega o IP resolvido
host = scanner.all_hosts()[0]

print(scanner.scaninfo())
print("Hosts encontrados:", scanner.all_hosts())
print("Scanning target:", target)
print("IP Address:", socket.gethostbyname(target))
print("Scan Results:")

if scanner[host].all_protocols():
    print(scanner[host].all_protocols())

    print("Open Ports:")
    for proto in scanner[host].all_protocols():
        lport = scanner[host][proto].keys()
        for port in sorted(lport):
            state = scanner[host][proto][port]['state']
            name = scanner[host][proto][port].get('name', 'N/A')
            print(f"Port: {port} | State: {state} | Service: {name}")

    print("\nOS Detection:")
    if 'osmatch' in scanner[host]:
        for os in scanner[host]['osmatch']:
            print(f"OS Name: {os['name']} | Accuracy: {os['accuracy']}%")
    else:
        print("Nenhuma informação de sistema operacional detectada.")

    print("\nService Versions:")
    for proto in scanner[host].all_protocols():
        lport = scanner[host][proto].keys()
        for port in sorted(lport):
            version = scanner[host][proto][port].get('version', 'N/A')
            print(f"Port: {port} | Version: {version}")

    print("\nVuln Information:")
    if 'vulners' in scanner[host]:
        print(scanner[host]['vulners'])
    else:
        print("Nenhuma informação de vulnerabilidades encontrada.")

    print("\nScript Results:")
    for proto in scanner[host].all_protocols():
        lport = scanner[host][proto].keys()
        for port in sorted(lport):
            script = scanner[host][proto][port].get('script', {})
            if script:
                print(f"Port: {port} | Script: {script}")
else:
    print("Nenhum protocolo encontrado.")

print("\nScan Completed.")
print("Scan Time:", scanner[host].get('timestr', 'N/A'))
print("Scan Duration:", scanner[host].get('timesecs', 'N/A'), "seconds")
