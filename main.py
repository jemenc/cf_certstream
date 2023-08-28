
import logging
import certstream.core as cs
from threading import Thread,Timer,Lock
from load_stack.stack import CreateAStack
from utils.comparations import compare_message
from decorators.decorators import format_message
from phishing_report.save_results import SaveResults
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

def analize_message():
    message = stack.get()
    compare = compare_message(value=message,keywords=keywords)
    if compare:
        save_results.write_result(compare)

#Fuction to extract the information from certstream
@format_message
def print_callback(message, context):
    """Fuction to save the messages into the stack in oder to analize them later
    """
    
    if message['issuer'] in ["Let's Encrypt","ZeroSSL"]:
        stack.put(item=message)
        logging.info( f" stack current size: {stack.qsize()}")
        logging.info("Messaged from stream -> {}".format(message))
        #logging.info("Messaged from stream -> {}".format(message))
    #logging.info("Messaged from stack -> {}".format(stack.get()))

#Threands

#Gather certstream messages
certstream = Thread(target=cs.listen_for_events,args=(print_callback,'wss://certstream.calidog.io/',True, ))
#analize = Thread(target=analize_message)

certstream.start()
#analize.start()

#certstream.join()
#analize.join()