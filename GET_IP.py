from requests import get
import pyperclip

ip = get('https://api.ipify.org').text
print('My public IP address is: {}'.format(ip))
pyperclip.copy(ip)
ip6 = get('https://api6.ipify.org').text
print('My public IP6 address is: {}'.format(ip6))

input("X")