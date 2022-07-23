from django.conf import settings  # settings の変数を使用する
from django.conf.urls.static import static  # media を使用する時に使う
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dog_cat_app.urls'))
]

# アップロードした画像を url で指定できるようになる
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)