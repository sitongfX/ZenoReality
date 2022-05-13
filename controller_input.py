def parse_multiple_data(input):
    ''' parse multiple string of json data manually into number '''
    data = str(input.strip())[1:-1]
    items = data.split(",")
    con = []
    for i in items:
        temp = i.split(":")
        con.append(int(temp[1][1:-1]))
    return con


def parse_single_data(input):
    ''' parse single json data manually into number '''
    data = str(input.strip())[1:-1]
    num = data.split(":")[1][1:-1]
    return num
