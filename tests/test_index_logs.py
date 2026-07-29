import pytest
import csv
from unittest.mock import patch, MagicMock
from index_logs import index_evtx

MOCK_XML = """
<Event xmlns="http://schemas.microsoft.com/win/2004/08/events/event">
  <System>
    <Provider Name="Microsoft-Windows-Kernel-Power"/>
    <EventID>41</EventID>
    <Level>1</Level>
    <TimeCreated SystemTime="2023-10-25T14:30:00.000000Z"/>
  </System>
  <EventData>
    <Data>System crash</Data>
  </EventData>
</Event>
"""

@patch('index_logs.evtx.Evtx')
def test_index_evtx(mock_evtx_class, tmp_path):
    # Setup mock record
    mock_record = MagicMock()
    mock_record.xml.return_value = MOCK_XML
    
    # Setup mock log context manager
    mock_log_instance = MagicMock()
    mock_log_instance.records.return_value = [mock_record]
    
    # Configure the mocked class to return our instance when used as a context manager
    mock_evtx_class.return_value.__enter__.return_value = mock_log_instance
    
    # Setup temporary output CSV path using pytest's built-in tmp_path fixture
    output_csv = tmp_path / "test_output.csv"
    
    # Execute the function
    index_evtx("dummy_path.evtx", str(output_csv))
    
    # Verify the output CSV
    with open(output_csv, 'r', encoding='utf-8') as f:
        reader = list(csv.reader(f))
        
        # Verify header row
        assert reader[0] == ['Index', 'Level', 'TimeCreated', 'EventID', 'Provider']
        
        # Verify parsed data row
        assert reader[1] == ['0', '1', '2023-10-25T14:30:00.000000Z', '41', 'Microsoft-Windows-Kernel-Power']
