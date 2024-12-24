import os

os.system('cls')

class Customer:
    def __init__(self, name, email, plan):
        self.name = name
        self.email = email
        self.list_plans = ['basic','premium']
        if plan in self.list_plans:
            self.plan = plan
        else:
            raise Exception('Plan is not on the list')

    def changePlan(self,new_plan):
        if new_plan in self.list_plans:
            self.plan = new_plan
        else:
            print('Invalid plan')

    def watch_movie(self, film, plan_film):
        if self.plan == plan_film:
            print(f'Watch the film {film}')

        elif self.plan == 'premium':
            print(f'Watch Movie {film}')

        elif self.plan == 'basic' and plan_film == 'premium':
            print(f'Upgrade to see this "{film}"')

        else:
            print('Invalid plan')


customer = Customer('Carlos', 'carlos@gmail.com', 'basic')
print(f'Customer name: {customer.name}')
print(f'Email: {customer.email}')
print(f'Plan: {customer.plan}')
customer.changePlan('premium')
print(f'New Plan: {customer.plan}')
customer.watch_movie('My father', 'premium')
print('')



