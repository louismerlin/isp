build:
	docker build -t hw7steal .
start:
	docker run --rm -p 8000:8000 --name hw7prediction com402/hw7
steal: build
	docker run --rm --link hw7prediction -it hw7steal
