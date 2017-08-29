import json
from django.shortcuts import render
from graph_implement_tests.schema import schema



def index(request):
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
    results = schema.execute(query)
    prettified_data = json.loads(json.dumps(results.data, sort_keys=False))
    context = {
        'test': prettified_data['menu']['edges'][0]['node']
    }

    return render(request, 'test.html', context)
