from main import app
import json, unittest

class Tests(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.assertEqual(app.debug, False)

    def test_sum_matrix(self):
        response = self.app.post(
            '/api/matrix/sum',
            data=json.dumps(dict(matrix=[ [ 1, 2, 3], [4, 5, 6], [7, 8, 9] ])),
            content_type="application/json"
        )

        expected = 45
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json().get("result"), expected)

    def test_sum_matrix_incorrect(self):
        response = self.app.post(
            '/api/matrix/sum',
            data=json.dumps(dict(matrix=[ [ 1, 2], [4, 5, 6], [7, 8, 9, 3] ])),
            content_type="application/json"
        )

        expected = 'Error, matrix is not square'
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_json().get("result"), expected)

    def test_diagonal_matrix(self):
        response = self.app.post(
            '/api/matrix/diagonal_sum',
            data=json.dumps(dict(matrix=[ [ 1, 2, 3], [4, 5, 6], [7, 8, 9] ])),
            content_type="application/json"
        )

        expected = 15
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json().get("result"), expected)

    def test_diagonal_matrix_incorrect(self):
        response = self.app.post(
            '/api/matrix/diagonal_sum',
            data=json.dumps(dict(matrix=[ [ 1, 3], [2, 4, 5, 6], [7, 8, 9] ])),
            content_type="application/json"
        )

        expected = 'Error, matrix is not square'
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_json().get("result"), expected)

    def test_string_encode(self):
        response = self.app.post(
            '/api/string/encode',
            data=json.dumps(dict(string="aaAabaccCBb")),
            content_type="application/json"
        )

        expected = "A4B1A1C3B2"
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json().get("result"), expected)


    def test_string_encode_incorrect(self):
        response = self.app.post(
            '/api/string/encode',
            data=json.dumps(dict(string="aaAabaÑccÁCBb")),
            content_type="application/json"
        )

        expected = 'Word %s has spanish letters.' % "aaAabaÑccÁCBb"
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_json().get("result"), expected)

if __name__ == "__main__":
    unittest.main()