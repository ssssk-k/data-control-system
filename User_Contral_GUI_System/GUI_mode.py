import json


class Userdata:
    def __init__(self):
        with open('User_information.json', mode='r', encoding='utf-8') as f:
            text = f.read()
        self.users = json.loads(text)

    def check_login(self, username, password):
        for user in self.users:
            if user['username'] == username:
                if user['password'] == password:
                    return True, '登 录 成 功!'
                else:
                    return False, '密 码 错 误'
        else:
            return False, '用户不存在'


GUI_mode = Userdata()
