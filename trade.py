from app import app
from flask import request
import sqlite3


@app.route('/tradeenter', methods=['GET', 'POST'])
def tradeenter():
    conn = sqlite3.connect("stock.db")
    sType = request.form['sType']
    symbol = request.form['symbol']
    price = request.form['price']
    conn.execute("INSERT INTO trade (type,symbol,buy) VALUES (?, ?, ? )", (sType, symbol, price))
    conn.commit()

    #cursor = conn.execute("Select * from trade")

    #cursor = tradedao.selectTrade()
    #for row in cursor:
        #print(row[0])
    return "Success"


@app.route('/trade')
def trade():
    user = {'nickname': 'Gann Buy Form'}  # fake user
    return '''
<html>
  <head>
    <title>Enter the Trades</title>
  </head>
  <body>
  <form action="tradeenter" method="post" name="buyfill">
    <h1>Hello, ''' + user['nickname'] + '''</h1>
<label for="sType">Type</label>
<input type="text" name="sType" id="sType"/><br><br>
<label for="symbol">Symbol</label>
<input type="text" name="symbol" id="symbol"><br><br>
<label for="price">Price</label>
<input type="text" name="price" id="price"><br><br>
 <p><input type="submit" value="Enter"></p>
    </form>
  </body>
</html>
'''
