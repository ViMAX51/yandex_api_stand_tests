import requests
import configuration
import data
import create_user_test


def post_new_user(user_body):

    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=user_body,
                         headers=data.headers)


response = post_new_user(data.user_body)


def get_users_table():

    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)



response = get_users_table()


print(response.status_code)











