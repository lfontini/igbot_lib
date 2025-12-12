from collections import defaultdict
from pydantic import BaseModel
from textfsm import TextFSM
from devices.datacom.models.vlans import Vlan

class VlanService4370:
    @staticmethod
    def parse(raw: str) -> list[Vlan]:
        with open("devices/datacom/parsers/templates/vlan_dm_4370.textfsm") as template:
            fsm = TextFSM(template)
            result = fsm.ParseText(raw)

        vlans_dict = {}
        current_vlan = None

        for row in result:
            entry = dict(zip(fsm.header, row))

            if entry.get("VLAN_ID"):
                # Nova VLAN
                current_vlan = entry["VLAN_ID"]
                vlans_dict[current_vlan] = {
                    "id": int(entry["VLAN_ID"]),
                    "name": entry["VLAN_NAME"],
                    "type": entry["VLAN_TYPE"],
                    "interfaces": [],
                    "status_interfaces": [],
                    "port_state_interfaces": []
                }

            if current_vlan is None:
                # Linha de interface antes de encontrar VLAN? Ignorar
                continue

            # Adiciona a interface à VLAN corrente
            vlans_dict[current_vlan]["interfaces"].append(entry["IFACE"])
            vlans_dict[current_vlan]["status_interfaces"].append(entry["STATUS"])
            vlans_dict[current_vlan]["port_state_interfaces"].append(entry["PORT_STATE"])

        # Cria instâncias Pydantic
        vlans = [Vlan(**data) for data in vlans_dict.values()]
        return vlans


class VlanService4050:
    @staticmethod
    def parse(raw: str) -> list[Vlan]:
        from textfsm import TextFSM
        from devices.datacom.models.vlans import Vlan

        # Detecta o tipo de output
        is_brief = "INTERFACE NAME" not in raw and "PORT STATE" not in raw

        # Seleciona o template correto
        if is_brief:
            template_file = "devices/datacom/parsers/templates/show_vlan_brief_id_dm_4050.textfsm"
        else:
            template_file = "devices/datacom/parsers/templates/show_vlan_membership_detail_dm_4050.textfsm"

        # Carrega template
        with open(template_file) as template:
            fsm = TextFSM(template)
            result = fsm.ParseText(raw)

        # Se for formato BRIEF, retorna direto sem agregação por interface
        if is_brief:
            vlans = []
            for row in result:
                entry = dict(zip(fsm.header, row))
                print(entry)
                print(fsm.header)
                vlans.append(Vlan(
                    id = int(entry["VLAN_ID"]),
                    name = entry.get("NAME") or entry.get("VLAN_NAME") or "",
                    type = entry["VLAN_TYPE"],
                    interfaces = [],
                    status_interfaces = [],
                    port_state_interfaces = []
                ))
            return vlans

        # --------------------------
        # Formato DETAIL (membership)
        # --------------------------
        vlans_dict = {}

        for row in result:
            entry = dict(zip(fsm.header, row))
            vlan_id = entry["VLAN_ID"]

            if vlan_id not in vlans_dict:
                vlans_dict[vlan_id] = {
                    "id": int(vlan_id),
                    "name": entry.get("VLAN_NAME") or entry.get("NAME") or "",
                    "type": entry["VLAN_TYPE"],
                    "interfaces": [],
                    "status_interfaces": [],
                    "port_state_interfaces": []
                }

            vlans_dict[vlan_id]["interfaces"].append(entry["IFACE"])
            vlans_dict[vlan_id]["status_interfaces"].append(entry["STATUS"])
            vlans_dict[vlan_id]["port_state_interfaces"].append(entry["PORT_STATE"])

        return [Vlan(**data) for data in vlans_dict.values()]

class VlanService4170:
    @staticmethod
    def parse(raw: str) -> list[Vlan]:
        with open("devices/datacom/parsers/templates/vlan_dm_4170.textfsm") as template:
            fsm = TextFSM(template)
            result = fsm.ParseText(raw)

        vlans_dict = {}
        current_vlan = None

        for row in result:
            entry = dict(zip(fsm.header, row))
            # Nova VLAN detectada
            if entry.get("VLAN_ID"):
                current_vlan = entry["VLAN_ID"]

                vlans_dict[current_vlan] = {
                    "id": int(entry["VLAN_ID"]),
                    "name": entry["VLAN_NAME"],
                    "type": entry["VLAN_TYPE"],
                    "interfaces": [],
                    "status_interfaces": [],
                    "port_state_interfaces": []
                }

            # Adicionar interface à VLAN corrente
            vlans_dict[current_vlan]["interfaces"].append(entry["IFACE"])
            vlans_dict[current_vlan]["status_interfaces"].append(entry["STATUS"])
            vlans_dict[current_vlan]["port_state_interfaces"].append(entry["PORT_STATE"])

        # Retorno final Pydantic
        return [Vlan(**v) for v in vlans_dict.values()]



class VlanService4100:
    @staticmethod
    def parse(raw: str) -> list[Vlan]:
        print(raw)
        with open("devices/datacom/parsers/templates/vlan_dm_4100.textfsm", encoding="utf-8") as template:
            fsm = TextFSM(template)
            result = fsm.ParseText(raw)

        vlans_dict = {}
        current_vlan = None

        for row in result:
            entry = dict(zip(fsm.header, row))
            # Nova VLAN detectada
            if entry.get("VLAN_ID"):
                current_vlan = entry["VLAN_ID"]

                vlans_dict[current_vlan] = {
                    "id": int(entry["VLAN_ID"]),
                    "name": entry["VLAN_NAME"],
                    "type": entry["VLAN_TYPE"],
                    "interfaces": [],
                    "status_interfaces": [],
                    "port_state_interfaces": []
                }

            # Adicionar interface à VLAN corrente
            vlans_dict[current_vlan]["interfaces"].append(entry["IFACE"])
            vlans_dict[current_vlan]["status_interfaces"].append(entry["STATUS"])

        # Retorno final Pydantic
        return [Vlan(**v) for v in vlans_dict.values()]
