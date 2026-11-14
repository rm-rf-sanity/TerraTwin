# TerraTwin — NASA Space Apps 2026 araştırma dosyası

**Konu:** Identify Earth Locations that Analog the Permanent Moon Base Locations and Mars  
**Araştırma kesim tarihi:** 14 Kasım 2026, Türkiye tarihi  
**Kaynak politikası:** Resmî görev metni, NASA yayınları, NASA veri servisleri ve NASA görevlerinin resmî arşivleri. Başka Space Apps takımlarının verileri, kodları, sonuçları ve proje fikirleri araştırmaya kaynak yapılmadı.  
**Çalışmanın niteliği:** Kaynak ve veri ürünü araştırması; bilimsel yöntem ve proje tasarımı önerisi. Bu dosyada raster indirilip analiz edilmiş saha sonuçları veya hesaplanmış benzerlik sıralaması bulunmuyor.

## 1. Ekibiniz için en önemli sonuç

TerraTwin’in savunulabilir amacı şu olabilir:

> Bir Ay veya Mars hedefinin belirli bir keşif ihtiyacı için, Dünya’da hangi küçük arazi parçalarının yararlı deney ortamı sağlayabileceğini NASA verileriyle araştırmak; eşleşmenin dayanaklarını, eksik verilerini ve geçerli olmadığı koşulları göstermek.

Bu bir **araştırma önerisidir**, NASA’nın onayladığı bir yöntem veya saha seçimi değildir. Yararlı çıktı, yalnızca benzeyen fotoğraflardan oluşan bir galeri yerine, veriden türetilmiş özelliklerle gerekçelendirilen bir karşılaştırma olabilir. İlk sürümde iki hedef profili yeterlidir: Ay güney kutbunda arazi/rota testi ve Mars’ta eski göl/evaporit süreçlerinin incelenmesi. Buz araştırmasını eklemek isterseniz ayrı bir profil olarak ele alın.

Türkiye odaklı başlangıç için **Nemrut kalderası ve Tuz Gölü’nü aday**, **Salda’yı bilinen karşılaştırma sahası** olarak öneriyorum. “Bu iki aday en iyi analogdur” sonucu çıkarılmadı. Bu tercih, aşağıda tanımlanan veri erişimi ve sınanabilir araştırma soruları üzerinden yapılmış bir çalışma önceliğidir.

## 2. Görev tam olarak ne istiyor?

Resmî görev, açık Dünya, Ay ve Mars verilerini kullanarak Dünya’da yararlı analog ortamlar tanımlayıp karakterize etmeyi istiyor. Tek bir alanı derinlemesine incelemek de, birkaç alanı karşılaştırmak da, sistematik arama yöntemi geliştirmek de kapsam içinde. Ürünün harita, rapor, uygulama veya başka bir anlatım biçimi olması mümkün. Önemli olan, benzerliğin hangi özelliklerde bulunduğunu ve nerede bozulduğunu açıklamak. [Resmî görev — Details](https://www.spaceappschallenge.org/2026/challenges/permanent-moon-base-locations-and-mars/?tab=details)

Görevin NASA kaynak listesi tarayıcıda doğrudan doğrulandı:

| Kaynak | Görevdeki rolü |
|---|---|
| [NASA Earthdata Search](https://search.earthdata.nasa.gov/) | Dünya gözlemlerini bulmak ve erişmek |
| [NASA Worldview](https://worldview.earthdata.nasa.gov/) | Uydu görüntüleri ve çevresel katmanları incelemek |
| [NASA Planetary Data System](https://pds.nasa.gov/) | Ay ve Mars görev verilerinin uzun dönem arşivi |
| [LRO resmî PDS arşivi](https://pds-geosciences.wustl.edu/missions/lro/) | Ay için çok araçlı gözlem koleksiyonu |
| [LRO Diviner](https://pds-geosciences.wustl.edu/missions/lro/diviner.htm) | Sıcaklık, kutup ve kaynak ürünleri |

Görev başka ajansların verilerine de izin veriyor; sizin isteğiniz doğrultusunda bu araştırmanın veri önerileri NASA ürünleri ve NASA görevleri üzerinden kuruldu. NASA’nın ortak ürettiği ürünler ayrıca belirtildi. [Resmî görev — Resources](https://www.spaceappschallenge.org/2026/challenges/permanent-moon-base-locations-and-mars/?tab=resources)

Global ödüller için, görevin Resources bölümünde yer alan NASA kaynaklarından en az birini kullanma koşulu organizasyonun resmî yanıtında açıklanıyor. “Kaynak linki koyduk” ile “veriyi analizde kullandık” ayrımını koruyun; sunumda kullanılan ürün, dosya ve işlemi gösterin. [NASA Space Apps organizasyon yanıtı](https://github.com/nasa/spaceapps/discussions/1849)

## 3. Güncellik denetimi: 14 Kasım 2026 itibarıyla

Bir sayfanın son düzenleme tarihi, uydunun ölçüm tarihi değildir. Dört tarihi ayrı kaydedin: **ölçüm zamanı, işleme/sürüm zamanı, yayımlanma zamanı, erişim zamanı**. “Bugün erişildi” ifadesi verinin bugün ölçüldüğünü göstermez.

| Konu | Doğrulanan güncel durum | Projeye etkisi |
|---|---|---|
| LRO genel arşivi | Release 67, 15 Eylül 2026’da yayımlandı; geciken Mini-RF kısmı 21 Eylül’de eklendi | Genel arşiv yayını ile her ürünün kapsadığı ölçüm dönemini ayrı kontrol edin |
| Diviner | Release 67 EDR/RDR ölçümleri 16 Mart–15 Haziran 2026 | Yeni ham/kalibre kayıtlar, eski birikimli haritaların da yenilendiği anlamına gelmez |
| LOLA | Release 67’de 24 Mart–13 Haziran 2026 ölçümleri bulunuyor | Ekibin veri düğümü PDS’nin üç aylık kopyasından daha sık güncellenebilir |
| MRO | 1 Eylül 2026 tarihli Release 78 duyurusu mevcut | CTX/HiRISE ürün kimlikleri ve ölçüm tarihleriyle çalışın |
| SHARAD | Release 78 radargram kapsamı 16 Kasım 2025–9 Şubat 2026; geciken EDR/RDR 4 Eylül’de yayımlandı | “2026’da yayımlandı” ile “2026’nın tamamını kapsıyor” farklıdır |
| MOLA | MEGDR/SHADR 25 Ağustos 2026’da sürdürülen PDS4 arşivine taşındı | Arşiv biçimi güncel; yükseklik ölçümleri yeni değil |
| EMIT | 19 Ekim 2026 resmî duyurusunda L2B mineral tanımlama V2 ve diğer yeni ürünler açıklandı | V001’i otomatik olarak en güncel ürün saymayın; yeniden işlenen arşivde AOI kapsamını kontrol edin |
| NISAR | L-band ilk açık bilim verisi yayını 20 Temmuz 2026; başlangıçta 17 Haziran ve sonrasındaki gözlemler | Yeni bir yardımcı veri seçeneği; tüm tarihlerin/sahaların hazır olduğunu varsaymayın |
| HLS | Resmî güncel açıklama V2.0’ı, 30 m ürünleri ve yaklaşık 2–3 günlük gecikmeyi tanımlıyor | Güncel yüzey durumu için iyi başlangıç; bulutsuz ölçüm garantisi değildir |

Kaynaklar: [LRO yayın takvimi](https://pds-geosciences.wustl.edu/missions/lro/), [Diviner](https://pds-geosciences.wustl.edu/missions/lro/diviner.htm), [LOLA](https://pds-geosciences.wustl.edu/missions/lro/lola.htm), [MRO Release 78](https://pds.nasa.gov/datasearch/subscription-service/SS-20260901.shtml), [SHARAD](https://pds-geosciences.wustl.edu/missions/mro/sharad.htm), [MOLA PDS4 geçişi](https://pds-geosciences.wustl.edu/missions/mgs/megdr.html), [EMIT Ekim 2026 duyurusu](https://forum.earthdata.nasa.gov/viewtopic.php?sid=dae91c5ef96f336491803c0490ce9060&t=8322), [NISAR resmî DAAC duyurusu](https://forum.earthdata.nasa.gov/viewtopic.php?p=26359&sid=c3064093e30bd71b2c255f9a1900719c&t=8068), [HLS erişim bilgisi](https://hls.gsfc.nasa.gov/data-access-and-tools/).

**Dikkat:** LROC, genel LRO teslimlerinden farklı olarak aylık yayımlanır. LRO sayfasında 68B için 13 Kasım 2026 tarihi takvimde yer alıyor; takvim satırını belirli bir ürünün gerçekten indirilebilir olduğunun kanıtı saymayın. Belirli NAC/WAC dosyasının kaydını doğrulayın.

**EMIT için çelişen kataloglar:** Bazı indekslenmiş Earthdata/CMR sayfaları V001’i göstermeye devam ediyor. Ekim duyurusu yeni sürümleri açıklıyor ve tarihsel yeniden işlemenin yaklaşık üç ay süreceğini belirtiyor. Güvenilir yaklaşım: canlı koleksiyon ve sahne sorgusunda hangi sürümün, hangi tarih ve alan için mevcut olduğunu kaydetmek; sürümleri sessizce birleştirmemek.

**Mars bilimi güncel bağlamı:** NASA’nın Mars Science Objectives sayfası 10 Kasım 2026’da güncellenmiş görünüyor; sayfa açıkça taslak olduğunu belirtiyor. Buzun insanlı keşif açısından önemi, hareketli yüzey süreçleri ve jeoteknik karakterizasyon için yararlı bağlam sağlar; bunu nihai mühendislik şartnamesi diye sunmayın. [NASA Mars Science Objectives — taslak](https://science.nasa.gov/planetary-science/programs/mars-exploration/mars-science-objectives/)

## 4. Analog kavramını bilimsel olarak doğru kurmak

Bir Dünya sahası, bütün bir gezegenin ikizi değildir. Analogluk bir **hedef + özellik + ölçek + deney amacı + zaman** ilişkisi olarak tanımlanmalı.

Örnek araştırma soruları:

- “Bu kaldera içindeki 2 km’lik koridorun eğim ve yerel rölyef dağılımı, seçtiğimiz Ay kutup koridoruna hangi ölçeklerde benziyor?”
- “Bu tuz düzlüğündeki mevsimsel su kaybı ve mineral yüzeyleri, Mars’ın eski evaporit ortamlarına ilişkin hangi gözlem yöntemlerini sınamaya elverişli?”
- “Bu arazide, gölgeye geçerken görüntü tabanlı navigasyonun hatası nasıl değişiyor?”
- “Bu örtülü buz sahası, bir radar ölçümünün yorumunu ve kazı planlama yöntemini sınamaya yarar mı?”

Bu soruların cevapları farklı saha sıralamaları üretebilir. Aynı saha, mineral süreçleri açısından yararlı; sıcaklık veya operasyon açısından zayıf olabilir. Bu nedenle tek ve evrensel bir “Mars’a benzerlik yüzdesi” vermek yerine, göreve bağlı benzerlik profili gösterin.

NASA analog araştırmalarının temel yaklaşımı da birden çok ortamın farklı güçlü yönlerini birlikte kullanmaktır. Bu dosyadaki sayısal yöntem önerileri ise aşağıda açıkça ekibinizin tasarım tercihleri olarak tanımlanmıştır. [NASA operasyonel saha testleri çalışması](https://ntrs.nasa.gov/api/citations/20210017110/downloads/8100_Janoiko_Using%20Earth-Based%20Operational%20Field%20Tests%20as%20High-Fidelity%20Analogs%20for%20Planetary%20Surface%20Exploration.pdf)

## 5. Ay için hedef profilleri

### 5.1. Güney kutbu: üs çevresi ve yüzey hareketliliği

NASA’nın güncel Moon Base açıklaması güney kutbu yakınında bir bölgeyi hedefliyor. Konum seçimi; tekrarlanan inişler, altyapı, kaynaklara erişim ve büyüyen operasyon alanı üzerinden ele alınıyor. Bu araştırmada incelenen güncel resmî açıklama, tek bir kesin üs koordinatı vermiyor. [NASA Moon Base — Sık sorulan sorular](https://www.nasa.gov/moon-base-frequently-asked-questions/)

20 Ekim 2026 tarihli NASA rover güncellemesi; arazi haritalama, bilimsel araştırma, kaynak arama ve taşımayı erken üs operasyonlarının parçaları olarak ele alıyor. Bu, analog projenizi soyut görüntü benzerliğinden somut bir mobilite veya keşif deneyine bağlamak için güncel bir gerekçe sağlar. [NASA Moon Base rover güncellemesi](https://www.nasa.gov/missions/moon-base/nasa-provides-progress-update-on-moon-base-rovers/)

Kutupsal ortamda düşük açılı ışık uzun gölgeler üretir; arazi, enerji ve hareketlilik kararları birbirine bağlıdır. Sürekli gölgeli bölgelerdeki uçucuların dağılımı aynı değildir. Keskin ve aşındırıcı regolit de uzun süreli operasyonların önemli bir parçasıdır. Dolayısıyla “en düz alan” tek başına yeterli hedef tanımı oluşturmaz. [NASA Lunar South Pole Environment](https://www.nasa.gov/reference/moonbase-environment/)

**Önerilen ölçülebilir özellikler:**

| Özellik | Türetilme biçimi | Dünya analogunda test edilebilecek konu |
|---|---|---|
| Eğim dağılımı | Aynı fiziksel ölçekte DEM türevleri; medyan, üst yüzdelikler | Rota seçimi, görüş kaybı, eğimli yüzey hareketi |
| Yerel rölyef | Belirli yarıçapta yükseklik aralığı | Koridor ve sırt geçişleri |
| Pürüzlülük | Düzleme göre yükseklik artıklarının dağılımı | Büyük ölçekli arazi karmaşıklığı |
| Ufuk engellenmesi | DEM üzerinde yönlere göre ufuk açısı | Düşük açılı aydınlatmada görüş |
| Gölge geometrisi | Hedefe uygun Güneş konumu ve arazi modeli | Görüntü işleme ve navigasyon |
| Kaynak-hedef erişimi | Seçilen soğuk bölge ile operasyon noktası arasında maliyetli rota | Keşif/örnekleme görev tasarımı |

Dünya’daki doğal bir krater gölgesini, Ay’daki sürekli gölgeli bölgenin termal eşdeğeri kabul etmeyin. Topografik gölge benzerliği ile vakum altındaki ısıl rejim farklı iddialardır. Dünya DEM’i ile yapılacak aydınlatma simülasyonu da gözlem değil, model çıktısıdır.

### 5.2. Tarihsel aday bölgeler nasıl kullanılmalı?

28 Ekim 2024 NASA açıklamasındaki dokuz bölge: Peak near Cabeus B, Haworth, Malapert Massif, Mons Mouton Plateau, Mons Mouton, Nobile Rim 1, Nobile Rim 2, de Gerlache Rim 2 ve Slater Plain. Bunları tarihli bir referans listesi olarak kullanabilirsiniz. Bu açıklamanın eski Artemis III görev tanımını, bugünün görev takvimi veya kesin kalıcı üs seçimi gibi aktarmayın. [2024 NASA bölge duyurusu](https://www.nasa.gov/news-release/nasa-provides-update-on-artemis-iii-moon-landing-regions/)

Başlangıç için bu bölgelerden yalnızca birinde, veri kapsamı doğrulanan küçük bir analiz alanı seçin. Nokta adı ile analiz poligonunu karıştırmayın: isim aynı kalsa bile poligon büyüklüğü eğim ve rölyef istatistiklerini değiştirecektir.

### 5.3. Bazaltik düzlükler ve mağaralar

Ay’ın mare alanlarının bazaltik geçmişi, Dünya lav sahalarını belirli jeolojik ve operasyonel testler için anlamlı kılar. Ancak böyle bir saha güney kutbundaki eski çarpma arazilerinin tümünü temsil etmez. [NASA Mare Crisium açıklaması](https://science.nasa.gov/resource/wrinkle-ridge-in-mare-crisium/)

Mare Tranquillitatis çukuruyla ilişkili mağara kanıtı, 2010 Mini-RF ölçümlerinin yeniden analizinden raporlandı. Bu, mağara/yeraltı keşif yöntemleri için ayrı bir araştırma hattını destekler. Oradaki kanıtı güney kutbunda uygun, erişilebilir bir mağara veya hazır barınak bulunduğu şeklinde genişletmeyin. [NASA mağara kanıtı — 18 Temmuz 2024](https://science.nasa.gov/solar-system/moon/new-evidence-adds-to-findings-hinting-at-network-of-caves-on-moon/)

## 6. Mars için birbirinden ayrılması gereken hedefler

### 6.1. Jezero: eski göl ve karbonat süreçleri

Jezero profili; eski göl, delta, sediment taşınımı, karbonatlar ve olası biyoişaretlerin korunması açısından kurulabilir. Türkiye’deki Salda, NASA’nın bu ilişkiyi zaten araştırdığı bilinen bir sahadır. Burada karşılaştırma **günümüz Mars yüzeyinde açık bir göl** varsayımına dayanmaz; Mars’ın eski çevresini anlamaya yöneliktir. [NASA Salda–Jezero araştırma bağlamı](https://science.nasa.gov/earth/earth-observatory/jez-like-mars-147041/)

Ölçülebilir öneriler: kıyı/teras geometrisi, drenaj ve yelpaze düzeni, seçilmiş yüzey mineral sınıfları, çıplak yüzey oranı. Uydu görüntüsü biyoişareti doğrulamaz; sahadan örnek, mikroskopi ve mineralojik inceleme ayrı kanıt gerektirir.

**Güncel bilimsel bağlam:** NASA’nın 10 Eylül 2025 açıklamasında, Cheyava Falls kayasından alınan Sapphire Canyon örneği için potansiyel biyoişaretler bildirildi. Bu ifade yaşamın doğrulandığı anlamına gelmiyor. Görüntü veya genel mineral benzerliği üzerinden yaşam sonucu çıkarılmaması, analog çalışmanızda da korunmalı. [NASA/JPL PIXL ve mineral bulguları](https://www.jpl.nasa.gov/images/pia26640-perseverances-pixl-finds-vivianite-greigite-in-cheyava-falls-sample/)

12 Ekim 2026 NASA görev güncellemesi, Perseverance’ın eski göl tabanından nehir sistemine ve krater kenarındaki farklı jeolojik ortamlara ilerlediğini vurguluyor. Bu nedenle “Jezero analoğu” etiketini kullanırken hangi alt ortamı hedeflediğinizi söyleyin: göl kıyısı, nehir çökelimi, karbonat birimi veya başka bir hedef aynı problem değildir. [NASA Perseverance — Ekim 2026 bilim/rota bağlamı](https://science.nasa.gov/blogs/perseverance-mars-rover/2026/10/12/nasas-perseverance-sets-off-world-record-for-total-distance-driven/)

### 6.2. Orta enlemler: gömülü buz ve kaynak keşfi

SWIM, MRO, Mars Odyssey ve Mars Global Surveyor gözlemlerini bir araya getirerek yüzey altı buz kanıtlarını haritalıyor. NASA’nın 2023 kamuya açık haritaları, yüzeye yakın buzun olası dağılımını ve bazı doğrulayıcı çarpma gözlemlerini anlatıyor. Tarihsel bir kaynak olduğu için bunu “2026’da yeni çekilmiş küresel buz haritası” diye etiketlemeyin. [NASA SWIM haritası](https://science.nasa.gov/resource/swim-map-shows-subsurface-water-ice-on-mars/)

SWIM’in farklı derinlik aralıklarına ait ürünlerini karıştırmayın. NASA’nın 2024–2044 Mars planındaki görselde 1–5 m aralığı ayrıca belirtiliyor. Harita rengi, tek başına buz saflığı, kazı verimi veya endüstriyel su rezervi anlamına gelmez. [NASA Mars Exploration Program planı](https://assets.science.nasa.gov/content/dam/science/psd/solar-system/mars/campaigns/mars-future-plan/20241204_Mars_Future_Plan_Final_Print.pdf)

Arcadia Planitia, NASA’nın önceki kaynak çalışmalarında yüzeye yakın buz açısından ilgi çekici bir bölge olarak ele alınmıştır. Bunu ilk insanlı Mars iniş yerinin kesin seçildiği şeklinde sunmayın. Profilinizi “Arcadia’da seçilmiş bir çalışma alanında buz erişimi” olarak adlandırın. [NASA Arcadia bağlamı](https://www.nasa.gov/solar-system/nasas-treasure-map-for-water-ice-on-mars/?site=msl)

**Dünya’da test edilebilecek işler:** örtü altı buz arama, radar yorumlama, yüzey özelliği ile yeraltı hedefi arasındaki ilişkinin sınanması, örnekleme rotası tasarımı. Dünya’da su veya kar görmek, o noktada uygun derinlikte gömülü buz bulunduğunu kanıtlamaz.

### 6.3. Bazaltik ve rüzgârla şekillenmiş yüzeyler

Volkanik jeoloji, iri bloklu yüzey hareketi, kum dalgaları ve tozun aletler üzerindeki etkisi ayrı test amaçları olabilir. NASA BASALT çalışması, bazalt sahalarında bilimsel araştırma ile insanlı görev operasyonlarını birlikte sınamanın bir örneğidir. [NASA BASALT](https://www.nasa.gov/missions/analog-field-testing/what-is-basalt/)

Mars’ın ince atmosferi ve farklı yerçekimi, Dünya’daki aynı rüzgâr hızının aynı tane hareketini üretmesini engeller. Arazinin benzer görünmesi, rüzgârla taşınma eşiğinin veya tozun elektrostatik davranışının eşit olduğu anlamına gelmez. Bu nedenle kumul geometrisini, atmosferik toz yoğunluğunu ve tekerlek-zemin etkileşimini tek değişkenmiş gibi puanlamayın.

## 7. Dünya veri kataloğu: neyi, hangi ürünle ölçebilirsiniz?

### 7.1. Çekirdek veri paketi

| Ürün | Sürüm / ölçek | Kullanım | Sınırlama / erişim |
|---|---|---|---|
| NASADEM_HGT | V001; 1 yay-saniyesi, ekvatorda yaklaşık 30 m | Eğim, rölyef, arazi şekli | Temel SRTM ölçümleri Şubat 2000; yaklaşık 60°K–56°G; kutupları kapsamaz |
| ASTER GDEM / ASTGTM | V003; 1 yay-saniyesi | Daha yüksek enlemlerde topografya | Yaklaşık 83°K–83°G; boşluk/artifakt ve kalite bilgisi kontrol edilmeli |
| HLSL30 / HLSS30 | V2.0 / 002; 30 m | Güncel yüzey yansıtımı, bitki/su/çıplak yüzey taraması | Bulut, gölge, kar ve su kalite bayrakları gerekli; NASA işlenmiş ortak kaynaklı ürün |
| MOD11A1 | V061; günlük, yaklaşık 1 km | Uzun dönem gündüz/gece yüzey sıcaklığı | Açık gökyüzü örneklemesi; hava sıcaklığı değildir |
| ECO_L2T_LSTE | V002; nominal 70 m | Daha yerel yüzey sıcaklığı ve emissivite | ISS gözlem alanı ve geçiş saatleri; her alan/her gün gözlenmez |
| EMIT L2B mineral tanımlama | Ekim 2026 duyurusuyla V2; nominal 60 m | Yüzey mineral göstergeleri, alterasyon/evaporit taraması | Hedefli kapsam; bitki, su, bulut ve düşük güven sonuçlarını maskeleyin |

Kaynaklar: [NASADEM ürün açıklaması](https://data.nasa.gov/dataset/nasadem-merged-dem-global-1-arc-second-v001), [ASTER GDEM V3](https://asterweb.jpl.nasa.gov/gdem.asp), [HLS ürünleri](https://hls.gsfc.nasa.gov/data-products/), [MODIS ürün açıklaması](https://search.earthdata.nasa.gov/portal/idn/search?fi=MODIS), [ECOSTRESS V002 kataloğu](https://search.earthdata.nasa.gov/search?q=ECOSTRESS+V002), [EMIT yeni sürüm duyurusu](https://forum.earthdata.nasa.gov/viewtopic.php?sid=dae91c5ef96f336491803c0490ce9060&t=8322).

### 7.2. Tamamlayıcı veri paketi

| Ürün / servis | Ölçek | Yararı | Yapılmaması gereken çıkarım |
|---|---|---|---|
| NASA POWER | Meteoroloji 0,5° × 0,625°; güneş parametreleri 1° × 1° | İklim ve bölgesel enerji bağlamı | Bir krater yamacının yerel sıcaklığını veya gölgesini çözdüğü varsayımı |
| GPM IMERG V07 ailesi | 0,1°; yarım saatlik ve türetilmiş zaman ölçekleri | Yağış rejimi ve kuraklık bağlamı | Küçük AOI’de yerel mikroiklim veya kesin sıfır yağış kanıtı |
| MERRA-2 M2T1NXAER | V5.12.4; saatlik, 0,5° × 0,625° | Bölgesel aerosol/toz bağlamı | Kolon aerosolünü zemindeki tane boyutu veya kaya yoğunluğu sanmak |
| NISAR L-band | Ürüne bağlı | Yüzey değişimi, radar geri saçılımı ve uygun koşullarda deformasyon araştırması | Tek radar görüntüsüyle mineral, mağara veya gömülü buzun kesin tespiti |
| Worldview / GIBS | Katmana bağlı görsel ölçek | Keşif, tarih karşılaştırması ve arayüz | Renklendirilmiş ekran pikselini kalibre fiziksel veri yerine kullanmak |

Kaynaklar: [POWER hizmetleri](https://power.larc.nasa.gov/docs/services/), [GPM güncel veri dizini](https://gpm.nasa.gov/data/directory), [MERRA-2 katalog dizini](https://cmr.earthdata.nasa.gov/search/site/collections/directory/GES_DISC/gov.nasa.eosdis), [NISAR yayın duyurusu](https://forum.earthdata.nasa.gov/viewtopic.php?p=26359&sid=c3064093e30bd71b2c255f9a1900719c&t=8068), [Worldview](https://worldview.earthdata.nasa.gov/).

IMERG Final ürününün yaklaşık 3,5 aylık gecikmesi vardır; daha yeni veriye ihtiyaç duyulduğunda Early/Late ile Final’i etiketlemeden karıştırmayın. POWER meteoroloji verisinin yakın tarihli kısmı da daha sonra iklim kalitesindeki ürünlerle değişebilir. “En yeni” ve “karşılaştırmada en tutarlı” seçimleri her zaman aynı değildir. [IMERG dokümantasyonu](https://gpm.nasa.gov/resources/documents/imerg-v07-technical-documentation), [POWER veri uyarıları](https://power.larc.nasa.gov/docs/services/)

### 7.3. EMIT’i doğru kullanma

EMIT, Dünya’nın özellikle kurak toz kaynaklarının yüzey mineralojisini araştırır. Kapsamı tüm Dünya’nın kesintisiz 60 m mineral haritası değildir. Aday poligon üzerinde sahne olup olmadığını, sahnenin geçerli piksellerini ve mineral tanımlama belirsizliğini kontrol edin. [NASA EMIT kapsam açıklaması](https://search.earthdata.nasa.gov/search?fpj=GEMx%21EMIT)

L3 EMITL3ASA V002, L2B ile aynı ürün değildir: 0,5° düzeyinde toplulaştırılmış ve belirli tarihsel gözlemlere dayanan bir mineral spektral bolluk ürünüdür. Küçük bir kıyı şeridini veya kaldera yamacını karakterize etmek için 60 m L2B’nin yerine geçmez. [NASA EMIT L3 ürün açıklaması](https://data.nasa.gov/dataset/emit-l3-aggregated-mineral-spectral-abundance-and-uncertainty-0-5-deg-v002)

EMIT ve CRISM mineral sınıfları arasında bir eşleme sözlüğü gerekir. Aynı genel “karbonat” etiketi; aynı mineral türü, tane boyutu, karışım oranı veya oluşum süreci demek değildir. Örneğin Salda’daki hidromanyezit ile Mars’taki karbonatların birebir aynı kimyasal bileşimde olduğu ileri sürülmemeli.

### 7.4. ECOSTRESS ve sıcaklık karşılaştırması

V002 ECOSTRESS ürünlerinde, V001’deki QC katmanından alışılmış bulut bilgisinin aynı biçimde bulunmadığına ilişkin katalog uyarısı var. Ürünün ilgili bulut/su katmanlarını ve kullanıcı kılavuzunu izleyin. Geçiş saati, görüş açısı ve açık gökyüzü seçilimi sıcaklık istatistiklerini etkiler. [ECOSTRESS V002 ve veri uyarısı](https://search.earthdata.nasa.gov/search?q=ECOSTRESS+V002)

Bir sahnenin yüzey sıcaklığını başka sahnenin farklı saatteki sıcaklığıyla karşılaştırmak yerine, yerel saat ve mevsim açısından uyumlu gözlemleri seçin. MODIS gündüz/gece örneklerinin farkını, ölçülmüş tam günlük maksimum-minimum aralığı gibi adlandırmayın. Termal atalet türetmek ayrıca model, sınır koşulları ve doğrulama gerektirir.

### 7.5. NASADEM ve ASTER için kritik ayrımlar

NASADEM’in adı küresel olsa da yüksek kutupları kapsamaz. Antarktika veya Devon Adası için aynı ürünü zorlamayın. ASTER’in daha geniş enlem kapsamı da kaliteli ve eksiksiz yerel topografyayı garanti etmez. Kapsamın son enlem sınırları ile etkin piksel kalitesini ayrı denetleyin.

1 yay-saniyelik grid, her enlemde iki yönde de 30 m kare piksel değildir. Eğim hesabından önce uygun metre tabanlı yerel projeksiyon kullanın. Uydudan türetilmiş bir DEM’i bütün alanlarda ağaç ve yapılardan tamamen arındırılmış mühendislik arazi modeli olarak kabul etmeyin.

ASTER’in SWIR alt sistemi tarihsel bir sınırlamaya sahiptir; yeni VNIR/TIR görüntüsü var diye güncel SWIR mineraloji ölçümü de var denemez. Sahne tarihi ve kullanılabilir bantları kontrol edin. NASA’nın 2025 işletim duyurusu VNIR/TIR’deki veri boşluklarını da açıklıyor. [ASTER resmî durum sayfası](https://asterweb.jpl.nasa.gov/)

SWIR ölçümleri Nisan 2008’den itibaren kullanılamaz olarak işaretlenmiştir. Güncel mineral araştırması için eski SWIR bantlarını yeni çekilmiş gibi sunmayın. [NASA/JPL ASTER SWIR kullanıcı uyarısı](https://asterweb.jpl.nasa.gov/swir-alert.asp)

## 8. Ay ve Mars veri kataloğu

### 8.1. Ay

| Veri | Ne sağlar? | Başlangıç tercihi | Kritik sınır |
|---|---|---|---|
| LOLA / PGDA 87–90°G mozaik | Yükseklik, eğim, ölçüm sayısı | 5 m/piksel GeoTIFF; seçilmiş AOI | Grid aralığı ile etkin çözünürlük aynı değildir |
| LOLA / PGDA geniş kutup ürünleri | DEM, eğim, hata, etkin çözünürlük, pürüzlülük | Örneğin 80–90°G için 20 m ürün ailesi | Büyük dosyalar; ara ürünler ve hata katmanları birlikte alınmalı |
| PGDA Shape-from-Shading | LOLA’ya bağlı, NAC görüntüleriyle geliştirilmiş topografya | Uygun bölgelerde 5 m gridli SDEM | Aydınlatılmış alanlardaki fotometrik model; doğrudan yeni lazer örneklemesi değildir |
| LROC NAC / WAC | Yüksek çözünürlüklü görüntü ve geniş alan bağlamı | Ortorektifiye/haritalanmış uygun RDR | Nominal görev ölçeği tüm sahnelerde geçerli değildir; gölge ve çekim geometrisi önemlidir |
| Diviner RDR | Kalibre radyometrik gözlemler | Ürün etiketi ve kanala göre | Eksik veri ve kanal sorunları maskeleme gerektirir |
| Diviner PCP / PRP | Kutup birikimli ve kaynakla ilişkili türetilmiş katmanlar | Hazır harita için önce bunları inceleyin | Gözlem dönemi ve model varsayımları RDR’den farklıdır |
| LEND / Mini-RF | Hidrojen göstergeleri / radar özellikleri | Buz araştırmasında yardımcı kanıt | Tek başına erişilebilir su rezervi veya mağara garantisi vermez |

Kaynaklar: [PGDA 5 m kutup mozaiği](https://pgda.gsfc.nasa.gov/products/81), [PGDA geniş kutup ürünleri ve belirsizlik katmanları](https://pgda.gsfc.nasa.gov/products/90), [PGDA SDEM](https://pgda.gsfc.nasa.gov/products/104), [LROC RDR ürün tanımı](https://pds.nasa.gov/ds-view/pds/viewProfile.jsp?dsid=LRO-L-LROC-5-RDR-V1.0), [Diviner](https://pds-geosciences.wustl.edu/missions/lro/diviner.htm), [LRO arşivi](https://pds-geosciences.wustl.edu/missions/lro/).

**Doğrudan kullanılabilir dosya ailesi örnekleri:** `LDEM_80S_20MPP_ADJ.TIF`, `LDEM_80S_20MPP_ADJ_EFFRES.TIF`, `LDEM_80S_20MPP_ADJ_ERR.TIF`, `LDSM_80S_20MPP_ADJ.TIF`. İsimler NASA PGDA sayfasında doğrulandı. Aynı dosya ailesinin çözünürlük, hata ve ölçüm yoğunluğu bilgilerini birlikte incelemek, yalnızca renkli hillshade göstermeye göre daha güçlü kanıt üretir.

PGDA’daki pürüzlülük ürünleri belirli fiziksel taban uzunluklarına göre tanımlıdır. Örneğin 100 m ve 800 m tabanlar farklı arazi özelliklerini anlatır; bunları farklı Dünya pencereleriyle karşılaştırmayın. Kutup ürünleri metre tabanlı güney kutup stereografik koordinatlarla ve MOON_ME / DE421 referansıyla sunuluyor. [PGDA ürün tanımları](https://pgda.gsfc.nasa.gov/products/90)

Diviner arşiv uyarısı, bazı RDR kanallarında eksik parlaklık sıcaklığı bulunduğunu ve eksik `tb` değerlerinin `-9999` ile gösterildiğini belirtiyor. Bu değerleri sıcaklık istatistiğine katmayın. Ayrıca kalibre kanal parlaklık sıcaklığı ile türetilmiş fiziksel yüzey sıcaklığı ürününü eşanlamlı kullanmayın. [Diviner veri kalitesi notu](https://pds-geosciences.wustl.edu/missions/lro/diviner.htm)

### 8.2. Mars

| Veri | Ölçek / özellik | Kullanım | Kritik sınır |
|---|---|---|---|
| MGS MOLA MEGDR | Küreselde 128 piksel/dereceye kadar; ekvatorda yaklaşık 463 m grid | Bölgesel yükseklik, büyük ölçekli rölyef | Rover tekerleği, küçük kaya veya 30 m eğim haritası için yeterli değildir |
| MRO CTX | Nominal yaklaşık 6 m/piksel görüntü | Arazi şekli, krater/delta/lav bağlamı | Görüntü tek başına DEM değildir; stereo ve işleme ayrı gerekir |
| MRO HiRISE | Uygun gözlemlerde yaklaşık 25–32 cm/piksel | Yerel bloklar, küçük arazi şekilleri, stereo DTM | Küresel kesintisiz kapsama sahip değildir |
| MRO CRISM | Hedefli modlarda yaklaşık 18 veya 36 m/piksel | Mineral imzaları ve alterasyon | Gözlem modu ve spektral kaliteye bağlı; 2023’te kapatıldı |
| Mars Odyssey THEMIS | TIR görüntüleri/haritaları; ürüne göre | Isıl yüzey özellikleri ve yerel bağlam | Bir IR mozaik otomatik olarak kalibre termal atalet haritası değildir |
| MGS TES | Küresel termal/mineral bağlam | Geniş ölçekte karşılaştırma | CTX/HiRISE kadar yerel ayrıntı içermez |
| MRO SHARAD | Yüzey altı radargramları | Büyük ölçekli yeraltı katmanları/buz kanıtları | Yüzeyden kaynaklanan yanıltıcı yankılar ve radar çözünürlüğü |
| SWIM | Birden çok gözlemin sentezi | Buzla tutarlılık ve kaynak keşif profili | Olasılık/tutarlılık ile konsantrasyon veya rezerv farklı büyüklüklerdir |
| Mars 2020 / MSL yer ölçümleri | Alete ve güzergâha bağlı | Jezero/Gale’de gerçek yer gözlemleri | Bir rover güzergâhını tüm Mars’ın yüzey koşulları saymayın |

Kaynaklar: [MOLA MEGDR](https://pds-geosciences.wustl.edu/missions/mgs/megdr.html), [CTX görev ölçeği](https://science.nasa.gov/resource/a-decade-of-compiling-the-sharpest-mars-map/), [HiRISE arşiv spesifikasyonu](https://pds-imaging.jpl.nasa.gov/documentation/HiRISE_RDR_v12_DTM_11_25_2009.pdf), [CRISM modları](https://pds-geosciences.wustl.edu/mro/mro-m-crism-3-rdr-targeted-v1/mrocr_2110/document/crism_dpsis.htm), [CRISM’in kapatılması](https://www.jpl.nasa.gov/news/nasa-retires-mineral-mapping-instrument-on-mars-orbiter/), [Mars Trek katman kataloğu](https://trek.nasa.gov/tiles/apidoc/trekAPI.html?body=mars), [SHARAD arşivi](https://pds-geosciences.wustl.edu/missions/mro/sharad.htm), [SWIM NASA açıklaması](https://www.nasa.gov/solar-system/planets/mars/nasa-is-locating-ice-on-mars-with-this-new-map/), [PDS](https://pds.nasa.gov/).

MOLA’nın 128 piksel/derece ızgarası için yaklaşık 463 m değeri Mars’ın ekvator çevresinden hesaplanan grid aralığıdır; yerel gerçek çözünürlük veya doğruluk garantisi değildir. Yükseklik, gezegen yarıçapı ve areoid ürünleri farklıdır; aynı `megr`/`megt` ailesini yanlış yorumlamayın. [MOLA ürün açıklaması](https://pds-geosciences.wustl.edu/missions/mgs/megdr.html)

CRISM’in 3 Nisan 2023’te kapatılmış olması, arşivdeki bilimsel verinin işe yaramadığı anlamına gelmez. “Yeni CRISM ölçümü” yerine, varsa güncel işlenmiş arşiv ürününden söz edin. [NASA/JPL CRISM duyurusu](https://www.jpl.nasa.gov/news/nasa-retires-mineral-mapping-instrument-on-mars-orbiter/)

## 9. Bilinen Dünya analogları: karşılaştırma için başlangıç kümesi

Bu sahalar kendi çalışmanızın dış doğrulaması için yararlı olabilir; “ilk kez keşfettik” iddiasına dayanak değildir. Aşağıdaki açıklamalar NASA’daki resmî bilim bağlamına dayanır; saha erişim koşullarının güncel olarak uygun olduğu sonucunu içermez.

| Saha | Temel karşılaştırma boyutu | Deney örneği | Analojinin sınırı |
|---|---|---|---|
| Atacama, Şili | Kurak çevre ve biyoişaret araştırması | Düşük organik sinyalde örnekleme/alet yaklaşımı | Dünya atmosferi ve biyolojisi mevcut |
| Haughton / Devon Adası, Kanada | Çarpma arazisi, kutup çölü, uzak operasyon | Jeoloji rotaları ve görev lojistiği | Ay vakumu veya Mars atmosferi yok |
| McMurdo Dry Valleys, Antarktika | Soğuk çöl | Çevresel örnekleme ve yaşam tespiti yaklaşımı | Ay kutup sıcaklık rejimiyle eşdeğer değil |
| University Valley, Antarktika | Buzla çimentolanmış zemin | Yeraltı örneklemesi | Yerel mikrobiyoloji ve ısıl koşullar ayrı |
| Kīlauea / Hawaii | Bazalt ve saha operasyonları | Örnek seçimi, ekip/robot iş bölümü | Kutup krater jeolojisini temsil etmez |
| Craters of the Moon, Idaho | Lav yüzeyi ve volkanik jeoloji | Arazi tanıma ve jeoloji eğitimi | Regolitin uzayda değişimi farklı |
| Askja çevresi, İzlanda | Örtülü buz ve dalgalı yüzeyler | Radar ve yüzey şekli izleme | Dünya’nın su döngüsü ve atmosferi etkin |
| Medicine Lake çevresi, Kaliforniya | Lav mağaraları | Yeraltı haritalama ve algılama | Ay mağarasının mekanik dayanımı buradan doğrudan çıkmaz |
| Death Valley, Kaliforniya | Bloklu yüzey ve tehlike algılama | Görsel navigasyon testi | Mineral ve ısıl benzerlik ayrıca doğrulanmalı |
| Salda, Türkiye | Eski göl süreçleri ve karbonatlar | Jezero yorumu, örnekleme stratejisi | Güncel Mars iklimi veya üs inşası analoğu değil |

Kaynaklar: [NASA Astrobiology saha listesi](https://astrobiology.nasa.gov/research-locations/), [NASA Haughton raporu](https://ntrs.nasa.gov/api/citations/20060013129/downloads/20060013129.pdf), [NASA BASALT](https://www.nasa.gov/missions/analog-field-testing/what-is-basalt/), [NASA Moonscapes of Idaho](https://science.nasa.gov/earth/earth-observatory/moonscapes-of-idaho-154207/), [NASA Analog Explorer](https://science.nasa.gov/solar-system/analog-explorer/), [NASA Salda saha anlatımı](https://science.nasa.gov/blogs/earth-matters/2021/02/17/what-a-lake-in-turkey-can-tell-us-about-mars/).

NASA Analog Explorer, Medicine Lake mağara çalışmalarını, İzlanda’daki buz radarını, Death Valley’deki tehlike algılama hazırlığını ve Salda–Jezero ilişkisini örnekliyor. Bu örnekleri bir değerlendirme ölçütü oluşturmak için kullanın; yalnızca aynı adları listelemek projenin yeni katkısını oluşturmaz.

## 10. Türkiye adayları: kanıt, hipotez ve gerekli analiz

### 10.1. Nemrut kalderası — arazi ve rota testi adayı

**NASA’da doğrulanan temel:** Bitlis/Tatvan yakınındaki, Van Gölü kıyısındaki volkanik Nemrut; kaldera, lav yüzeyleri, mevsimsel kar ve göl içerir. NASA açıklaması lav bileşiminde bazalttan obsidiyene çeşitlilik olduğunu belirtiyor. Adıyaman’daki heykelli Nemrut Dağı ile karıştırılmamalı. Kullanılan açıklama 2009 tarihli ve fotoğraf 3 Aralık 2008’e ait; bugünkü yüzey/kar durumu için yeni veri gerekir. [NASA/JSC Nemrut](https://eol.jsc.nasa.gov/Collections/EarthObservatory/articles/MountNemrutTurkey.htm)

**Sınanacak hipotez:** Kalderanın belirli sırt, yamaç ve taban koridorları; seçilmiş bir Ay güney kutbu koridoruyla, büyük ölçekli eğim/rölyef ve düşük açılı görüş koşulları bakımından karşılaştırılabilir.

**Gerekli veri:** NASADEM; güncel HLS yüzey maskeleri; uygun ECOSTRESS/MODIS sıcaklık gözlemleri; Ay tarafında LOLA ve LROC. Mineral iddiası eklenirse EMIT kapsamı ve mineral tanımlama kalitesi ayrıca kontrol edilmeli.

**Analiz önerisi:** Göl ve bitki örtüsünü maskeleyin; kaldera içini tek AOI saymak yerine birkaç ayrı arazi birimine bölün. Eğim histogramlarını, 100–1000 m ölçeklerinde rölyefi ve DEM tabanlı ufuk engellenmesini karşılaştırın. Yağış ve suyla şekillenme etkilerini farklar paneline yazın.

**Test fikri:** Aynı robotik navigasyon algoritmasını farklı gölge ve eğim koridorlarında sınamak. Bu çalışma Ay yerçekiminde çekişi veya vakumda donanım dayanımını doğrulamaz.

**Mevcut kanıt düzeyi:** NASA’da yer şekli/jeoloji açıklaması var; bu araştırmada sayısal analog eşleşmesi hesaplanmadı. Ay kutup buzunun veya kesin benzer litolojinin kanıtı yok.

### 10.2. Tuz Gölü — kuruma ve tuzlu yüzey süreçleri adayı

**NASA’da doğrulanan temel:** İç Anadolu’daki tuzlu gölde su alanı zamana göre değişiyor; NASA Earth Observatory, Landsat temelli uzun dönem kuruma araştırmasını açıklıyor. 2021’deki durum, 2026’nın güncel su/zemin durumu gibi kullanılmamalı. [NASA Disappearing Lake Tuz](https://science.nasa.gov/earth/earth-observatory/disappearing-lake-tuz-149211/)

**Sınanacak hipotez:** Gölün belirli kuru kıyı veya taban kesimleri, Mars’taki eski tuzlu çökelme/kuruma ortamlarını incelemek ve spektral yüzey tarama yöntemlerini sınamak için yararlı olabilir.

**Gerekli veri:** Mevsimsel HLS; EMIT varsa mineral ürünleri; MODIS/ECOSTRESS; IMERG veya POWER ile bölgesel bağlam. Mars tarafında hedefi mineral kanıtıyla tanımlanmış küçük bir çökel alanı olarak seçin.

**Analiz önerisi:** Su, ıslak zemin, tuz kabuğu ve bitkili kıyı alanlarını farklı sınıflar olarak ele alın. Birden fazla ay ve yılda kararlılığı inceleyin. “Beyaz piksel” doğrudan aynı mineral anlamına gelmez; yüzey yansıtımı ve mineral kanıtı birlikte gerekçelendirilmeli.

**Test fikri:** Tuzlu yüzey örnekleme planı, spektral tarama ve yanlış pozitifleri ayırt etme. Kabuk üstünde araç hareketinin uygunluğu uydu verisiyle onaylanamaz; taşıma gücü ve koruma izinleri saha konusu olarak açık bırakılmalı.

**Mevcut kanıt düzeyi:** NASA’da çevresel/su değişimi temeli var; Mars mineralojisiyle sayısal eşleşme bu araştırmada doğrulanmadı. Gölün bütününü steril, sürekli kuru veya erişime açık saymayın.

### 10.3. Salda — yeni keşif değil, bilinen karşılaştırma sahası

**NASA’da doğrulanan temel:** NASA’nın Salda saha anlatımı karbonat sedimentleri, mikrobiyalitler, teraslar ve delta/yelpaze süreçlerini Jezero araştırmasıyla ilişkilendiriyor. Bu ilişki, örnekleme ve eski çevre yorumu için güçlü bir bilimsel dayanak sağlar. [NASA Salda saha çalışması](https://science.nasa.gov/blogs/earth-matters/2021/02/17/what-a-lake-in-turkey-can-tell-us-about-mars/)

**TerraTwin’de rolü:** Bilinen bir analog için sisteminizin hangi boyutlarda eşleşme üretebildiğini ve hangi boyutlarda düşük benzerlik göstermesi gerektiğini sınamak. Salda’yı yalnızca sıcaklığı veya rengi üzerinden eşleştiren bir sistem, önemli jeolojik ilişkiyi kaçırabilir.

**Özgün katkı ihtimali:** Bütün gölü işaretlemek yerine, kıyıdaki belirli küçük alanları bilimsel amaçlarına göre ayırmak; yansıtım, su durumu ve varsa mineral göstergeleriyle gerekçelendirmek. Bu mikroalanların daha önce çalışılmadığı ayrıca kanıtlanmadan “keşfedilmemiş analog” denemez.

**Sınır:** Uydudan karbonat göstergesi görmek yaşam kanıtı değildir. Korunması gereken yüzeyler üzerinde fiziksel test önerisi, bilimsel benzerlikten otomatik olarak çıkmaz. [NASA Salda kıyısı açıklaması](https://science.nasa.gov/photojournal/lake-salda-beach/)

### 10.4. Kapadokya — aşınmış tüf arazisi ve navigasyon adayı

**NASA’da doğrulanan temel:** NASA Earth Observatory; volkanik külün tüfe dönüşmesini, rüzgâr ve suyla aşınmış şekilleri, insan yapımı oyulmuş mekânları açıklıyor. Kullanılan Landsat görüntüsü tarihsel; güncel koşullar için HLS gerekir. [NASA Göreme](https://science.nasa.gov/earth/earth-observatory/goreme-national-park-turkey-38876/)

**Sınanacak hipotez:** Belirli vadiler, aşınmış yüzey geometrisini yorumlama veya karmaşık arazide görsel navigasyon için yararlı olabilir. Hedef Mars süreci, malzemesi ve ölçeği ayrıca seçilmeli.

**Sınır:** Tüf, bazalt değildir. İnsan eliyle oyulmuş yeraltı mekânı, doğal lav tüpü değildir. Kapadokya’yı doğrudan “Ay lav tüpü üssü analoğu” diye etiketlemeyin.

### 10.5. Bu aşamada neden daha çok Türkiye adı eklemiyorum?

Kula, Karapınar/Meke veya başka volkanik alanlar ileride incelenebilir. Ancak bu araştırmada onlar için NASA kaynaklarından yeterli doğrudan dayanak doğrulanmadığından, doğrulanmış katalog satırı üretmedim. Bir yerin az bilinir olması, bilimsel eşleşmenin kanıtı değildir. Önce NASA gözlem kapsamı ve özellik çıkarımıyla adaylığını sınayın.

## 11. Küresel genişleme için üç aday araştırma hattı

Bu bölümdeki **coğrafya/jeoloji açıklamaları NASA kaynaklıdır**; belirli hedeflerle eşleştirme önerileri benim hipotezlerimdir. Alanların dünyada ilk kez analog olarak önerildiği iddia edilmiyor.

### 11.1. Harrat Khaybar, Suudi Arabistan

NASA’nın 2024 Landsat 9 açıklaması, lav ve kül yüzeylerinin belirgin renk/jeoloji farklarını gösteriyor. [NASA Harrat Khaybar](https://science.nasa.gov/earth/earth-observatory/white-and-black-volcanoes-of-saudi-arabia-152839/)

**Soru:** Seçilmiş lav akış birimleri, Ay mare veya Mars bazalt sahaları için yüzey şekli/mineral ayrımı ve rota planlama testine uygun mu? NASADEM + HLS + varsa EMIT ile farklı malzemeleri ayırın. Açık renkli ve koyu renkli volkanik birimleri aynı bazalt etiketi altında toplamayın. Aktif jeolojik risk ve saha erişimi ayrıca araştırılmalı.

### 11.2. El Pinacate, Meksika

NASA, alandaki maar kraterlerinin magma–yeraltı suyu etkileşimiyle oluştuğunu açıklıyor. [NASA Pinacate](https://science.nasa.gov/earth/earth-observatory/pinacate-biosphere-reserve-3923/)

**Soru:** Belirli bir maarın morfometrisi, seçilmiş Ay krateriyle yalnızca geometri ve navigasyon açısından karşılaştırılabilir mi? Çap/derinlik oranı, duvar eğimi ve yaklaşım koridorları ölçülebilir. Oluşum mekanizması çarpma olmadığı için “aynı krater jeolojisi” iddiası kurulamaz. Korunan alan statüsündeki araziye ilişkin deney erişimi ayrıca doğrulanmalı.

### 11.3. Makgadikgadi, Botsvana

NASA açıklaması, eski gölün kalıntısı tuz düzlüklerini ve mevsimsel ekolojik önemini ortaya koyuyor. [NASA Makgadikgadi](https://science.nasa.gov/earth/earth-observatory/makgadikgadi-salt-pans-92394/)

**Soru:** Farklı kuruma durumları ve yüzey mineral göstergeleri, eski Mars göl tabanlarının yorumuna yararlı bir süreç analoğu oluşturabilir mi? Büyük alanı tek etiketlemek yerine doğal düzlükleri, su/bitki alanlarını ve insan yapımı tuz üretim yüzeylerini ayırın. Mevsimsel su varlığı, buranın bütünüyle cansız olduğu anlamına gelmez. [NASA doğal ve yapay tuz yüzeyleri ayrımı](https://science.nasa.gov/earth/earth-observatory/salty-botswana-145216/)

## 12. Önerilen analiz yöntemi — NASA standardı değildir

Bu bölümdeki ağırlıklar, eşikler ve formüller bir **uygulama tasarımı önerisi**dir. NASA tarafından onaylanmış analog puanlama standardı olarak sunulmamalı. Puanlama ancak gerçek ürünler indirildikten, kalite denetiminden geçirildikten ve özellikler hesaplandıktan sonra sonuç üretir.

### 12.1. Önce hedef ve deney amacını sabitleyin

Her analiz kaydında şunlar yazılı olmalı:

- Hedef cisim ve adlandırılmış analiz poligonu.
- Deney: örneğin rota planlama, mineral örnekleme veya buz radar yorumu.
- Ölçülen değişkenler, birimleri ve karşılaştırma ölçekleri.
- Hedefin veri tarihi, sürümü ve kalite maskeleri.
- Analizden beklenmeyen fiziksel doğrulamalar: örneğin Dünya saha testi düşük yerçekimini temsil etmiyor.

Bir “Ay profili” ve “Mars profili” yeterli ayrıntı sağlamaz. “Ay güney kutbu / 500 m tabanda arazi hareketliliği” gibi açık profil daha denetlenebilir.

### 12.2. Karşılaştırma özellikleri

| Boyut | Önerilen özellikler | Uygun veri | Yorum |
|---|---|---|---|
| Topografya | Eğim dağılımı, rölyef, düzleme göre artıklar | DEM | Aynı fiziksel pencere ve etkin çözünürlük gerekir |
| Yüzey malzemesi | Güvenilir mineral sınıfları, bant derinliği, çıplak yüzey oranı | EMIT / CRISM / HLS | Sınıf sözlüğü ve algılama sınırları gerekli |
| Isıl durum | Uyumlu saatte LST dağılımı, mevsimsel değişim | MODIS / ECOSTRESS / Diviner / Mars termal ürünleri | Aynı fiziksel büyüklük ve ölçüm koşulu karşılaştırılmalı |
| Su/buz bağlamı | Açık su süresi, kar varlığı, yeraltı buzuna ilişkin kanıt türü | HLS ve uygun kar ürünleri / SWIM / radar | Kar, açık su ve gömülü buz ayrı değişkenler |
| Arazi şekli | Krater oranları, drenaj/yelpaze düzeni, sırt dizileri | DEM ve görüntü | Benzer şekil, aynı oluşum mekanizması demek değildir |
| Operasyon | Rota uzunluğu, çıkış, görüş, veri kapsamı | Türetilmiş GIS | Donanım sınırları ve saha izinleri ayrı ele alınır |

Mutlak yüksekliği doğrudan eşleştirmeyin: Dünya’da 2000 m rakım ile Mars areoidine göre 2000 m yüksekliğin atmosfer/enerji anlamı aynı değildir. Benzer biçimde çıplak yüzey oranı, yaşam yokluğu ölçümü değildir.

### 12.3. Basit ve açıklanabilir puanlama

Sayısal bir özellik için isteğe bağlı benzerlik fonksiyonu:

```text
s_j = exp(-0.5 * ((x_earth,j - x_target,j) / tau_j)^2)
```

Burada `tau_j`, deney açısından anlamlı fark ölçeğidir. Bunu aday kümesinin en küçük/en büyük değerlerinden rastgele üretmek yerine görev amacına göre belirleyin ve duyarlılık analizi yapın. “Normal dağılım kanıtlandı” varsayımı bu formülün kullanılmasından otomatik olarak çıkmaz.

Dağılımlar için yalnızca ortalama farkı yerine yüzdelikler veya histogram uzaklıkları kullanılabilir. Kategorik mineraller için güvenilir ortak sınıfların uyumu değerlendirilebilir. Spektral karşılaştırmada aynı dalga boyu aralığı, maskeleme ve spektral tepki uyumu gerekir; iki RGB görüntüsünün renk uzaklığı mineral benzerliğinin yerine geçmez.

Boyut puanı:

```text
S = sum(w_j * q_j * a_j * s_j) / sum(w_j * q_j * a_j)
C = sum(w_j * a_j) / sum(w_j)
Q = sum(w_j * a_j * q_j) / sum(w_j * a_j)
```

`a_j` veri geçerli/mevcut göstergesi, `q_j` belgelenmiş kalite katsayısı, `w_j` göreve özgü önemdir. `S` benzerlik, `C` kapsam, `Q` kalite özeti olarak ayrı gösterilir. Sıfır payda durumunda puan üretmeyin. Kalite katsayısını kanıtsız bir uzman hissine dönüştürmeyin; kuralları yazılı tutun.

Eksik boyutları paydadan çıkarmak, az verili adayı gereğinden iyi gösterebilir. Bu nedenle zorunlu boyut, asgari kapsam ve yeterli gözlem sayısı koşullarını önceden tanımlayın. Yetersiz veri durumunda sıralamayı kapatıp “araştırma gerekli” gösterin. Bir duyarlılık görünümü, eksik özellikler için iyimser/kötümser varsayımlarda sıralamanın nasıl değiştiğini açıklayabilir; bunlar ölçüm değil senaryodur.

### 12.4. Ağırlıklar nasıl belirlenebilir?

İlk prototipte yüzdeler vermek zorunlu değil. Kullanıcıya deney amacını seçtirip sadece ilgili boyutları karşılaştırmak daha savunulabilir. Ağırlık istenirse başlangıç tasarımı şöyle olabilir:

| Deney amacı | Yüksek önem | Orta önem | Sonuç dışı veya ayrı gösterilecek |
|---|---|---|---|
| Ay kutbu rota/navigasyon | Eğim, rölyef, gölge/ufuk | Bloklu yüzey ve erişim | Dünya atmosferiyle termal dayanım doğrulaması |
| Eski Mars göl süreçleri | Jeoloji/mineral, çökel şekilleri | Kuruma rejimi ve yüzey açıklığı | Güncel Mars yaşamı veya üs inşaat güvenliği |
| Gömülü buz araştırması | Buz kanıt türü, örtü, radar kalitesi | Arazi ve örnekleme erişimi | Uydu haritasından doğrudan su üretim miktarı |

Kullanıcının ağırlığı değiştirmesine izin verirseniz, sıralamanın ne kadar değiştiğini gösterin. Değişkenlerin birbirini tekrar etmesini azaltın: eğim, rölyef ve pürüzlülük yüksek korelasyonlu olduğunda üç bağımsız güçlü kanıtmış gibi ödüllendirmeyin.

### 12.5. Tek bir saha yerine tamamlayıcı saha paketi

Bir deney programı üç farklı sahada farklı özellikleri sınayabilir: lav yüzeyinde navigasyon, tuz düzlüğünde örnekleme, soğuk ortamda ekip operasyonu. Bu yaklaşım, bir araziyi bütün koşullarda “en iyi” ilan etme zorunluluğunu azaltır.

Ürün fikri olarak, seçilen deneylerin gerektirdiği özellikleri en az sayıda sahayla kapsayan bir saha paketi önerilebilir. Bu ekibinizin geliştirebileceği optimizasyon yaklaşımıdır; bu araştırmada çözülmüş bir sonuç değildir.

## 13. Karşılaştırmayı bozabilecek teknik hatalar

### 13.1. Koordinat sistemleri

Ay ve Mars koordinatlarını WGS84 Dünya koordinatı gibi işlemeyin. Cisim, referans çerçevesi, projeksiyon, gezegen yarıçapı, doğu/batı boylam yönü, boylam aralığı ve yükseklik referansını dosya etiketinden okuyun. Mars’ta planetosentrik/planetografik enlem farkını da kontrol edin. Hata, haritada küçük görünüp eşleştirmeyi yanlış araziye kaydırabilir. [MOLA koordinat bilgisi](https://pds-geosciences.wustl.edu/missions/mgs/mola.html), [LOLA PGDA referansı](https://pgda.gsfc.nasa.gov/products/81)

### 13.2. Çözünürlük ve yeniden örnekleme

Bir MOLA gridini 30 m’ye büyütmek, 30 m arazi bilgisi üretmez. CTX görüntüsü küçük şekilleri gösterebilir ama tek görüntüden aynı ölçekte güvenilir eğim çıktığı varsayılamaz. DEM türevlerini, veri çözünürlüğünün desteklediği pencerelerde hesaplayın.

Sayısal katmanlarda uygun filtreleme ve yeniden örnekleme seçin; kategorik mineral/maske sınıflarını bilinear yöntemle karıştırmayın. Her özellik ailesinin kendi karşılaştırma ölçeği olabilir. Tüm katmanları tek ızgaraya büyütüp eşit bilgi taşıdıklarını varsaymak zorunda değilsiniz.

### 13.3. Ölçek seçimi

“3 × 3 piksel pürüzlülük” 5 m LOLA’da 15 m, 30 m Dünya DEM’inde 90 m, 463 m MOLA’da yaklaşık 1,4 km alanı ifade eder. Böyle üç ölçümü aynı değişkenmiş gibi karşılaştırmayın. Pencereleri metreyle tanımlayın; çözünürlük değişimine duyarlılığı kaydedin.

### 13.4. Bulutlar, gölgeler, su ve eksik veri

Bulut ve gölge, koyu renkli mineral veya soğuk zemin gibi görünerek yanlış eşleşme üretebilir. Tüm kalite kontrollerini skordan önce uygulayın. `NoData`, `-9999` ve su/kar maskelerini bilimsel değer gibi işlemeyin. Dünya’daki geçici karı Ay gömülü buzu diye eşlemeyin.

### 13.5. Birim ve büyüklük karışıklıkları

LST ile 2 m hava sıcaklığı; radyans ile yansıtım; parlaklık sıcaklığı ile yüzey sıcaklığı; termal atalet ile gün-gece sıcaklık farkı; aerosol optik derinliği ile yüzey toz tane boyutu farklıdır. Etiketlerde birim, ölçek çarpanı ve ofset açık tutulmalı. Her ürün için kendi metadata/kılavuzunu kullanın; bütün NASA rasterlerine tek bir çarpan uygulamayın.

### 13.6. Tarih ve mevsim

Mars güneş boylamı/mevsimi ile Dünya takvim ayı aynı şey değildir. Yerel saat, mevsim, gün uzunluğu ve gözlem açısını eşleştirme gerekçenize ekleyin. Değişmeyen arazi topografyasında eski ölçüm yararlı olabilir; 2021 su görüntüsüyle 2026 kıyı durumuna karar vermek aynı güvene sahip değildir.

### 13.7. Nedensellik ve fizik

Maar, kaldera ve çarpma krateri benzer geometriler taşıyabilir; oluşum süreçleri farklıdır. Dünya’daki mağara testi navigasyonu sınayabilir; Ay mağarasının stabilitesini doğrulamaz. Dünya sahası tam vakum, düşük yerçekimi veya uzay radyasyonu sağlamaz. Bu sınırlamaları bir dipnota gizlemek yerine aday kartının parçası yapın.

## 14. Veriye erişim ve tekrarlanabilir çalışma akışı

### 14.1. En hızlı resmî araçlar

| İhtiyaç | Araç | Çıktı |
|---|---|---|
| Dünya koleksiyonu/sahnesi bulma | [Earthdata Search](https://search.earthdata.nasa.gov/) | Ürün, sürüm, alan ve tarih kapsamı |
| Ön görsel inceleme | [Worldview](https://worldview.earthdata.nasa.gov/) | Katman ve tarih bağlamı |
| Programatik metadata arama | [CMR Search API](https://cmr.earthdata.nasa.gov/search/site/docs/search/api.html) | Koleksiyon ve granül kayıtları |
| Ay katmanları ve ölçümleri | [Moon Trek](https://trek.nasa.gov/moon/) | Yükseklik profili, eğim/aydınlatma araçları |
| Mars katmanları | [Mars Trek](https://trek.nasa.gov/mars/) | Katman keşfi ve bölgesel karşılaştırma |
| Görev arşivi | [PDS](https://pds.nasa.gov/) | Bilim ürünü, etiket ve dokümantasyon |
| NASA meteoroloji bağlamı | [POWER API kılavuzu](https://power.larc.nasa.gov/docs/tutorials/service-data-request/api/) | Nokta/bölge zaman serileri |

Moon Trek; yükseklik profili, eğim, Güneş açısı ve görüş doğrultusu gibi araçlar sunuyor. Haritadaki her katman NASA kökenli değildir; kaynağı metadata üzerinden seçin. Trek arayüzü kullanmak, bütün girdilerin NASA verisi olduğu anlamına gelmez. [Moon Trek araçları](https://trek.nasa.gov/moon/), [Trek katman API’si](https://trek.nasa.gov/tiles/apidoc/index.html)

### 14.2. Koleksiyonu sürümüne göre bulun

Aşağıdaki URL örnekleri bir erişim tarifidir; bu araştırmada çalıştırılmış veri sorgusu veya indirilen ölçüm değildir:

```text
https://cmr.earthdata.nasa.gov/search/collections.json?short_name=NASADEM_HGT&version=001&page_size=10
https://cmr.earthdata.nasa.gov/search/collections.json?short_name=HLSL30&version=002&page_size=10
https://cmr.earthdata.nasa.gov/search/collections.json?short_name=EMITL2BMIN&page_size=20
```

Önce dönüşteki koleksiyon kimliğini ve sürümünü doğrulayın. Sonra ilgili koleksiyon için `granules` sorgusunda alan, tarih ve kalite/kapsam bilgilerini inceleyin. Bir katalog kaydının mevcut olması, seçtiğiniz küçük poligonda geçerli veri olduğu anlamına gelmez. Kamuya açık metadata araması ile bilim dosyası indirmek farklı adımlardır; birçok Earthdata indirmesi hesap gerektirir. [CMR API resmî dokümantasyon](https://cmr.earthdata.nasa.gov/search/site/docs/search/api.html), [HLS erişim koşulu](https://hls.gsfc.nasa.gov/data-access-and-tools/)

### 14.3. Her girdi için kaynak kaydı

Önerilen asgari kayıt şeması:

```json
{
  "source_agency": "NASA or NASA joint product",
  "mission": null,
  "instrument": null,
  "product_short_name": null,
  "product_version": null,
  "collection_concept_id_or_pds_lidvid": null,
  "granule_or_product_id": null,
  "observation_start_utc": null,
  "observation_end_utc": null,
  "release_date": null,
  "accessed_at_utc": null,
  "doi_or_source_url": null,
  "body": null,
  "crs_and_reference_frame": null,
  "nominal_pixel_spacing_m": null,
  "effective_resolution_note": null,
  "unit_scale_offset": null,
  "quality_mask_rule": null,
  "valid_fraction_in_aoi": null,
  "processing_steps": [],
  "file_sha256": null
}
```

Bu boş alanlar ölçüm değeri değildir. İndirme ve işleme tamamlandığında doldurulmalı. Özellikle `product_version` ve gözlem tarihini yalnızca ürün sayfasının son güncelleme tarihinden türetmeyin.

### 14.4. İşleme sırası

1. Araştırma sorusunu ve karşılaştırılan iki poligonu tanımlayın.
2. Kaynak, sürüm, kapsam ve kullanım kılavuzlarını sabitleyin.
3. Bilim dosyalarını ve kalite/metadata dosyalarını birlikte alın.
4. Maskeleri uygulayın; uygun karşılaştırma ölçeğini seçin.
5. Özellikleri her cisim için doğru projeksiyonda hesaplayın.
6. Özellikleri ve veri kapsamını karşılaştırın.
7. Benzerlik, belirsizlik, kapsam ve operasyonel uygunluğu ayrı sunun.
8. Bilinen analog ve olumsuz karşılaştırmayla yöntemi sınayın.
9. İşlem adımlarını, parametreleri ve dosya özetlerini arşivleyin.

## 15. Doğrulama: bir haritanın bilimsel iddiasını nasıl savunursunuz?

### 15.1. Kanıt düzeyi etiketleri

| Etiket | Anlamı | Örnek |
|---|---|---|
| Görev gözlemi | NASA görevinin kalibre verisi | Seçilmiş bir sahnedeki ölçüm |
| NASA türetilmiş ürün | Belirli algoritmadan geçmiş bilim katmanı | DEM veya işlenmiş mineral ürünü |
| NASA bilim açıklaması | Resmî yazıda aktarılan ilişki | Salda–Jezero bağlamı |
| Bizim türettiğimiz özellik | Ekibin koduyla hesaplanan değer | Seçilmiş AOI’de eğim yüzdelikleri |
| Hipotez | Henüz sınanmamış eşleştirme | Nemrut koridorunun kutup rotasına yararı |
| Eksik / doğrulanmadı | Gerekli veri yok veya kontrol edilmedi | Saha taşıma gücü, izin, mineral eşleşmesi |

Bu etiketler tek bir doğruluk sırası değildir; farklı kanıt türlerini gösterir. NASA’nın veri sağlaması, ekibin hipotezini onayladığı anlamına gelmez.

### 15.2. Bilinen ve olumsuz karşılaştırmalar

Salda–Jezero karşılaştırmasında yöntemin jeoloji/çökel boyutunda anlamlı ilişki bulabilmesi beklenebilir; ancak hangi özellikleri kullandığınıza bağlıdır. Yalnızca DEM kullanan sistemin biyoişaret potansiyelini keşfettiğini söylemeyin.

Olumsuz karşılaştırma olarak, benzer renkli ama farklı jeolojik süreçli bir yüzey seçilebilir. Bir başka kontrol: yalnızca eğim bakımından benzeyen fakat yoğun bitki örtüsü taşıyan Dünya sahasının, çıplak zemin robot testi için nasıl elendiğini göstermek. Kontrol seçiminde hedef sonucu garantileyecek etiketleme yapmayın.

### 15.3. Belirsizlik ve sağlamlık denemeleri

- AOI sınırını makul ölçüde değiştirince sonuç değişiyor mu?
- Aynı yeri başka mevsimde incelerken benzerlik korunuyor mu?
- DEM’i desteklenen daha kaba ölçekte işleyince sıralama değişiyor mu?
- Ağırlıkları değiştirince ilk adaylar yer değiştiriyor mu?
- Düşük kaliteli bir mineral gözlemi çıkarılınca sonuç sürüyor mu?
- Aynı bilgiyi tekrarlayan özellikler azaltılınca sonuç kararlı mı?

Bir pikseli bağımsız deney gibi saymayın: komşu pikseller mekânsal olarak ilişkilidir. Belirsizlik hesabında mekânsal bloklama veya ayrı bölgeler kullanmak daha uygundur. Makine öğrenmesi eklenirse, aynı sahanın komşu piksellerini hem eğitim hem teste koymak genelleme başarısını abartabilir. Önce açıklanabilir temel yöntemle ilerlemek, küçük hackathon veri kümesinde daha kolay denetlenebilir.

## 16. TerraTwin için somut ürün önerisi

Bu, resmî görev gereksinimlerinden türetilmiş bağımsız bir tasarım önerisidir; başka bir takımın uygulaması temel alınmadı.

**Ana akış:** Kullanıcı hedef alanı ve deney amacını seçer → Dünya adayları görünür → bir adayda neden eşleştiği, hangi verilerle değerlendirildiği ve nerede benzemediği açılır.

**Aday kartında bulunması gerekenler:**

| Alan | Gösterilecek içerik |
|---|---|
| Hedef ve amaç | Örneğin Ay güney kutbu / rota planlama |
| İncelenen mikroalan | İsim, poligon, karşılaştırma ölçeği |
| Boyut bazında sonuç | Arazi, malzeme, termal, su/buz; yalnızca hesaplananlar |
| Kanıt | Kullanılan sahne ve ürün kimliği, tarih, kaynak |
| Kapsam | Geçerli piksel/gözlem oranı ve eksik boyutlar |
| Benzerliğin sınırı | Farklı süreç, atmosfer, yerçekimi veya malzeme |
| Deney önerisi | Bu sahada hangi yöntemin sınanabileceği |
| Saha hazırlığı | Erişim/koruma/zemin güvenliği bilgisi doğrulanmadıysa açık etiket |

**Önerilen görsel:** Solda seçilmiş Ay/Mars hedefi, sağda Dünya mikroalanı; altta aynı fiziksel ölçekle eğim dağılımları ve kaynak kartları. Araziyi 3B gösterebilirsiniz, fakat düşey abartıyı açıkça yazın. Radar grafiği kullanılacaksa eksik boyutu sıfır benzerlik gibi çizmekten kaçının; boş/eksik gösterin.

“Yeni analog keşfi” iddiası için tüm literatürde bulunmadığını bu araştırma kanıtlamıyor. Daha doğru proje ifadesi: **NASA verileriyle aday mikroalanlar buluyor, belirli deneyler açısından karşılaştırıyor ve doğrulama gerektirenleri gösteriyoruz.**

## 17. 48 saatlik uygulanabilir çalışma planı

Bu plan görev koşulu değil, kapsamı yönetmek için öneridir. Tam otomatik küresel arama ve bütün veri ailelerini aynı anda tamamlamaya çalışmak yerine, iki iyi belgelenmiş örnek üzerinden uçtan uca doğrulama hedeflenebilir.

| Süre | Yapılacak iş | Somut çıktı |
|---|---|---|
| 0–3 saat | İki hedef/deney tanımı; NASA veri kapsamı sorgusu | AOI’ler, kaynak listesi ve erişilebilir ürünler |
| 3–9 saat | Küçük kesitleri indirme ve kalite denetimi | Ham dosya + metadata + maske |
| 9–17 saat | Eğim/rölyef ve yüzey durumu özellikleri | Yeniden üretilebilir hesaplar |
| 17–25 saat | Aday/karşılaştırma ve duyarlılık | Kanıtlı sonuç tabloları; eksik veri işaretleri |
| 25–35 saat | Harita ve aday açıklamaları | Çalışan etkileşimli gösterim |
| 35–43 saat | Bilinen analog, olumsuz kontrol, kaynak denetimi | Sınırlamalar ve hata düzeltmeleri |
| 43–48 saat | Demo ve kısa sunum | Veri → yöntem → bulgu → kullanım zinciri |

**Asgari bitirilebilir kapsam:** Bir Ay arazi hedefi, Nemrut’ta birkaç küçük koridor, gerçek DEM özellikleri ve kaynak kartı. Mars tarafında Salda’yı resmî bilim bağlamıyla gösterip, ek nicel iddia ancak veri işlenmişse ekleyin. Tuz Gölü’nü ikinci aday olarak HLS mevsimselliğiyle incelemek mümkün olabilir. EMIT sahnesi yoksa mineral puanı uydurmak yerine o boyutu eksik bırakın.

**Zaman kalırsa:** Küresel aday taraması, EMIT–CRISM sınıf eşlemesi, kutupsal aydınlatma modeli, saha paketi optimizasyonu. Bunlar çalışır temel gösterimin önüne geçmemeli.

## 18. Sunumda kullanılabilecek ve kaçınılacak ifadeler

| Kaçının | Kanıta uygun ifade |
|---|---|
| “NASA üs için bu koordinatı seçti.” | “Güncel NASA açıklaması güney kutbu bölgesini hedefliyor; biz bu AOI’yi analiz için seçtik.” |
| “Nemrut Ay’ın yüzde 94 aynısı.” | “Bu AOI, bu çözünürlükte, seçilen arazi özellikleri açısından şu sonuçları veriyor.” |
| “Salda’yı Mars analoğu olarak keşfettik.” | “NASA’nın bilinen Salda–Jezero ilişkisini karşılaştırma örneği olarak kullandık.” |
| “Tuz Gölü’nde Mars’taki aynı mineraller var.” | “Bu mineral sınıflarına ilişkin uzaktan algılama göstergelerini araştırıyoruz; eşleşme doğrulama gerektiriyor.” |
| “MOLA ile kaya tehlikelerini bulduk.” | “MOLA’yı bölgesel topografya için kullandık; yerel tehlikeler daha yüksek çözünürlüklü veri gerektiriyor.” |
| “SWIM mavi alanı çıkarılabilir su rezervidir.” | “Bu katman, tanımlı derinlik aralığında buzla tutarlılık kanıtını gösteriyor.” |
| “Bu mağarada güvenle üs kurulabilir.” | “Yeraltı araştırma yöntemleri için aday; stabilite ve erişim doğrulanmadı.” |
| “Tüm NASA verileri 2026’da çekildi.” | “Erişim/sürüm durumu 14 Kasım 2026’da kontrol edildi; ölçüm tarihleri ürün bazında belirtiliyor.” |

Önerilen kısa anlatım:

> TerraTwin, Ay ve Mars keşif deneyleri için Dünya’daki aday arazileri NASA gözlemleriyle araştırır. Her öneri, hangi özelliklerde benzerlik bulunduğunu, hangi verilerin kullanıldığını ve analojinin nerede geçersiz olduğunu gösterir. Amaç, araştırmacılara saha testini tasarlarken izlenebilir bir başlangıç sunmaktır.

## 19. Açık kalan sorular ve araştırmanın sınırları

1. Nemrut/Tuz Gölü için belirli AOI’lerde EMIT V2’nin geçerli sahne kapsamı henüz bu çalışmada sorgulanıp indirilmedi.
2. Gerçek DEM, spektral veya sıcaklık dosyaları indirilip sayısal özellik/benzerlik hesaplanmadı; adaylar sonuç değil hipotezdir.
3. Dünya mikroalanlarının bugün sahaya giriş, koruma, jeoteknik güvenlik veya araç testi bakımından uygun olduğu doğrulanmadı.
4. “Literatürde ilk kez” veya “daha önce hiçbir ekip önermedi” iddiası kurulmadı. Başka takımların materyalleri kaynak olarak kullanılmadı.
5. Görev sayfasının ayrıntıları ve Resources sekmesi araştırma aracıyla açılmadığından resmî sayfa tarayıcıdan okunarak doğrulandı. Bazı Earthdata ürün sayfaları erişim kısıtı verdi; bu durumlarda resmî NASA katalog kayıtları ve DAAC personel duyuruları kullanıldı.
6. Büyük Moon Base PDF’si araştırma aracının boyut sınırını aştı; raporda o PDF’den doğrulanmamış ayrıntı kullanılmadı. Üs bağlamı NASA’nın erişilebilen güncel sayfalarına dayanıyor.
7. NASA arşivindeki üniversite/DAAC sunucuları, başka yarışma takımları değildir. PDS Geosciences gibi resmî NASA arşiv düğümleri bu araştırmanın kaynak kapsamına dâhildir.
8. NASA ortak ürünlerinde diğer ajans girdileri olabilir: HLS, NASA’nın Landsat ve Sentinel-2’den işlediği üründür; ASTER ve NISAR da ortak görev/ürün bağlamı taşır. Bunlar bağımsız takım verisi değildir; kökenleri arayüzde açık yazılmalı.

## 20. Önce okunacak kaynaklar

Okuma önceliği, bu rapordaki kaynakların tamamının önüne geçmez; hızlı ekip paylaşımı içindir.

1. [Resmî görev — Details](https://www.spaceappschallenge.org/2026/challenges/permanent-moon-base-locations-and-mars/?tab=details)
2. [Resmî görev — Resources](https://www.spaceappschallenge.org/2026/challenges/permanent-moon-base-locations-and-mars/?tab=resources)
3. [NASA Moon Base FAQ](https://www.nasa.gov/moon-base-frequently-asked-questions/)
4. [NASA Lunar South Pole Environment](https://www.nasa.gov/reference/moonbase-environment/)
5. [NASA PGDA kutup topografyası](https://pgda.gsfc.nasa.gov/products/90)
6. [NASA Diviner arşivi ve kalite notları](https://pds-geosciences.wustl.edu/missions/lro/diviner.htm)
7. [HLS ürün ve erişim bilgisi](https://hls.gsfc.nasa.gov/data-access-and-tools/)
8. [EMIT Ekim 2026 yeni sürüm duyurusu](https://forum.earthdata.nasa.gov/viewtopic.php?sid=dae91c5ef96f336491803c0490ce9060&t=8322)
9. [NASA Analog Explorer](https://science.nasa.gov/solar-system/analog-explorer/)
10. [NASA Salda saha anlatımı](https://science.nasa.gov/blogs/earth-matters/2021/02/17/what-a-lake-in-turkey-can-tell-us-about-mars/)
11. [NASA SWIM açıklaması](https://www.nasa.gov/solar-system/planets/mars/nasa-is-locating-ice-on-mars-with-this-new-map/)
12. [NASA CMR API](https://cmr.earthdata.nasa.gov/search/site/docs/search/api.html)

Bu dosyadaki bütün bağlantıların tekilleştirilmiş listesi aynı klasördeki `kaynaklar.json` dosyasındadır. Teknik ürün özeti `veri_katalogu.json` içinde bulunur. Hiçbiri indirilen bilim verisinin yerine geçmez.
