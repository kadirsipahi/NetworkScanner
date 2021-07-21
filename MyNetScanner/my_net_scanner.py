import scapy.all as scapy
import optparse



def get_user_input():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i","--ipaddress", dest="ip_address",help="Enter IP Address")

    (user_input,arguments) = parse_object.parse_args()

    if not user_input.ip_address:
        print("Enter IP Address")

    return user_input

#1)arp_request oluşturmalıyız
#2)broadcast yapmalıyız
#3)response alabilmeyiz

def scan_my_network(ip):
    arp_request_packet = scapy.ARP(pdst=ip)   
    # scapy.ls(scapy.ARP()) ≌ ARP --help
    #ARP paketimiz oluşturulmış oldu

    broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    #scapy.ls(scapy.Ether()) ≌ Ether --help
    #dst >  Destination(hedef) MAC adresi

    combined_packet = broadcast_packet/arp_request_packet
    # iki ayrı paketi birleştirebilmemiz için bu metodu kullandık

    (answered_list,unanswered_list) = scapy.srp(combined_packet,timeout=1)
    #cevap verilenler ve verilmeyenleri tuple türünde almak istedik.
    #cevap verilenler ve verilmeyenleri görebilmek için srp kullanmamız gerekiyor.
    #timeout=1 ifadesi ise cevap verilmeyince devam et anlamına geliyor.
    
    answered_list.summary()

user_ip_address = get_user_input()
scan_my_network(user_ip_address.ip_address)