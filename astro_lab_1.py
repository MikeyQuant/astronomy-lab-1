import streamlit as st
import plotly.express as px
import pandas as pd
file=open("astro_scale.txt", "r").read()

ls=[]
for m in file.split("\n"):
    st.write(m)
    data={}
    ob=m.split(":")[0]
    base=(m.split(":")[1].split("x")[0].replace(" ",""))
    exp=(m.split(":")[1].split("^")[1].replace(" m",""))
    n=float(base+"E+"+exp)
    data["distance"]=n
    data["object"]=ob
    ls.append(data)
for k,v in data.items():
    print(k,v,type(v))
df = pd.DataFrame(ls)
d1=[]
for dis,obj in zip(df["distance"],df["object"]):
    d2=[]
    d2.append(obj)
    for dis2, obj2 in zip(df["distance"], df["object"]):
        d2.append(dis2/dis)
    d1.append(d2)
dfm=pd.DataFrame(d1,columns=["Measured"]+[x for x in df["object"]])
st.header("Distance Ratio Matrix")
st.write("The table below shows how many times one distance can fit into another distance. Simply put, the numbers represent the distance of the objects in the column names divided by the distance of the object in the Measured column ")
st.write(dfm)
objects=[]
st.header("Distance Illustration")
st.write("Select distances to Graph")
for o in df["object"]:
    y=st.checkbox(o,True,key=o)
    if y:

        objects.append(o)
st.header(" ")
dff=df[df["object"].isin(objects)]
log=st.checkbox("Use Log Scale?",True)
fig=px.bar(dff,x="object",y="distance",color="object",log_y=log)

st.plotly_chart(fig)