import pytest
from unittest.mock import patch
from win_log_parser import filter_critical_events

# Mock data simulating XML strings returned by the get_all_events generator
MOCK_EVENTS = [
    "<Event><System><Level>4</Level></System><EventData>Information Event</EventData></Event>",
    "<Event><System><Level>1</Level></System><EventData>Critical Error 1</EventData></Event>",
    "<Event><System><Level>3</Level></System><EventData>Warning Event</EventData></Event>",
    "<Event><System><Level>2</Level></System><EventData>Standard Error 1</EventData></Event>",
    "<Event><System><Level>0</Level></System><EventData>Undefined Event</EventData></Event>"
]

@patch('win_log_parser.get_all_events')
def test_filter_critical_events(mock_get_all_events):
    # Setup the mock to return our predefined list of XML strings
    mock_get_all_events.return_value = MOCK_EVENTS
    
    # Execute the function with a dummy filepath
    result = filter_critical_events("dummy_path.evtx")
    
    # Assertions
    assert len(result) == 2, "Should only filter Level 1 (Critical) and Level 2 (Error) events"
    assert "<Level>1</Level>" in result[0], "First item should be the Critical error"
    assert "<Level>2</Level>" in result[1], "Second item should be the Standard error"
