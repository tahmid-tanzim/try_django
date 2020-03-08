from django.test import TestCase
from .views import ACL


class ACLTestCase(TestCase):
    # def setUp(self):

    def test_acl_validation(self):
        user = "fahim"
        data = {
            "tbl": "profile",
            "row": "2",
            "col": "name",
            "value": "Fahim"
        }
        action = "read"
        acl = ACL()
        result = acl.validation(user, data, action)
        print(result)
        self.assertEqual(result, data)