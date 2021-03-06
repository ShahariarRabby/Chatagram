from flask import Flask
from flask_socketio import SocketIO, send, emit
import chatBot

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
socketio = SocketIO(app)



@socketio.on('faceverify')
def handlefaceverify(payload):
    print(payload['acc_no'])
    response = chatBot.converse(payload['acc_no'])
    print(response)
    emit('message',{'message':response['data']})


@socketio.on('message')
def handleMessage(payload):
    print(payload['dataset'])
    response = chatBot.converse(payload['message'])
    print(response)
    if('map' in response):
        emit('map', {"map":1,'markers':response['data']})
    elif('faceverify' in response):
        emit('message',{'message':response['data'],'faceverify':1})
    else:
        emit('message',{'message':response['data']})


if __name__ == '__main__':
    #socketio.run(app) #This WILL NOT WORK. The tutorial was sucky. Use the command below
    socketio.run(app, host='0.0.0.0', debug = True, port = 3110, use_reloader = True) #Open localhost:3110 to run this in your browser -.-
