#!/usr/bin/env python
# -*- coding: utf-8 -*-

######################################################
###                                                ###         
###        Shodan3r V.:1.0                         ###
###             by                                 ###
###            n3x07                               ###
###                                                ###
###     www.netc0de.blogspot.com                   ###
###           07/01/2013                           ###
###                                                ###
###  Requiere: shodan                              ###
###  easy_install shodan                           ###
###  Testeado en Debian Wheezy con Python 2.7.x    ### 
###                                                ###
######################################################

from shodan import WebAPI
import re


class Shodan:
    """ Clase para buscar en Shodan """
    def __init__(self,API_KEY):
        self.api =  WebAPI(API_KEY)    

    def buscar(self,cadena):
        """ Busca segun la cadena dada """
        try:
           # Buscamos lo de la cadena pasada como parametro
	   resultado = self.api.search(str(cadena))
	   return resultado
        except Exception as e:
	   print 'Ups! Ha ocurrido un error: %s' % e
	   resultado = []
	   return resultado

        
    def obtener_info_host(self,IP):
        """ Obtiene la info que pueda tener shodan sobre una IP """
        try:
	    host = self.api.host(IP)
	    return host
	except Exception as e:
	    print 'Ups! Ha ocurrido un error: %s' % e
	    host = []
	    return host	    


def usage():
    print """Uso: Shodan3r.py {OPTION} {CADENA | HOST}
     OPCIONES:
      -s, --search: Para buscar segun una determinada cadena
      -h, --host: Para obtener la informacion de un host segun su IP
     EJEMPLOS
      Shodan3r.py -s apache
      Shodan3r.py -h 8.8.8.8"""

def banner():
    	print """
		 ____  _               _             _____      
                / ___|| |__   ___   __| | __ _ _ __ |___ / _ __ 
                \___ \| '_ \ / _ \ / _` |/ _` | '_ \  |_ \| '__|
                 ___) | | | | (_) | (_| | (_| | | | |___) | |   
                |____/|_| |_|\___/ \__,_|\__,_|_| |_|____/|_|
		                                  Version 1.0
	""" 

def main():
    import sys
    import time

    API_KEY = 'API KEY AQUI'
    shodan = Shodan(API_KEY)
    if len(sys.argv) < 3:
        usage()
	sys.exit(2)
    else:
        if sys.argv[1] == '-s' or sys.argv[1] == '--search':
             banner()
	     time.sleep(3)
             resultado = shodan.buscar(sys.argv[2])
	     if len(resultado) != 0:
	         print 'Cantidad de resultados encontrados: %s' % resultado['total']
		 for i in resultado['matches']:
		     print 'Ciudad: %s' % i.get('city','Unknown')
		     print 'Pais: %s' % i.get('country_name','Unknown')
		     print 'IP: %s' % i.get('ip')
		     print 'O.S: %s' % i.get('os','Unknown')
		     print 'Puerto: %s' % i.get('port')
		     print 'Hostnames: %s' % i.get('hostnames')
		     print 'Latitude: %s' % i.get('latitude','Unknown')
		     print 'Longitude: %s' % i.get('longitude','Unknown')
		     print 'Actualizado en: %s' % i.get('updated')
		     print i['data']
		     print ''
		     
	elif sys.argv[1] == '-h' or sys.argv[1] == '--host':
            banner()
	    time.sleep(3)
            host = shodan.obtener_info_host(sys.argv[2])
	    if len(host) != 0:
		    # Imprimiendo la informacion obtenida
	  	    print 'IP: %s' % host.get('ip')
	   	    print 'Pais: %s' % host.get('country_name','Unknown')
	  	    print 'City: %s' % host.get('city','Unknown')
	   	    print 'Latitude: %s' % host.get('latitude')
	   	    print 'Longitude: %s' % host.get('longitude')
	   	    print 'Hostnames: %s' % host.get('hostnames')
	       	    # Imprimimos los banners
	   	    for i in host['data']:
		  	   print 'Puerto: %s' % i['port']
		  	   print 'Banner: %s' % i['banner']
			   print ''
			   
	else:
	    usage()
	    sys.exit(2)

if __name__ == '__main__':
    main()
