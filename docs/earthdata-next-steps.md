# Earthdata bağlantısı ve veri işleme durumu

**Güncel durum:** Earthdata erişimi doğrulandı. 12 gerçek NASA dosyası (413,531,230 bayt) indirildi. Kalite eşiğini geçen NDVI: 2/26; gece ışığı: 0/26; ASTER v3: 1/26. Salda için kalite/maske/belirsizlik bilgili EMIT spektral mineral bağlamı üretildi.

Aşağıdaki401 denemeleri bağlantı kurulmadan önceki tanılama kaydıdır; mevcut erişim sorunu çözülmüştür.

Resmî kayıt: https://urs.earthdata.nasa.gov/users/new

Hesabı oluşturup e-posta doğrulamasını tamamlayın. NASA Earthdata Search’e bu hesapla giriş yapılabilir: https://search.earthdata.nasa.gov/ . Kayıt, yalnızca kimliksiz erişimde401 dönen ürünlerin yetkili indirilmesini sağlar; analiz doğruluğunu veya her alanda veri bulunacağını garanti etmez.

## TerraTwin’e hesabı bağlama

NASA profilinde **Generate Token → Generate Token → Show Token** adımlarıyla kullanıcı erişim anahtarı oluşturulur: https://urs.earthdata.nasa.gov/profile . NASA’nın açıklamasına göre bu anahtarların süresi60 gündür: https://urs.earthdata.nasa.gov/documentation/for_users/user_token .

```powershell
python -m analysis.earthdata_access --setup
```

Bağlantı aracı NASA’nın resmî Python örneğindeki `requests.Session` yöntemini kullanır: https://urs.earthdata.nasa.gov/documentation/for_users/data_access/python_user_token_script . Farklı sunucuya yönlendirmede Authorization başlığı aktarılmaz; sertifika doğrulaması kapatılmaz.

Açılan yerel penceredeki gizli alana anahtarı yapıştırıp bağlantıyı test edin. Araç üç gerçek korumalı veri bağlantısında yalnızca ilk32 baytı okumayı dener; büyük veri dosyalarını indirmez. En az bir erişim doğrulanınca anahtar Windows kullanıcı hesabına bağlı DPAPI ile şifrelenerek `.local/earthdata-token.bin` dosyasına saklanır. `.local/` Git dışında tutulur. Parola istenmez, anahtar sohbete veya normal çıktılara yazılmaz. TLS hatası, zaman aşımı, HTTP401 ve yönlendirme sorunları ayrı gösterilir. Gizli olmayan bağlantı sonucu `.local/earthdata-status.json` içinde tutulur.

Tekrar erişim kontrolü:

```powershell
python -m analysis.earthdata_access --check
```

Bu yalnızca yetkili erişimi doğrular; MODIS/EMIT/Black Marble işlem hattının tamamlandığı anlamına gelmez. Oturum ayarlanması gerçek indirme, ürün kalite bantları, mekânsal işleme ve doğrulama adımlarından ayrıdır.

## Bu çalışmada gerçekten bulunan ama indirilemeyen ürünler

Salda çevresinde CMR sorguları gerçek granüller buldu; dosya indirme denemeleri EarthdataHTTP401 döndürdü. Sorgular, granülkimlikleri ve tam bağlantılar `data/source-registry.json`→`granule_access_checks` içinde; ham CMR yanıtları `data/provenance/granule-*.json` dosyalarında bulunuyor.

| Ürün | Gereken iş |
|---|---|
|MOD13Q1.061|NDVI, ölçek/NoData ve kalite bantlarıyla; sahaya ait geçerli dönemlerin seçilmesi. NDVI doğrudan bitki alanı oranı değildir.|
|EMITL2BMIN.002|Kapsam, mineral sınıfları ve kalite/belirsizlik alanları; MarsCRISM ile uyumlu mineral tanımı ve çözünürlük seçilmesi.|
|VNP46A2.2|Gece ışığı radyansı ve kalite maskeleri; bulut/ay ışığı gibi etkilerin denetlenmesi.|

Ek olarak MOD11A1.061 yüzey sıcaklığı, ASTGTM003/NASADEM ve uygun kalite katmanları değerlendirilmelidir. Pilotun erişilebilirASTERv2 önbelleğini kullanması en yeniDEM kullanıldığı anlamına gelmez.

## Hesaptan sonra uygulama sırası

1. Tanımlı AOI’ler için doğru dönem ve ürün sürümüyle granül kapsamını doğrulamak.
2. Yetkili indirme oturumuyla verileri almak; ham dosya hashleri ve ölçüm tarihlerini kaydetmek.
3. Ürünün ölçek, dolgu değeri ve kalite bantlarını uygulamak; ortak fiziksel ölçekte özellik çıkarmak.
4. Yeni özellikleri mevcut kapsam kontrollü skor bileşenlerine bağlamak ve yeniden hesaplamak.
5. Kontrol alanlarının gerçek bitki/arazi kullanımını doğrulamak; başarısız kontrolleri koruyarak doğrulamayı yinelemek.

PACE NDVI servisinin tarihe kilitlenmiş örnekleme istekleri bu ortamda zaman aşımına uğradı. ORNL MODIS API’sinde TLS/erişim sorunu görüldü. Earthdata hesabı bunların çalışacağını garanti etmez; doğrudan resmî ürün indirme yolu kullanılmalıdır. NEO, NASA’nın açıklamasına göre Eylül2026’da kapatıldığı için alternatif veri yolu olarak seçilmedi: https://science.nasa.gov/earth/nasa-earth-observations-neo/ .

Yeraltı buzu, mineral eşleşmesi, Ay/Mars termal karşılaştırması ve etkin çözünürlük harmonizasyonu ayrıca bilimsel yöntem gerektirir; hesap açılması bunları kendiliğinden tamamlamaz.
