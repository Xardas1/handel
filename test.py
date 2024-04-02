import numpy as np
import matplotlib.pyplot as plt
import alpaca_trade_api as tradeapi


API_KEY = "TU BZRYTOSZ DA API KEY"
API_SECRET = "TU BZRYTOSZ DA API SECRET ZE SWOJEJ STRONY"
API_URL = "https://api.alpaca.markets" 


api = tradeapi.REST(API_KEY, API_SECRET, API_URL, api_version='v2')


api.submit_order(
    symbol='AAPL' #Firma apple
    qty=1 # Ile chcemy kupić akcji
    side='sell' #Czy chcemy sprzedać czy kupuić
    type='market' #Sposób w jaki chcemy chcemy kupować akcję bzrytosz ogarnię swoją teorią
    time_in_force='gtc' #Czas trawania ile order będze aktywny zanim wygaśnie
)






def calculate_difference():
    x = np.linspace(-10, 10, 400)
    y = 10*x + 10
    above_x = y > 0 
    below_x = y < 0
    distance_from_x_axis = np.abs(y)
    return distance_from_x_axis[below_x]

#print(calculate_difference())
