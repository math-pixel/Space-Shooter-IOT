USE_MICROPYTHON = True

if USE_MICROPYTHON:
    import usocketio as libSocket
else:
    import socketio as libSocket


class SocketIOClientManager:

    def __init__(self, server_url) -> None:
        # Créer une instance de Socket.IO
        self.client = libSocket.Client()
        # Connexion au serveur Socket.IO
        self.conn = self.client.connect(server_url)

    def sendMessage(self, channel, myData):
        self.client.emit(channel, data=myData)

    def disconnect(self):
        self.client.disconnect()

    def on_connect(self):
        print('Connexion établie avec le serveur')

    def on_disconnect(self):
        print('Connexion au serveur perdue')

    def on_message(self, data):
        print('Message reçu :', data)

    def on_error(self, data):
        print('Erreur :', data)

    def setup_event_handlers(self):
        self.client.on('connect', self.on_connect)
        self.client.on('disconnect', self.on_disconnect)
        self.client.on('message', self.on_message)
        self.client.on('error', self.on_error)

# URL du serveur Socket.IO
#server_url = 'http://localhost:8000'  # Remplacez localhost:3000 par l'URL de votre serveur

# manager = SocketIOClientManager(server_url)
# manager.setup_event_handlers()
# manager.sendMessage("fire", "toto")
# input("Appuyez sur Entrée pour quitter...\n")