from app import app
from flask import request

@app.route('/sellfill', methods=['GET', 'POST'])
def sellfill():
    filesell =open("D:\\Veeramani\\01programming\\py\\sell.txt","w")
    filesell.write(request.form['t4'])
    filesell.write("\n")
    filesell.write(request.form['t3'])
    filesell.write("\n")
    filesell.write(request.form['t2'])
    filesell.write("\n")
    filesell.write(request.form['t1'])
    filesell.write("\n")
    filesell.write(request.form['sell'])
    filesell.write("\n")
    filesell.write(request.form['ssl'])
    filesell.close()
    return "Success"
@app.route('/sell')
def sell():
    user = {'nickname': 'Gann Sell'}  # fake user
    return '''
<html>
  <head>
    <title>Home Page</title>
  </head>
  <body>
  <form action="sellfill" method="post" name="sellfill">
    <h1>Hello, ''' + user['nickname'] + '''</h1>
<label for="t4">T4</label>
<input type="text" name="t4" id="t4"/><br><br>
<label for="t3">T3</label>
<input type="text" name="t3" id="t3"><br><br>
<label for="t2">T2</label>
<input type="text" name="t2" id="t2"><br><br>
<label for="t1">T1</label>
<input type="text" name="t1" id="t1"><br><br>
<label for="sell">Sell</label>
<input type="text" name="sell" id="sell"><br><br>
<label for="ssl">SL</label>
<input type="text" name="ssl" id="ssl">
 <p><input type="submit" value="Sign In"></p>
    </form>
  </body>
</html>
'''
