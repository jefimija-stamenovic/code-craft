from processor import *

class Client: 

    def call_processor(self, processor: PaymentProcessor, amount: float) -> None: 
        processor.process(amount)
        print("--------------------")