# İstenen16 gereksinimin uygulama durumu

Bu belge yazılımın çalışmasını bilimsel hipotezin doğrulanmasından ayırır. “Yapıldı” bir modelin doğru bulunduğu veya bütün NASA ürünlerinin işlendiği anlamına gelmez.

| # | Gereksinim | Mevcut karşılık | Kalan sınır |
|---|---|---|---|
|1|Kesin analiz alanları|26 Dünya penceresi ve2 gezegen alanının merkez/poligonları `data/project.json` ve GeoJSON’da|10km sınırlar analist seçimi; resmî iniş alanı değil|
|2|Deney amacı|500m aralıkta arazi geometrisi karşılaştırması ve ayrı deneysel operasyonel ön eleme|Mineral/yaşam/buz deneylerinin tam modeli henüz yok|
|3|Gerçek veri edinme|NASA DEM, POWER, HBASE ve12 gerçek korumalı ürün; piksel/QA kanıtları|Earthdata erişimi açıldı; NDVI kalite/ayakizi sınırlı, NTL kalite eşiğini geçmedi; ASTERv3 yalnızcaSalda|
|4|Kalite kontrolü|NoData, sayısal aralık, takvim, birim, geçerli düğüm ve hash kontrolleri|ASTERv2 önbelleğinde NUM/hata katmanı yok; bütün ürünlerin kalite maskesi henüz yok|
|5|Karşılaştırılabilirlik|Metre birimleri, gökcismi yarıçapı, ortak500m örnekleme ve10km pencereler|Etkin çözünürlük/PSF ve hata dağılımı tam eşitlenmedi|
|6|Özellik hesapları|Eğim, rölyef, pürüzlülük, düşük eğim oranı, iklim, tarihsel yapılaşma alt/üst sınırı|NDVI2alan veEMITbağlamı var; Marsmineral eşleşmesi, yeraltı buzu, kullanılabilirNTL ve hedef termal ölçümler eksik|
|7|Benzerlik hesabı|Gerçek Dünya/hedef değerlerinden Gaussian bileşenler ve kapsam kontrollü ağırlıklı skor|Toleranslar deneysel; NASA standardı/kalibrasyon sonucu değil|
|8|Ağırlık–sonuç bağlantısı|Görev düğmeleri gerçek hesaplanmış görev sonuçlarını değiştiriyor|Eksik kapsamda skor bilinçli olarak kapalı|
|9|Doğrulama|Referans/kontrol karşılaştırmaları, üst%10 ve şehir elemesi çalıştırıldı|Jezero referans-medyan testi başarısız; tam bilimsel doğrulama sonuçlandırılamadı|
|10|Aday değerlendirmesi|21 araştırma sahası ve5 kontrol için52 gerçek arazi karşılaştırması|Yeni bir analoğun keşfedildiği kanıtlanmadı; saha/erişim araştırması yok|
|11|Harita sonuçları|AOI, skor, eğim, sıcaklık, yağış ve tarihsel yapılaşma alt sınırı katmanları|Seçilmiş pencereler; küresel raster tarama veya alanlar arası enterpolasyon değil|
|12|Açıklanabilirlik|Ham Dünya/hedef değerleri, sigma, bileşenler, ağırlıklar, katkı, kapsam, duyarlılık, eleme gerekçesi|Ölçüm belirsizliğinin tam yayılımı yok|
|13|NASA kaynak politikası|Sayısal indirmelerde NASA alan adı sınırı; Hanksville/Pilbara resmî kaynakları düzeltildi|Özgün raporlar tarihsel belge; yeni skor girdisi sayılmıyor|
|14|Sürüm ve tekrar üretim|URL/istek, ürün, dönem, SHA-256, kod/yapılandırma hashleri; çevrimdışı tekrar|Bazı tarihselDEM servisleri piksel bazında edinim tarihi sunmuyor|
|15|Doğru site metinleri|Çalışmayan küresel hesaplama/maskeye dair ifadeler düzeltildi; README yenilendi|Tam model tamamlanmış gibi sunulmuyor|
|16|İçerik tutarlılığı|`data/content.json`→üretilen`site/data.js`; model/içerik/çıktı/hash entegrasyon kontrolü|Araştırma metni değişirse bilimsel editör incelemesi gerekir; otomatik metin yorumlama yok|

## Doğrulama sonucu

80 Python birim testi ve4 JavaScript testi geçti. Gerçek Chrome’da dil, saha seçimi, kategori/görev/hedef kontrolleri, şehir elemesi, JSON/CSV/GeoJSON indirme ve390px mobil yerleşim doğrulandı. Harici harita/yazı tipi bağımlılıkları engellendiğinde analiz paneli çalışmaya devam ediyor. Önbellekten ağsız hesaplama çalışıyor.

Bu kontroller yazılım davranışını doğrular. Bilimsel doğrulama toplam durumu `inconclusive` kalır: Shackleton referans/kontrol medyan kontrolü geçti; Jezero’da geçmedi. Sonuç zayıflığı çıktıdan silinmedi veya eşiği değiştirilerek gizlenmedi.

## Hesap gerektiren sonraki aşama

Kullanıcı Earthdata hesabını açtı. Yerel token bağlama ve korumalı erişim kontrol aracı eklendi; yetkili oturum ve gerçek dosya indirmeleri doğrulandı. [Giriş/kayıt ve kalan veri işleri](earthdata-next-steps.md) belgesinde somut sonraki adımlar bulunur. Bu nedenle “16 maddenin bütün bilimsel kapsamı tamamlandı” denemez; çalışan yazılım ve ölçülebilen pilot tamamlandı, korumalı veri pilot entegrasyonu tamamlandı; bütün sahalarda yeterli ürün/kalite kapsamı ve tam bilimsel doğrulama açık kaldı.

## Son tamamlanan aşama

Earthdata erişimi doğrulandı. 12 gerçek NASA dosyası (413,531,230 bayt) indirildi. Kalite eşiğini geçen NDVI: 2/26; gece ışığı: 0/26; ASTER v3: 1/26. Salda için kalite/maske/belirsizlik bilgili EMIT spektral mineral bağlamı üretildi.

HamAOI/QA kanıtlarından tekrar üretimde ölçümler birebir aynı bulundu. `node scripts/verify.mjs --browser`80Python+4JS testi, veri/kod/hash tutarlılığı, JSON/CSV/GeoJSON indirme,26alan,2hedef,390pxmobil ve harici harita bağımlılıkları kapalıyken analiz davranışını doğruladı. Bilimsel sonuç yine `inconclusive`; başarısız kontrol gizlenmedi.
