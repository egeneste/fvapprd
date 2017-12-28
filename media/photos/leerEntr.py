#!/usr/bin/env python
import serial, sys, django, os, uuid, base64
import time, requests
sys.path.append('C:/Users/EGeneste')#sys.path.append('E:/proyects')
os.environ["DJANGO_SETTINGS_MODULE"] = 'fvapprd.settings'
django.setup()
from interface.models import LecturaTempHume, Alertas, Module
from managerserial import sendmail
from PIL import Image as pimg
import media
def connection():
    try:
        ser = serial.Serial('COM16', 57600, timeout=1)
        return ser
    except Exception as ex:
        print('con fail')
        time.sleep(3)
        connection()


def main(ser):
    # notif = Alertas()
    # notif.modulo = 1001
    # notif.Tipo = 'sensor'
    # notif.alert_image = 'photos/login_bg.jpg'
    # notif.save()


    #inicializar valores
    modd = 0
    temm = 0
    humm = 0
    #set md to 1
    md = 2
    try:
        ser.close()
        ser.open()
        #k = ser.read_all()
        while ser.is_open:
            new_msg = ser.readall()
            print(len(new_msg), 'len', new_msg)
            if (len(new_msg) > 12 and len(new_msg) < 50):
                parts = str(new_msg).split(',')
                print(parts)
                #si la salida del split es mayor a dos, el mensaje esta completa
                if len(parts) > 2:
                    lec = LecturaTempHume()
                    #cambiar el estado del sensor de temperatura a ON
                    if md > 1 :
                        mmdl = Module()
                        mmdl.s_temperatura = 'ON'
                        mmdl.s_humedad = 'ON'

                        mmdl.save()


                    for x in range(0, len(parts) - 1):
                        if parts[x][0].__eq__('d'):
                            lec.modulo = str(parts[x][1:])
                            modd = int(parts[x][1:])

                        elif parts[x][0].__eq__('t'):
                            lec.temperatura = parts[x][1:]
                            temm = int(float(parts[x][1:]))

                        elif parts[x][0].__eq__('h'):
                            lec.humedad = parts[x][1:]
                            humm = int(float(parts[x][1:]))



                    try:
                        print(modd, temm, humm)
                        if(temm <10):
                            temm = temm/1
                        sent_req = requests.get('https://forest-vigilance-rd.herokuapp.com/interface/datos/%d/%d/%d' %(modd, temm, humm))
                        print(sent_req)
                    except:
                        lec.save()
                        pass



            elif len(new_msg) > 1000:
                foto = new_msg  #ser.readall()

                print(len(foto), foto, '78')

                filename = str(uuid.uuid4()) + '.png'

                print(filename, 'aki')
                with open(filename, 'wb') as f:
                    f.write(base64.b64decode(foto))
                    time.sleep(2)
                    noti = Alertas()

                    noti.modulo = 1001
                    while len(ser.read()) < 1:
                        tipo = ser.read()
                        print('tipo is:', str(tipo))
                    if int(str(ser.readall())[2:3]) == 1:
                        print('sound')
                        noti.modulo = 'Sound'
                        idd = 1
                    elif int(str(ser.readall())[2:3]) == 2:
                        print('humo')
                        noti.Tipo = 'Humo'
                        idd = 2
                    elif int(str(ser.readall())[2:3]) == 3:
                        print('sensor failed')
                        noti.Tipo = 'Sensor Temp/Humedad failed'
                        idd = 3
                        #     mm = Module()
                        #     mm.s_humedad = 'OUT'
                        #     mm.s_temperatura = 'OUT'
                        #     mm.save()
                        #     md = 0
                    else:
                        print('unknown')
                    noti.alert_image = 'photos/%s' %(filename)
                try:
                    #sendmail.sensorFailmsg('jfco2058@gmail.com', str(new_msg))
                    #
                    # noti = Alertas()
                    #
                    # noti.modulo = 1001
                    #
                    # if new_msg[0].__eq__('S'):
                    #
                    #     noti.Tipo = 'Sonido'
                    #     id = 1
                    # elif new_msg[0].__eq__('H'):
                    #
                    #     noti.Tipo = 'Humo'
                    #     id = 2
                    #
                    # else:
                    #     noti.Tipo = 'Sensor Temp/Humedad failed'
                    #     id = 3
                    #     mm = Module()
                    #     mm.s_humedad = 'OUT'
                    #     mm.s_temperatura = 'OUT'
                    #     mm.save()
                    #     md = 0
                    #
                    # noti.save()


                    not_req = requests.get('https://forest-vigilance-rd.herokuapp.com/interface/notifications/%d/%d/%s' % (modd, idd, foto))
                    print(not_req)
                except:
                    noti.save()
                    # pass
            ser.flush()
            #time.sleep(4)
    except Exception as ex:
        print(ex.args)
        time.sleep(3)
        main(connection())




if ( __name__ == "__main__"):
    main(connection())
