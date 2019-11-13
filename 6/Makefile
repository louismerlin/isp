start:
	docker run --rm -it -p 80:80 --name hw6ex1 com402/hw6ex1
pwn:
	@docker cp solution.py hw6ex1:/root/
	@docker exec -it hw6ex1 python /root/solution.py
	@docker exec -it hw6ex1 cat /root/solutions/solution.txt
	@echo ""
