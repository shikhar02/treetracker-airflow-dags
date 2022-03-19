
import io
import requests
import psycopg2
import psycopg2.extras

# go though all planters, generate unified name as key, create row in entity, and 
# link the entity with the planter
def create_authors(conn, DISABLE_ORGANIZATION_FILTER):
  cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
  try:
      if(DISABLE_ORGANIZATION_FILTER):
          growerCursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
          growerCursor.execute("""
            SELECT *
            FROM treetracker.grower_account
          """);

          growerRows = growerCursor.fetchall()
          insertCursor = conn.cursor()
          for growerRow in growerRows:
              insertCursor.execute("""
                INSERT INTO messaging.author
                (handle)
                values
                (%s)
                ON CONFLICT DO NOTHING
              """, ( growerRow['wallet'], ) )
              print("SQL result:", insertCursor.query)
          return



      approvedStakeholderIds = ["fa0148f2-7bfc-47ba-9152-446b2cfa3f56", "04600c41-edd8-405e-bb2b-59f26f69ef51"]
      for stakeholderId in approvedStakeholderIds:
          print (stakeholderId)
          # cursor.execute("""
          #   SELECT *
          #   FROM stakeholder.stakeholder
          # """ )
          # print("SQL result:", cursor.query)
          # rows = cursor.fetchall()
          cursor.execute("""
            SELECT *
            FROM stakeholder.getStakeholderChildren( %s )
          """, ( stakeholderId, ) )
          print("SQL result:", cursor.query)
          rows = cursor.fetchall()
          # print(rows)

          if(stakeholderId == "all"):
            rows
          
          growerCursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
          for row in rows:
              #do something with every single row here
              print(row)

              growerCursor.execute("""
                SELECT *
                FROM treetracker.grower_account
                WHERE organization_id = %s
              """, ( row['stakeholder_id'], ) );

              growerRows = growerCursor.fetchall()
              insertCursor = conn.cursor()
              for growerRow in growerRows:
                  insertCursor.execute("""
                    INSERT INTO messaging.author
                    (handle)
                    values
                    (%s)
                    ON CONFLICT DO NOTHING
                  """, ( growerRow['wallet'], ) )
                  print("SQL result:", insertCursor.query)

      conn.commit()
  except Exception as e:
      print("get error when exec SQL:", e)
      raise ValueError('Error executing query')
      return False
  return True
