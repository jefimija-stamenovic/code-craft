from abc import ABC, abstractmethod 

# --- Product Interface ---
class PaymentGateway(ABC): 
    @abstractmethod
    def pay(self, amount: float) -> str: 
        pass 

# --- Concrete Product A ---
class GatewayPayPal(PaymentGateway): 
    def pay(self, amount: float) -> str:
        return f"Processing PayPal payment of ${amount:.2f}"
    
# --- Concrete Product B ---
class GatewayStripe(PaymentGateway): 
    def pay(self, amount: float) -> str:
        return f"Processing Stripe payment of ${amount:.2f}"
    
# --- Concrete Product C ---
class GatewayBitcoin(PaymentGateway): 
    def pay(self, amount: float) -> str:
        return f"Processing Bitcoin payment of ${amount:.2f}"