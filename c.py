
def send_msg ():
    text =   input("input message : ")
    key = int(input("input key : "))
    hasil = ""

    mod_key = key % 26

    alfabeth = list("abcdefghijklmnopqrstuvwxyz")
    d = alfabeth[mod_key:] + alfabeth[:mod_key]
    for huruf in text :
        if huruf in alfabeth:
            pos = alfabeth.index(huruf)
            hasil += (d[pos],mod_key)
        else:
            hasil += huruf
    return hasil
    
def recv_msg(pesan):
    text, key = pesan # pesan var sementara 

    alfabeth = list("abcdefghijklmnopqrstuvwxyz")
    d = alfabeth[-key:] + alfabeth[:-key]
    dekrip = ""
    for huruf in text :
        pos = d.index(huruf)
        dekrip += (alfabeth[pos])
        
    return dekrip




#def decode_msg()
    #rs = clin.recv(2048).decode(FORMAT)
    
