# Try Django

pipenv shell

### Choosing the base class to use

We have seen 4 ways to build API views until now
* Pure Django views
* APIView subclasses
* generics.* subclasses
* viewsets.ModelViewSet

So which one should you use when? My rule of thumb is,
* Use viewsets.ModelViewSet when you are going to allow all or most of CRUD operations on a model.
* Use generics.* when you only want to allow some operations on a model
* Use APIView when you want to completely customize the behaviour.


### Testing and Continuous Integeration
* APIRequestFactory: This is similar to Django’s RequestFactory. It allows you to create requests
with any http method, which you can then pass on to any view method and compare responses.
* APIClient: similar to Django’s Client. You can GET or POST a URL, and test responses.
* APITestCase: similar to Django’s TestCase. Most of your tests will subclass this.