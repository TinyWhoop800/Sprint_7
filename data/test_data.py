class TestData:

    @staticmethod
    def get_order_data(
            first_name="Naruto",
            last_name="Uchiha",
            address="Konoha, 142 apt.",
            metro_station=4,
            phone="+7 800 355 35 35",
            rent_time=5,
            delivery_date="2024-12-31",
            comment="Saske, come back to Konoha",
            color=None
    ):
        order_data = {
            "firstName": first_name,
            "lastName": last_name,
            "address": address,
            "metroStation": metro_station,
            "phone": phone,
            "rentTime": rent_time,
            "deliveryDate": delivery_date,
            "comment": comment
        }

        if color is not None:
            order_data["color"] = color

        return order_data