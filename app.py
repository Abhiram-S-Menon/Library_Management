import psycopg2
from flask import Flask,render_template, redirect, request
#------------------------App Initialization---------------------------------
app= Flask(__name__)
#---------------------------------------------------------------------------
#------------------------Home Page------------------------------------------
@app.route('/')
def index():
    return render_template('index.html')
#---------------------------------------------------------------------------
#------------------------Search_by_Author-----------------------------------
@app.route('/search_by_author',methods=["GET","POST"])

def author():
    if request.method=="GET":
        return render_template('search_author.html')
    if request.method=="POST":
        author=request.form["auth_name"]
        conn=None
    #commit
        try:
            conn=psycopg2.connect(database="lis",user="postgres",password="007007",host="/var/run/postgresql",port="5432")
            
            cur=conn.cursor()
            cur.execute("select bc.title,bc.publisher,bc.year from book_catalogue bc,\
                         book_authors ba where bc.isbn_no=ba.isbn_no and\
                         ba.author_fname=%s",(author,))
                         
            rows=cur.fetchall()
            return render_template('search_result.html',books=rows)

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                    conn.close()



#--------------------Run Flask App--------------------------------------------
if __name__=='__main__':
    app.run(debug=True)
    




