from flask import Flask, render_template, request
import requests
#import cgi, cgitbuu
import json
import APICalls as tmdb
#import psycopg2 as db
"""
try:
    connection = db.connect(user = "postgres",
                                  password = "password",
                                  host = "127.0.0.1",
                                  port = "5432",
                                  database = "postgres")
    cursor = connection.cursor()
    # Print PostgreSQL Connection properties
    print ( connection.get_dsn_parameters(),"\n")
    # Print PostgreSQL version
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected to - ", record,"\n")
    
    cursor.execute("select * from userdata;")
    record = cursor.fetchone()
    print("Records : ", record[1],"\n")
    
    
    app = Flask(__name__)

    

    
except (Exception, db.Error) as error :
    print ("Error while connecting to PostgreSQL", error)
    
finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
"""            
            
app = Flask(__name__)           
@app.route("/")
def home():
    
    ids=[]
    j=0
    k=0
    l=0
    moviesR=[]
    moviesT=[]
    moviesF=[]
    movies = []
    ids = tmdb.getRecommend()
    for i in ids: 
        
        mTitle=tmdb.getTitle(i)
        print(mTitle)
        mDescr=tmdb.getOverview(i)
        mPoster=tmdb.getPosterPath(i)
        mUrl=tmdb.getURL(i)
        mRat=tmdb.getRatings(i)
        movie={"Title": mTitle, "Info": mDescr, "Poster": mPoster, "Url": mUrl, "Rating": mRat}
        moviesR.append(movie)
        j=j+1
        if(j>3):
            break
    
    ids = tmdb.getTrending()
    for i in ids: 
        
        mTitle=tmdb.getTitle(i)
        print(mTitle)
        mDescr=tmdb.getOverview(i)
        mPoster=tmdb.getPosterPath(i)
        mUrl=tmdb.getURL(i)
        mRat=tmdb.getRatings(i)
        movie={"Title": mTitle, "Info": mDescr, "Poster": mPoster, "Url": mUrl, "Rating": mRat}
        moviesT.append(movie)
        k=k+1
        if(k>3):
            break
        
    ids = tmdb.getUpcoming()
    for i in ids: 
        
        mTitle=tmdb.getTitle(i)
        print(mTitle)
        mDescr=tmdb.getOverview(i)
        mPoster=tmdb.getPosterPath(i)
        mUrl=tmdb.getURL(i)
        mRat=tmdb.getRatings(i)
        movie={"Title": mTitle, "Info": mDescr, "Poster": mPoster, "Url": mUrl, "Rating": mRat}
        moviesF.append(movie)
        l=l+1
        if(l>3):
            break    
        
         
    movies.append(moviesT)
    movies.append(moviesR)
    movies.append(moviesF)
    
    """ response = response.json()
    rating = response['Ratings']

    response = json.dumps(rating, sort_keys = True, indent = 40)"""
    #response = response.replace(",","***********\n")
    return render_template('welcome.html', response=movies)

  
@app.route('/search',methods=['POST','GET']) 
def search():
    if(request.method=='POST'):
        title=request.form['search']
    else:
        title=request.args.get('search')
    print("blabla")
    print(title)
    print("blabla")
    ids=[]
    movies=[]  
    ids=tmdb.getIdsfromQuery(title)
    for i in ids: 
        
        mTitle=tmdb.getTitle(i)
        print(mTitle)
        mDescr=tmdb.getOverview(i)
        mPoster=tmdb.getPosterPath(i)
        mUrl=tmdb.getURL(i)
        mRat=tmdb.getRatings(i)
        movie={"Title": mTitle, "Info": mDescr, "Poster": mPoster, "Url": mUrl, "Rating": mRat}
        movies.append(movie)
        
    #response = requests.get('http://www.omdbapi.com/?apikey=aa44e6ff&t=blade')
    #response = response.json()
    #rating = response['Ratings']

    #response = json.dumps(rating, sort_keys = True, indent = 40)
    #response = response.replace(",","***********\n")
    return render_template('search.html', response=movies)

@app.route("/register") 
def register():
    
    response = requests.get('http://www.omdbapi.com/?apikey=aa44e6ff&t=blade')
    response = response.json()
    rating = response['Ratings']

    response = json.dumps(rating, sort_keys = True, indent = 40)
    #response = response.replace(",","***********\n")
    return render_template('home.html', response=rating)

@app.route("/login")
def login():
    
    
    j=0
    trending=[[]]
    for i in tmdb.getTrending():
        trending.append(tmdb.getTitle(i), tmdb.getPosterPath(i))
        j=j+1
        if(j>3):
            break
    
 
        
    upcoming=[[]]
    j=0
    for i in tmdb.getUpcoming():
        upcoming.append(tmdb.getTitle(i), tmdb.getPosterPath(i))
        j=j+1
        if(j>3):
            break
        
    
        
    recommendation=[[]]
    j=0
    for i in tmdb.getRecommendation():
        recommendation.append(tmdb.getTitle(i), tmdb.getPosterPath(i))
        j=j+1
        if(j>5):
            break
        
    
    
    response = requests.get('http://www.omdbapi.com/?apikey=aa44e6ff&t=blade')
    response = response.json()
    rating = response['Ratings']

    response = json.dumps(rating, sort_keys = True, indent = 40)
    #response = response.replace(",","***********\n")
    return render_template('home.html', response=final)

    



if __name__ == "__main__":
    app.run(debug=True)            









