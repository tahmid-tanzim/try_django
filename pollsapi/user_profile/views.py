from django.http import JsonResponse
from django.views import View
from django.core.files import File
import casbin

import os
from django.conf import settings


class Home(View):
    model_conf = os.path.join(settings.BASE_DIR, 'user_profile/config/model.conf')
    policy = os.path.join(settings.BASE_DIR, 'user_profile/config/policy.csv')
    e = casbin.Enforcer(model_conf, policy)
    # e.add_policy("eve", "data3", "read")
    def get(self, request, *args, **kwargs):

        sub = "tanzim"  # the user that wants to access a resource.
        obj = "financial_data"  # the resource that is going to be accessed.
        act = "write"  # the operation that the user performs on the resource.
        # sub = "eve"  # the user that wants to access a resource.
        # obj = "data3"  # the resource that is going to be accessed.
        # act = "read"  # the operation that the user performs on the resource.

        if self.e.enforce(sub, obj, act):
            roles = self.e.get_roles_for_user(sub)
            print("Roles for {} - ".format(sub), roles)
            return JsonResponse({'message': "Wow!!, {} can {} {}".format(sub, act, obj)}, status=200)
        else:
            return JsonResponse({'message': "Sorry, {} cannot {} {}".format(sub, act, obj)}, status=404)


