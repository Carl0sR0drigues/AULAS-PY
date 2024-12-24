import os
os.system('cls')


class RemoteControl:
    def __init__(self, color, heicht, depths, width):
        self.color = color
        self.heicht = heicht
        self.depths = depths #profundidade
        self.width = width #largura
        print('Active Remote Contral:')

    def ChangeChannel(self, button): #MUDAR DE CANAL
        if button == '+':
            print('Increase the chanel\n') #AUMENTAR CANAL

        elif button == '-':
            print('Decrease the chanel\n') #DIMINUIR CANAL
    








remote_control = RemoteControl('Black','10cm', '2cm', '5cm')

print(remote_control.color)
print(remote_control.heicht)
print(remote_control.depths)
print(remote_control.width, sep='\n')
print(sep='\n')

remote_control.ChangeChannel('-')
