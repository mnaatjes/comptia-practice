import sys
import Evtx.Evtx as evtx

def get_all_events(filepath):
    """
    Yields XML string representations of events from the specified .evtx file.
    Generator is used to handle large files (e.g., 20MB) efficiently without loading all into memory.
    """
    with evtx.Evtx(filepath) as log:
        for record in log.records():
            yield record.xml()

def filter_critical_events(filepath):
    """
    Parses the evtx file and returns a list of XML strings for Critical (Level 1) 
    and Error (Level 2) events.
    """
    critical_events = []
    for xml_str in get_all_events(filepath):
        # Simple string match for the event level in the Windows Event XML schema
        if "<Level>1</Level>" in xml_str or "<Level>2</Level>" in xml_str:
            critical_events.append(xml_str)
    return critical_events

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python win_log_parser.py <path_to_evtx_file>")
        sys.exit(1)
        
    log_file = sys.argv[1]
    print(f"Parsing {log_file} for critical errors...")
    errors = filter_critical_events(log_file)
    print(f"Found {len(errors)} critical/error events.")
    
    if errors:
        print("\nFirst identified error:")
        print(errors[0])
