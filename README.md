## NetworkScanner
<strong>Projenin Özeti</strong>
<p>Ağımızın/Bilgisayarımızın ARP Spoofing saldırılarına karşı durumunun kontrol edilebilmesi veya ağımızdaki aygıtları MAC ve IP adresleri yönünden inceleyebilmemizi sağlar.</p>

*<strong>Uygulama içerisinde kullanılan kütüphaneler nelerdir ? Özet</strong><br>*
  <p>scapy.all, optparse kütüphaneleri kullanıldı;<br>
<p>• scapy.all > Çok geniş bir kütüphane olmakla birlikte benim kullanım amacım çeşitli network paketleri oluşturmak, göndermek ve yakalamak oldu.<br>
<p>• optparse > Terminal/Command Prompt üzerinde kullanıcıdan input alma işlemi için ve kullanıcıdan alınan argümanların sistem üzerinde uygulanıp kaydedilebilmesi için kullanıldı.<br>
  Bu kütüphanenin kullanılabilmesi için bir obje oluşturma şartı vardır. Uygulama içerisinde bu objeyi "parse_pbject" olarak tanımladım.<br>
  Argümanların kaydedilmesi için; dest="ip_address",help="Enter IP Address" yani dest ve help kwargs kullanıldı.<br>
  
<strong>Projeyi Geliştirenler:</strong><br>
<strong><i>Kadir SİPAHİ</i></strong>

*<strong>Uygulama nasıl çalıştırılır ?</strong><br>*
<p>Terminal/Command Prompt üzerinden uygulamanın bulunduğu dizine gidilir,
Uygulamamıza sistemin içerisinde bulundupu private IP adresi ve o ağın türüne göre bir CIDR değeri verilmelidir. Örneğin C sınıfı bir IP adresi için 192.168.1.0/16 gibi.<br>
python veya python3 kullanarak uygulamamızı başlatabiliriz.<br>
  

```
python my_net_scanner.py -i <PrivateIP/CIDR>

python3 my_net_scanner.py -i <PrivateIP/CIDR>
