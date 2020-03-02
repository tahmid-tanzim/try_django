from django.http import JsonResponse
from django.views import View
from django.core.files import File
import casbin


class Home(View):
    # e = casbin.Enforcer("config/model.conf", "config/policy.csv")

    def get(self, request, *args, **kwargs):

        with open('config/policy.csv', 'r') as f:
            data = File(f)
            print(data.read)
            # return JsonResponse(dict(data))
            return JsonResponse({'id': 420})

        # sub = "alice"  # the user that wants to access a resource.
        # obj = "address_data"  # the resource that is going to be accessed.
        # act = "read"  # the operation that the user performs on the resource.
        #
        # if self.e.enforce(sub, obj, act):
        #     roles = self.e.get_roles_for_user(sub)
        #     print("Roles for {} - ".format(sub), roles)
        #     return JsonResponse({'message': 'Hello, World!'}, status=200)
        # else:
        #     return JsonResponse({'message': "Sorry, {} cannot {} {}".format(sub, act, obj)}, status=404)


