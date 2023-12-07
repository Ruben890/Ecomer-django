# import requests
# from .models import Product
# def obtener_tasas_de_cambio(api_key, currencies):
#     url = "https://api.currencyapi.com/v3/latest"
#     params = {"apikey": api_key, "currencies": currencies}

#     try:
#         response = requests.get(url, params=params)
#         response.raise_for_status()
#         data = response.json()
#         return data.get('data')

#     except requests.exceptions.RequestException as e:
#         print(f"Error en la solicitud: {e}")
#         return None

# # # Ejemplo de uso
# # api_key = "cur_live_g7Rb0Q1Qr5NQcPbDmNrhtIrA6JCl5y8Lho9i1RrO"
# # currencies = "EUR,USD,DOP"

# # # Imprime la respuesta completa
# # respuesta = obtener_tasas_de_cambio(api_key, currencies)
# # print(respuesta)

# # def update_all_prices_products(api_key, currencies):
# #     products = Product.objects.all()

# #     for product in products:
# #         current_price = product.price

# #         # Get exchange rates
# #         rates_data = obtener_tasas_de_cambio(api_key, currencies)

# #         if rates_data:
# #             # Apply exchange rates based on provided currencies
# #             for currency, exchange_rate in rates_data.items():
# #                 if currency == product.currency:
# #                     # Check if the exchange_rate is a dictionary and extract the value
# #                     if isinstance(exchange_rate, dict):
# #                         exchange_rate_value = exchange_rate.get('value', 1)  # Use a default of 1 if 'value' is not present
# #                     else:
# #                         exchange_rate_value = exchange_rate

# #                     new_price = current_price * exchange_rate_value
# #                     product.price = new_price

# #             # Save the updated product
# #             product.save()
# #         else:
# #             print("No se pudo obtener la información de tasas de cambio.")
