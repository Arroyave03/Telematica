# Mapa SIATA
## Instrucciones
1. clona el repositorio de github
```bash
git clone https://github.com/Arroyave03/Telematica.git
```

2. utiliza el comando ``ifconfig`` o ``ip address`` para observar la direccion IP del equipo

  Ejemplo ifconfig
  ```bash
  eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 172.24.35.90  netmask 255.255.240.0  broadcast 172.24.47.255
        inet6 fe80::215:5dff:fee3:3cad  prefixlen 64  scopeid 0x20<link>
        ether 00:15:5d:e3:3c:ad  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 7  bytes 586 (586.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
  ```
  en este caso debemos utilizar la direccion ``172.24.35.90``

  Ejemplo ip address
  ```bash
  2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP group default qlen 1000
    link/ether 00:15:5d:e3:3c:ad brd ff:ff:ff:ff:ff:ff
    inet 172.24.35.90/20 brd 172.24.47.255 scope global eth0
       valid_lft forever preferred_lft forever
    inet6 fe80::215:5dff:fee3:3cad/64 scope link
       valid_lft forever preferred_lft forever
  ```
  en este caso debemos utilizar la direccion ``172.24.35.90``

  3. ahora modificamos web.py sustituyendo los host a la direccion IP que obtuvimos con el comando anterior, para este ejemplo usaremos 172.24.35.90 que fue la IP obtenida en el caso anterior, para desplegarlo en otro equipo se debe remplazar por la direccion obtenida en el comando anterior

   Linea 10
  ```python
  dataFrame = pd.read_json('http://172.24.35.90:5000',convert_dates=True)
  ```

  Linea 43
  ```python
  users = pd.read_json('http://172.24.35.90:5001',convert_dates=True)
  ```

  4. Ahora ejecutamos el script ``setup.sh``, este bash script realizara el resto de los pasos necesarios e iniciara los contenedores

  5. Una vez termine de ejecutarse el script podemos realizar una prueba con la direccion IP en el puerto 80

  
