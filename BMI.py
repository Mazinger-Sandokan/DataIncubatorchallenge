# import the streamlit library
import streamlit as st
from streamlit.elements.doc_string import CONFUSING_STREAMLIT_MODULES
import math
import numpy as np
import matplotlib 
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


#st.set_page_config(layout="t") 
# give a title to our app



from PIL import Image
mapana = Image.open("mapana.jpeg")
tomate=Image.open("rotten.png")
tensor=Image.open("tensor.png")
pythonlogo=Image.open("python.jpeg")
movie=Image.open("movie.png")
star=Image.open("star.png")
zero=Image.open("zero.jpeg")

col1, col2 ,col3,col4,col5,col6= st.columns([12,8,3,3,3,3])


col1.image(mapana, use_column_width=True,width=200)
col5.image(tomate,use_column_width=False,width=50)
col6.image(movie,use_column_width=False,width=50)
col3.image(pythonlogo, use_column_width=False,width=50)
col4.image(tensor,use_column_width=False,width=50)
st.title('How many stars did the movie get?')

# display image using streamlit
# width is used to set the width of an image
# Subheader
#st.subheader("This is a subheader")
 
# TAKE WEIGHT INPUT in kgs
review = st.text_input("Please enter the review you want to interpret")
# weight = st.number_input("Please enter the review you want to interpret")
 

values=dict()
values["good"]=1
values["great"]=2
values["awesome"]=2
values["loved"]=2
values["bad"]=-1
values["horrible"]=-2
values["bored"]=-1
values["dread"]=-1
review=review.split()
score=0
for x in review:
    if x in values.keys():
        score=score+values[x]

if(st.button('Interpret the review')):
     
    # print the BMI INDEX

    st.text("Here is my advise on the movie")
     
    # give the interpretation of BMI index
   #"""  if(bmi < 16):
     #   st.error("You are Extremely Underweight")
    #elif(bmi >= 16 and bmi < 18.5):
    #    st.warning("You are Underweight")
    #elif(bmi >= 18.5 and bmi < 25):
    #    st.success("Healthy")       
    #elif(bmi >= 25 and bmi < 30):
    #    st.warning("Overweight")
    #elif(bmi >= 30):
    #    st.error("Extremely Overweight") """
    
    if score >1.5:
        st.success("The movies is great!")
        stars= st.columns([2,2,2,2,2,15])
        for i in range(5):
            stars[i].image(star,width=50)

        
    elif score >0.5:
        st.success("This is a good movie") 
        stars= st.columns([2,2,2,2,2,15])
        for i in range(3):
            stars[i].image(star,width=50)  
    elif score >-0.5:
        st.warning("Not too bad")
        stars= st.columns([2,2,2,2,2,15])
        for i in range(4):
            stars[i].image(star,width=50)
    elif score >-1.5:
        st.error("Don´t waste your time!") 
        stars= st.columns([2,2,2,2,2,15])
        for i in range(2):
            stars[i].image(star,width=50)   
    else:
        st.error("Get away from this boring nightmare!")
        rto= st.columns([2,2,2,2,2,15])
        for i in range(5):
            rto[i].image(zero,width=50) 


if(st.button('make sound')):
    st.audio("metal.mp3")

with st.expander("Want to learn about neural networks?"):
    st.video("https://www.youtube.com/watch?v=aircAruvnKk")    

    def isprime(n):
        ans=1
        for i in range(2,int(math.sqrt(n))+1):
            if n%i==0:
                ans=0
                break
        return ans
    Pi=dict()
    for i in range(2,5001):
        Pi[i]=isprime(i)  

    def pi(n):
        ans=0
        for i in range(2,n+1):
            if Pi[i]==1:
                ans = ans+1
        return ans 



with st.expander("Want to learn about the prime number theorem?"):
    data=[]
    N=st.slider("Please chose an integer you want to consider", min_value=5, max_value=5000, step=1)
    N=int(N)

    for i in range(2, N+1):
        data.append(pi(i)) 
    data=np.array(data)    

    fig, ax = plt.subplots()
    ax.plot(range(2,N+1),data,"b",label="Number of primes")
    approx=[]
    for i in range(2,N+1):
        approx.append(i/math.log(i))
    ax.plot(range(2,N+1),approx,"g",label="Aproximation")
    ax.legend()
    st.pyplot(fig)
    

with st.expander("Want to see the probability that two numbers are relatively prime?"):
    
    M=st.slider("Please chose an the size of the grid", min_value=5, max_value=200, step=1)
    def relprim(a,b):
        ans=0
        if math.gcd(a,b)==1:
            ans=1
        return ans

    
    temp=np.random.normal(size=(M,M))
    for i in range(1,M+1):
        for j in range(1,M+1):
            temp[i-1][j-1]=relprim(i,j)
    df = pd.DataFrame(np.array(temp), columns=range(1,M+1))
    sns.color_palette("mako", as_cmap=True)
    heat, ax = plt.subplots()
    micolor = st.sidebar.radio('Select one of the following excellent numbers:', ["Blues","Greens","magma","BuPu_r","pink","rainbow"])
    sns.heatmap(df,cmap=micolor,annot=False,yticklabels=False,xticklabels=False, ax=ax)
    
    st.write(heat)