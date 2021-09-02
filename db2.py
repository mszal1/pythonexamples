import jaydebeapi
import jpype

#set this variables
db2jcc4 = 'path_to_db2jcc4.jar'
db2jcc_license_cisuz = 'path_to_db2jcc_license_cisuz.jar'
dsn_hostname='db2_ip'
dsn_port='db2_port'
dsn_database='dbname'
user = 'db2 user'
passwd = 'db2 passw'
sql = 'sql to execute'


#create env
jar = db2jcc4 + ';' + db2jcc_license_cisuz
args='-Djava.class.path=%s' % jar
jvm = jpype.getDefaultJVMPath()
jpype.startJVM(jvm, args)
connection_string='jdbc:db2://'+dsn_hostname+':'+dsn_port+'/'+dsn_database


#connect to db
conn = jaydebeapi.connect('com.ibm.db2.jcc.DB2Driver', connection_string, [user, passwd])
curs = conn.cursor()
curs.execute(sql)

print(curs.fetchall())
