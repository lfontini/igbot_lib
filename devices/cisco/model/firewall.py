from pydantic import BaseModel


class Firewall(BaseModel):
    acl_type: str
    acl_name: str
    line_num: str
    action: str
    protocol: str
    src_host: str
    src_any: str
    src_network: str
    src_wildcard: str
    src_network_object_group_name: str
    dst_host: str
    dst_any: str
    dst_network: str
    dst_wildcard: str
    dst_network_object_group_name: str
    dst_port_range_start: str
    dst_port_range_end: str
    service_object_group_name: str
    flags_match: str
    tcp_flag: str
    log: str
    log_tag: str
    icmp_type: str
