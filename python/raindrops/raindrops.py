def convert(number):
    sounds = {
        3: 'Pling',
        5: 'Plang',
        7: 'Plong'
        }

    final_sound = ''

    for key, value in sounds.items():
        if number % key == 0:
            final_sound += value

    if final_sound == '':
        final_sound = f"{number}"

    return final_sound

    pass
