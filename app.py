from flask import Flask, render_template, json, request
from flask.ext.mysql import MySQL
from werkzeug import generate_password_hash, check_password_hash

app = Flask(__name__)

mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'sql'
app.config['MYSQL_DATABASE_DB'] = 'BucketList'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

@app.route("/")
def main():
    return render_template('index.html')

@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')

@app.route('/signUp',methods=['POST', 'GET'])
def signUp():
    try:
      # read the posted values from the UI
      _name = request.form['inputName']
      _email = request.form['inputEmail']
      _password = request.form['inputPassword']

      # validate the received values
      if _name and _email and _password:
          conn = mysql.connect()
          cursor = conn.cursor()
          _hashed_password = generate_password_hash(_password)
          cursor.callproc('sp_createUser',(_name,_email,_hashed_password))
          data = cursor.fetchall()

          if len(data) is 0:
              conn.commit()
              return json.dumps({'message':'User create successfully'})
          else:
              return json.dumps({'error': str(data[0])})

      else:
          return json.dumps({'html':'<span>Enter the required fields</span>'})
    except Exception as e:
        return json.dumps({'html': str(e)})
    finally:
        cursor.close()
        conn.close()

@app.route('/showSignin')
def showSignin():
    return render_template('signin.html')


if __name__ == "__main__":
    app.run()
