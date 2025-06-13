from client import Client 
from processor import *
from typing import List, Tuple

if __name__ == "__main__": 
    client: Client = Client()
    processors : List[Tuple[PaymentProcessor, float]] = [
        (ProcessorPayPall(), 99.25), 
        (ProcessorStripe(), 56.23), 
        (ProcessorBitcoin(), 75.96)
    ]

    for processor, amount in processors: 
        client.call_processor(processor, amount)