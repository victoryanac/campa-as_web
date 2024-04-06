
from campaña import Campaña, LargoExcedidoError 
from anuncio import Video, SubTipoInvalidoError 
from datetime import date

def main():
    # Creación de una campaña con un anuncio de tipo Video
    anuncio_video = Video(url_archivo="video.mp4", url_clic="http://clickeaquí.com", sub_tipo="instream", duracion=30)
    campaña = Campaña(nombre="Campaña de Prueba", fecha_inicio=date.today(), fecha_termino=date.today(), anuncios=[anuncio_video])
    
    print("Modificación de la Campaña:")
    try:
        # Intentar cambiar el nombre de la campaña
        nuevo_nombre = input("Ingrese el nuevo nombre de la campaña: ")
        campaña.nombre = nuevo_nombre

        # Intentar cambiar el subtipo del anuncio
        nuevo_subtipo = input("Ingrese el nuevo subtipo para el anuncio de video ('instream' o 'outstream'): ")
        anuncio_video.sub_tipo = nuevo_subtipo

    except LargoExcedidoError as e:
        print(f"Error: {e}")
        with open('error.log', 'a') as file:
            file.write(f"{e}\n")

    except SubTipoInvalidoError as e:
        print(f"Error: {e}")
        with open('error.log', 'a') as file:
            file.write(f"{e}\n")

    print(campaña)

if __name__ == "__main__":
    main()
