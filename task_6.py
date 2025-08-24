tickets = {
    1: ['API_45', 'API_76', 'E2E_4'],
    2: ['UI_19', 'API_65', 'API_76', 'E2E_45'],
    3: ['E2E_45', 'API_45', 'E2E_2'],
    4: ['E2E_9', 'API_76'],
    5: ['E2E_2', 'API_61']
}

types = {
    1: 'Блокирующий',
    2: 'Критический',
    3: 'Значительный',
    4: 'Незначительный',
    5: 'Тривиальный'
} 

def remove_duplicates(tickets_dict):
    unique_tasks = []  
    for key, value in tickets_dict.items():
        for task in value[:]: 
            if task not in unique_tasks:
                unique_tasks.append(task)  
            else:
                value.remove(task)
    return tickets_dict

def connect_dict(tickets_dict, types_dict):
    connected_dict = {}
    for key_types, value_types in types_dict.items():
        for key_tickets, value_tickets in tickets_dict.items():
            if key_tickets == key_types:
                connected_dict[value_types] = value_tickets
                break
    return connected_dict
