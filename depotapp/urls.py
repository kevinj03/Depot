
from django.conf.urls.defaults import *
from models import *
from views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from djangorestframework.views import ListOrCreateModelView, InstanceModelView
from resources import *
urlpatterns = patterns('',

    (r'product/create/$', create_product),
    (r'product/list/$', list_product ),
    (r'product/edit/(?P<id>[^/]+)/$', edit_product),
    (r'product/view/(?P<id>[^/]+)/$', view_product),
    (r'product/delete/(?P<id>[^/]+)/$', delete_product),
    (r'store/$', store_view),
    (r'cart/view/', view_cart),
    (r'cart/clean/', clean_cart),
    (r'cart/add/(?P<id>[^/]+)/$', add_to_cart),
    (r'API/cart/items', RESTforCart.as_view(resource=LineItemResource)),
    (r'^restframework', include('djangorestframework.urls', namespace='djangorestframework')),
    (r'order/create/$', create_order),
    (r'order/list/$', list_order ),
    (r'order/edit/(?P<id>[^/]+)/$', edit_order),
    (r'order/view/(?P<id>[^/]+)/$', view_order),
    (r'product/(?P<id>[^/]+)/who_bought$', atom_of_order),
    #(r'store/about/$', about_view),
)
urlpatterns += staticfiles_urlpatterns()
