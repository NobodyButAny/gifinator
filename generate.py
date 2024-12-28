import os
import glob
from jinja2 import Template

def main():
    if os.path.isdir('./resources'):
        images = glob.glob('*.gif', root_dir='./resources')
        options = {i+1: image for i, image in enumerate(images)}
    
        for i in options:
            print(f'{i}: {options[i]}')

        print('\n0: ABORT \n')

        while True:
            option = int(input('Select image: '))
            if option not in range(len(images) + 1):
                continue
            else: 
                break
        
        if option == 0:
            exit()

        selected_image = f'./resources/{options[option]}' 
    else:
        selected_image = 'in.gif'


    if not os.path.isfile('ffmpeg.template.j2'):
        print('No ffmpeg.template.j2 found!')
        exit()

    with open('filterconfig.txt', 'r') as file:
        filters = file.read()

    with open('ffmpeg.template.j2', 'r') as file:
        run_template = Template(file.read())
        run_command = run_template.render({
            "input_file": selected_image,
            "filters": filters
        })

    print(run_command)
    os.system(run_command)

if __name__ == '__main__':
    main()
 