from devices.cisco.model.firewall import Firewall


class FirewallParser:
    @staticmethod
    def parse(raw_firewall: any) -> list[Firewall]:
        firewalls = []

        for entry in raw_firewall:
            if entry.get("acl_name"):
                firewalls.append(
                    Firewall(
                        acl_type=entry["acl_type"],
                        acl_name=entry["acl_name"],
                        line_num=entry["line_num"],
                        action=entry["action"],
                        protocol=entry["protocol"],
                        src_host=entry["src_host"],
                        src_any=entry["src_any"],
                        src_network=entry["src_network"],
                        src_wildcard=entry["src_wildcard"],
                        src_network_object_group_name=entry[
                            "src_network_object_group_name"
                        ],
                        dst_host=entry["dst_host"],
                        dst_any=entry["dst_any"],
                        dst_network=entry["dst_network"],
                        dst_wildcard=entry["dst_wildcard"],
                        dst_network_object_group_name=entry[
                            "dst_network_object_group_name"
                        ],
                        dst_port_range_start=entry["dst_port_range_start"],
                        dst_port_range_end=entry["dst_port_range_end"],
                        service_object_group_name=entry["service_object_group_name"],
                        flags_match=entry["flags_match"],
                        tcp_flag=entry["tcp_flag"],
                        log=entry["log"],
                        log_tag=entry["log_tag"],
                        icmp_type=entry["icmp_type"],
                    )
                )

        return firewalls
