# Test the procedural functions


def create_new_account(number, name, balance, limit):
    account = {'number': number, 'name': name, 'balance': balance, 'limit': limit}
    return account


def apply_money(account, value):
    account['balance'] += value


def get_value(account, value):
    account['balance'] -= value


def account_report(account):
    print('The balance is {}'.format(account['balance']))

