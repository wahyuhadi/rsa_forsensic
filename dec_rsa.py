#mencari nilai private key menggunakan fungsi eucledian

def eucledian(e, phi):
    #membuat nilai variable sementara

    d = 0
    a = 0
    b = 1
    c = 1
    sementara_phi = phi
    
    while e > 0:
        sementara1 = sementara_phi/e
        sementara2 = sementara_phi - sementara1 * e
        sementara_phi = e
        e = sementara2
        
        x = b- sementara1* a
        y = d - sementara1 * c
        
        b = a
        a = x
        d = c
        c = y
    
    if sementara_phi == 1:
        return d + phi
#mencari nilai bilangan prima dari nilai 1 sampa n (dimana nilai n = p * q)
def BilanganPrima(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in xrange(3, int(num**0.5)+2, 2):
        if num % n == 0:
            return False
    return True
#memasukan kunci
def kunci(p, q):
    #jika nilai yang di inputkan bukan bilangan prima 
    if not (BilanganPrima(p) and BilanganPrima(q)):
        raise ValueError('Harus Bilangan Prima ')
    #jika nilai yang di inputkan sama 

    elif p == q:
        raise ValueError('Tidak Boleh Sama ')
    #n = pq
    n = p * q

   
    phi = (p-1) * (q-1)
    #memasukan nilai bilangan prima dari 1 sampai n ke sabuah array 
    data = []
    for i in range(0,n):
        if BilanganPrima(i) == True:
            data.append(i)
    print ("Pilih Nilai E dari bilangan Prima di bawah ini \n ")
    #mendapatkan nilai d (private)
    print(data)
    e = input("Masukan Nilai e : ")
    d = eucledian(e, phi)
    return ((e, n), (d, n))

#fungsi decrypt
def decrypt(pk, ciphertext):
    key, n = pk
    print "Kunci : ",key
    print "n : ",n
    #melakukan parsing setiap huruf yang di inputkan 
    for char in ciphertext:
        a = (char**key) % n
        print "Hasil Decrypt : ",char,"**",key," mod ",n," = ",a

    plain = [chr((char ** key) % n) for char in ciphertext]

    print "Plain Decrypt : ",
    return ''.join(plain)
    
    
if __name__ == '__main__':
    p = input("masukan Nilai P : " )
    q = input("Masukan Nilai q : ")
    public, private = kunci(p, q)
    print "Public Key ", public , "private key ", private
    pesan = input("Masukan pesan yang akan di decryp : ")
    print decrypt(private,pesan)
