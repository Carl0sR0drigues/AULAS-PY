import limpar

class Connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None

    #QUANDO PRECISO ACESSAR O SELF

    def set_user(self, user):
        self.user = user

    def set_password(self, password):
        self.password = password

    #QUANDO PRECISO APENAS A CLASSE E NÃO O SELF

    @classmethod
    def create_with_auth(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection
    
    #É UM FUNÇÃO SIMPLES DENTRO DA CLASSE

    @staticmethod
    def sum(x, y):
        return x + y


print('QUANDO PRECISO ACESSAR O SELF:')

c1 = Connection()
c1.set_user('Carlos')
c1.set_password('456')
print(f'Nome: {c1.user}')
print(f'Senha: {c1.password}')

print('')
print('QUANDO PRECISO APENAS A CLASSE E NÃO O SELF:')

c2 = Connection.create_with_auth('Pedro', '789')
print(f'Nome: {c2.user}')
print(f'Senha: {c2.password}')

print('')
print('É UM FUNÇÃO SIMPLES DENTRO DA CLASSE:')

print(f'Soma: {Connection.sum(45,55)}')

print('')

