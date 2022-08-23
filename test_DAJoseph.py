import unittest
import DA_Joseph

class ApplicationTest(unittest.TestCase):
    def statuscode_test(self):
        import requests
        # Set the target webpage
        url = 'http://172.18.58.80/nantes’
        r = requests.get(url)
        # This will get the full page
        print(r.text)
        print("Status code:")
        print("\t *", r.status_code)


if __name__ == '__main__':
    unittest.main()