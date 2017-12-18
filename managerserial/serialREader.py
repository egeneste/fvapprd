#!/usr/bin/env python
import serial, sys, django, os
import time, requests
sys.path.append('C:/Users/EGeneste')#sys.path.append('E:/proyects')
os.environ["DJANGO_SETTINGS_MODULE"] = 'fvapprd.settings'
django.setup()
from interface.models import LecturaTempHume, Alertas, Module
from managerserial import sendmail
def connection():
    try:
        ser = serial.Serial('COM16', 9600, timeout=1)
        return ser
    except Exception as ex:
        print('con fail')
        time.sleep(3)
        connection()


def main(ser):
    modd = 0
    temm = 0
    humm = 0
    md = 1
    try:
        ser.close()
        ser.open()
        #k = ser.read_all()
        while ser.is_open:
            new_msg = ser.readall()
            print(len(new_msg), 'len')
            if (len(new_msg) > 12):
                parts = str(new_msg).split(',')
                print(parts)

                if len(parts) > 2:
                    lec = LecturaTempHume()

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

                    lec.save()

                    try:
                        print(modd, temm, humm)
                        if(temm <10):
                            temm = temm/1
                        sent_req = requests.get('https://forest-vigilance-rd.herokuapp.com/interface/datos/%d/%d/%d' %(modd, temm, humm))
                        print(sent_req)
                    except:
                        pass



                else:
                    try:

                        #sendmail.sensorFailmsg('jfco2058@gmail.com', str(new_msg))

                        noti = Alertas()

                        noti.modulo = 1001

                        if new_msg[0].__eq__('S'):

                            noti.Tipo = 'Sonido'
                            id = 1
                        elif new_msg[0].__eq__('H'):

                            noti.Tipo = 'Humo'
                            id = 2

                        else:
                            noti.Tipo = 'Sensor Temp/Humedad failed'
                            id = 3
                            mm = Module()
                            mm.s_humedad = 'OUT'
                            mm.s_temperatura = 'OUT'
                            mm.save()
                            md = 2

                        noti.save()

                        not_req = requests.get('https://forest-vigilance-rd.herokuapp.com/interface/notifications/%d/%d' % (modd, id))
                        print(not_req)
                    except:
                        pass
            ser.flush()
            #time.sleep(4)
    except Exception as ex:
        print(ex.args)
        time.sleep(3)
        main(connection())




if ( __name__ == "__main__"):
    main(connection())
