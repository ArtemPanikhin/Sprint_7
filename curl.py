class Url:
    create_courier_url = None
    MAIN_URL = 'https://qa-scooter.praktikum-services.ru'
    CREATE_COURIER = '/api/v1/courier'
    COURIER_LOGIN = '/api/v1/courier/login'
    COURIER_DELETE = '/api/v1/courier/'
    CREATE_ORDER = '/api/v1/orders'
    GET_ORDER_LIST = '/api/v1/orders'
    ORDER_CANCEL = '/api/v1/orders/cancel/track='
    TRACK_ORDER = '/api/v1/orders/track?t='

    @classmethod
    def create_courier_url(cls):
        return cls.MAIN_URL + cls.CREATE_COURIER

    @classmethod
    def courier_login_url(cls):
        return cls.MAIN_URL + cls.COURIER_LOGIN

    @classmethod
    def courier_delete_url(cls, courier_id):
        return cls.MAIN_URL + cls.COURIER_DELETE + str(courier_id)

    @classmethod
    def create_order_url(cls):
        return cls.MAIN_URL + cls.CREATE_ORDER

    @classmethod
    def get_order_list_url(cls):
        return cls.MAIN_URL + cls.GET_ORDER_LIST

    @classmethod
    def order_cancel_url(cls, track):
        return cls.MAIN_URL + cls.ORDER_CANCEL + str(track)

    @classmethod
    def track_order_url(cls, track):
        return cls.MAIN_URL + cls.TRACK_ORDER + str(track)