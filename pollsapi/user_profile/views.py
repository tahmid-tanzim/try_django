from django.http import JsonResponse
from django.views import View

import casbin
from casbin_sqlalchemy_adapter import Adapter

import os
from django.conf import settings


class Home(View):
    model_conf = os.path.join(settings.BASE_DIR, 'user_profile/config/model.conf')
    # policy = os.path.join(settings.BASE_DIR, 'user_profile/config/policy.csv')
    # e = casbin.Enforcer(model_conf, policy)

    pg_adapter = Adapter('postgresql://tanzim:roo101@localhost:5432/tanzim')
    e = casbin.Enforcer(model_conf, pg_adapter, True)
    # e.add_policy("alice", "address_data", "read", "allow")
    # e.add_policy("superadmin", "financial_data", "write", "allow")

    # e.add_grouping_policy("tanzim", "superadmin")
    # e.add_role_for_user("tahmid", "admin")

    # UPDATE
    # e.remove_policy("alice", "address_data", "read", "allow")
    # e.add_policy("alice", "address_data", "read", "deny")

    # Remove from a Role
    # e.delete_role_for_user("tahmid", "admin")
    def get(self, request, *args, **kwargs):

        sub = "tanzim"  # the user that wants to access a resource.
        obj = "financial_data"  # the resource that is going to be accessed.
        act = "read"  # the operation that the user performs on the resource.
        # sub = "eve"  # the user that wants to access a resource.
        # obj = "data3"  # the resource that is going to be accessed.
        # act = "read"  # the operation that the user performs on the resource.

        if self.e.enforce(sub, obj, act):
            roles = self.e.get_roles_for_user(sub)
            print("Roles for {} - ".format(sub), roles)
            return JsonResponse({'message': "Wow!!, {} can {} {}".format(sub, act, obj)}, status=200)
        else:
            return JsonResponse({'message': "Sorry, {} cannot {} {}".format(sub, act, obj)}, status=404)


