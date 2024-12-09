from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from store.views import index, product_detail, create_products, signup, login_view, logout_view, frontpage, add_to_cart, cart, add_get_bank_account

from shop import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('product/<str:slug>/', product_detail, name="products"),
    path('product/<str:slug>/add_to_cart', add_to_cart, name="add_to_cart"),
    path('create_products/', create_products, name="create_products"),
    path('cart/', cart, name="cart"),
    
    path('', frontpage, name="frontpage"),
    path('index/', index, name="index"),
    path('bank/', add_get_bank_account, name="bank"),
    
    path('signup/', signup, name="signup"),
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name="logout"),
        
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
