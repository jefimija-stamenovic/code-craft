from abc import ABC
from gateway import *

# --- Creator Abstract Class ---
class PaymentProcessor(ABC): 

    def process(self, amount: float) -> None: 
        gateway: PaymentGateway = self.create_gateway()
        self.authenticate()
        print(gateway.pay(amount))
        self.log_transaction(amount)

    def authenticate(self) -> None: 
        print("Authenticating payment...")
    
    def log_transaction(self, amount: float) -> None:
        print(f"Logging transaction of ${amount:.2f}...")

    @abstractmethod
    def create_gateway(self) -> PaymentGateway: 
        pass 

# --- Concrete Creator A ---
class ProcessorPayPall(PaymentProcessor):
    def create_gateway(self) -> PaymentGateway:
        return GatewayPayPal()
    
# --- Concrete Creator B ---
class ProcessorStripe(PaymentProcessor):
    def create_gateway(self) -> PaymentGateway:
        return GatewayStripe()
    
# --- Concrete Creator C ---
class ProcessorBitcoin(PaymentProcessor):
    def create_gateway(self) -> PaymentGateway:
        return GatewayBitcoin()