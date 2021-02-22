from flask import Flask
#from flask import render_template

# just serve all the static files under root
app = Flask(__name__, static_folder='.', static_url_path='')

# for / root, return Hello Word
@app.route("/")
def root():
    #return render_template('index.html', name="Charles")
    return app.send_static_file('index.html')


# Remember from flask import request
# for /request and POST method
@app.route('/request',methods=['POST'])
def request():
  payload=request.data
  # if accept json object as string
  data = json.loads(payload)
  # if accept normal string
  data = payload
  # After process
  
  # If still return json, Remember using jsonify(data) to return.
  # Do not need to return status, and mimetype. jsonify has
  # already helped you do that.
  return jsonify(data)
  return data, 200, {'Content-Type': 'application/json'}
  
  
  # Otherwise, just return with status and type
  # The mimetype can be text/xml, text/html.
  return data, 200, {'Content-Type': 'text/txt'}



#    http://127.0.0.1:5000/startMove
@app.route('/startMove',methods=['GET'])
def startMove():
    #rtMotor.start()
    #lfMotor.start()
    return "Started the motors"
#, 200, {'Content-Type': 'text/txt'}

@app.route('/stopMove',methods=['GET'])
def stopMove():
    #rtMotor.stop()
    #lfMotor.stop()
    return "Stopping the motors"

@app.route('/turnRight',methods=['GET'])
def turnRight():
    #turn off the right motor and turn on the left motor
    return "Turning right"

@app.route('/turnLeft',methods=['GET'])
def turnLeft():
    #turn off the left motor and turn on the right motor
    return "Turning left"

@app.route('/setSpeed/<int:speed>')
def setSpeed(speed):
    print("new speed: "+str(speed))
    return "setting speed to " + str(speed)

# start listening
if __name__ == "__main__":
    app.run(debug=True)