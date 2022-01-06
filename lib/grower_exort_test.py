import grower_export
import unittest   # The test framework

class Test_Grower_Export(unittest.TestCase):
    def test_grower_export(self):
        import psycopg2
        # read env variables DB_URL
        import os
        print("grower export");
        # read env variables DB_URL
        DB_URL = os.environ['DB_URL']
        print("DB_URL:", DB_URL)
        conn = psycopg2.connect(DB_URL, sslmode='require')
        CKAN_DOMAIN = os.environ['CKAN_DOMAIN']
        # assert CKAN_DOMAIN exists
        self.assertTrue(CKAN_DOMAIN)
        CKAN_DATASET_NAME_GROWER_DATA = os.environ['CKAN_DATASET_NAME_GROWER_DATA']
        self.assertTrue(CKAN_DATASET_NAME_GROWER_DATA)
        CKAN_API_KEY = os.environ['CKAN_API_KEY']
        self.assertTrue(CKAN_API_KEY)
        # dict of env variables
        ckan_config = {
            "CKAN_DOMAIN": CKAN_DOMAIN,
            "CKAN_DATASET_NAME_GROWER_DATA": CKAN_DATASET_NAME_GROWER_DATA,
            "CKAN_API_KEY": CKAN_API_KEY,
        }
        # execute capture_export.capture_export(conn, '2020-12') should throw an error
        result = grower_export.grower_export(conn, '2020-11-10', ckan_config)
        # use unittest to check the result
        self.assertTrue(result)

if __name__ == '__main__':
    # Run the unit tests in the test suite with name 'Test_TestIncrementDecrement'
    unittest.main()