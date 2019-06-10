import psycopg2


class DB_query:

        def __init__(self,image_Name):
                self.image_Name = image_Name

        def Version_Vuln(self,image_Name):
                host = "localhost"
                user = "ann"
                dbname = "Dachore"
                password = "p@ssw0rdtlqkfdjfuqwl"      
                sslmode = "require"

                conn_string = "host={0} user={1} dbname={2} password={3} sslmode={4}".format(host,user,dbname,password,sslmode)

                conn = psycopg2.connect(conn_string)
                print ("Connection established")
                cursor = conn.cursor()

                cursor.execute("select * from "+image_Name)
                result = cursor.fetchall()

                conn.commit()
                cursor.close()
                conn.close()

                return result

        def Package_Vuln(self,image_Name):
                f=open('/home/ubuntu/test.txt', 'r')
                words = []
                for line in f.readlines():
                        line = line.strip()
                        words.append(line.split())
                words = words[5:]
                string = []
                for i in range(len(words)):
                        string.append([words[i][1],words[i][2]])
                output=[]
                for j in range(len(string)):
                        output.append("".join(string[j]))
                f.close()

                host = "localhost"
                user = "ann"
                dbname = "Dachore"
                password = "p@ssw0rdtlqkfdjfuqwl"
                sslmode = "require"
                conn_string = "host={0} user={1} dbname={2} password={3} sslmode={4}".format(host,user,dbname,password,sslmode)
                conn = psycopg2.connect(conn_string)
                cursor = conn.cursor()

                n = 0
                result = []
                image_Name += '_package'
                for n in range(len(output)):
                        test = output[n]
                        cursor.execute("select * from "+image_Name+" where package_name = '"+test+"'")

                        result.append(cursor.fetchall())



             #   cursor.execute("select * from "+image_Name)
             #   result = cursor.fetchall()
                conn.commit()
                cursor.close()
                conn.close()

                return result
