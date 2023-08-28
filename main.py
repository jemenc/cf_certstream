import time
import logging
from certstream.core import CertStreamClient
from threading import Thread,Timer,Lock
from load_stack.stack import CreateAStack
from utils.comparations import compare_message
from decorators.decorators import format_message
from phishing_report.save_results import SaveResults
from concurrent.futures import ProcessPoolExecutor
from load_keywords.load_keywords import LoadKeyworsFromFile

logging.basicConfig(
    level=10,
    format='%(asctime)s-%(levelname)s-%(message)s'
)

lock = Lock()

#Load keywords
keywords = LoadKeyworsFromFile().keys

#create a stack
stack = CreateAStack().urls_stack

#Create object to save results 
save_results = SaveResults()

#cs validation
run_cs = True

def analize_message():
    message = stack.get()
    compare = compare_message(value=message,keywords=keywords)
    if compare:
        save_results.write_result(compare)
    logging.info( f" stack current size from the end of the connection: {stack.qsize()}")

#Fuction to extract the information from certstream
@format_message
def print_callback(message, context):
    """Fuction to save the messages into the stack in oder to analize them later
    """

    if message['issuer'] in ["Let's Encrypt","ZeroSSL"]:
        stack.put(item=message)
        #Gather certstream messages
        qsize = stack.qsize()
        logging.info( f" stack current size: {qsize}")
        logging.info("Messaged from stream -> {}".format(message))
        #logging.info("Messaged from stream -> {}".format(message))
    #logging.info("Messaged from stack -> {}".format(stack.get()))

#Threands
#cs.listen_for_events(message_callback=print_callback,url='wss://certstream.calidog.io/',event_run=run_cs)


while True:
    try:
        while run_cs:
                c = CertStreamClient(print_callback,'wss://certstream.calidog.io/', skip_heartbeats=True, on_open=None, on_error=None)
                c.run_forever(ping_interval=15)
                time.sleep(5)
                qsize = stack.qsize()
                logging.info( f" stack current size from the end of the connection: {qsize}")
                if qsize > 500:
                    run_cs = False
        with ProcessPoolExecutor(max_workers=4) as executor:
            while stack.qsize() > 0:
                executor.submit(analize_message)
        run_cs = True
    except KeyboardInterrupt:
        logging.info("Kill command received, exiting!!")










#certstream = Thread(target=cs.listen_for_events,args=(print_callback,'wss://certstream.calidog.io/',True, ))
#analize = Thread(target=analize_message)

#certstream.start()
#analize.start()

#certstream.join()
#analize.join()