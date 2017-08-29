import pytest
import json
from django.test import TestCase
from graph_implement_tests.schema import schema
from .data_handler import initialize


pytestmark = pytest.mark.django_db

class SchemaTestCase(TestCase):
    def test_correct_fetch_menu_with_page_url(self):
        initialize()
        query = '''
        query {
          menu(first:1){
            edges{
              node{
                name
                page{
                  url
                }
              }
            }
          }
        }
        '''
        expected = {
            "menu": {
                "edges": [
                    {
                        "node": {
                            "name": "menu_for_test",
                            "page": {
                                "url": "url_for_tests"
                            }
                        }
                    }
                ]
            }
        }

        result = schema.execute(query)
        prettified_data = json.dumps(result.data, sort_keys=False)

        assert not result.errors
        assert json.loads(prettified_data) == expected

    def test_mutations_page(self):
        pass
