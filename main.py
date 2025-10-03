from ib_insync import *

ib = IB()
ib.connect('127.0.0.1', 4002, clientId=1)

contract=Stock('AAPL', 'SMART', 'USD')

#market_data=ib.reqMktData(contract, genericTickList='', snapshot=True, regulatorySnapshot=True)

#ib.sleep(2)

#print(f'Precio actual de AAPL: {market_data.last}')
#print(f'Precio actual de AAPL: {market_data.bid}')
#print(f'Precio actual de AAPL: {market_data.ask}')

bars = ib.reqHistoricalData(
    contract,
    endDateTime='',
    durationStr='1 D',  # Último día disponible
    barSizeSetting='1 day',  # Datos diarios
    whatToShow='TRADES',  # Precio de cierre basado en transacciones
    useRTH=True,  # Solo horas regulares de mercado
    formatDate=1
)

if bars:
    print(f"Último precio de cierre: {bars[-1].close}")
else:
    print("No se pudieron obtener los datos.")

ib.disconnect()
