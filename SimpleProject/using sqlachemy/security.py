from werkzeug.security import safe_str_cmp                                  #safe string compare
from resources.user import UserModel


def authenticate(username, password):
    user = UserModel.find_by_username(username)
    print ("coba ya")
    if user and safe_str_cmp(user.password, password) :                 # this is simple way for not  using safe_str_cmp"if user and user.password == password :"
        print ("bisa nih")
        return user

def identity(payload) :                                                     # payload is JWT token
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)