from app import app
from flask import request

@app.route('/buyfill', methods=['GET', 'POST'])
def buyfill():
    filebuy =open("D:\\Veeramani\\01programming\\py\\buy.txt","w")
    filebuy.write(request.form['t4'])
    filebuy.write("\n")
    filebuy.write(request.form['t3'])
    filebuy.write("\n")
    filebuy.write(request.form['t2'])
    filebuy.write("\n")
    filebuy.write(request.form['t1'])
    filebuy.write("\n")
    filebuy.write(request.form['buy'])
    filebuy.write("\n")
    filebuy.write(request.form['bsl'])
    filebuy.close()
    return "Success"
@app.route('/buy')
def buy():
    user = {'nickname': 'Gann Buy Form'}  # fake user
    return '''
<html>
  <head>
    <title>Home Page</title>
  </head>
  <body>
  <form action="buyfill" method="post" name="buyfill">
    <h1>Hello, ''' + user['nickname'] + '''</h1>
<label for="t4">T4</label>
<input type="text" name="t4" id="t4"/><br><br>
<label for="t3">T3</label>
<input type="text" name="t3" id="t3"><br><br>
<label for="t2">T2</label>
<input type="text" name="t2" id="t2"><br><br>
<label for="t1">T1</label>
<input type="text" name="t1" id="t1"><br><br>
<label for="buy">Buy</label>
<input type="text" name="buy" id="buy"><br><br>
<label for="bsl">SL</label>
<input type="text" name="bsl" id="bsl">
 <p><input type="submit" value="Sign In"></p>
    </form>
  </body>
</html>
'''
