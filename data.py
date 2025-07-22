import generators


class DataForRegistration:
    reg_data = [
        {
            'login': generators.login_generator(), 'name': generators.name_generator()
        },
        {
            'password': generators.password_generator(), 'name': generators.name_generator()
        }
    ]

class DataForAutorization:
    aut_data = [
        {
            'login': generators.login_generator(), 'password': ''
        },
        {
            'login': '', 'password': generators.password_generator()
        }
    ]

class OrderData:
    order_data = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha"
    }
    scooter_color = (
        ('BLACK',),
        ('GREY',),
        ('BLACK', 'GREY'),
        ()
    )

class ResponseBody:
    COURIER_CREATION_SUCCESS = {'ok': True}
    COURIER_NAME_ALREADY_EXIST = {
        'code': 409,
        'message': 'Этот логин уже используется. Попробуйте другой.'
    }
    COURIER_REGISTRATION_NOT_ENOUGH_DATA = {
        'code': 400,
        'message': 'Недостаточно данных для создания учетной записи'
    }
    COURIER_ACCOUNT_NOT_FOUND = {
        'code': 404,
        'message': 'Учетная запись не найдена'
    }
    COURIER_LOGIN_NOT_ENOUGH_DATA = {
        'code': 400,
        'message': 'Недостаточно данных для входа'
    }

class Flags:
    SUCCESSFUL_ORDER_CREATION = 'track'
    SUCCESSFUL_GET_ORDER_LIST = 'orders'