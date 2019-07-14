from werkzeug.security import safe_str_cmp                                  #safe string compare
from user import User

#simple security
                                                                        #   users = [
                                                                            # {
                                                                            #     'id' : 1,
                                                                            #     'username': 'cobauser',
                                                                            #     'password': 'asdf'
                                                                            # }
                                                                        #     ]
users = [                                                                     
    User(1,'aan','asdf')
]

                                                                            # username_mapping = {
                                                                            #     'cobauser' : {
                                                                            #         'id' : 1,
                                                                            #         'username': 'cobauser',
                                                                            #         'password': 'asdf'
                                                                            #     }
                                                                            # }

                                                                            # userid_mapping = {
                                                                            #     1 : {
                                                                            #         'id' : 1,
                                                                            #         'username': 'cobauser',
                                                                            #         'password': 'asdf'
                                                                            #     }
                                                                            # }

username_mapping = {u.username: u for u in users}
userid_mapping = {u.id: u for u in users}

def authenticate(username, password):
        user = username_mapping.get(username, None)
        # user = userid_mapping.get(username, None)
        print ("coba ya")
        # print(safe_str_cmp(user.password, password))
        if user and safe_str_cmp(user.password, password) :                 # this is simple way for not  using safe_str_cmp"if user and user.password == password :"
                print ("bisa nih")
                return user

def identity(payload) :                                                     # payload is JWT token
    user_id = payload['identity']
    return userid_mapping.get(user_id, None)