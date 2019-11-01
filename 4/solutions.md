## Exercise 1 and Exercise 2

In the `client` container, run:

```bash
route del default
route add default gateway ${ip_of_mitm}
```

In the `mitm` container, run:

```bash
iptables -t nat -A POSTROUTING -j MASQUERADE -o eth0
iptables -A FORWARD -i eth0 -j ACCEPT
iptables -D FORWARD -i eth0 -j ACCEPT
iptables -A FORWARD -j NFQUEUE --queue-num 1
```

And then

```bash
python3 mitm.py
```
