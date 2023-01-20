from videos import *

def muestra_iterable(iterable):
    for elem in iterable:
        print(elem)
        

def test_lectura(datos):
    print("Test de la funcion de lectura")
    print("Hay", len(datos), "datos")
    print("Estos son los dos primeros datos:","\n")
    muestra_iterable(datos[:2])
    print()

def test_media_visitas(videos):
    print("Test de la función media visitas")
    fecha_str = '11/1/2017' 
    fecha = datetime.strptime(fecha_str, '%d/%M/%Y').date() 
    print ("La media de visitas del día", fecha_str, "es", media_visitas(videos, fecha))
    print()

def test_video_mayor_ratio_likes_dislikes(videos):
    print("Test de la funcion video_mayor_ratio_likes_dislikes")
    print(video_mayor_ratio_dislikes(videos, categoria=None))
    
def test_video_mas_likeability(videos):
    print("Test pocho","\n")
    res=video_mas_likeability_por_categoria(videos, 20)
    for clave, valor in res.items():
        print(clave,"-->",valor)
        
if __name__ == "__main__":
    videos=lee_videos("data/MX_Youtube_2017_utf8.csv")
    test_lectura(videos)
    test_media_visitas(videos)
    test_video_mayor_ratio_likes_dislikes(videos)
    print(canales_top(videos, 5))
    print()
    test_video_mas_likeability(videos)
