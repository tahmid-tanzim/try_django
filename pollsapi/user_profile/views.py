from django.http import JsonResponse
from django.views import View
from django.core.files import File
import casbin

import os
from django.conf import settings


class Home(View):
    model_file = os.path.join(settings.BASE_DIR, 'user_profile/config/model.conf')
    policy_file = os.path.join(settings.BASE_DIR, 'user_profile/config/policy.csv')
    e = casbin.Enforcer(model_file, policy_file)

    def get(self, request, *args, **kwargs):

        #return JsonResponse({'id': 420})

        sub = "tanzim"  # the user that wants to access a resource.
        obj = "crime_data"  # the resource that is going to be accessed.
        act = "write"  # the operation that the user performs on the resource.

        if self.e.enforce(sub, obj, act):
            roles = self.e.get_roles_for_user(sub)
            print("Roles for {} - ".format(sub), roles)
            return JsonResponse({'message': 'Hello, World!'}, status=200)
        else:
            return JsonResponse({'message': "Sorry, {} cannot {} {}".format(sub, act, obj)}, status=404)


