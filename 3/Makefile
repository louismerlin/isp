test: test1a test1b test1c test2
test1a:
	@docker run -it --read-only -v ${PWD}:/usr/src/homework -w /usr/src/homework python:3.8.0-alpine python 1a_brute_force.py
test1b:
	@docker run -it --read-only -v ${PWD}:/usr/src/homework -w /usr/src/homework python:3.8.0-alpine python 1b_dictionary.py
test1c:
	@docker run -it --read-only -v ${PWD}:/usr/src/homework -w /usr/src/homework python:3.8.0-alpine python 1c_salt.py
test2:
	@docker run --read-only -v ${PWD}:/app/student com402/hw3ex2
