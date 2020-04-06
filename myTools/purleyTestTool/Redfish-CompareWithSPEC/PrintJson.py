# -*- coding: utf-8 -*-


class PrintJson(object):
    def __init__(self):
        self.input_json = []
        pass

    def set_json(self, input_json, key_key=''):
        if isinstance(input_json, dict):
            for key in input_json.keys():
                key_value = input_json.get(key)
                if isinstance(key_value, dict):
                    # print key_key + str(key) + " =  " + str(key_value)
                    self.input_json.append((key_key + str(key), str(key_value)))
                    key_key2 = key_key + str(key) + '->'
                    self.set_json(key_value, key_key2)
                elif isinstance(key_value, list):
                    # print key_key + str(key) + " =  " + str(key_value)
                    self.input_json.append((key_key + str(key), str(key_value)))
                    for json_array in key_value:
                        key_key2 = key_key + str(key) + '->'
                        self.set_json(json_array, key_key2)
                else:
                    # print key_key + str(key) + " = " + str(key_value)
                    self.input_json.append((key_key + str(key), str(key_value)))
        elif isinstance(input_json, list):
            for input_json_array in input_json:
                self.set_json(input_json_array)

    def get_json(self):
        return self.input_json


if __name__ == '__main__':
    num1 = {"SKU": "Default string", "PowerState": "On", "SerialNumber": "LSITR013  ", "PartNumber": "SB27A00782", "@odata.type": "#Chassis.v1_5_0.Chassis", "Description": "This resource is used to represent a chassis or other physical enclosure for a Redfish implementation.", "Power": {"@odata.id": "/redfish/v1/Chassis/1/Power/"}, "@odata.context": "/redfish/v1/$metadata#Chassis.Chassis", "Oem": {"Lenovo": {"Sensors": {"@odata.id": "/redfish/v1/Chassis/1/Oem/Lenovo/Sensors/"}, "LEDs": {"@odata.id": "/redfish/v1/Chassis/1/Oem/Lenovo/LEDs/"}, "Slots": {"@odata.id": "/redfish/v1/Chassis/1/Oem/Lenovo/Slots/"}, "LocatedIn": {"Room": "405", "FullPostalAddress": "Test_address", "ContactPerson": "test1", "Height": 4, "DescriptiveName": "Test_Des_Name", "Location": "lenovo", "Position": 10, "Blade-Bay": 0, "Rack": "5"}, "ProductName": "ThinkSystem SR950"}}, "NetworkAdapters": {"@odata.id": "/redfish/v1/Chassis/1/NetworkAdapters/"}, "Manufacturer": "LNVO", "Status": {"State": "Enabled", "Health": "OK"}, "Name": "Chassis", "HeightMm": 177.8, "AssetTag": "my_asset_tag111111", "@odata.id": "/redfish/v1/Chassis/1/", "IndicatorLED": "Off", "LogServices": {"@odata.id": "/redfish/v1/Systems/1/LogServices/"}, "ChassisType": "RackMount", "Model": "7X12ABC1WW", "Links": {"ManagersInChassis": [{"@odata.id": "/redfish/v1/Managers/1/"}], "ComputerSystems": [{"@odata.id": "/redfish/v1/Systems/1/"}], "Storage": [{"@odata.id": "/redfish/v1/Systems/1/Storage/RAID_Slot18/"}], "Drives": [{"@odata.id": "/redfish/v1/Systems/1/Storage/RAID_Slot18/Drives/Disk.0"}, {"@odata.id": "/redfish/v1/Systems/1/Storage/RAID_Slot18/Drives/Disk.1"}], "CooledBy": [{"@odata.id": "/redfish/v1/Chassis/1/Thermal/#/Fans/0"}, {"@odata.id": "/redfish/v1/Chassis/1/Thermal/#/Fans/1"}, {"@odata.id": "/redfish/v1/Chassis/1/Thermal/#/Fans/2"}, {"@odata.id": "/redfish/v1/Chassis/1/Thermal/#/Fans/3"}, {"@odata.id": "/redfish/v1/Chassis/1/Thermal/#/Fans/4"}, {"@odata.id": "/redfish/v1/Chassis/1/Thermal/#/Fans/5"}], "ManagedBy": [{"@odata.id": "/redfish/v1/Managers/1/"}], "PoweredBy": [{"@odata.id": "/redfish/v1/Chassis/1/Power/#/PowerSupplies/0"}, {"@odata.id": "/redfish/v1/Chassis/1/Power/#/PowerSupplies/1"}], "PCIeDevices": [{"@odata.id": "/redfish/v1/Systems/1/PCIeDevices/ob_1"}, {"@odata.id": "/redfish/v1/Systems/1/PCIeDevices/slot_8"}, {"@odata.id": "/redfish/v1/Systems/1/PCIeDevices/slot_9"}, {"@odata.id": "/redfish/v1/Systems/1/PCIeDevices/slot_11"}, {"@odata.id": "/redfish/v1/Systems/1/PCIeDevices/slot_12"}, {"@odata.id": "/redfish/v1/Systems/1/PCIeDevices/slot_13"}, {"@odata.id": "/redfish/v1/Systems/1/PCIeDevices/slot_18"}]}, "Thermal": {"@odata.id": "/redfish/v1/Chassis/1/Thermal/"}, "Id": "1", "@odata.etag": "W/\"426bed11eefa6608659d63be79b6b667\""}

    a = PrintJson()
    a.set_json(num1)
    print a.get_json()
    for i in a.get_json():
        print i


