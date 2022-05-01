#!/user/bin/env python3
# -*- coding: utf-8 -*-

import OpenSSL,ssl,socket,sslsocket
import time
from dateutil import parser

hostname = 'www.mmup.cn'
port = 443
context = ssl.SSLContext(sslsocket.PROTOCOL_TLS)

cert_s = sslsocket.get_server_certificate((hostname, port)).encode()

print(cert_s)
cert = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert_s)
# certIssue = cert.get_issuer()

print(cert_s)
datetime_struct = parser.parse(cert.get_notBefore().decode("UTF-8"))
print ("有效期从:             ",datetime_struct.strftime('%Y-%m-%d'))
datetime_struct = parser.parse(cert.get_notAfter().decode("UTF-8"))
print ("到:                   ",datetime_struct.strftime('%Y-%m-%d'))
print ("证书是否已经过期:      ",cert.has_expired())
