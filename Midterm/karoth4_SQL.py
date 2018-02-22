import psycopg2

# Try to connect

try:
        conn=psycopg2.connect("dbname='midterm' user='g479' password='g479'")
        conn.autocommit = True
except:
        print "I am unable to connect to the database."

cur = conn.cursor()

cur.execute("""CREATE TABLE karoth4
                (
                 city varchar(40),
                 city_ascii varchar(40),
                 lat float,
                 lng float,
                 pop float,
                 country varchar(40),
                 iso2 varchar(6),
                 iso3 varchar(6),
                 province varchar(60)
                )""")


f = open("worldcities_noheader.csv")
cur.copy_from(f,'karoth4',sep=",")
f.close()

cur.execute("""ALTER TABLE karoth4 ADD COLUMN geom geometry(POINT,4326)""")
cur.execute("""UPDATE karoth4 SET geom = ST_GeomFromText('POINT(' || lng || ' ' ||lat || ')',4326)""")



