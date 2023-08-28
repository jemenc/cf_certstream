# CertStream

[**Certificate Transparency Logs**](https://certificate.transparency.dev/), es una herramienta [**OSINT**](https://www.arimetrics.com/glosario-digital/osint-open-source-intelligence) que nos permite acceder a la informacion de los certificados SSL que tienen un estatus de preaprobacion, lo que quiere decir que su informacion puede ser diferente una vez el certificado SSL sea puesto en funcionamiento, pero que nos permite, y este es uno de sus posibles usos, idenficicar urls maliciosas que pretendan suplantar urls officiales por medio del [*Typosquatting*](https://latam.kaspersky.com/resource-center/definitions/what-is-typosquatting), antes de que las mismas esten en funcionamiento o ya se encuentren online.

El modulo de Certstram, proporcionado por la empresa [Cali Dog Security](https://calidog.io/), es un modulo que nos permite tener acceso a este flujo de datos, del cual se basa nuestro proyecto.

_____________________________________________________________________________________________________________________

# Organizacion del proyecto

* CERTSTREAM

	* certstream
		* cli.py
		* core.py
	* decorators
		* decorators.py	 
	* load_keywords
		* keywords.py
		* keywords.csv
		* load_keywords.py 
	* load_stack
		* stack.py 
	* phishing_report
		* save_results.py	 
	* utils
		* comparations.py	 
	* main.py

______________________________________________________________________________________________________________________

# Uso
    
Para el uso simplemente temos que correr el script main.py que se encuentra en la carpetra principal del correo, una vez alli, se observara el flujo de informacion proveniente de los certificados de seguridad 

![image](https://github.com/jemenc/cf_certstream/assets/59877687/aeb140f4-fa50-49d1-a1a4-64490401bd44)
