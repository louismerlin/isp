import re
from netfilterqueue import NetfilterQueue

def print_and_accept(pkt):
  payload = pkt.get_payload()
  payload2 = [b for b in payload]
  if len(payload2) == 256:
    payload2[115] = 47
  pkt.set_payload(bytes(payload2))
  pkt.accept()

nfqueue = NetfilterQueue()
nfqueue.bind(1, print_and_accept)
try:
  nfqueue.run()
except KeyboardInterrupt:
  print('')

nfqueue.unbind()
