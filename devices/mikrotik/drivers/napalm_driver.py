from napalm import get_network_driver
from .base_mikrotik import BaseMikrotik
import json

class MikrotikNapalm(BaseMikrotik):
    """Driver NAPALM para MikroTik RouterOS"""
    
    def __init__(self, ip, username, password, port=8728):
        """
        Inicializa o driver NAPALM
        Nota: NAPALM usa porta 8728 (API) por padrão para RouterOS
        """
        super().__init__(ip, username, password, port)
        self.driver = get_network_driver('ros')
        
    def _connect(self):
        """Estabelece conexão usando NAPALM"""
        self.client = self.driver(
            hostname=self.ip,
            username=self.username,
            password=self.password,
            optional_args={'port': self.port}
        )
        self.client.open()
    
    def run(self, command):
        """
        Execute free command usando NAPALM cli
        """
        self._connect()
        try:
            # NAPALM retorna dict com comando como chave
            result = self.client.cli([command])
            return result.get(command, '')
        except Exception as e:
            # Se cli não estiver disponível, tenta alternativa
            return f"Command execution not fully supported via NAPALM: {str(e)}"
    
    def get_interfaces(self):
        """Obtém interfaces usando NAPALM"""
        self._connect()
        interfaces = self.client.get_interfaces()
        
        # Formata saída similar ao comando MikroTik
        output = []
        for iface, details in interfaces.items():
            status = "enabled" if details['is_enabled'] else "disabled"
            up_down = "up" if details['is_up'] else "down"
            output.append(
                f"{iface}: {status}, {up_down}, "
                f"MAC: {details.get('mac_address', 'N/A')}, "
                f"Speed: {details.get('speed', 'N/A')}"
            )
        return '\n'.join(output)
    
    def get_ips(self):
        """Obtém endereços IP usando NAPALM"""
        self.connect()
        ip_interfaces = self.client.get_interfaces_ip()
        
        # Formata saída similar ao comando MikroTik
        output = []
        for iface, ip_data in ip_interfaces.items():
            for ip_version, addresses in ip_data.items():
                for ip, details in addresses.items():
                    output.append(
                        f"{iface}: {ip}/{details['prefix_length']}"
                    )
        return '\n'.join(output)
    
    def get_arp(self):
        """Obtém tabela ARP usando NAPALM"""
        self._connect()
        arp_table = self.client.get_arp_table()
        
        # Formata saída similar ao comando MikroTik
        output = []
        for entry in arp_table:
            output.append(
                f"IP: {entry['ip']}, "
                f"MAC: {entry['mac']}, "
                f"Interface: {entry.get('interface', 'N/A')}, "
                f"Age: {entry.get('age', 'N/A')}"
            )
        return '\n'.join(output)
    
    def get_mac(self):
        """Obtém tabela MAC usando NAPALM"""
        self._connect()
        try:
            mac_table = self.client.get_mac_address_table()
            
            # Formata saída similar ao comando MikroTik
            output = []
            for entry in mac_table:
                output.append(
                    f"MAC: {entry['mac']}, "
                    f"Interface: {entry['interface']}, "
                    f"VLAN: {entry.get('vlan', 'N/A')}, "
                    f"Active: {entry.get('active', True)}"
                )
            return '\n'.join(output)
        except Exception as e:
            return f"MAC table not available: {str(e)}"
    
    def get_firewall(self):
        """
        Obtém regras de firewall
        Nota: NAPALM não tem método direto para firewall
        """
        self._connect()
        # Tenta executar via CLI
        return self.run("/ip firewall filter print")
    
    def get_users(self):
        """
        Obtém usuários
        Nota: NAPALM não tem método direto para usuários
        """
        self._connect()
        # Tenta executar via CLI
        return self.run("/user print")
    
    def get_logs(self):
        """
        Obtém logs
        Nota: NAPALM não tem método direto para logs
        """
        self._connect()
        # Tenta executar via CLI
        return self.run("/log print")
    
    def get_system(self):
        """Obtém recursos do sistema usando NAPALM"""
        self._connect()
        
        # Usa get_facts e get_environment
        facts = self.client.get_facts()
        
        try:
            environment = self.client.get_environment()
        except:
            environment = {}
        
        # Formata saída similar ao comando MikroTik
        output = [
            f"Hostname: {facts.get('hostname', 'N/A')}",
            f"Model: {facts.get('model', 'N/A')}",
            f"Version: {facts.get('os_version', 'N/A')}",
            f"Uptime: {facts.get('uptime', 'N/A')} seconds",
            f"Serial: {facts.get('serial_number', 'N/A')}",
        ]
        
        # Adiciona informações de ambiente se disponíveis
        if environment:
            if 'memory' in environment:
                output.append(f"Memory: {json.dumps(environment['memory'])}")
            if 'cpu' in environment:
                output.append(f"CPU: {json.dumps(environment['cpu'])}")
            if 'temperature' in environment:
                output.append(f"Temperature: {json.dumps(environment['temperature'])}")
                
        return '\n'.join(output)
    
    def get_config(self):
        """Obtém configuração completa usando NAPALM"""
        self._connect()
        config = self.client.get_config()
        
        # Retorna configuração running
        return config.get('running', '')
    
    def close(self):
        """Fecha conexão NAPALM"""
        if self.client:
            self.client.close()
    
    # Métodos adicionais específicos do NAPALM
    
    def get_facts(self):
        """Obtém fatos do dispositivo (método NAPALM nativo)"""
        self._connect()
        return json.dumps(self.client.get_facts(), indent=2)
    
    def get_interfaces_counters(self):
        """Obtém contadores das interfaces"""
        self._connect()
        counters = self.client.get_interfaces_counters()
        
        output = []
        for iface, counter_data in counters.items():
            output.append(f"\nInterface: {iface}")
            for counter, value in counter_data.items():
                output.append(f"  {counter}: {value}")
        
        return '\n'.join(output)
    
    def ping(self, destination, count=5):
        """Executa ping do dispositivo"""
        self.connect()
        try:
            result = self.client.ping(
                destination=destination,
                count=count
            )
            return json.dumps(result, indent=2)
        except Exception as e:
            return f"Ping not supported: {str(e)}"
    
    def compare_config(self, new_config):
        """Compara configuração nova com atual"""
        self.connect()
        try:
            self.client.load_merge_candidate(config=new_config)
            diff = self.client.compare_config()
            self.client.discard_config()
            return diff
        except Exception as e:
            return f"Config comparison error: {str(e)}"
    
    def apply_config(self, config, test=True):
        """Aplica nova configuração"""
        self._connect()
        try:
            self.client.load_merge_candidate(config=config)
            
            if test:
                diff = self.client.compare_config()
                if not diff:
                    return "No changes to apply"
                
                print(f"Changes to be applied:\n{diff}")
                confirm = input("Apply changes? (y/n): ")
                
                if confirm.lower() != 'y':
                    self.client.discard_config()
                    return "Changes discarded"
            
            self.client.commit_config()
            return "Configuration applied successfully"
            
        except Exception as e:
            self.client.discard_config()
            return f"Configuration error: {str(e)}"