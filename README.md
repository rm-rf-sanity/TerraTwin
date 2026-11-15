# TerraTwin

NASA Space Apps 2026 için Dünya’daki Ay ve Mars analoglarını araştıran iki dilli saha atlası ve tekrarlanabilir NASA veri analizi pilotu.

**Görev:** [Identify Earth Locations that Analog the Permanent Moon Base Locations and Mars](https://www.spaceappschallenge.org/2026/challenges/permanent-moon-base-locations-and-mars/)

## Çalışan özellikler

- 21 araştırma sahası ve5 tanılayıcı kontrol alanı; toplam26 Dünya penceresi ve2 gezegen hedefi.
- NASA servislerinden indirilen gerçek yükseklik ve 2025 günlük iklim verileriyle pilot hesaplama.
- Sınırları tanımlanmış Dünya çalışma alanları; adlandırılmış Ay ve Mars hedefleri; negatif kontrol alanları.
- Aynı 500 m örnekleme aralığında eğim, rölyef ve pürüzlülük karşılaştırması;52 gerçek arazi karşılaştırması.
- NASA HBASE2010 sınıflamasından25 düğümlü yerleşim/yol kontrolü; bilinmeyen noktaları sıfır saymadan alt/üst sınırlar.
- Görev ağırlıkları, ölçüt bazında açıklamalar, eksik veri kapsamı ve ağırlık duyarlılığı.
- Araştırma notlarından ayrı hesaplanmış sonuçlar; alan, eğim, iklim ve skor harita görünümleri.
- JSON, CSV ve Dünya alanları için GeoJSON dışa aktarımı.
- Türkçe/İngilizce, mobil görünüm, klavye ile kullanım.
- Yalnızca TerraTwin içeriğiyle ilgili soruları yanıtlayan site rehberi (sohbet penceresi); anahtarsız site içi arama ve isteğe bağlı Claude modu.

**Bilimsel kapsam:** Bu pilot sınırlı alanlarda arazi şekillerini karşılaştırır. 500 m örnekleme aralığı kaynakların etkin çözünürlüğünü eşitlemez. NDVI yalnızca kaliteyi geçen iki alanda kullanılır; Salda için EMIT mineral bağlamı ve ASTERv3 işlenmiştir. Altı gece ışığı gözlemi kalite eşiğini geçmediği için skor girdisi değildir. Mineral eşleşmesi, yeraltı buzu ve hedef termal analizi tamamlanmadığından tam analog uygunluğu doğrulanmış değildir. Görev skorları varsa kısmi operasyonel ön elemedir; NASA onayı, iniş güvenliği veya saha erişim izni değildir. Başarısız kontroller sonuçlardan çıkarılmaz.

## Earthdata entegrasyonu

Earthdata erişimi doğrulandı. 12 gerçek NASA dosyası (413,531,230 bayt) indirildi. Kalite eşiğini geçen NDVI: 2/26; gece ışığı: 0/26; ASTER v3: 1/26. Salda için kalite/maske/belirsizlik bilgili EMIT spektral mineral bağlamı üretildi.

Ham dosyalar ve erişim anahtarı Git dışında `.local/` altında tutulur. `data/protected-evidence/` içindeki küçük gerçek piksel/QA kesitleri, tekrar giriş veya büyük dosyalar olmadan aynı ölçümleri üretir. Ürünler farklı gözlem dönemlerine sahiptir; yıllık ortak bir kompozit sayılmaz.

## Yerelde çalıştırma

Python 3.10+ ve içerik/tarayıcı kontrolleri için Node.js 22+ yeterlidir. Analiz Python standart kütüphanesiyle çalışır; Earthdata hesabı veya API anahtarı gerektirmez.

```powershell
cd "$env:USERPROFILE\Downloads\TerraTwin"
python -m http.server 5173 --bind 127.0.0.1
```

Tarayıcı: <http://127.0.0.1:5173/>. Sitede gösterilen sonuçlar `site/analysis-results.json` dosyasından okunur; sayfayı açmak her ziyaretçi için yeniden uydu verisi indirmez.

Python kurulu olmayan Windows makinelerde aynı işi PowerShell yapar (adres: <http://localhost:5173/>):

```powershell
powershell -ExecutionPolicy Bypass -File .claude\serve.ps1
```

## Site rehberi (sohbet botu)

Sayfanın sağ altındaki **Soru sor** düğmesi TerraTwin Rehberi’ni açar. Rehber yalnızca bu projeyle ilgili soruları yanıtlar; konu dışı soruları geri çevirir. İki modu vardır:

- **Site içi arama (varsayılan):** Hesap, anahtar veya sunucu gerektirmez. Soruyu sitedeki metinlerle (bölümler, 21 saha, veri kataloğu, yöntem, pilot analiz özeti) eşleştirir ve ilgili içeriği gösterir. Yapay zeka değildir; pencere başlığında bu açıkça yazar.
- **Yapay zeka (Claude):** `site/chat-config.js` içindeki `endpoint` doluysa sorular bir ara sunucu üzerinden Claude’a gider. Ara sunucu API anahtarını tarayıcıdan gizler, modele yalnızca TerraTwin hakkında ve yalnızca sitedeki içeriğe dayanarak yanıt verme kuralını uygular. Yapay zeka yanıt veremezse rehber kendiliğinden site içi aramaya döner.

Dosyalar: `site/chat.js`, `site/chat.css`, `site/chat-config.js` ve `worker/terratwin-chat-worker.js`. Rehber `site/data.js` dosyasına dokunmaz; kendi arayüz metinlerini `site/chat.js` içinde taşır.

### Yapay zeka modunu açma

1. [Anthropic Console](https://platform.claude.com/) üzerinde bir API anahtarı oluşturun ve hesabınıza aylık harcama sınırı koyun.
2. Cloudflare panelinde **Workers & Pages → Create → Worker** ile boş bir Worker oluşturun, **Edit code** ekranında örnek kodu silip `worker/terratwin-chat-worker.js` dosyasının tamamını yapıştırın ve **Deploy** edin.
3. Worker’ın **Settings → Variables and Secrets** bölümünde `ANTHROPIC_API_KEY` adıyla bir **Secret** ekleyin. İsteğe bağlı: `ALLOWED_ORIGINS` (sitenin adresi; boşsa her adresten istek kabul edilir) ve `MODEL`.
4. Worker adresini (`https://…workers.dev`) `site/chat-config.js` içindeki `endpoint` alanına yazın.
5. Kontrol: Worker adresini tarayıcıda açınca `{"service":"terratwin-chat","configured":true}` görünmelidir.

Varsayılan model `claude-opus-5-5`’tir; `MODEL=claude-haiku-5-5` çok daha ucuzdur. Ara sunucu her adres için 10 dakikada 20 soru sınırı uygular; bu sınır en iyi çabayla çalışır, asıl güvence Anthropic hesabındaki harcama sınırıdır. API anahtarını hiçbir zaman `site/` altındaki dosyalara yazmayın.

### İçerik değişince

Ara sunucu sitedeki içeriğin bir kopyasını taşır. `data/content.json` veya analiz sonuçları değiştiğinde siteyi yerelde açın, rehber penceresini bir kez açın, tarayıcı konsolunda `copy(TTChat.workerKnowledge())` çalıştırın, kopyalanan metni `worker/terratwin-chat-worker.js` içindeki `KNOWLEDGE_START` ve `KNOWLEDGE_END` satırları arasına yapıştırın ve Worker’ı yeniden yayınlayın. Site içi arama modu için bir şey yapmak gerekmez; içeriği sayfadan okur.

## Korunan dosyaları işleme ortamı

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r analysis/requirements-protected.txt
.\.venv\Scripts\python.exe -m analysis.protected_download --offline --all-recorded
.\.venv\Scripts\python.exe -m analysis.protected_features
.\.venv\Scripts\python.exe -m analysis.dem_v3
```

Ham dosyalar başka bilgisayarda yoksa Earthdata oturumuyla `--offline` olmadan indirin. Paylaşılan küçük kanıtlardan tekrar üretmek için `python -m analysis.protected_features --evidence-only` kullanılır (bilimsel ortamda). Ana skor hesaplama modülü stdlib ile mevcut çıkarım JSON’larını okuyabilir. `node scripts/verify.mjs --browser` yerel `.venv` Python’unu otomatik seçer.

## Analizi tekrar üretme

```powershell
python -m analysis.run
```

İlk çalıştırma gerçek NASA yanıtlarını `data/cache/` altında saklar. Sonraki çalıştırma doğrulanmış önbelleği kullanır. Ağsız yeniden hesaplama ve bilinçli veri yenileme:

```powershell
python -m analysis.run --offline
python -m analysis.run --refresh
```

İndirme başarısızlıkları ve eksik özellikler çıktıya açıkça yazılır. `--refresh` servislerin erişilebilirliğine bağlıdır; işlem tarihinin yeni olması gözlemin yeni olduğu anlamına gelmez.

- Deney tanımı ve analiz alanları: `data/project.json`.
- Hesaplanmış sonuç: `site/analysis-results.json`.
- Ham yanıtlar ve SHA-256 bilgileri: `data/cache/`.
- İşlem ve kaynak kaydı: `data/provenance.json`.
- Gövde bilgisi taşıyan tüm çalışma alanları: `data/analysis-areas.geojson`. Ay/Mars koordinatları Dünya koordinatı olarak kullanılmamalıdır; siteden GeoJSON dışa aktarımı yalnızca Dünya alanlarını verir.
- Kaynak/sürüm denetimi: `data/source-registry.json` ve `docs/source-audit.md`.
- Hesaplama ayrıntıları: [analysis/README.md](analysis/README.md).
- 16 gereksinimin dürüst durum tablosu: [docs/implementation-status.md](docs/implementation-status.md).
- Hesap açıldıktan sonraki veri adımları: [docs/earthdata-next-steps.md](docs/earthdata-next-steps.md).

## NASA kaynak politikası

Sayısal veri indirmeleri yalnızca `nasa.gov` ve alt alanlarındaki resmî servislerden yapılır. Başka Space Apps takımlarının veri veya sonuçları kullanılmaz. NASA/METI ortak ASTER ürünü ortaklığıyla, tarihsel HBASE de NASA/SEDAC ürünü olarak belirtilir. Hanksville ve Pilbara kartları resmî NASA/NTRS kaynaklarıyla yeniden kaynaklandırılmıştır. D3, TopoJSON, world-atlas ve yazı tipleri sunum bağımlılıklarıdır; bilimsel skor girdisi değildir.

Erişilebilen NASA WorldWind Dünya katmanı **ASTER GDEM v2** önbelleğidir; katalogda bulunan v3 ile aynı değildir. Ay LOLA ve Mars MOLA ürünleri tarihsel görevlerden türetilmiştir. Güncel servis erişimi, ürün sürümü ve gözlem dönemi ayrı kaydedilir. Bu nedenle tüm verilerin 2026 ölçümü veya her ürünün en yeni işleme sürümü olduğu iddia edilmez. Salda artık gerçek ASTERv3DEM+NUM ile, diğer sahalar henüz WorldWindv2 ile işlenir.

## İçeriği güncelleme

Site metinleri, saha kartları, kaynak bağlantıları ve katalog için tek düzenleme kaynağı `data/content.json` dosyasıdır. Tarayıcı paketi deterministik üretilir:

```powershell
node scripts/build_content.mjs
node scripts/build_content.mjs --check
```

`site/data.js` üretilmiş dosyadır; doğrudan düzenlenmemelidir. `data/project.json` deney seçimlerini, toleransları ve görev ağırlıklarını tanımlar; içerik/model tutarlılık kontrolü değişikliklerin birbirinden kopmasını yakalar. `arastirma/` içindeki özgün raporlar tarihsel araştırma belgeleri olarak korunur; yeni hesaplanmış sonuçların yerine geçmez ve kendiliğinden güncellenmez.

## Kontroller

Önbellekten analizi yeniden üretip tüm yazılım/içerik/veri bütünlüğü kontrollerini tek komutla çalıştırmak için `node scripts/verify.mjs` kullanın. Yerel sunucu açıkken `--browser` eklemek tarayıcı kontrolünü de çalıştırır. Ayrı komutlar:

```powershell
python -m unittest discover -s tests -p "test_*.py"
node --test tests/frontend.test.cjs
node scripts/build_content.mjs --check
node scripts/check_project.mjs
```

Yerel sunucu açıkken gerçek Chromium tarayıcısıyla etkileşim, dışa aktarım ve mobil kontrol:

```powershell
node scripts/verify_site.mjs
```

Kontrol aracı varsayılan olarak Windows Chrome yolunu kullanır. Başka kurulumda `CHROME_PATH`, başka portta `TERRATWIN_URL` ortam değişkenini ayarlayın. Tarayıcı geçici ayrı profille görünmez başlatılır; kişisel tarayıcı oturumu değiştirilmez. Ekran görüntüleri ve deneme dışa aktarımları geçici klasöre yazılır.

## Araştırma belgeleri

- [Birleşik rapor](arastirma/ay-mars-analog-birlesik-rapor.md)
- [NASA veri ürünleri ve yöntem araştırması](arastirma/NASA_Space_Apps_2026_Arastirma_TR.md)
- [Ayrıntılı analog araştırması](arastirma/ay-mars-analog-yerler-detayli-arastirma.md)
- [Kaynak bağlantıları](arastirma/kaynaklar.json)
- [Özgün veri kataloğu](arastirma/veri_katalogu.json)

Lisans: [MIT](LICENSE). NASA veri ürünlerinin kendi kaynak, atıf ve kullanım koşulları ayrıca geçerlidir.
