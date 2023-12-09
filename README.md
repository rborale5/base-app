# base-app

Install python packatges using:
pip3 install -r requirements.txt

To run use following command

python3 app.py


To run redis server locally:

docker run -d -p 6379:6379 -p 8001:8001 redis/redis-stack:latest

To view redis data in gui:
sudo npm install -g redis-commander
run this tool with command: redis-commander
access with browser at http://127.0.0.1:8081


Moved Confluence PAT to .env file


To hit the server APIs:

curl 'localhost:8000/query' \
--header 'Content-Type: application/json' \
--data '{
    "query" : "What color is apple",
    "chat_history": []
}'
