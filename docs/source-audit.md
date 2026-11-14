# NASA kaynak ve veri erişimi denetimi

Denetim tarihi: 14 Kasım 2026. Makine tarafından okunabilir kayıt: `data/source-registry.json`. Resmî servis yanıtlarının anlık kopyaları ve SHA-256 özetleri `data/provenance/` klasöründedir.

## Kaynak politikası

Bilimsel ölçüm ve analiz girdileri resmî NASA servislerinden alınır. NASA/METI ASTER ve NASA/ISRO NISAR gibi ortak ürünler ortaklıkları belirtilerek tanımlanır. Başka Space Apps takımlarının verileri, skorları veya sonuçları bu çalışmada kullanılmamıştır. D3, TopoJSON, dünya kıta çizgileri ve yazı tipleri yalnızca yazılım/sunum bağımlılıklarıdır; bilimsel analiz kanıtı sayılmaz.

`arastirma/` içindeki mevcut belgeler önceki araştırmanın tarihsel kopyalarıdır. Site kartındaki bir düzeltme bu belgelerdeki her cümlenin yeniden doğrulandığı anlamına gelmez. Hesaplamaya hangi ürünün gerçekten girdiği, ürün keşif kataloğundan ayrı kaydedilir.

## Çalıştığı doğrulanan sayısal servisler

| Kaynak | Gerçekte doğrulanan erişim | Kullanım sınırı |
|---|---|---|
| NASA WorldWind `aster_v2` | WMS GetMap, `application/bil16`; 20 × 20 hücre için 800 bayt ve makul metre cinsinden yükseltiler | Eski ASTER GDEM V2 önbelleği; güncel V3 olarak sunulamaz. |
| NASA Moon Trek LOLA | `LRO_LOLA_DEM_Global_256ppd_v06/ImageServer`; canlı servis metaverisi ve getSamples | Bölgesel/küresel tarihsel DEM; en yeni yerel kutup DEM’i değildir. |
| NASA Mars Trek MOLA | `mola128_mola64_merge_90Nto90S_SimpleC_clon0/ImageServer/getSamples`; Jezero yakınında -2594 m örneği | ~128 piksel/derece ızgara; küçük kaya/iniş tehlikesi analizi değildir. |
| NASA POWER | T2M ve PRECTOTCORR JSON isteği HTTP 200 | Bölgesel yeniden analiz; 2 m hava sıcaklığı yüzey sıcaklığı değildir. |

WorldWind örnek isteği:

```text
https://worldwind26.arc.nasa.gov/elev?SERVICE=WMS&VERSION=1.1.1&REQUEST=GetMap&LAYERS=aster_v2&STYLES=&SRS=EPSG:4326&BBOX=29.6,37.5,29.7,37.6&WIDTH=20&HEIGHT=20&FORMAT=application/bil16
```

WMS 1.1.1 için BBOX sırası batı, güney, doğu, kuzeydir. Yanıt little-endian işaretli 16 bit yükselti verisi olarak okunur. `aster_v2` üst katmanı kullanılmalıdır; ölçeğe bağlı alt katmanlardan biri testte sıfır döndürmüştür. Sıfır otomatik olarak eksik veri değildir; deniz düzeyini de temsil edebilir. ASTER boşluk işareti -9999 ve tamsayı uç değerleri analiz dışında tutulmalıdır.

Resmî servis yapılandırmaları: [Moon Trek](https://trek.nasa.gov/moon/jpl/config/config.json), [Mars Trek](https://trek.nasa.gov/mars/jpl/config/config.json). WorldWind katmanları: [WMS GetCapabilities](https://worldwind26.arc.nasa.gov/elev?service=WMS&request=GetCapabilities).

## Güncellik: servis sürümü ile gözlem tarihi farklıdır

NASA CMR koleksiyon sorguları bu denetimde canlı çalıştırıldı. Aşağıdaki sürümler katalogda bulundu; bu, her analiz alanında kaliteli granül bulunduğu veya hepsinin indirildiği anlamına gelmez.

| Kısa ad | Katalogda bulunan sürüm | Gözlem dönemi metaverisi |
|---|---|---|
| ASTGTM | 003 | 1 Mart 2000–30 Kasım 2013 |
| NASADEM_HGT | 001 | 11–21 Şubat 2000 |
| EMITL2BMIN | 001 ve 002 | 9 Ağustos 2022’den itibaren; 002 için açık uçlu |
| EMITL3ASA | 001 ve 002 | 002 için 10 Ağustos 2022–20 Ocak 2024 |
| MOD11A1 | 061 | 24 Şubat 2000’den itibaren |
| HLSL30 | 2.0 | 11 Nisan 2013’ten itibaren |
| HLSS30 | 2.0 | 28 Kasım 2015’ten itibaren |
| VNP46A2 | 2 | 19 Ocak 2012’den itibaren |

Örnek [ASTER CMR sorgusu](https://cmr.earthdata.nasa.gov/search/collections.json?short_name=ASTGTM&page_size=20). ASTER V3 iyileştirilmiş güncel katalog ürünüdür; pilotun V2 önbellek kullanması bilimsel bir sınırlamadır. V3 ile yeniden çalıştırılmadan “en güncel DEM ile tamamlandı” denemez. [NASA ASTER V3 kılavuzu](https://www.earthdata.nasa.gov/s3fs-public/2025-04/ASTGTM_User_Guide_V3.pdf).

## Ay hedefinin adı ve koordinatı

NASA’nın 26 Mayıs 2026 duyurusu Moon Base I için Shackleton Connecting Ridge hedefini belirtir. Bu bir görev hedefidir; tamamlanmış kalıcı üssün hassas inşaat sınırı değildir. [NASA duyurusu](https://www.nasa.gov/news-release/nasa-provides-update-on-moon-base-rovers-landers-missions/).

NASA Lunar Surface Data Book, Rev A, Tablo A2-2’de Connecting Ridge (R01 / Site01) merkezi **89.4632° güney, 137.49° batı** olarak yer alır. Doğu-pozitif sayısal gösterim `lat=-89.4632, lon=-137.49` şeklindedir. Pilot bu merkez çevresinde analistin tanımladığı pencereyi kullanabilir; pencere sınırı NASA tarafından onaylanmış iniş alanı değildir. [NASA referans kitabı, s.58](https://ntrs.nasa.gov/api/citations/20230007818/downloads/ACD-50044%20Lunar%20Surface%20Data%20Book%20Rev%20A.pdf?attachment=true).

NASA’nın bağımsız bir termal kule çalışmasında yakın bir SCR noktası `-89.46752, -138.012788` olarak kullanılmıştır. Bu da bölgenin yaklaşık boylamını destekler. [NASA kule çalışması](https://ntrs.nasa.gov/api/citations/20240009936/downloads/TDEA%20TSPD%20Tall%20Tower%20Lunar%20Thermal%20Analysis%20v3.pdf).

## Saha kaynaklarında yapılan düzeltmeler

- **Hanksville:** NASA NTRS 20110014304, Kasım 2009 DOMEX yeraltı örnekleme/robotik çalışmasının NASA-MMAMA desteğini belgeliyor. Sitedeki doğrulanmamış yıllık yağış ve ortalama sıcaklık sayıları kaldırıldı; yerine bu resmî dayanak eklendi. [NASA NTRS](https://ntrs.nasa.gov/citations/20110014304).
- **Pilbara:** NASA Astrobiyoloji kataloğu bölgeyi eski Dünya saha araştırmaları içinde listeliyor. Kart buna göre yeniden kaynaklandırıldı; bölgesel koordinat belirli bir fosil sahasının kesin yeri olarak sunulmuyor. [NASA saha kataloğu](https://astrobiology.nasa.gov/research-locations/).
- Her iki kart da değerlendirilmemiş skorlarını koruyor. Kaynak bulunması, sayısal benzerliğin doğrulandığı anlamına gelmez.
- Jezero kartındaki Mars genel sıcaklık bağlamı yerel Jezero ölçümü olarak sunulmamalı; yaklaşık 33 K ifadesi de bütün Ay hedefinin sıcaklığı sayılamaz.

## Karşılaştırılabilirlik ve açık eksikler

Aynı 500 m örnekleme aralığı, üç kaynağın etkin çözünürlüğünü ve hata yapısını eşitlemez. Özellikle kutuplarda boylamın metre karşılığı değişir; Ay ve Mars için Dünya yarıçapı kullanılamaz. Mutlak yükseltiler farklı referans yüzeylerine dayanır; şekil/eğim/rölyef karşılaştırmaları tercih edilmelidir.

Küçük eğim, tek başına iniş güvenliği veya geçilebilirlik kanıtı değildir. Mineral, buz, bitki örtüsü, gece ışığı ve yerel sıcaklık verisi gerçekten işlenmedikçe bunlar eksik kalmalıdır. Kontrol sonuçları başarısızsa korunmalıdır; analoğun doğrulandığı ilan edilmemelidir.

Görev sayfasına bu denetimde iki web isteği HTTP 502 döndürdü. Kullanıcının verdiği bağlantı korunmuştur; canlı görev metninin bu denetimde yeniden okunabildiği iddia edilmez.


## NDVI ve yerleşim: ek resmî servisler

NASA Earthdata GIS kataloğundaki PACE OCI LANDVI servisi, tek bantlı Float32 `ndvi` değişkeni sunuyor. Varsayılan getSamples sorgusunda Salda için 0.207548469, İstanbul için 0.139735565 ve Amazon ormanı (-62.5°, -3.5°) için 0.607282102 değerleri döndü. Bunlar renk kodu değil, fiziksel NDVI değerleridir; ek MODIS 0.0001 ölçeği uygulanmamalıdır. İlgili ilk yanıt rasterId118 idi; bu varsayılan rasterın tarihini doğrulamadan Haziran2025 olarak etiketlemek doğru değildir. [Resmî NASA PACE ürün anlatımı](https://nasa.github.io/oceandata-notebooks/notebooks/oci/oci_terrestrial_data.html).

Katalog sorgusu Haziran2025 için `ndvi` değişkenli V3_1 2km 8-günlük dosyaları doğruladı: raster58 (2–9Haziran),59 (10–17Haziran),60 (18–25Haziran),61 (26Haziran–3Temmuz). Buna karşın bu rasterları kilitleyen sayısal örnekleme istekleri ve bazı tarih/metaveri sorguları20–30saniyede zaman aşımına uğradı. Uygulama her yanıtta gerçek rasterId/tarihi kontrol etmeli; başarısız isteği sentetik NDVI ile doldurmamalıdır. Tek8günlük anlık görüntü yıllık bitki örtüsü veya arazi kullanım sınıfı değildir. Kaynak çözünürlüğü yaklaşık0.0208333°/2km; tek tek kalite bayrakları bu arayüzde sunulmuyor.

NASA SEDAC HBASE katmanı ise canlı sayısal örneklerde Salda ve Amazon ormanı için200, İstanbul için201 döndürdü. Resmî NASA portalındaki açıklama kodları doğruluyor:

| DN | Anlamı |
|---|---|
|200|HBASE değil|
|201|İnsan yapımı yerleşim/yapılaşma|
|202|Yol|
|255|Eksik veri, bulut veya gölge|

200 değeri su anlamına gelmez ve bölgenin bitkisiz olduğunu göstermez. Katman Landsat’tan üretilmiş2010 hedef yıllı tarihsel bir üründür; güncel2025/2026 kent sınırları sayılamaz. Antarktika ve bazı küçük adalar kapsam dışındadır. Sınırlı sayıda örnekleme düğümünün oranı, bütün30m pikseller üzerinden hesaplanan kesin alan oranı olarak sunulmamalıdır. [NASA HBASE servis açıklaması ve lejantı](https://gis.earthdata.nasa.gov/portal/home/item.html?id=771a3adbe22f48eaafacf18ec8ba8127).

Eşlik eden NASA GMIS ürününde0–100 arası değerler geçirimsiz yüzey yüzdesi,200 HBASE dışı ve255 eksik veri kodudur. Bu ürün yeni yapılmış binaların güncel haritası değildir. [NASA GMIS açıklaması](https://gis.earthdata.nasa.gov/portal/home/item.html?id=921b3fc59ef2439087cd77ca61f32117).

## Oturum açma gereksinimi ve çalışmayan alternatiflerin kanıtı

Salda çevresinde gerçek CMR granülleri bulundu: MOD13Q1.061, EMITL2BMIN.002 ve VNP46A2.2. Her biri için gerçek HTTPS veri bağlantısına kimlik bilgisi olmadan küçük Range isteği yapıldı. Üçü de `urs.earthdata.nasa.gov` üzerindeHTTP401 döndürdü. Granülün bulunması verinin indirildiği anlamına gelmez. Ham CMR metaverisi `data/provenance/granule-*.json` dosyalarında, bağlantılar ve deneme sonuçları kaynak kaydında saklanıyor. Kimlik bilgisi oluşturulmadı veya gönderilmedi.

ORNL DAAC TESViS dokümantasyonu açık ve NASA Earthdata tarafından resmî MODIS erişim yolu olarak gösteriliyor. Ancak bu ortamda canlı API; Python’da sertifika zinciri doğrulama hatası, Windows Invoke-WebRequest’te25saniye zaman aşımı, curl’de20saniye sonundaHTTP000 verdi. TLS doğrulaması kapatılmadı. Dokümantasyona göre eşzamanlı altküme isteği en fazla10kompozit tarih içerebilir; tüm yıl tek istekle istenmemelidir. [ORNL API dokümantasyonu](https://modis.ornl.gov/data/modis_webservice.html), [NASA erişim açıklaması](https://forum.earthdata.nasa.gov/viewtopic.php?t=3534).

NASA NEO alternatifi güncel çalışan bir veri servisi değildir: resmî sayfa Eylül2026’da hizmetin kapatıldığını bildiriyor. Eski CSV/floating-point GeoTIFF çıktıları da NASA’nın açıklamasına göre basitleştirilmiş, yeniden örneklenmiş eğitim/görselleştirme ürünleriydi; orijinal araştırma verisinin yerine geçirilmedi. [NEO kapanış bilgisi](https://science.nasa.gov/earth/nasa-earth-observations-neo/), [NEO veri biçimleri açıklaması](https://neo.gsfc.nasa.gov/blog/2020/12/23/raster-and-floating-point-geotiffs-what-is-the-difference/).

## Uygulamada kullanılan ek kaynak ve kontrol düzeltmesi

HBASE ana analiz hattına bağlandı. Her Dünya alanında25 düğüm okunur; eksik değerlerin sıfır sayılmasını önlemek için yapılaşma/yol örneklerinin alt/üst sınırı saklanır. Doğrulanmış alt sınır%50 veya üzerindeyse yalnızca görev profili skoru dışlanır; ham arazi karşılaştırması korunur. Bu deneysel eşik NASA standardı değildir. NDVI ana skora bağlanmadı.

HBASE denetimi ilk taslaktaki iki kontrol etiketini yanlışladı: (-3.1,-60.0) Manaus kenti, (37.87,32.55) Konya kentidir. İkisi silinmeden kent kontrolü olarak korundu. Ayrı Amazon(-3.5,-62.5) ve Konya doğusu(37.75,32.8) orman/tarım aday pencereleri eklendi. Bunların2010 örneklerinde yapılaşma kodu bulunmadı; bu tek başına güncel orman veya tarım sınıfını kanıtlamaz. Bu revizyon nedeniyle kontroller bağımsız, önceden ayrılmış saha doğrulaması olarak sunulmaz.
