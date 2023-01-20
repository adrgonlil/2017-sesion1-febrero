from datetime import datetime, timedelta, date
from collections import defaultdict, namedtuple
import csv

Video=namedtuple("Video","id, fecha_trending, titulo, canal, categoria, visitas, likes, dislikes")

def parsea_fecha(cadena):
    return datetime.strptime(cadena, "%d/%M/%Y").date()

def lee_videos(fichero):
    with open(fichero, encoding="utf-8") as f:
        lector=csv.reader(f, delimiter=";")
        next(lector)
        res=[]
        for id, fecha_trending, titulo, canal, categoria, visitas, likes, dislikes in lector:
            fecha_trending=parsea_fecha(fecha_trending)
            visitas=int(visitas)
            likes=int(likes)
            dislikes=int(dislikes)
            res.append(Video(id, fecha_trending, titulo, canal, categoria, visitas, likes, dislikes))
    return res

def media_visitas(videos, fecha):
    visitas=[v.visitas for v in videos if v.fecha_trending==fecha]
    media=0
    if len(visitas)>0:
        media = sum(visitas)/len(visitas)
    return media

def video_mayor_ratio_dislikes(videos, categoria=None):
    tupla=[]
    for v in videos:
        if v.categoria==categoria or categoria==None and v.dislikes>0:
            tupla.append(v)
    return max(tupla, key = lambda v:v.likes/v.dislikes)

def canales_top(videos, n=3):
    dicc=defaultdict(int)
    for v in videos:
        dicc[v.canal]+=1
    return sorted(dicc.items(), key=lambda x:x[1], reverse=True)[:n]

def likeability(video, k):
    return (video.likes*k - video.dislikes)/(k*video.visitas)

def video_mas_likeability_por_categoria(videos, k=20):
    dicc=defaultdict(list)
    for v in videos:
        dicc[v.categoria].append((likeability(v, k), v.id))
    for categoria, gustamiento in dicc.items():
        dicc[categoria]=max(gustamiento, key=lambda x:x[0])
    for clave, lista in dicc.items():
        dicc[clave]=lista[1]
    return dicc
    

    
        
    

    