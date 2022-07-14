import sys
#clients = ['pablo','ricardo']
clients = [
    {
        'name': 'Pablo',
        'company': 'Google',
        'email': 'pablo@gmail.com',
        'position': 'Software engineer'
    },
    {
        'name': 'Ricardo',
        'company': 'Facebook',
        'email': 'ricardo@gmail.com',
        'position': 'Data engineer'
    }
]

def create_client(client_name):
    global clients

    if client_name not in clients:
        clients.append(client_name)
        #clients += client_name
        #_add_comma()
    else:
        print('Client already is in the client\'s list')

def list_clients():
    for id,client in enumerate(clients):
        #print('{}: {}'.format(id,client['name']))
        print('{uid}|{name}|{company}|{email}|{position}'.format(
            uid = id,
            name = client['name'],
            company = client['company'],
            email = client['email'],
            position = client['position']
        ))
    #global clients
    #print(clients)


def update_client(client_name,update_client_name):
    global clients
    #if client_name in clients:
    for id,client in enumerate(clients):
        if client['name'] != client_name:
            continue
        else:
            clients[id]['name'] = update_client_name
            return
        #index = clients.index(client_name)
        #clients[index] = update_client_name
        
        #clients = clients.replace(client_name+',',update_client_name+',')
    else:
        print('Client is not in client\'s list')


def delete_client(client_name):
    global clients
    #if client_name in clients:
        #clients.remove(client_name)
    for id,client in enumerate(clients):
        if client['name'] != client_name:
            continue
        else:
            clients.pop(id)
            return
        #clients = clients.replace(client_name+',','')
    else:
        print('Client is not in client\'s list')


def search_client(client_name):
    #client_list = clients.split(',')
    #print('lista: {}'.format(client_list))
    #for client in clients:
     #   if client != client_name:
    for id,client in enumerate(clients):
        if client['name'] != client_name:
            continue
        else:
            return True


'''def _add_comma():
    global clients
    clients += ',' '''


def _print_welcome():
    print('WELCOME TO PLATZI VENTAS')
    print('*'*50)
    print('What would you like to do today?')
    print('[C] create client')
    print('[L] list client')
    print('[U] update client')
    print('[D] delete client')
    print('[S] search client')

def _get_client_field(field_name):
    field = None
    while not field:
        field = input('What is the client {}?'.format(field_name))
    return field


def _get_client_name():
    client_name = None
    while not client_name:
        client_name = input('What is the client name? ')
        if client_name == 'exit':
            client_name = None
            break
    if not client_name:
        sys.exit()

    return client_name


if __name__ == '__main__':
    _print_welcome()

    command = input()
    command = command.upper()

    if command == 'C':
        #client_name = _get_client_name()
        client = {
        'name': _get_client_field('Name'),
        'company': _get_client_field('Company'),
        'email': _get_client_field('Email'),
        'position': _get_client_field('Position')
        }
        create_client(client)
        list_clients()
    
    elif command == 'L':
        list_clients()

    elif command == 'D':
        client_name = _get_client_name()
        delete_client(client_name)
        list_clients()

    elif command == 'U':
        client_name = _get_client_name()
        update_client_name = input('What is the updated client name? ')
        update_client(client_name,update_client_name)
        list_clients()
    
    elif command == 'S':
        client_name = _get_client_name()
        found = search_client(client_name)
        if found:
            print('The client is in the client\'s list')
        else:
            print('The client {} is not in our client\'s list'.format(client_name))

    else:
        print('Invalid command')
