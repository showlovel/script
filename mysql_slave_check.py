import os

devs    = {
         "ip":"password"
          }

lookup  = {
         "Slave_IO_Running":"Yes",
         "Slave_SQL_Running":"Yes"
          }

message = ""

for (ip, psw) in devs.items():
  cmd    = 'mysql -e "show slave status\G" -u zin -h ' + ip + ' --password=' + psw
  status = os.popen(cmd).read()
  for st in status.split("\n"):
    options = st.strip().split(":")
    if len(options)==2:
      key   = options[0].strip()
      value = options[1].strip()
      if lookup.has_key(key) and lookup[key] != value:
        message +=  "ERROR IN "+ key +" EXPECT "+ lookup[key] + " BUT NOW IS " + value + " IN " + ip +"\n"

mailCmd = 'echo "' + message + '"|mail -s "MySQL Slave ERROR" shengyu.yang@chinacache.com'
if len(message) != 0:
  os.system(mailCmd)
