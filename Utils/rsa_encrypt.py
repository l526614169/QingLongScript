#!/usr/bin/python3
# -- coding: utf-8 --
# -------------------------------
# @Author : github@limoruirui https://github.com/limoruirui
# @Time : 2022/8/23 13:05
# -------------------------------
from Crypto.PublicKey.RSA import importKey, construct
from Crypto.Cipher import PKCS1_v1_5
from base64 import b64encode


def public_key(rsaExponent, rsaModulus=10001):
    e = int(rsaExponent, 16)
    n = int(rsaModulus, 16)  # snipped for brevity
    pubkey = construct((n, e)).export_key()
    return pubkey


class RSA_Encrypt:
    def __init__(self, key):
        if isinstance(key, str):
            # 若提供的rsa公钥不为pem格式 则先将hex转化为pem格式
            # self.key = bytes.fromhex(key) if "PUBLIC KEY" not in key else key.encode()
            self.key = public_key(key) if "PUBLIC KEY" not in key else key.encode()
        else:
            print("提供的公钥格式不正确")

    def encrypt(self, data, b64=False):
        pub_key = importKey(self.key)
        cipher = PKCS1_v1_5.new(pub_key)
        rsa_text = cipher.encrypt(data.encode("utf8"))
        rsa_text = b64encode(rsa_text).decode() if b64 else rsa_text.hex()
        return rsa_text
