## StringManipulationService
---

# What is it?
- This is a service consisting of four API's.
- The services are basically to operate the API's to perform different forms of operations.

# Short discussion on API's
- /insertData : This is to insert a given string into database.
  - Method: GET
  - Payload: stringName=""

 - /fetchAllRecords : API to fetch all the strings stored in the database.
   - Method: GET

 - /performOperation : API to perform different operations on the given string id's value.
   - Method: GET
   - Payload: stringId="", 
   			  opType= reverse/reverse-word/flip/sort

 - /fetchOperationCount : API to fetch number of performances performed on the given string id along with its performed string.
   - Method: GET
   - Payload: stringId=""


# Note:
- I've also attached the postman collection's in the repository under folder /postman_collection