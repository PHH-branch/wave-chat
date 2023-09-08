# wave-chat
Healthcare related chat API service for Wave Money Hackathon

## API URL
### User URLs

* [pup-able-camel.ngrok-free.app/users](pup-able-camel.ngrok-free.app/users)

  __Description__: Get or Create users

  __Methods__: GET, POST

* [pup-able-camel.ngrok-free.app/users/(id)](pup-able-camel.ngrok-free.app/users/1)

  __Description__: Get or Update individual user

  __Methods__: GET, PUT
  
  __Params__:
  * id: integer

* [pup-able-camel.ngrok-free.app/users/waveid/(waveId)](pup-able-camel.ngrok-free.app/users/waveid/10000)

  __Description__: Get user by Wave ID

  __Methods__: GET
  
  __Params__:
  * waveId: integer

* [pup-able-camel.ngrok-free.app/users/phone/(phoneNo)](pup-able-camel.ngrok-free.app/users/phone/09123456)

  __Description__: Get user by phone number

  __Methods__: GET
  
  __Params__:
  * phoneNo: str