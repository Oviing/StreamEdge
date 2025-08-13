import unittest
from unittest.mock import patch
from ingest.zmq_client import build_payload

class TestZMQClient(unittest.TestCase):
    @patch('builtins.input', side_effect=['123', '45.6'])  # Adjust for your payload_config.yaml
    def test_build_payload(self, mock_input):
        payload = build_payload()
        self.assertIsInstance(payload, dict)
        self.assertIn('field1', payload)  # Adjust field names
        self.assertIn('field2', payload)

if __name__ == "__main__":
    unittest.main()
