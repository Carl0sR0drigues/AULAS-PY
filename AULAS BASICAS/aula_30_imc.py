while True:
    nome = str(input('Qual o seu nome?'))
    altura =  float(input('Qual a sua altura em metros?'))
    peso = float(input('Qual o seu peso em quilos?'))
    imc = peso / (altura * altura )
    print('Seu IMC é',imc)
    if imc <= 18.5:
        print('Peso adequado')
    elif imc >= 25 and imc <= 29.9:
        print('Sobrepeso')
    elif imc >= 30.0 and imc < 34.9:
        print('Obesidade grau 1')
    elif imc > 35 and imc < 39.9:
        print('Obesidade grau 2')
    elif imc > 40: 
        print('Obesidade extrema')

    close = input('Quer inserar por aqui?\nSIM= S\nNÃO= N\n').lower()
    if close == 's':
        break
    
