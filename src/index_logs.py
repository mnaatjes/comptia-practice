import sys
import csv
import xml.etree.ElementTree as ET
import Evtx.Evtx as evtx

def get_namespace(tag):
    return tag.split('}')[0] + '}' if '}' in tag else ''

def index_evtx(filepath, output_csv):
    with evtx.Evtx(filepath) as log, open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Index', 'Level', 'TimeCreated', 'EventID', 'Provider'])
        
        index = 0
        for record in log.records():
            try:
                xml_str = record.xml()
                # Fast string check for Critical (1), Error (2), and Warning (3)
                if "<Level>1</Level>" in xml_str or "<Level>2</Level>" in xml_str or "<Level>3</Level>" in xml_str:
                    root = ET.fromstring(xml_str)
                    ns = get_namespace(root.tag)
                    system = root.find(f'{ns}System')
                    if system is not None:
                        level = system.find(f'{ns}Level')
                        level_val = level.text if level is not None else "Unknown"
                        
                        event_id = system.find(f'{ns}EventID')
                        event_id_val = event_id.text if event_id is not None else "Unknown"
                        
                        provider = system.find(f'{ns}Provider')
                        provider_val = provider.get('Name') if provider is not None else "Unknown"
                        
                        time_created = system.find(f'{ns}TimeCreated')
                        time_val = time_created.get('SystemTime') if time_created is not None else "Unknown"
                        
                        writer.writerow([index, level_val, time_val, event_id_val, provider_val])
            except Exception as e:
                pass
            index += 1

if __name__ == "__main__":
    index_evtx('data/raw/windows_system_log.evtx', 'data/processed/error_index.csv')
    print("Indexing complete. Data written to data/processed/error_index.csv")
