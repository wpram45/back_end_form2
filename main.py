# -*- coding: utf-8 -*-


#dependencies at below

#pip install -U flask-cors

from flask import Flask,jsonify,make_response,request

from flask_cors import CORS, cross_origin
from  flask_mysqldb import MySQL
from collections import OrderedDict 
import random
import json
app = Flask(__name__)

app.config['MYSQL_USER'] = 'wpram45'
app.config['MYSQL_PASSWORD'] = 'serif4545'
app.config['MYSQL_DB'] = 'tez_oneri_formu'
app.config['MYSQL_HOST'] = 'localhost'


mysql = MySQL(app)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'



#geri değer döndürme

#form 31 sıkıntılı

 # data = {'message': 'Created', 'code': 'SUCCESS'}
    #return make_response(jsonify(data), 200)






#sorgu ogrenci noya göre
#select * from form30 where 
# user_id=( select id from ogrenciBilgileri where ogrenciNo=342667);


#ornek get http://127.0.0.1:5000/form34?ogrencino=342667


@app.route('/form33',methods=['GET'])

def form33():

    ogrenci_no=request.args.get("ogrencino")
    
    form34_sql="select *  from form33 where user_id IN (select id from ogrenciBilgileri where ogrenciNo=%s)"
    
    cursor = mysql.connection.cursor()
    kontrol = cursor.execute(form34_sql,(ogrenci_no,))
    sonuc={}
   
    if kontrol > 0:
        data = cursor.fetchone()
        #print("tuple",data)
        for i in range(len(data)):
            sonuc[i]=str(data[i])

        
   

       # beyanBelge = data["fikirBeyanBelge"]
    else:
        print("Kayıt bulunamadı!")

    #print("veri belge",veriBelge)
    #print("beyan belge",beyanBelge)
    #cursoru kapat
    cursor.close()
    print("sonuc",sonuc)
    return sonuc





#form 31 get

@app.route('/form31',methods=['GET'])

def form31():

    ogrenci_no=request.args.get("ogrencino")
    
    form34_sql="select *  from form31 where user_id IN (select id from ogrenciBilgileri where ogrenciNo=%s)"
    
    cursor = mysql.connection.cursor()
    kontrol = cursor.execute(form34_sql,(ogrenci_no,))
    sonuc={}
   
    if kontrol > 0:
        data = cursor.fetchone()
        #print("tuple",data)
        for i in range(len(data)):
            sonuc[i]=str(data[i])

        
   

       # beyanBelge = data["fikirBeyanBelge"]
    else:
        print("Kayıt bulunamadı!")

    #print("veri belge",veriBelge)
    #print("beyan belge",beyanBelge)
    #cursoru kapat
    cursor.close()
    print("sonuc",sonuc)
    return sonuc









#ogrenci bilgileri 

@app.route('/ogrbilgi',methods=['GET'])

def ogrbilgi():
    ogrenci_no=request.args.get("ogrencino")
    
    ogr_sql="SELECT * FROM ogrenciBilgileri WHERE ogrenciNo=%s"
    
    cursor = mysql.connection.cursor()
    kontrol = cursor.execute(ogr_sql,(ogrenci_no,))
    sonuc={}
   
    if kontrol > 0:
        data = cursor.fetchone()
        #print("tuple",data)
        for i in range(len(data)):
            sonuc[i]=str(data[i])

        
   

       # beyanBelge = data["fikirBeyanBelge"]
    else:
        print("Kayıt bulunamadı!")

    #print("veri belge",veriBelge)
    #print("beyan belge",beyanBelge)
    #cursoru kapat
    cursor.close()
    print("sonuc",sonuc)
    return sonuc





@app.route('/form34',methods=['GET'])
def  form34():
    

    ogrenci_no=request.args.get("ogrencino")
    
    form34_sql="select *  from form30 where user_id IN (select id from ogrenciBilgileri where ogrenciNo=%s)"
    
    cursor = mysql.connection.cursor()
    kontrol = cursor.execute(form34_sql,(ogrenci_no,))
    sonuc={}
   
    if kontrol > 0:
        data = cursor.fetchone()
        #print("tuple",data)
        for i in range(len(data)):
            sonuc[i]=str(data[i])

        
   

       # beyanBelge = data["fikirBeyanBelge"]
    else:
        print("Kayıt bulunamadı!")

    #print("veri belge",veriBelge)
    #print("beyan belge",beyanBelge)
    #cursoru kapat
    cursor.close()
    print("sonuc",sonuc)
    return sonuc
    





@app.route('/',methods = ['POST'])
def main():
    

    

    gelen_data=request.form.to_dict()
   # print("json istedigin",gelen_data)
    #ornek olarak calismaAlanina yazdir
   # print(gelen_data["calismaAlan"])
    

    #write to database

  
   
    
    return  writeToDatabase(gelen_data)
    


   # return gelen_data

     
    
    
   # response = jsonify({'some': 'data'})
    
   # return response


  

def writeToDatabase(gelenData):

    
    columns=[]
    values=[]
    for k in gelenData.keys():
         
         print(k,":",gelenData[k])

    #split keys by [] to remove "[] symbols" and add them to columns array
    #and we can use columns array to add database
    for key in gelenData.keys():
      #  print("sliced key",key.split("[]"))
        columns.append(key.split("[]")[0])


    #add values in gelenData  to values array
    for k in gelenData:
        #print("key",k,"value :",gelenData[k])
        values.append(gelenData[k])
    
   # print("values array",values)
   # print("columns array",columns)
    # return this function to prevent sql insert error
    form_adi=gelenData["formAdi"]
  
    
    if form_adi=="Form30":
        try:

            ad=gelenData["ad"] #ogrenci bilgileri
            soyad=gelenData["soyad"]  #ogrenci bilgileri
            ogrenciNo=gelenData["ogrenciNo"]  #ogrenci bilgileri
            danismanad=gelenData["danismanad"]  #ogrenci bilgileri
            danismansoyad=gelenData["danismansoyad"] #ogrenci bilgileri
            calismatarzi=gelenData["calismatarzi"]  #form30 ama değer yanlış geliyor
            anaBilimdali=gelenData["anaBilimdali"]  #form30
            oybirligi=gelenData["oybirligi"]    #form30
            oybirligi1=gelenData["oybirligi1"]  #form30
            oybirligi2=gelenData["oybirligi2"]  #form30
            kabul=gelenData["kabul"]  #form30
            bilimdali=gelenData["bilimdali"]  #ogrenci bilgileri
            gerekce=gelenData["gerekce"]  #form30
            ilkteklifdegisiklik=gelenData["ilkteklifdegisiklik"] #form30
            turkcetezbasligi=gelenData["turkcetezbasligi"]  #form30
            anahtarkelimeler=gelenData["anahtarkelimeler"]  #form30
            ingilizcetezbasligi=gelenData["ingilizcetezbasligi"] #form30
            endustrialaniA=gelenData["endustrialaniA"] #form30
            endustrialaniB=gelenData["endustrialaniB"] #form30 
            fikirhaksay= gelenData["fikirhaksay"] if "fikirhaksay" in gelenData.keys() else ""
            veriKullanimsay=gelenData["veriKullanimsay"] if "veriKullanimsay" in gelenData.keys() else ""
            etikKurulsay=gelenData["etikKurulsay"] if "etikKurulsay" in gelenData.keys() else ""
            kurumizinsay=gelenData["kurumizinsay"] if "kurumizinsay" in gelenData.keys() else ""
            ogrenciderstamamlama=0 # veritabanında alan yok
            if ("ogrenciderstamamlama" in gelenData.keys()):
                ogrenciderstamamlama=gelenData["ogrenciderstamamlama"]

            dilSecim=gelenData["dilSecim"] #form30
            kurumizinsay=gelenData["kurumizinsay"]  #formdan değer gelmiyor form30 tablosunda alan var

            #random user id generator
            user_id=random.randint(1,9959959)

            #sorgu30 -> form 30 tablosuna yazar.
            sorgu30 = "INSERT INTO form30  VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            
            #ogrenci bilgileri sorgusu
            ogrenci_bilgileri="INSERT INTO ogrenciBilgileri  VALUES(%s,%s,%s,%s,%s,%s,%s)"
    
            
            cursor = mysql.connection.cursor()
            cursor.execute(ogrenci_bilgileri,(user_id,ad,soyad,ogrenciNo,bilimdali,danismanad,danismansoyad))
            mysql.connection.commit()
            cursor.close()
        #  sorgu30_2="INSERT INTO form30  VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            

          


            cursor = mysql.connection.cursor()
            cursor.execute(sorgu30,(user_id,oybirligi,oybirligi1,oybirligi2,kabul,
            anaBilimdali,ilkteklifdegisiklik,
            gerekce,turkcetezbasligi,anahtarkelimeler,
            ingilizcetezbasligi,dilSecim,calismatarzi,endustrialaniA,endustrialaniB,
            0,etikKurulsay,0,veriKullanimsay
             ,0,kurumizinsay,0,fikirhaksay,0))
            mysql.connection.commit()
            cursor.close()



            print("form db ye eklendi,basarili")
            data = {'dilSecim':dilSecim}

            return make_response(jsonify(data), 200)

            
            
          
            


      #form 31'in ajaxını değiştirince bozuluyor      


        except Exception as ex:
            print(" form 30'da  hata :",ex)






    elif form_adi=="Form31":
        #radio16=cevap16
        try:
            
            user_id=random.randint(1,679959959)
            tezTurkce= gelenData["tezTurkce"] if "tezTurkce" in gelenData.keys() else ""
            tezIngilizce= gelenData["tezIngilizce"] if "tezIngilizce" in gelenData.keys() else ""
            tezamac=gelenData["tezamac"] if "tezamac" in gelenData.keys() else ""
            tezTanim=gelenData["tezTanim"] if "tezTanim" in gelenData.keys() else ""
            tezHipotez=gelenData["tezHipotez"] if "tezHipotez" in gelenData.keys() else ""
            tezMotivasyon=gelenData["tezMotivasyon"] if "tezMotivasyon" in gelenData.keys() else ""
            konudetay=gelenData["konudetay"] if "konudetay" in gelenData.keys() else ""
            kaynak1=gelenData["kaynak1"] if "kaynak1" in gelenData.keys() else ""
            kaynak1Tarih=gelenData["kaynak1Tarih"] if "kaynak1Tarih" in gelenData.keys() else ""
            kaynak2=gelenData["kaynak2"] if "kaynak2" in gelenData.keys() else ""
            kaynak2Tarih=gelenData["kaynak2Tarih"] if "kaynak2Tarih" in gelenData.keys() else ""
            kaynak3=gelenData["kaynak3"] if "kaynak3" in gelenData.keys() else ""
            kaynak3Tarih=gelenData["kaynak3Tarih"] if "kaynak3Tarih" in gelenData.keys() else ""
            kaynak4=gelenData["kaynak4"] if "kaynak4" in gelenData.keys() else ""
            kaynak4Tarih=gelenData["kaynak4Tarih"] if "kaynak4Tarih" in gelenData.keys() else ""
            kaynak5=gelenData["kaynak5"] if "kaynak5" in gelenData.keys() else ""
            kaynak5Tarih=gelenData["kaynak5Tarih"] if "kaynak5Tarih" in gelenData.keys() else ""
            kaynak6=gelenData["kaynak6"] if "kaynak6" in gelenData.keys() else ""
            kaynak6Tarih=gelenData["kaynak6Tarih"] if "kaynak6Tarih" in gelenData.keys() else ""
            kaynak7=gelenData["kaynak7"] if "kaynak7" in gelenData.keys() else ""
            kaynak7Tarih=gelenData["kaynak7Tarih"] if "kaynak7Tarih" in gelenData.keys() else ""
            kaynak8=gelenData["kaynak8"] if "kaynak8" in gelenData.keys() else ""
            kaynak8Tarih=gelenData["kaynak8Tarih"] if "kaynak8Tarih" in gelenData.keys() else ""
            kaynak9=gelenData["kaynak9"] if "kaynak9" in gelenData.keys() else ""
            kaynak9Tarih=gelenData["kaynak9Tarih"] if "kaynak9Tarih" in gelenData.keys() else ""
            kaynak10=gelenData["kaynak10"] if "kaynak10" in gelenData.keys() else ""
            kaynak10Tarih=gelenData["kaynak10Tarih"] if "kaynak10Tarih" in gelenData.keys() else ""
            kaynak11=gelenData["kaynak11"] if "kaynak11" in gelenData.keys() else ""
            kaynak11Tarih=gelenData["kaynak11Tarih"] if "kaynak11Tarih" in gelenData.keys() else ""
            kaynak12=gelenData["kaynak12"] if "kaynak12" in gelenData.keys() else ""
            kaynak12Tarih=gelenData["kaynak12Tarih"] if "kaynak12Tarih" in gelenData.keys() else ""
            kaynak13=gelenData["kaynak13"] if "kaynak13" in gelenData.keys() else ""
            kaynak13Tarih=gelenData["kaynak13Tarih"] if "kaynak13Tarih" in gelenData.keys() else ""
            kaynak14=gelenData["kaynak14"] if "kaynak14" in gelenData.keys() else ""
            kaynak14Tarih=gelenData["kaynak14Tarih"] if "kaynak14Tarih" in gelenData.keys() else ""
            kaynak15=gelenData["kaynak15"] if "kaynak15" in gelenData.keys() else ""
            kaynak15Tarih=gelenData["kaynak15Tarih"] if "kaynak15Tarih" in gelenData.keys() else ""
            literatur=gelenData["literatur"] if "literatur" in gelenData.keys() else ""
            yontemBolum=gelenData["yontemBolum"] if "yontemBolum" in gelenData.keys() else ""
            ozgun=gelenData["ozgun"] if "ozgun" in gelenData.keys() else ""
            kurum=gelenData["kurum"] if "kurum" in gelenData.keys() else ""
            aciklama=gelenData["aciklama[]"] if "aciklama[]" in gelenData.keys() else ""
            baslama=gelenData["baslama[]"] if "baslama[]" in gelenData.keys() else ""
            bitis=gelenData["bitis[]"] if "bitis[]" in gelenData.keys() else ""
            radio=gelenData["radio"] if "radio" in gelenData.keys() else ""
            radio1=gelenData["radio1"] if "radio1" in gelenData.keys() else ""
            radio2=gelenData["radio2"] if "radio2" in gelenData.keys() else ""
            radio4=gelenData["radio4"] if "radio4" in gelenData.keys() else ""
            radio5=gelenData["radio5"] if "radio5" in gelenData.keys() else ""
            radio6=gelenData["radio6"] if "radio6" in gelenData.keys() else ""
            radio7=gelenData["radio7"] if "radio7" in gelenData.keys() else ""
            radio8=gelenData["radio8"] if "radio8" in gelenData.keys() else ""
            radio9=gelenData["radio9"] if "radio9" in gelenData.keys() else ""
            radio10=gelenData["radio10"] if "radio10" in gelenData.keys() else ""
            radio11=gelenData["radio11"] if "radio11" in gelenData.keys() else ""
            radio12=gelenData["radio12"] if "radio12" in gelenData.keys() else ""
            radio13=gelenData["radio13"] if "radio13" in gelenData.keys() else ""
            radio14=gelenData["radio14"] if "radio14" in gelenData.keys() else ""
            radio15=gelenData["radio15"] if "radio15" in gelenData.keys() else ""
            radio16=gelenData["radio16"] if "radio16" in gelenData.keys() else ""
            calismaAlan=gelenData["calismaAlan"] if "calismaAlan" in gelenData.keys() else ""
            destekleyenKurum=gelenData["destekleyenKurum"] if "destekleyenKurum" in gelenData.keys() else ""
            ikinciDanisman=gelenData["ikinciDanisman"] if "ikinciDanisman" in gelenData.keys() else ""
            tezDisiplin=gelenData["tezDisiplin"] if "tezDisiplin" in gelenData.keys() else ""
            ticariUrun=gelenData["ticariUrun"] if "ticariUrun" in gelenData.keys() else ""
            calismaLab=gelenData["calismaLab"] if "calismaLab" in gelenData.keys() else ""
            patentalinmasi=gelenData["patentalinmasi"] if "patentalinmasi" in gelenData.keys() else ""
            destek=gelenData["destek"] if "destek" in gelenData.keys() else ""
            ogrenciadi=gelenData["ogrenciadi"] if "ogrenciadi" in gelenData.keys() else ""
            ogrencisoyad=gelenData["ogrencisoyad"] if "ogrencisoyad" in gelenData.keys() else ""
            ogrencinumara=gelenData["ogrencinumara"] if "ogrencinumara" in gelenData.keys() else ""
            bilimdali=gelenData["bilimdali"] if "bilimdali" in gelenData.keys() else ""
            danismanad=gelenData["danismanad"] if "danismanad" in gelenData.keys() else ""
            danismansoyad=gelenData["danismansoyad"] if "danismansoyad" in gelenData.keys() else ""
            anabilimdali=gelenData["anabilimdali"] if "anabilimdali" in gelenData.keys() else ""
            yaygin=gelenData["yaygin"] if "yaygin" in gelenData.keys() else ""

            cursor = mysql.connection.cursor()
            sorgu1="INSERT INTO form31 VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

            cursor.execute(sorgu1,(user_id,
                        radio16,
                        tezamac,
                        tezTanim,
                        tezHipotez,
			            tezMotivasyon,
			            konudetay,
			            literatur,
			            yontemBolum,
			            ozgun,
			            yaygin,
			            kurum))
            mysql.connection.commit()
            cursor.close()



            cursor = mysql.connection.cursor()
            sorgu3="INSERT INTO kaynaklar31 VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            
            cursor.execute(sorgu3,(
			            user_id,
                        kaynak1,
                        kaynak1Tarih,
                        kaynak2,
                        kaynak2Tarih,
                        kaynak3,
                        kaynak3Tarih,
                        kaynak4,
                        kaynak4Tarih,
                        kaynak5,
                        kaynak5Tarih,
                        kaynak6,
                        kaynak6Tarih,
                        kaynak7,
                        kaynak7Tarih,
                        kaynak8,
                        kaynak8Tarih,
                        kaynak9,
                        kaynak9Tarih,
                        kaynak10,
                        kaynak10Tarih,
                        kaynak11,
                        kaynak11Tarih,
                        kaynak12,
                        kaynak12Tarih,
                        kaynak13,
                        kaynak13Tarih,
                        kaynak14,
                        kaynak14Tarih,
                        kaynak15,
                        kaynak15Tarih))

            mysql.connection.commit()
            cursor.close()




            cursor = mysql.connection.cursor()

            sorgu4="INSERT INTO ogrenciBilgileri VALUES(%s,%s,%s,%s,%s,%s,%s)"

            cursor.execute(sorgu4,(
                        user_id,
                        ogrenciadi,
                        ogrencisoyad,
                        ogrencinumara,
                        bilimdali,
			            danismanad,
			            danismansoyad))
            mysql.connection.commit()
            cursor.close()




            cursor = mysql.connection.cursor()


            sorgu5="INSERT INTO secmeliSorular31 VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

            cursor.execute(sorgu5,(
			            user_id,
                       radio,
                        radio1,
                        radio2,
                        calismaLab,
			            radio4,
                        radio5,
                        destek,
                        radio6,
                        radio7,
                        radio8,
                        ticariUrun,
                        radio9,
                        patentalinmasi,
                        radio10,
                        radio11,
                        radio12,
                        tezDisiplin,
                        radio13,
                        ikinciDanisman,
                        radio14,
                        radio15,
                        destekleyenKurum,
                        calismaAlan))
			

            mysql.connection.commit()
            cursor.close()




            aciklama0=""
            baslama0=""
            bitis0=""
            aciklama1=""
            baslama1=""
            bitis1=""
            aciklama2=""
            baslama2=""
            bitis2=""
            aciklama3=""
            baslama3=""
            bitis3=""
            aciklama4=""
            baslama4=""
            bitis4=""
            aciklama5=""
            baslama5=""
            bitis5=""
            aciklama6=""
            baslama6=""
            bitis6=""
            aciklama7=""
            baslama7=""
            bitis7=""
            aciklama8=""
            baslama8=""
            bitis8=""
            aciklama9=""
            baslama9=""
            bitis9=""


            cursor = mysql.connection.cursor()
            

            
            sorgu2="INSERT INTO isPaketleri31 VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

            cursor.execute(sorgu2,(
			            user_id,
                        aciklama0,
                        baslama0,
                        bitis0,
                        aciklama1,
			            baslama1,
                        bitis1,
                        aciklama2,
                        baslama2,
                        bitis2,
                        aciklama3,
                        baslama3,
                        bitis3,
                        aciklama4,
                        baslama4,
                        bitis4,
                        aciklama5,
                        baslama5,
                        bitis5,
                        aciklama6,
                        baslama6,
                        bitis6,
                        aciklama7,
                        baslama7,
                        bitis7,
                        aciklama8,
                        baslama8,
                        bitis8,
                        aciklama9,
                        baslama9,
                        bitis9))
            mysql.connection.commit()
            cursor.close()

            print("db'ye başarıyla eklendi")
            data = {'message': 'Created', 'code': 'SUCCESS'}
            return make_response(jsonify(data), 200)
            




        except Exception as ex:
            print("form31'de hata",ex)


    
    elif form_adi=="Form32":
        try:
            user_id=random.randint(1,679959959)
            beyan=gelenData["message_pri"]
            sorgu32="INSERT INTO form32  VALUES(%s,%s)"

            cursor = mysql.connection.cursor()
            cursor.execute(sorgu32,(user_id,beyan))
            mysql.connection.commit()
            cursor.close()
            print("form 32 db'ye eklendi")
            data = {'message': 'Created', 'code': 'SUCCESS'}
            return make_response(jsonify(data), 200)
            

        except Exception as ex:
            print("form32'de hata",ex)

    elif form_adi=="form33":
        try:
            user_id=random.randint(1,679959959)
            toplantiyeri=str(gelenData["toplantiyeri"]) if "toplantiyeri" in gelenData.keys() else ""
            toplantitarihi=str(gelenData["toplantitarihi"]) if "toplantitarihi" in gelenData.keys() else ""
            toplantisaati=str(gelenData["toplantisaati"]) if "toplantisaati" in gelenData.keys() else ""
            abdbaskaniadi=gelenData["abdbaskaniadi"] if "abdbaskaniadi" in gelenData.keys() else ""
            abdbaskanisoyadi=gelenData["abdbaskanisoyadi"] if "abdbaskanisoyadi" in gelenData.keys() else ""
            ogrenciadi=gelenData["ogrenciadi"] if "ogrenciadi" in gelenData.keys() else ""
            ogrencisoyadi=gelenData["ogrencisoyadi"] if "ogrencisoyadi" in gelenData.keys() else ""
            ogrencino=gelenData["ogrencino"] if "ogrencino" in gelenData.keys() else ""
            ogrencikayittarihi=str(gelenData["ogrencikayittarihi"]) if "ogrencikayittarihi" in gelenData.keys() else ""
            birinciogretimuyesininadi=gelenData["birinciogretimuyesininadi"] if "birinciogretimuyesininadi" in gelenData.keys() else ""
            birinciogretimuyesininsoyadi=gelenData["birinciogretimuyesininsoyadi"] if "birinciogretimuyesininsoyadi" in gelenData.keys() else ""
            ikinciogretimuyesininadi=gelenData["ikinciogretimuyesininadi"] if "ikinciogretimuyesininadi" in gelenData.keys() else ""
            ikinciogretimuyesininsoyadi=gelenData["ikinciogretimuyesininsoyadi"] if "ikinciogretimuyesininsoyadi" in gelenData.keys() else ""
            ucuncuogretimuyesininadi=gelenData["ucuncuogretimuyesininadi"] if "ucuncuogretimuyesininadi" in gelenData.keys() else ""
            ucuncuogretimuyesininsoyadi=gelenData["ucuncuogretimuyesininsoyadi"] if "ucuncuogretimuyesininsoyadi" in gelenData.keys() else ""
            birinciogretimuyesininepostasi=gelenData["birinciogretimuyesininepostasi"] if "birinciogretimuyesininepostasi" in gelenData.keys() else ""
            tikuyeleritarih1=str(gelenData["tikuyeleritarih1"]) if "tikuyeleritarih1" in gelenData.keys() else ""
            ikinciogretimuyesininepostasi=gelenData["ikinciogretimuyesininepostasi"] if "ikinciogretimuyesininepostasi" in gelenData.keys() else ""
            tikuyeleritarih2=str(gelenData["tikuyeleritarih2"]) if "tikuyeleritarih2" in gelenData.keys() else ""
            ucuncuogretimuyesininepostasi=gelenData["ucuncuogretimuyesininepostasi"] if "ucuncuogretimuyesininepostasi" in gelenData.keys() else ""
            tikuyeleritarih3=str(gelenData["tikuyeleritarih3"]) if "tikuyeleritarih3" in gelenData.keys() else ""


            #olmayan degerler default  olarak '' set olacak

            programiniz=gelenData["programiniz"] if "programiniz" in gelenData.keys() else ""
            birinciogretimuyesininunvani=gelenData["birinciogretimuyesininunvani"] if "birinciogretimuyesininunvani" in gelenData.keys() else ""
            ikinciogretimuyesininunvani=gelenData["ikinciogretimuyesininunvani"] if "ikinciogretimuyesininunvani" in gelenData.keys() else ""
            ucuncuogretimuyesininunvani=gelenData["ucuncuogretimuyesininunvani"] if "ucuncuogretimuyesininunvani" in gelenData.keys() else ""
            birinciogretimuyesininkurumu=gelenData["birinciogretimuyesininkurumu"] if "birinciogretimuyesininkurumu" in gelenData.keys() else ""
            ikinciogretimuyesininkurumu=gelenData["ikinciogretimuyesininkurumu"] if "ikinciogretimuyesininkurumu" in gelenData.keys() else ""
            ucuncuogretimuyesininkurumu= gelenData["ucuncuogretimuyesininkurumu"] if "ucuncuogretimuyesininkurumu" in gelenData.keys() else ""
            bilimdali=gelenData["bilimdali"] if "bilimdali" in gelenData.keys() else ""
            danismanad=gelenData["danismanad"] if "danismanad" in gelenData.keys() else ""
            danismansoyad=gelenData["danismansoyad"] if "danismansoyad" in gelenData.keys() else ""
            abdbaskaniUnvani=gelenData["abdbaskaniUnvani"] if "abdbaskaniUnvani" in gelenData.keys() else ""


            cursor = mysql.connection.cursor()
            sorgu33="INSERT INTO form33 VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(sorgu33,(user_id,
                        toplantiyeri,
                        toplantitarihi,
                        toplantisaati,
                        abdbaskaniadi,
                        abdbaskanisoyadi,
                        abdbaskaniUnvani,
                        programiniz,
                        birinciogretimuyesininadi,
                        ikinciogretimuyesininadi,
                        ucuncuogretimuyesininadi,
                        birinciogretimuyesininsoyadi,
                        ikinciogretimuyesininsoyadi,
                        ucuncuogretimuyesininsoyadi,
                        birinciogretimuyesininunvani,
                        ikinciogretimuyesininunvani,
                        ucuncuogretimuyesininunvani,
                        birinciogretimuyesininkurumu,
                        ikinciogretimuyesininkurumu,
                        ucuncuogretimuyesininkurumu,
                        birinciogretimuyesininepostasi,
                        ikinciogretimuyesininepostasi,
                        ucuncuogretimuyesininepostasi,
                        tikuyeleritarih1,
                        tikuyeleritarih2,
                        tikuyeleritarih3))
          



            mysql.connection.commit()
            cursor.close()


            cursor = mysql.connection.cursor()
            ogrenci_bilgileri="INSERT INTO ogrenciBilgileri  VALUES(%s,%s,%s,%s,%s,%s,%s)"

            cursor.execute(ogrenci_bilgileri,(user_id,
                                    ogrenciadi,
                                  ogrencisoyadi,
                                  ogrencino,
                                  bilimdali,
                                  danismanad,
                                  danismansoyad))
            mysql.connection.commit()
            cursor.close()

            data = {'message': 'Created', 'code': 'SUCCESS'}
            return make_response(jsonify(data), 200)
            print("veritabanına basariyla kaydedildi")

            

        except Exception as ex:
            print("form33'de hata",ex)

        
    
    elif form_adi=="form34":
        try:    
            ogrencino=gelenData["ogrencino"] if "ogrencino" in gelenData.keys() else ""
            ogrenciadi=gelenData["ogrenciadi"] if "ogrenciadi" in gelenData.keys() else ""
            ogrencisoyadi=gelenData["ogrencisoyadi"] if "ogrencisoyadi" in gelenData.keys() else ""
            anabilimdali=gelenData["anabilimdali"] if "anabilimdali" in gelenData.keys() else ""
            ogrencisoyadi=gelenData["ogrencisoyadi"] if "ogrencisoyadi" in gelenData.keys() else ""
            kayittarihi=gelenData["kayittarihi"] if "kayittarihi" in gelenData.keys() else ""
            tezdanismani=gelenData["tezdanismani"] if "tezdanismani" in gelenData.keys() else ""
            turkcetezbasligi=gelenData["turkcetezbasligi"] if "turkcetezbasligi" in gelenData.keys() else ""
            anahtarkelime=gelenData["anahtarkelime"] if "anahtarkelime" in gelenData.keys() else ""
            ingilizcetezbasligi=gelenData["ingilizcetezbasligi"] if "ingilizcetezbasligi" in gelenData.keys() else ""
            endustrialaniA=gelenData["endustrialaniA"] if "endustrialaniA" in gelenData.keys() else ""
            endustrialaniB=gelenData["endustrialaniB"] if "endustrialaniB" in gelenData.keys() else ""
            savunmavekonudegisikligi=gelenData["savunmavekonudegisikligi"] if "savunmavekonudegisikligi" in gelenData.keys() else ""
            toplantiyeri=gelenData["toplantiyeri"] if "toplantiyeri" in gelenData.keys() else ""
            toplantitarihi=gelenData["toplantitarihi"] if "toplantitarihi" in gelenData.keys() else ""
            toplantisaati=gelenData["toplantisaati"] if "toplantisaati" in gelenData.keys() else ""
            retgerekcesi=gelenData["retgerekcesi"] if "retgerekcesi" in gelenData.keys() else ""
            oybirligi=gelenData["oybirligi"] if "oybirligi" in gelenData.keys() else ""
            oybirligicheck=gelenData["oybirligicheck"] if "oybirligicheck" in gelenData.keys() else ""
            degistirilentezbasligi=gelenData["degistirilentezbasligi"] if "degistirilentezbasligi" in gelenData.keys() else ""
            redKabul=gelenData["customCheck2"] if "customCheck2" in gelenData.keys() else ""





            sorgu4="INSERT INTO form34 VALUES(%s,%s,%s,%s,%s,%s)"
            cursor = mysql.connection.cursor()
            cursor.execute(sorgu4,(
                            ogrencino,
                            savunmavekonudegisikligi,
                            redKabul,
                            oybirligi,
                            retgerekcesi,
                            degistirilentezbasligi))
            
    
            mysql.connection.commit()
            cursor.close()
            print("veritabanına basariyla yazildi form 34")
            #success döndür
            data = {'message': 'Created', 'code': 'SUCCESS'}
            return make_response(jsonify(data), 200)

        except Exception as ex:
            print("form34'de hata",ex)

    #success döndür
    data = {'message': 'Created', 'code': 'SUCCESS'}
    return make_response(jsonify(data), 200)
   

if __name__ == '__main__':
    mysql.init_app(app)
    #app.run(debug=True)