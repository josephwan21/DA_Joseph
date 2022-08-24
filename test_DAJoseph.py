import unittest
import DA_Joseph
import requests

class ApplicationTest(unittest.TestCase):
    def test_statuscode(self):
        # Set the target webpage
        DA_Joseph.url = "http://172.18.58.80/nantes"
        r = requests.get(DA_Joseph.url)
        # This will get the full page
        print(r.text)
        print("Status code:")
        print("\t *", r.status_code)


if __name__ == '__main__':
    unittest.main()