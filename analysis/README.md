# NASA veri analizi pilotu: protokol ve tekrar üretim

**Korunan veri aşaması:** Earthdata erişimi doğrulandı. 12 gerçek NASA dosyası (413,531,230 bayt) indirildi. Kalite eşiğini geçen NDVI: 2/26; gece ışığı: 0/26; ASTER v3: 1/26. Salda için kalite/maske/belirsizlik bilgili EMIT spektral mineral bağlamı üretildi.

Ürün işleme kuralları `docs/protected-products.md`, indirme kayıtları `data/protected-manifest.json`, gerçek AOI/QA kesitleri `data/protected-evidence/`, çıkarımlar `data/protected-features.json` ve `data/dem-v3-features.json` içindedir.

Bu modül, seçilmiş Dünya alanlarını adlandırılmış Ay ve Mars alanlarının arazi şekilleriyle karşılaştırır. Veri ürünü değerleri gerçek resmî NASA servislerinden alınır. Ölçülmeyen özellikler `null` kalır. Bir NASA açıklamasında bir yerin analog olarak anılması, bu modülün verdiği sayısal skoru doğrulamaz.

## Deney tanımı

Yetkili tanım `data/project.json` dosyasıdır: hedef merkezleri, Dünya sahaları ve kontrol alanları, 10 km alan boyutu, 21×21 örnekleme düğümü, 500 m düğüm aralığı, 2025-01-01–2025-12-31 iklim dönemi, ağırlıklar, toleranslar ve kapsam eşikleri burada kayıtlıdır. Hedef merkezleri NASA kaynaklarıyla ilişkilendirilir; çalışma penceresi boyutu analist seçimidir ve resmî iniş alanı sınırı değildir. İlk denetimde Manaus ve Konya merkezlerinin yanlışlıkla orman/tarım olarak adlandırıldığı görüldü. Bu noktalar kent kontrolü olarak korundu; ayrı orman/tarım aday pencereleri eklendi. Değişiklik yapılandırmada kayıtlıdır. Bunlar bağımsız, ayrılmış saha doğrulama seti değildir; yeni orman/tarım etiketleri güncel NDVI ile henüz doğrulanmadı.

## Veri edinme ve köken kaydı

- Dünya yükseklik: NASA Ames WorldWind `aster_v2`, WMS 1.1.1, `application/bil16`, little-endian signed16.
- Ay yükseklik: NASA Trek LOLA global DEM v06, ImageServer `getSamples`.
- Mars yükseklik: NASA Trek MOLA128/MOLA64 birleşik DEM, ImageServer `getSamples`.
- Yerleşim: NASA Earthdata GIS üzerinden NASA/SEDAC HBASEv1,2010 hedef yıllı sınıflama.
- Dünya iklim bağlamı: NASA POWER günlük `T2M`, `T2M_MAX`, `T2M_MIN`, `PRECTOTCORR`; UTC günleri.

Her yanıtta tam URL, POST gövdesi varsa istek parametreleri, alınma zamanı, ürün/sürüm bilgisi, yanıt uzunluğu ve SHA-256 saklanır. Önbellek tekrar okunurken hash doğrulanır. `data/provenance.json`, kullanılan istekleri ve işlem kodu/yapılandırma hashlerini toplar. Başka takımlardan veya üçüncü taraf yeniden işlenmiş arazi servislerinden sayısal veri alınmaz.

Servis erişim tarihi, gözlem tarihi değildir. WorldWind ASTERv2 eski bir önbellektir; en yeni ASTGTM003 ürününün yerine geçmiş gibi gösterilmez. LOLA/MOLA da tarihsel görev gözlemlerinden türetilmiştir. Dikey datumlar farklı olduğundan gezegenlerin mutlak yükseklikleri birbirine eşitlenmez; yerel şekil özellikleri kullanılır.

## Mekânsal karşılaştırma

Her gökcisminin yarıçapı kullanılarak 500 m yerel düğüm aralığı kurulur. Dünya WMS örnekleri enlem-boylam piksel merkezlerinden okunur; Ay/Mars için yerel uzaklıklar küresel geometriyle koordinata çevrilir. Alan sınırları ve bütün örnek düğümleri çıktıda saklanır.

Bu işlem ortak örnekleme aralığı sağlar; kaynakların etkin çözünürlüğünü, hata dağılımını veya frekans içeriğini eşitlemez. Özellikle kutup alanları ve farklı DEM kaynaklarının karşılaştırılması keşif niteliğindedir. Tam bilimsel harmonizasyon için ortak fiziksel filtreleme, etkin çözünürlük/DEM hata katmanları ve ölçek duyarlılığı ayrıca gerekir.

## Gerçek veriden çıkarılan özellikler

- **Medyan eğim:** iç düğümlerde iki yönde merkezi yükseklik farkı; `atan(sqrt(gx²+gy²))` dereceye çevrilir. 500 m aralıkta türev iki komşu arasında yaklaşık1 km tabana sahiptir.
- **Rölyef:** alandaki yüksekliklerin %95 ve %5 yüzdelikleri arasındaki fark. Doğrudan sırt–krater ilişkisi tespiti değildir.
- **Pürüzlülük:** düğüm yüksekliğinin 3×3 komşuluk ortalamasından farkının RMS değeri.
- **Düşük eğim oranı:** geçerli iç düğümlerde eğim5° altında olanların oranı. İniş güvenliği veya taş/blok tehlikesi ölçümü değildir.
- **İklim:** ortalama2 m hava sıcaklığı, günlük yağış toplamı, ortalama günlük maksimum–minimum hava sıcaklığı farkı ve minimumu0°C altındaki gün sayısı. Bunlar uydu yüzey sıcaklığı veya kalıcı donmuş zemin ölçümü değildir.
- **Gün uzunluğu:** enlem ve Dünya eksen eğikliğinden geometrik yaz gündönümü hesabı. Yerel ufku, kırılmayı ve Ay kutup aydınlanmasını temsil etmez.

DEM ve iklim için geçerli veri eşiği yapılandırmada bulunur. Eksik takvim günleri reddedilir; yıllık yağış eksik günlerden sessizce tamamlanmaz. Ölçülmeyen mineral, bitki örtüsü, buz ve gece ışığı alanları eksik kalır.

## Tarihsel yerleşim elemesi

10km pencere içinde5×5 sabit düğümden HBASE sınıfları okunur. NASA lejantına göre200 yapılaşma dışı,201 yapılaşma,202 yol,255 eksiktir. Boş dönen örnekler bilinmeyen kalır. Alt sınır `doğrulanmış yapılaşma+yol / istenen25düğüm`; üst sınır `(doğrulanmış+yapılaşma olabilecek bilinmeyen) /25` olarak hesaplanır. Bu, gerçek piksel alanı oranı değildir. Veri2010 hedef yıllıdır; güncel arazi kullanımı değildir.

Deneysel kuralda doğrulanmış alt sınır%50 veya üzerindeyse görev profili skorları yayımlanmaz. Ham arazi geometrisi karşılaştırması korunur; böylece kentsel bir alanın yalnızca şekil açısından benzer çıkması gizlenmez. Kural bir NASA standardı veya modelin bağımsız doğrulandığı anlamına gelmez. NDVI eşiği yalnızca tarih/kalite doğrulanmış MODIS ölçümü bulunan alanlarda etkindir; diğer alanlarda bitki elemesi tamamlanmış sayılmaz. `analysis/surface.py` içindeki NDVI okuma/ölçek kontrolleri testlidir; geçerli tarihli veri olmadan ana hatta çağrılmaz; artık iki alandaki gerçekMODIS NDVI görev ölçütüne bağlanır.

## İki ayrı skor türü

**Arazi pilotu:** eğim, rölyef ve pürüzlülük için `exp(-(x-target)^2/(2*sigma^2))`; üç bileşenin eşit ağırlıklı ortalaması0–100 olarak gösterilir. Üç özellik de mevcut olmalıdır. Sigma başlangıç değerleri `data/project.json` içinde bulunur; NASA standardı veya sonuçlarla kalibre edilmiş toleranslar değildir.

**Göreve göre operasyonel ön eleme:** mevcut yedi ölçütlü tasarımın ölçülebilen bileşenleri kullanılır. Eksik ölçütün ağırlığı kapsama katılmaz. Skor yalnızca ağırlıklı kapsam eşik üzerindeyse, mevcut ağırlıklara bölünerek hesaplanır. Bu nedenle farklı kapsamlı kısmi skorların karşılaştırılması dikkat gerektirir ve tam gezegen benzerliği olarak yorumlanamaz. Soğukluk/kuraklık endeksleri Dünya üzerindeki yönlü operasyonel göstergelerdir; hedef gezegenin sıcaklığına veya yağışına eşitlik değildir. Kullanılan dönüşümler kod ve çıktı açıklamalarında kayıtlıdır.

## Duyarlılık ve doğrulama

Her ağırlık sırayla±%20 değiştirilip toplam ağırlığa göre yeniden normalize edilir; sonuç aralığı raporlanır. Bu aralık istatistiksel güven aralığı veya DEM/iklim ölçüm belirsizliği değildir.

Tanılayıcı kontroller; bilinen analogların medyan skorunu negatif kontrollerle karşılaştırır ve kontrollerin en üst%10 içine girip girmediğini gösterir. Kontroller başarısız olduğunda sonuçlar aynen korunur; model geçerli ilan edilmez. Tarihsel HBASE kent elemesi görev profiline uygulanır; ham arazi skorunun bitkili/kentsel alanları kendiliğinden dışlayacağı varsayılmaz. Orman/tarım adaylarının güncel sınıfı NDVI ile doğrulanmadığı için kontrol yorumları sınırlıdır. Mineral, buz, bitki ve hedef termal ölçümler eksik olduğundan tam model doğrulaması sonuçlandırılamaz.

## Komutlar

```powershell
python -m analysis.run
python -m analysis.run --offline
python -m analysis.run --refresh
python -m unittest discover -s tests -p "test_*.py"
```

`site/analysis-results.json` arayüz sözleşmesidir. `data/project.json` değiştiğinde analizi yeniden üretin. Özgün araştırma belgeleri ve niteliksel saha notları hesaplama girdisi yerine geçmez.

## Yeni yönlü gösterge dönüşümleri

MODIS NDVI için bitkisizlik göstergesi `clamp(1-NDVI/0.6)`; kaliteyi geçen gece radyansı varsa yalıtılmışlık `exp(-radiance/5)` olarak tanımlıdır. Bunlar `scoring.proxyScales` içindeki analist tercihleridir; NASA standardı veya yaşam/iniş güvenliği kanıtı değildir. Şu an NTL kalite eşiğini geçen alan yoktur, bu bileşen eksik kalır. EMIT kütüphane eşleşmeleri mineral bolluğu veya Mars mineral eşleşmesi olarak kullanılmaz.
