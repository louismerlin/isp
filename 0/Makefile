start-web:
	docker run -d -p 8081:80 --name tools -v "${PWD}/html":/html dedis/com402-tools
start-scripts:
	docker run -d --name tools -v "${PWD}/scripts":/scripts dedis/com402-tools
exec-scrapper:
	docker exec -it tools python3 /scripts/scrapper.py
stop:
	docker rm -f tools
