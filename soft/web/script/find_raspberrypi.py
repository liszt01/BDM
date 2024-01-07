import ipaddress
import subprocess
import re
from scapy.all import ARP, Ether, srp

def get_network():
    try:
        # ifconfigを実行してネットワーク情報を取得
        result = subprocess.check_output(["ifconfig"]).decode("utf-8")
        
        # inetアドレスとサブネットマスクを正規表現で抽出
        match = re.search(r'inet (\d+\.\d+\.\d+\.\d+)  netmask (\d+\.\d+\.\d+\.\d+)  broadcast (\d+\.\d+\.\d+\.\d+)', result)
        # print(match)
        
        if match:
            ip_address = ipaddress.IPv4Address(match.group(1))
            subnet_mask = ipaddress.IPv4Address(match.group(2))
            
            network = ipaddress.IPv4Network(f'{ip_address}/{subnet_mask}', strict=False)
            
            return network
        else:
            print("ネットワーク情報が見つかりませんでした。")
            return None
    except Exception as e:
        print(f"エラー: {e}")
        return None

def get_raspberry_pi_ip(target_ip):
    raspberry_pi_mac_prefix = "b8:27:eb"  # ラズベリーパイのMACアドレスプレフィックス

    # ARPリクエストを作成
    arp = ARP(pdst=target_ip)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp

    # ARPリクエストを送信し、応答を取得
    # root 権限がないと実行できない
    result = srp(packet, timeout=3, verbose=0)[0]

    # 応答からIPアドレスを取得
    rasp_pi_ips = [res[1].psrc for res in result if res[1].hwsrc.startswith(raspberry_pi_mac_prefix)]

    return rasp_pi_ips

if __name__ == "__main__":
    network = get_network()
    if network:
        print(f"ネットワークの範囲: {network}")

        rasp_pi_ips = get_raspberry_pi_ip(network)
        print(rasp_pi_ips)
        if rasp_pi_ips:
            print("Raspberry PiのIPアドレス:")
            for ip in rasp_pi_ips:
                print(ip)
        else:
            print("Raspberry Piが見つかりませんでした。")
    else:
        print("ネットワークの範囲を取得できませんでした。")
