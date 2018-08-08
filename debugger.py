
SETTINGS = {
  'misc': False,
  'overview': False,
  'temp': True
}

def print_log(msg, type):
  if SETTINGS[type]:
    print(msg)
