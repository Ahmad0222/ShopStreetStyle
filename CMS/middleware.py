# from datetime import datetime, timedelta
# from django.conf import settings
# from django.contrib import auth
#
#
# class AutoLogout:
#   def process_request(self, request):
#     if not request.user.is_authenticated() :
#       #Can't log out if not logged in
#       return
#
#     try:
#       if datetime.now() - request.session['last_activity'] > timedelta( 0, settings.AUTO_LOGOUT_DELAY * 60, 0):
#         auth.logout(request)
#         del request.session['last_activity']
#         return
#     except KeyError:
#       pass
#
#     request.session['last_activity'] = datetime.now()


# from datetime import datetime
# from django.http import HttpResponseRedirect

# class SessionExpiredMiddleware:
#     def process_request(self, request):
#         last_activity = request.session['last_activity']
#         now = datetime.now()
#
#         if (now - last_activity).minutes > 10:
#             # Do logout / expire session
#             # and then...
#             return HttpResponseRedirect("LOGIN_PAGE_URL")
#
#         if not request.is_ajax():
#             # don't set this for ajax requests or else your
#             # expired session checks will keep the session from
#             # expiring :)
#             request.session['last_activity'] = datetime.now()
