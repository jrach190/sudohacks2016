from pubnub import Pubnub

pubnub = Pubnub(publish_key='demo', subscribe_key='sub-c-b06c619a-0414-11e6-bb6c-02ee2ddab7fe')


def _callback(message, channel):

    if message == "open":
        print("All good")
	pubnub.unsubscribe(channel='demo')
        

    elif message != "" :
        pubnub.unsubscribe(channel='demo')
        pubnub.subscribe(channels="demo", callback=_callback, error=_error)
        print("Test")

    else:
        print(message)


def _error(message):
    print(message)

pubnub.subscribe(channels="my_channel", callback=_callback, error=_error)