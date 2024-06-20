import requests
import json

BASE_URL: str = "https://cpmewan.anasov.ly/api"

class CPMEwan:

    def __init__(self, access_key) -> None:
        self.auth_token = None
        self.access_key = access_key
    
    def login(self, email, password) -> int:
        payload = { "account_email": email, "account_password": password }
        
        response = requests.post(f"{BASE_URL}/account_login", params=params, data=payload)
        response_decoded = json.loads(response.text)
        if response_decoded.get("ok"):
            self.auth_token = response_decoded.get("auth")
        return response_decoded.get("error")
    
    def register(self, email, password) -> int:
        payload = { "account_email": email, "account_password": password }
        
        response = requests.post(f"{BASE_URL}/account_register", params=params, data=payload)
        response_decoded = json.loads(response.text)
        return response_decoded.get("error")
    
    def delete(self):
        
        
        requests.post(f"{BASE_URL}/account_delete", params=params, data=payload)

    def get_player_data(self) -> any:
        
        
        response = requests.post(f"{BASE_URL}/get_data", params=params, data=payload)
        response_decoded = json.loads(response.text)
        return response_decoded
    
    def set_player_rank(self) -> bool:
        
        
        response = requests.post(f"{BASE_URL}/set_rank", params=params, data=payload)
        response_decoded = json.loads(response.text)
        return response_decoded.get("ok")
    
    def get_key_data(self) -> any:
        
        response = requests.get(f"{BASE_URL}/get_key_data", params=params)
        response_decoded = json.loads(response.text)
        return response_decoded
    
    def set_player_money(self, amount) -> bool:
        payload = {
            "account_auth": self.auth_token,
            "amount": amount
        }
        
        response = requests.post(f"{BASE_URL}/set_money", params=params, data=payload)
        response_decoded = json.loads(response.text)
        return response_decoded.get("ok")
    
    def set_player_coins(self, amount) -> bool:
        payload = {
            "account_auth": self.auth_token,
            "amount": amount
        }
        
        response = requests.post(f"{BASE_URL}/set_coins", params=params, data=payload)
        response_decoded = json.loads(response.text)
        return response_decoded.get("ok")
    
    def set_player_name(self, name) -> bool:
        payload = { "account_auth": self.auth_token, "name": name }
        
        response = requests.post(f"{BASE_URL}/set_name", params=params, data=payload)
        response_decoded = json.loads(response.text)
        return response_decoded.get("ok")
    
    def set_player_localid(self, id) -> bool:
        payload = { "account_auth": self.auth_token, "id": id }
        
        response = requests.post(f"{BASE_URL}/set_id", params=params, data=payload)
        response_decoded = json.loads(response.text)
        return response_decoded.get("ok")

    def set_player_plates(self) -> bool:
        
        
        response = requests.post(f"{BASE_URL}/set_plates", params=params, data=payload)
        response_decoded = json.loads(response.text)
        return response_decoded.get("ok")
    
    def delete_player_friends(self) -> bool:
        
        
        response = requests.post(f"{BASE_URL}/delete_friends", params=params, data=payload)
        response_decoded = json.loads(response.text)
        return response_decoded.get("ok")
    
    def unlock_w16(self) -> bool:
        
        
        response = requests.post(f"{BASE_URL}/unlock_w16", params=params, data=payload)
        response_decoded = json.loads(response.text)
        return response_decoded.get("ok")
    
    def unlock_horns(self) -> bool:
        
        
        response = requests.post(f"{BASE_URL}/unlock_horns", params=params, data=payload)
        response_decoded = json.loads(response.text)
        return response_decoded.get("ok")
    
    def disable_engine_damage(self) -> bool:
        
        
        response = requests.post(f"{BASE_URL}/disable_damage", params=params, data=payload)
        response_decoded = json.loads(response.text)
        return response_decoded.get("ok")

    def unlimited_fuel(self) -> bool:
        
        
        response = requests.post(f"{BASE_URL}/unlimited_fuel", params=params, data=payload)
        response_decoded = json.loads(response.text)
        return response_decoded.get("ok")
    
    def set_player_wins(self, amount) -> bool:
        payload = {
            "account_auth": self.auth_token,
            "amount": amount
        }
        
        response = requests.post(f"{BASE_URL}/set_race_wins", params=params, data=payload)
        response_decoded = json.loads(response.text)
        return response_decoded.get("ok")

    def set_player_loses(self, amount) -> bool:
        payload = {
            "account_auth": self.auth_token,
            "amount": amount
        }
        
        response = requests.post(f"{BASE_URL}/set_race_loses", params=params, data=payload)
        response_decoded = json.loads(response.text)
        return response_decoded.get("ok")

    def unlock_houses(self) -> bool:
        
        
        response = requests.post(f"{BASE_URL}/unlock_houses", params=params, data=payload)
        response_decoded = json.loads(response.text)
        return response_decoded.get("ok")
    
    def unlock_smoke(self) -> bool:
        
        
        response = requests.post(f"{BASE_URL}/unlock_smoke", params=params, data=payload)
        response_decoded = json.loads(response.text)
        return response_decoded.get("ok")
    
    def unlock_paid_cars(self) -> bool:
        
        
        response = requests.post(f"{BASE_URL}/unlock_paid_cars", params=params, data=payload)
        response_decoded = json.loads(response.text)
        return response_decoded.get("ok")
    