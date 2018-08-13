curl --header "Content-Type: application/json" --request POST \
  --data '{"subject":"First!","message":"This is an awesome first message!"}' \
  http://localhost:5000/

curl --header "Content-Type: application/json" --request POST \
  --data '{"subject":"Second.","message":"Is Second better than first?"}' \
  http://localhost:5000/

curl --header "Content-Type: application/json" --request POST \
  --data '{"subject":"THIRD","message":"First comes second then third.!"}' \
  http://localhost:5000/

curl --header "Content-Type: application/json" --request POST \
  --data '{"subject":"4th","message":"Will Smith did some good on 4th of July.!"}' \
  http://localhost:5000/

curl --header "Content-Type: application/json" --request POST \
  --data '{"subject":"FITH","message":"Sith Lords Go to the Fifth!!"}' \
  http://localhost:5000/

curl --header "Content-Type: application/json" --request POST \
  --data '{"subject":"seis","message":"SIX is my favorite color......"}' \
  http://localhost:5000/
