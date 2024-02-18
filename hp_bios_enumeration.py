import osquery
import win32com.client as win32

@osquery.register_plugin
class HPBIOSEnumerationTablePlugin(osquery.TablePlugin):
    def name(self):
        """Table name to be used in SQL queries."""
        return "hp_bios_enumeration"

    def columns(self):
        """Defines the columns of your table."""
        return [
            osquery.TableColumn(name="name", type=osquery.STRING),
            osquery.TableColumn(name="possible_values", type=osquery.STRING),
            osquery.TableColumn(name="current_value", type=osquery.STRING),
        ]

    def generate(self, context):
        """Generates the data for each row in your table."""
        query_data = []
        try:
            wmi_service = win32.GetObject("winmgmts:\\\\.\\root\\HP\\InstrumentedBIOS")
            bios_enumerations = wmi_service.ExecQuery("SELECT * FROM HP_BIOSEnumeration")
            for bios_enum in bios_enumerations:
                possible_values = ', '.join(bios_enum.PossibleValues) if bios_enum.PossibleValues else ""
                query_data.append({
                    "name": bios_enum.Name,
                    "possible_values": possible_values,
                    "current_value": bios_enum.CurrentValue
                })
        except Exception as e:
            osquery.log(f"An error occurred while querying HP BIOS settings: {str(e)}")
        return query_data

if __name__ == "__main__":
    osquery.start_extension(name="hp_bios_enumeration_extension", version="1.0.0")
